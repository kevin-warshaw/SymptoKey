from django.shortcuts import render
from SymptoKey.models import Symptoms


# Create your views here.
def UpdateChoices(request):
    block = request.POST.get['id']
    StoreInfo(request, block)
    #Hide(request, block)
    #DisplayNextBlocks()

# Update relevant variables
def StoreInfo(request, block):
    if (block == "I'm feeling dizzy"):
        Symptoms.dizzy = True

'''
# Mark the block itself and all associated blocks as hidden
def Hide(request, block):
    if request.method == 'POST':
        document.getElementByID(block).style.visibility = "hidden"
'''
'''
# If following blocks not empty, mark them as not hidden
def DisplayNextBlocks(request):
    return render(request, "homepage.html")
'''

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
