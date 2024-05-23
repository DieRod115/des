from django.shortcuts import render, HttpResponse

html_base = """
    <h1> Pagina en construccion </h1>
    <ul>
        <li><a href="/">U</a></li>
        <li><a href="/about/">R</a></li>
        <li><a href="/contact/">E</a></li>
        <li><a href="/pago/">p</a></li>
    </ul>


"""

# Create your views here.
def base(request):
    return render(request, "home/base.html")
def home(request):
    return render(request, "home/home.html")
def about(request):
    return render(request, "home/about.html")
def contact(request):
    return render(request, "home/contact.html")
def pago(request):
    return render(request, "home/pago.html")
                  
