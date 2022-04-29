from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('books/<int:id>/', views.show, name='library-show'),
    path("books/new/", views.create, name="library-create"),
]
