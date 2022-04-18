from django.urls import path
from .import views


# CRUD operations 


urlpatterns = [
    path('',views.APioverview,name = 'home'),
    path('create/',views.add_items,name = 'add-items'),
    path('all/',views.view_items,name = 'view-items'),
    path('all/',views.view_items,name = 'view-items'),
    path('update/<int:_id>', views.update_items,name = 'update-items'),
    path('item/<int:_id>', views.delete_items,name = 'delete-items'),
    
]
