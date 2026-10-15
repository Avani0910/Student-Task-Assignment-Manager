from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="tasks/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("assignments/add/", views.assignment_create, name="assignment_create"),
    path("assignments/<int:pk>/edit/", views.assignment_edit, name="assignment_edit"),
    path("assignments/<int:pk>/toggle/", views.assignment_toggle, name="assignment_toggle"),
    path("assignments/<int:pk>/delete/", views.assignment_delete, name="assignment_delete"),
]
