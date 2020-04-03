from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
	path('', views.index, name='index'),
    path('paytype/view/', views.paytype_view, name='paytype_view'),
    path('paytype/view/<int:paytype_id>/', views.paytype_view_id, name='paytype_view_id'),
    path('paytype/add/', views.paytype_add, name='paytype_add'),
    path('paytype/add/add/', views.paytype_add_add, name='paytype_add_add'),
]