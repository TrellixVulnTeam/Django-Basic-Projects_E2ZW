from django.views.generic import TemplateView
from .models import Student


class IndexView(TemplateView):

    context_object_name = 'product'
    template_name = "home.html"
    student = Student()

    def details(self):
        pass
