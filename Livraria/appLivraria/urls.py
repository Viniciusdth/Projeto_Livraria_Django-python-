from django.urls import path
from appLivraria.views import index
from . import views

urlpatterns = (

    path('index/', index.as_view(), name='index'),
    path('empresa/', views.EmpresaListView.as_view(), name='app_name_empresa_list'),
    path('empresa/formulario', views.questionario, name='questionario'),
    path('empresa/create/', views.EmpresaCreateView.as_view(), name='app_name_empresa_create'),
    path('empresa/detail/<int:pk>/', views.EmpresaDetailView.as_view(), name='app_name_empresa_detail'),
    path('empresa/update/<int:pk>/', views.EmpresaUpdateView.as_view(), name='app_name_empresa_update'),

)

