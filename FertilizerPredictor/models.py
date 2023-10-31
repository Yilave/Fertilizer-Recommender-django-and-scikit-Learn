from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from requests import request
from sklearn.tree import DecisionTreeClassifier
from django.contrib.auth.models import User
import joblib
from profiles.models import Profile

# Create your models here.


class Data(models.Model):

    BAR = 'Bar'
    LINE = 'Line'
    PIE = 'Pie'

    CHART_CHOICES = (
        (BAR, 'bar'),
        (LINE, 'line'),
        (PIE, 'pie')
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    Nitrogen = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(200)], null=True)
    Phosphorus = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(200)], null=True)
    Potassium = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(200)], null=True)
    predictions = models.CharField(max_length=100, blank=True)
    chart_type = models.CharField(max_length=20, choices=CHART_CHOICES, default=BAR)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
    

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/FertRecommender.joblib')
        self.predictions = ml_model.predict([[self.Nitrogen, self.Phosphorus, self.Potassium]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']
   