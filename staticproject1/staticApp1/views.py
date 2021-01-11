from django.shortcuts import render

# Create your views here.
def view1(request):
    myName="nammu"
    favPlayer="sehwag"
    favAnimal="dog"
    favSubject="sql"
    d={'name':myName,'player':favPlayer,'animal':favAnimal,'subject':favSubject}
    return render(request,'staticApp1/1.html',d)