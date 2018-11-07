from django.contrib import admin
from .models import Snippet, PieUser, Issue
# Register your models here.

admin.site.register(Snippet)
admin.site.register(PieUser)
admin.site.register(Issue)
