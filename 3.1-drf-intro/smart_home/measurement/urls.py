from django.urls import path

from measurement.views import SensorAPIList, SensorAPIRetrieveUpdate, MeasurementAPICreate

urlpatterns = [
    path('v1/sensors/', SensorAPIList.as_view()),
    path('v1/sensors/<int:pk>/', SensorAPIRetrieveUpdate.as_view()),
    path('v1/measurement/', MeasurementAPICreate.as_view()),
]
