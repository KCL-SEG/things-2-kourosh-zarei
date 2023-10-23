from django.shortcuts import render
from things import forms


def home(request):
    form = (
        forms.ThingForm(request.POST) if request.method == "POST" else forms.ThingForm()
    )
    return render(request, "home.html", {"form": form})
