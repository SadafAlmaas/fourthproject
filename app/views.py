from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':100,'b':34,'c':31}
    return render(request,'conditional.html',d)