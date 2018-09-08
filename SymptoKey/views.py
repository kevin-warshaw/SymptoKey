from django.shortcuts import render
from SymptoKey.models import Symptoms


# Create your views here.
def UpdateChoices(request):
    block = request.POST.get['id']
    StoreInfo(request, block)

# Update relevant variables
def StoreInfo(request, block):
    if (block == "I'm feeling dizzy"):
        Symptoms.dizzy = True

# redirect to HTML page that tells patient to call 911 or go to ER
def DisplayEmergencyPage(request):
    return render(request, "homepage.html")

# redirect to HTML page that tells patient to schedule doctor's appointment
def DisplayAppointment(request):
    return render(request, "homepage.html")

# redirect to HTML page that tells patient to call doctor
def DisplayCallDoctor(request):
    return render(request, "homepage.html")

# redirect to HTML page that tells patient to wait out their symptoms
def DisplayLowRisk(request):
    return render(request, "homepage.html")
