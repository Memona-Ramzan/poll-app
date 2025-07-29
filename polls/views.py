from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choices
# Create your views here.
# def index(request):
#     return HttpResponse("hello django")
def listining_ques(request):
    Question_data=Question.objects.prefetch_related("choices").all()
    return render(request,"Question.html",{"data":Question_data})
    # Fetch all records

def voting(request):
    selected_choices = []  # to store user's selected choice objects

    if request.method == "POST":
        for key in request.POST:
            if key.startswith('choices_'):
                choice_id = request.POST[key]
                choice = Choices.objects.get(id=choice_id)
                choice.votes += 1
                choice.save()

                selected_choices.append(choice)  # save this choice to show in result

    return render(request, "result.html", {"selected_choices": selected_choices})
