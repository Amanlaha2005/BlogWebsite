from django.urls import path
from .views import HomePage,base,BlogLogin,BlogLogout,BlogRegister

urlpatterns = [
    path('HomePage/',HomePage,name='HomePage'),
    path('',base,name='base'),
    path('BlogLogout/',BlogLogout,name="BlogLogout"),
    path('BlogLogin/',BlogLogin,name="BlogLogin"),
    path('BlogRegister/',BlogRegister,name="BlogRegister")
]