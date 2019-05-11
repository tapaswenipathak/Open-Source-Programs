from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lists-index'),
    path('SOCPrograms/', views.soc_view, name='soc'),
    path('OpenSourceCompetitions/', views.osc_view, name='osc'),
    path('UniversitySoC-WoC/', views.usocwoc, name='u-soc-woc'),
    path('add-new-soc/', views.soc_create_view.as_view(), name='soc-create'),
    path('add-new-osc/', views.osc_create_view.as_view(), name='osc-create'),
    path('add-new-u_woc_soc/', views.u_woc_soc_create_view.as_view(), name='u_woc_soc-create')
    ]
