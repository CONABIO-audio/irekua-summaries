from django.urls import path
from irekua_summaries import views


urlpatterns = [
    path('collections/', views.data_collections, name='collections'),
]
