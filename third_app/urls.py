from django.urls import path
from third_app.views import index

urlpatterns = [
    path('', index)
]