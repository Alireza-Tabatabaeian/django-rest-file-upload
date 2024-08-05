from django.urls import path

from main.views import EditRequestView

urlpatterns = [
    path('edit-rqeuest', EditRequestView.as_view(), name='edit-request')
]
