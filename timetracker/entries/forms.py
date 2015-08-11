from django import forms
from django.utils import timezone
import datetime
from .models import Project, Client


class HelloWorldForm(forms.Form):
    name = forms.CharField()


class ClientForm(forms.Form):
    name = forms.CharField(label="Client Name")


class ProjectForm(forms.Form):
    name = forms.CharField(label="Project Name")
    client = forms.ModelChoiceField(queryset=Client.objects.all())


class EntryForm(forms.Form):
    start = forms.DateTimeField(label="Start Time", help_text="Format: 2006-10-25 14:30")
    end = forms.DateTimeField(label="End Time", help_text="Format: 2006-10-25 14:30")
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    description = forms.CharField()

    def clean_start(self):
        start = self.cleaned_data.get('start')
        now = timezone.localtime(timezone.now())
        diff = now - start       
        if diff.total_seconds() < 0:
            raise forms.ValidationError("Start time is invalid.")
        return start


    def clean_end(self):
        end = self.cleaned_data.get('end')
        start = self.cleaned_data.get('start')
        diff = end - start
        print("start ", start)
        print("end ", end)
        print("diff.total_seconds() ", diff.total_seconds())
        if diff.total_seconds() < 0:
            raise forms.ValidationError("End time should be later than start time.")
        return end
