from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

"""App user_auth possui views para cadastro e login"""

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('exit/', views.exit, name='exit'),
    path('recuperar_senha/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"), name="password_reset"),
    path('email_recuperacao/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name="password_reset_done"),
    path('redefinir_senha/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm_view.html"), 
            name="password_reset_confirm"),
    path('senha_redefinida/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), 
        name="password_reset_complete"),
]