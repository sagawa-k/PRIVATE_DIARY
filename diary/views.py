from django.views import generic

class IndexVIew(generic.TemplateView):
    template_name = "index.html"
