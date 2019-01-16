from django.shortcuts import render, redirect
from django.views import View


class ContactView(View):
    template_name = "contact.html"

    def get(self, request):
        return render(request, self.template_name)


class AboutUsView(View):
    template_name = "team.html"

    def get(self, request):
        string = "This is about us page"
        return render(request, self.template_name, {"msg":string})