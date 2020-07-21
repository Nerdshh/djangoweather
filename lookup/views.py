from django.shortcuts import render

def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89117&distance=5&API_KEY=24E04444-E0A5-4617-9E34-7D1C2BFF2DC0")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89117&distance=5&API_KEY=24E04444-E0A5-4617-9E34-7D1C2BFF2DC0
	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})