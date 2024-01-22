from django.shortcuts import render

# Create your views here.

# home page
def home_page_view(request):

    return render(request, "main/index.html")

# contact page 
def contact_page_view(request):

    return render(request, 'main/contact.html')

# portfolio page
def portfolio_page_view(request):

    return render(request, 'main/portfolio-details.html')