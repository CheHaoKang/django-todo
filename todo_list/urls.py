from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('uncross/<int:item_id>', views.uncross, name='uncross'),
    path('cross_off/<int:item_id>', views.cross_off, name='cross_off'),
    path('edit/<int:item_id>', views.edit, name='edit'),
    path('delete/<int:item_id>', views.delete, name='delete'),
    path('upload/<int:item_id>', views.upload, name='upload'),
]
