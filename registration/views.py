from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import AddGymForm, FindGymForm
from registration.models import Gym
from django.contrib.gis.geos import Point, GEOSGeometry
import requests
#r.json()["rows"][0]['elements'][0]['distance']['text']
location = ""


class HomeView(View):

	def get(self, request, *args, **kwargs):
		return render(request, "home.html", {})

class UserDetailView(View):

	def get(self, request, *args, **kwargs):
		return render(request, "user.html", {})

class AddGymView(View):

	def get(self, request, *args, **kwargs):
		form = AddGymForm()
		return render(request, "addgym.html", { "form": form, })

	def post(self, request, *args, **kwargs):
		if request.POST['location']=='':
			form = AddGymForm(request.POST)
			form.errors['location'][0]=form.errors['location'][0].replace("No geometry value provided.", "Gym location not set!")
			return render(request, "addgym.html", { "form": form,})

		obj = Gym.objects.create(name=request.POST['name'], location=request.POST['location'], contact_no=request.POST['contact_no'])
		obj.save()

		return HttpResponse("Gym added successfully.")

class FindGymView(View):

	def get(self, request, *args, **kwargs):
		form = FindGymForm()
		return render(request, "gymfinder.html", { "form": form, })

	def post(self, request, *args, **kwargs):
		print(request.POST)
		if request.POST['location']=='':
			form = FindGymForm(request.POST)
			form.errors['location'][0]=form.errors['location'][0].replace("No geometry value provided.", "Need your location to find nearby gyms!")
			return render(request, "gymfinder.html", { "form": form,})
		radius = int(request.POST['max_distance'])
		location = GEOSGeometry(request.POST["location"])
		location = Point(location.coords)
		area = location.buffer(radius/ 40000 * 360)
		gyms_found = list(Gym.objects.all())

		for i in range(len(gyms_found)):
			dist = requests.get("http://maps.googleapis.com/maps/api/distancematrix/json?origins="+ str(location.coords[1]) +","+str(location.coords[0])+"&destinations="+ str(gyms_found[i].location.coords[1]) +","+str(gyms_found[i].location.coords[0])).json()["rows"][0]['elements'][0]['distance']['text'].split(" ")[0]
			gyms_found[i] = (gyms_found[i], dist)

		gyms_found = list(filter(lambda gym: float(gym[-1])<radius, gyms_found))

		context = {
			"gyms_found": len(gyms_found),
			"max_distance": radius,
			"gyms": gyms_found,
			"location":location,
		}
		return render(request, "gyms_found.html", context)

class LandingView(View):

	def get(self, request, *args, **kwargs):
		return render(request, "dash.html", {})


class GymDetailView(View):

	def get(self, request, pk, *args, **kwargs):
		print(request.GET, args, kwargs)
		gym = Gym.objects.get(pk=pk)
		location = Point((float(request.GET.get("latitude")), float(request.GET.get("longitude"))))
		context = {
		"gym": gym,
		"location":location
		}
		return render(request, "gymdetail.html", context)

class SubscribeView(View):

	def get(self, request, *args, **kwargs):
		return render(request, "sub.html", {})