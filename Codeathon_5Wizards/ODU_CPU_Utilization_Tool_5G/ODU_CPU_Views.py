from django.shortcuts import render

# Create your views here.

def odu_cpu_homepage(request):
    return render(request,"ODU_CPU_Utilization_Pages/odu_cpu_homepage.html")

def odu_cpu_calculation(request):
    return render(request, "ODU_CPU_Utilization_Pages/odu_cpu_homepage.html")
