from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class ResumeView(TemplateView):
    template_name = "resume.html"


class ProjectView(TemplateView):
    template_name = "projects.html"


class ContactView(TemplateView):
    template_name = "contact.html"
