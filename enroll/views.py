from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import  StudentRegistration
# Create your views here.
from .models import  User



def home(request):
    form=StudentRegistration()
    stud=User.objects.all
    return render(request,'enroll/home.html',{'form':form,'stu':stud})


def save_data(request):
    if request.method=="POST" :
        form=StudentRegistration(request.POST)
        if form.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            sid=request.POST.get('stuid')


# in case of save the data, sid will be null
            if (sid==""):
                usr=User(name = name,email = email,password = password)
            # here "usr" is model instance
            else:
                usr=User(id=sid,name = name,email = email,password = password)

            usr.save()

            # //we have to pass the data model as a list 
            stud=User.objects.values()
            # print(stud)
            
            student_data=list(stud)
            # here we send the response as dictionary
            return JsonResponse({"status":1,'student_data':student_data})
        else:
            return JsonResponse({'status':False})
    else:
        return JsonResponse({'error': 'Only POST method allowed'})


def delete_data(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        print(id)
        # map the id with primary key of model
        pi=User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


def edit_data(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        print(id)

        student=User.objects.get(pk=id)

        student_data={'id':student.id,"name":student.name,"email":student.email,"password":student.password}

        return JsonResponse(student_data)


    