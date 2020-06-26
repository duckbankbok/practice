from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),
    path('about/', myapp.views.about, name="about"),
    path('detail/<int:book_id>', myapp.views.detail, name='detail'),
    path('new', myapp.views.new, name='new'), 
    path('create/', myapp.views.create, name='create'),
    path('delete/<int:book_id>', myapp.views.delete, name='delete'),
    path('update/<int:book_id>', myapp.views.update, name='update'),
    path('update_final/<int:book_id>', myapp.views.update_final, name='update_final'),
]
