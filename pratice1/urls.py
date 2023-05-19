
from django.contrib import admin
from django.urls import path
from news import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postnews/',views.postnews),
    path('getnews/',views.getnews),
    path('updatenews/<int:id>/',views.updatenews),
    path('deletenews/<int:id>/',views.deletenews),
    
]

urlpatterns+=staticfiles_urlpatterns()