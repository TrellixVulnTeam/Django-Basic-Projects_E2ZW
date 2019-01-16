from django.shortcuts import render, redirect
from django.views import View
from DjangoApp.models import DjangoApp


class HomeView(View):
    template_name = "home.html"
    model = DjangoApp()
    data = DjangoApp.objects.all()

    def get(self, request):
        self.data
        return render(request, self.template_name, {"user":self.data})

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        age = int(request.POST['age'])


        self.model.first_name = first_name
        self.model.last_name = last_name
        self.model.phone = phone
        self.model.age = age
        self.model.save()

        return redirect('home')


def view_details(request, slug):
    abc = DjangoApp.objects.get(slug=slug)
    return render(request, "details.html", {"abc":abc})