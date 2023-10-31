from django.contrib import admin
from.models import Data

# Register your models here.


class DataAdmin(admin.ModelAdmin):


    list_display = ('Nitrogen', 'Phosphorus', 'Potassium', 'predictions')
admin.site.register(Data, DataAdmin)




