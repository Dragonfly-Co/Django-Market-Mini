from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class BaseView(View):

    def get(self, request):
        return render(request, 'index.html')

class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')

class ProductsVies(View):

    def get(self, request): 
        return render(request, 'product.html')

class ContactView(View):

    def get(self, request): 
        return render(request, 'contact.html')