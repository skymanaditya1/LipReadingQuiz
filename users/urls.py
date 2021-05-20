# This file has all the url mapping to their corresponding views 
#from django.conf.urls import url 
from users.views import dashboard, register
from django.urls import path, include

# names are usually used for reverse mapping where the full url path need not be specified
urlpatterns = [
    # this gives us access to all django related auth urls like login, logout etc. The urls automatically render the corresponding html pages.
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
]