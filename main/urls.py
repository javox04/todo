from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name="index_url"),
    path('create-tack-url', create_tack_view, name="create_task_url"),
    path('swap-status-deleted/<int:pk>/', swap_status_deleted, name="swap_status_deleted_url"),
    path('swap_status_finished/<int:pk>/', swap_status_finished, name="swap_status_finished_url"),
    path('get-inprogress', inprogress_view, name="inprogress_url"),
    path('delete-task/<int:pk>/', delete_task_view, name="delete_task_url"),
    path('get-finished', finished_view, name="finished_url"),
    path('get-delete', deleted_task_view, name="deleted_task_url"),
]