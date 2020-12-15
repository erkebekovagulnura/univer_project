from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.users.models import Student, Teacher

User = get_user_model()

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)