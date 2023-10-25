from django.contrib import admin
from django.urls import path
from mainApp.views import homepage, majors, subjects, teachers, delete_major, update_major, delete_subject, \
    update_subject, delete_teacher, update_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('majors/', majors),
    path('delete_major/<int:num>/', delete_major),
    path('update_major/<int:num>/', update_major),
    path('subjects/', subjects),
    path('delete_subject/<int:num>/', delete_subject),
    path('update_subject/<int:num>/', update_subject),
    path('teachers/', teachers),
    path('delete_teacher/<int:num>/', delete_teacher),
    path('update_teacher/<int:num>/', update_teacher),
]
