from django.contrib import admin
from .models import Assignment
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "due_date", "priority", "status")
    list_filter = ("priority", "status", "due_date")
    search_fields = ("title", "description", "user__username")
