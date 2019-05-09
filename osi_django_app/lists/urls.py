from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lists-index'),
    path('SOCPrograms/', views.soc_view, name='soc'),
    path('OpenSourceCompetitions/', views.osc, name='osc'),
    path('UniversitySoC-WoC/', views.usocwoc, name='u-soc-woc'),
    path('add-new-soc/', views.soc_create_view.as_view(), name='soc-create')

    ]
