from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_chai, name="all_chai"),    

    path("<int:chai_id>/", views.chai_detail, name="chai_detail"),   

    path("delete/<int:chai_id>", views.delete_chai, name="delete_chai"),

    path("add/", views.add_chai, name="add_chai"),

    path("update/<int:chai_id>/", views.update_chai, name="update_chai"),

    path('chai_stores/', views.chai_store_view, name="chai_stores"), 
    
    path("lang/", views.all_languages, name="all_languages")    
]