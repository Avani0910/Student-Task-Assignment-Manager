from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AssignmentForm
from .models import Assignment

def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account was created successfully.")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "tasks/register.html", {"form": form})

@login_required
def dashboard(request):
    assignments = Assignment.objects.filter(user=request.user)
    return render(request, "tasks/dashboard.html", {
        "assignments": assignments,
        "total": assignments.count(),
        "completed": assignments.filter(status="Completed").count(),
        "pending": assignments.filter(status="Pending").count(),
    })

@login_required
def assignment_create(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.user = request.user
            assignment.save()
            messages.success(request, "Assignment added.")
            return redirect("dashboard")
    else:
        form = AssignmentForm()
    return render(request, "tasks/assignment_form.html", {
        "form": form, "page_title": "Add assignment", "button_label": "Save assignment"
    })

@login_required
def assignment_edit(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    if request.method == "POST":
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            messages.success(request, "Assignment updated.")
            return redirect("dashboard")
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, "tasks/assignment_form.html", {
        "form": form, "page_title": "Edit assignment", "button_label": "Save changes"
    })

@login_required
def assignment_toggle(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    if request.method == "POST":
        assignment.status = "Completed" if assignment.status == "Pending" else "Pending"
        assignment.save(update_fields=["status"])
        messages.success(request, "Assignment status updated.")
    return redirect("dashboard")

@login_required
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    if request.method == "POST":
        assignment.delete()
        messages.success(request, "Assignment deleted.")
        return redirect("dashboard")
    return render(request, "tasks/assignment_confirm_delete.html", {"assignment": assignment})
