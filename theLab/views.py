from django.shortcuts import render
from django.http import HttpResponse
tax_rate=0.15
# Create your views here.
def homePage(request):
    return render(request,"theLab/homePage.html")

def anyNumber(request, num):
    return render(request, "theLab/taxCalculator.html", {
        "num": num, "totprice": tax_rate*num+num})
    

def taxrate(request):
    return render(request, "theLab/taxRate.html", {
        "taxRate":tax_rate*100
    })
