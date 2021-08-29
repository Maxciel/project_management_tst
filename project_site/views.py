from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from core.models import Project
from project_site.forms import IncludeProjectForm
from core.serializers import ProjectSerializer

import json

# Main Page
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "index.html"


# List the Projects
# ----------------------------------------------

class ProjectListView(ListView):
    template_name = "list_project.html"
    model = Project
    context_object_name = "project_list"
    def get_context_data(self, **kwargs):
        list = Project.objects.all()
        serialized = ProjectSerializer(list, many=True)
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['json_data'] = json.dumps(serialized.data) 
        context['json_risks'] = '["Baixo", "Médio", "Alto"]'
        context['json_roi'] = [0.05, 0.10, 0.20]
        return context


# Include Project
# ----------------------------------------------

class ProjectCreateView(CreateView):
    template_name = "create_project.html"
    model = Project
    form_class = IncludeProjectForm
    success_url = reverse_lazy("lista_projetos")


# Update Project
# ----------------------------------------------

class ProjectUpdateView(UpdateView):
    template_name = "update_project.html"
    model = Project
    #fields = '__all__'
    form_class = IncludeProjectForm
    context_object_name = 'project'
    success_url = reverse_lazy("lista_projetos")


# Delete Project
# ----------------------------------------------

class ProjectDeleteView(DeleteView):
    template_name = "conf_delete_project.html"
    model = Project
    fields = '__all__'
    context_object_name = 'project_obj'
    success_url = reverse_lazy("lista_projetos")


# Simulate View
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "simulate_roi.html"
