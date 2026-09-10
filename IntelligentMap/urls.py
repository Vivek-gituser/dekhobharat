from django.contrib import admin
from django.urls import include, path
from .views import Signup

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("goplan_home.urls")),
    path("map/", include("map_engine.urls")),
    path("shristi/", include("chatbot.urls")),
    path("metro/", include("metro.urls")),
    path("native/", include("native_language.urls")), 
    path('accounts/',include('django.contrib.auth.urls')),
    path("signup/",Signup.as_view(),name="signup")
]
