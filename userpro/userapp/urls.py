
from django.urls import path
from .views import *
urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('employee/add/', employee_add, name='employee_create'),
    path('employee/<int:pk>/', employee_detail, name='employee_detail'),

    path('employee/<int:pk>/update/', employee_edit, name='employee_update'),
    path('employee/<int:pk>/delete/', employee_delete, name='employee_delete'),
    path('api/employee/', employee_list_api, name='employee_list_api'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]