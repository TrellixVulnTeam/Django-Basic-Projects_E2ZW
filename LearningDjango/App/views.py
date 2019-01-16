from django.shortcuts import render, redirect
from django.views import View
from .models import Person


class SaveData(View):

	def get(self, request):
		data = Person.objects.all()
		return render(request, "index.html", {"data":data})

	def post(self, request):
		person = Person(
			first_name = request.POST["fname"],
			last_name = request.POST["lname"],
			email = request.POST["email"],
			address = request.POST["address"]
		)
		person.save()
		success = "Data inserted!"

		return render(request, "index.html", {"success":success})


class UpdateData(View):

	def get(self, request, id):
		edit_data = Person.objects.get(id=id)
		return render(request, "index.html", {"edit_data":edit_data})

	def post(self, request, id):
		edit_data = Person.objects.get(id=id)
		edit_data.first_name = request.POST["fname"]
		edit_data.last_name = request.POST["lname"]
		edit_data.email = request.POST["email"]
		edit_data.address = request.POST["address"]
		edit_data.save()
		success = "Data updated!"

		return redirect("/", {"success":success})



class LoginView(View):

	def get(self, request):
		return render(request, "login.html")

	def post(self, request):
		fname = request.POST["fname"]
		email = request.POST["email"]
		query = "SELECT * FROM emp_table WHERE first_name = {} AND email = {}".format(fname, email)

		if Person.objects.raw(query):
			return redirect("/")
		else:
			return redirect("/login/")
		




		