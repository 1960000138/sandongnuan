from django.conf.urls import url
from django.contrib import admin
import sdn.views as views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', views.to_indexPage,name='indexPage')
]