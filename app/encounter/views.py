from django.views.generic.base import TemplateView

# Create your views here.
class Encounter(TemplateView):
    template_name = 'encounter/index.html'