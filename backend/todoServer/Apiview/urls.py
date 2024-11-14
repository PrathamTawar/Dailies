from django.urls import path
from . import views

urlpatterns = [
    path('get', views.GetData, name= 'GetData'),
    path('set', views.SetData, name= 'SetData'),
    path('delete/<int:pk>', views.DeleteData, name= 'DeleteData'),
    path('check/<int:pk>', views.CheckData, name= 'CheckData'),
]
