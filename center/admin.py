from django.contrib import admin
from django.contrib.auth.models import Group
from .models import (Courses, Sections, Contact, Messages)

admin.site.unregister(Group)

admin.site.register(Courses)
admin.site.register(Sections)
admin.site.register(Contact)
admin.site.register(Messages)
