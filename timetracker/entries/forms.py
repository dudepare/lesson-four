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

    def clean(self):
        # Just call the super class version of clean()
        cleaned_data = super(EntryForm, self).clean()
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        now = timezone.localtime(timezone.now())

        if start:
            if start > now:
                raise forms.ValidationError("Start time should come before the current time.")
        
            if end:
                if end < start:
                    raise forms.ValidationError("End time should come after start time.")
