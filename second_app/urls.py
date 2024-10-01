from django.urls import path
from second_app.views import index

urlpatterns = [
    path('', index)
]

