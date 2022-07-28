from django.contrib import admin
from django.urls import path
from mvt_familia.views import familia
from familia.views import familia
urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', familia, name='familia')
]
