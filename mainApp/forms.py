from django import forms
from .models import *


class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
