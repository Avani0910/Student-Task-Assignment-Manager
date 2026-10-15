from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["title", "description", "due_date", "priority", "status"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Submit Python project"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Optional notes"}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
