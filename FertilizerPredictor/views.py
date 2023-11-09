from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import DataForm, ChartChoiceForm
from .models import Data
from profiles.models import Profile


# Create your views here.


def home(request):
    return render(request, 'dashboard/index.html')


@login_required
def analysis(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user) 
        form = DataForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            print(instance)
            instance.user = profile
            instance.save()
            return redirect('predictions')
    form = DataForm
    context = {
        'form': form,
    }
    return render(request, 'dashboard/analysis.html', context)

@login_required
def predictions(request):
    user = Profile.objects.get(user=request.user)
    predicted_fertilizer = Data.objects.filter(user=user)
    context = {
        'predicted_fertilizer': predicted_fertilizer
    }
    return render(request, 'dashboard/predictions.html', context)

@login_required
def object_chart_js(request, pk):
    obj = get_object_or_404(Data, pk=pk)
    
    labels = ['Nitrogen', 'Phosphorus', 'Potassium']
    data = [f'{obj.Nitrogen}', f'{obj.Phosphorus}', f'{obj.Potassium}']
    return JsonResponse({'labels': labels, 'data': data, 'type': obj.chart_type.lower(), 'recommedations': obj.predictions}, safe=False)




def object_chart(request, pk):
    obj = Data.objects.get(pk=pk)
    redirect_url = '.'
    form = ChartChoiceForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            chart_type = form.cleaned_data['chart_type']
            print(chart_type)
            form.save()
        #     return JsonResponse({'success': True})
        # else: return JsonResponse({'success': False, 'errors': form.errors})
        headers = {'HX-Redirect': redirect_url} 
        return HttpResponse(headers=headers)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/chart.html', {'chart': context})


@login_required
def delete(request, pk):
    Data.objects.get(pk=pk).delete()
    return redirect('predictions')


    








