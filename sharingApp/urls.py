from django.urls import path
from . import views

app_name = 'sharingApp'

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('share/',views.share_form,name="share"),
    path('signup/', views.register, name="signup"),
    path('',views.ui,name='ui'), 
    path('delete-text/<str:id>',views.deletetext,name="delete-text"),
    path('logout/', views.user_logout, name='logout'),
]