from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    #path('register/', register_view, name='register'),
    path('signup_teacher/', signup_teacher, name='signup_teacher'),
    path('signup_student/', signup_student, name='signup_student'),
    path('login/', login, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIR)
