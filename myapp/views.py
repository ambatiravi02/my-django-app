from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
import datetime
from django.template import loader
from myapp.form import StudentForm
from myapp.functions.function import handle_uploaded_file  
import csv
from myapp.models import Employee
# Create your views here.
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  

def index(request):  
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html) 

def index(request):  
    a = 1  
    if a:  
        return HttpResponseNotFound('<h1>Page not found</h1>')  
    else:  
        return HttpResponse('<h1>Page was found</h1>')
    
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')  

def index(request):  
   template = loader.get_template('myapp/index.html') 
   return HttpResponse(template.render())

def index(request):  
    template = loader.get_template('myapp/index.html')
    name = {  
        'student':'rahul'  
    }  
    return HttpResponse(template.render(name))  

def index(request):  
    student = StudentForm()  
    return render(request,"myapp/register.html",{'form':student}) 

def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"myapp/register.html",{'form':student})  
    
def setsession(request):  
    request.session['sname'] = 'irfan'  
    request.session['semail'] = 'irfan.sssit@gmail.com'  
    return HttpResponse("session is set")  
def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail);  

def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['java-tutorial']  
    return HttpResponse("java tutorials @: "+  tutorial);  

def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response  

def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    employees = Employee.objects.all()  
    writer = csv.writer(response)  
    for employee in employees:  
        writer.writerow([employee.eid,employee.ename,employee.econtact])  
    return response  

def login(request):  
   template = loader.get_template('myapp/login.html') 
   return HttpResponse(template.render())