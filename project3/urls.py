from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from vege.views import receipes, delete_recipe, login_page, register, logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receipes/', receipes, name='receipes'),
    path('delete-recipe/<int:id>/', delete_recipe, name='delete_recipe'),
       path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

