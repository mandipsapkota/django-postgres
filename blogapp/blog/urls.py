from django.urls import path
from . import views 

urlpatterns = [
    # This is how we create a path. We specify route, view that handles the logic behind the url, and a app-specific name to avoid further issues.
    path('' , views.home, name = "blog-home"),
    path('about' , views.about, name = "blog-about")    
]