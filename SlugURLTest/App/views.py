from django.shortcuts import render, redirect
from App.models import Product


def home(request):
    template_name = "index.html"
    prd = Product();
    if request.method == "POST":

        prd.product_name = request.POST["product_title"]
        prd.product_model = request.POST["product_model"]
        prd.product_price = request.POST["product_price"]
        prd.product_status = request.POST["product_status"]
        prd.product_slug_url = str(prd.product_model+"-"+prd.product_price+"-"+prd.product_name+"-"+prd.product_status)
        prd.save()

        return redirect('home')
    else:
        prd = Product.objects.all()
        return render(request, template_name, {"prd":prd})


def view(request, slug):
    prd = Product.objects.get(product_slug_url = slug)
    return render(request, "views.html", {"prd":prd})
