from django import forms
from .models import Task


# from Crudapp.models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
