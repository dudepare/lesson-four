from django.shortcuts import redirect, render, get_object_or_404

from .forms import EntryForm, ClientForm, ProjectForm
from .models import Client, Entry, Project


def clients(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client = Client()
            client.name = client_form.cleaned_data.get('name')
            client.save()
    else:
        client_form = ClientForm(request.POST)

    client_list = Client.objects.all()
    return render(request, 'clients.html', {
        'client_list': client_list,
        'client_form': client_form,
        'operation': "Create Client"
    })

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client_list = Client.objects.all()
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client.name = client_form.cleaned_data.get('name')
            client.save()
            return redirect( 'client-list' )
    else:
        client_form = ClientForm(initial={'name':client.name})

    return render(request, 'clients.html', {
        'client_list': client_list,
        'client_form': client_form,
        'operation': "Save Client"
        })

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {
        'client': client,
    })


def entries(request):
    if request.method == 'POST':
        # Create our form object with our POST data
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            # If the form is valid, let's create and Entry with the submitted data
            entry = Entry()
            entry.start = entry_form.cleaned_data.get('start')
            entry.end = entry_form.cleaned_data.get('end')
            entry.project = entry_form.cleaned_data.get('project')
            entry.description = entry_form.cleaned_data.get('description')
            entry.save()
    else:
        entry_form = EntryForm(request.POST)

    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
        'entry_form': entry_form,
    })


def projects(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = Project()
            project.name = project_form.cleaned_data.get('name')
            project.client = project_form.cleaned_data.get('client')
            project.save()
    else:
        project_form = ProjectForm(request.POST)

    project_list = Project.objects.all()
    return render(request, 'projects.html', {
        'project_list': project_list,
        'project_form': project_form,
        'operation': "Create Project"
    })


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_list = Project.objects.all()
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project.name = project_form.cleaned_data['name']
            project.client = project_form.cleaned_data['client']
            project.save()
            return redirect('project-list')
    else:
        project_form = ProjectForm(initial={'name': project.name, 'client': project.client})

    return render(request, 'projects.html' ,{
        'project_list': project_list,
        'project_form': project_form,
        'operation': "Save Project"
        })

