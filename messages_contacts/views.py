from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    var = "hi Brian. Are you happy there?"
    dictionary_ = {
        "var":var,
    }
    return render(request,'messages_contacts_index.html', context=dictionary_)
