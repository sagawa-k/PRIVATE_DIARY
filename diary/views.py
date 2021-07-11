from django.views import generic
from .forms import InquiryForm

class IndexVIew(generic.TemplateView):
    template_name = "index.html"

class InquiryVIew(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
