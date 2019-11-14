from django.db.models import Count, Value, CharField
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Faculty,Student,Feedback
from django.contrib import messages
import csv
# Create your views here.
def showIndex(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def home(request):
    return redirect('main')
def aboutUs(request):
    return render(request,"aboutUs.html")

def contactUs(request):
    return render(request,"contact_us.html")

def getRegister(request):
    type=request.GET.get("usertype")
    if type== "Faculty":
        return render(request,"facultyRegister.html")
    else:
        return render(request,"studentRegistration.html")
def saveFaculty(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    email=request.POST.get("email")
    username=request.POST.get("username")
    password=request.POST.get("password")
    savedata=Faculty(Id_Number=id,Faculty_Name=name,Email_Id=email,username=username,password=password)
    savedata.save()
    messages.success(request,"your data saved sucessfully")
    return render(request,"facultyRegister.html")
def saveStudent(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    year=request.POST.get('year')
    branch=request.POST.get('branch')
    email=request.POST.get("email")
    username=request.POST.get("username")
    password=request.POST.get("password")
    stu_data=Student(Id_Number=id,Student_Name=name,Batch_year=year,Branch=branch,Email_Id=email,
            username=username,password=password)
    stu_data.save()
    messages.success(request,"your data saved sucessfully")
    return render(request,"studentRegistration.html")
def loginFacultyStudent(request):
    type=request.POST.get('usertype')
    uname=request.POST.get('username')
    pword=request.POST.get('password')
    if type== "Administrator":
        if uname=="admin" and pword=="admin":
            return redirect("/admin/")
        else:
            return render(request, "login.html", {"data": "invalid deatils"})
    elif type== "Faculty":
        try:
            data=Faculty.objects.get(username=uname,password=pword)
            request.session["username1"]=uname
        except:
            return render(request, "login.html", {"data": "invalid deatils"})
        if data:
            fs=request.session['username1']
            f_data=Faculty.objects.filter(username=fs)
            return render(request,"facultyHome.html",{"fdata":f_data})
        else:
            return render(request,"login.html",{"data":"invalid deatils"})
    elif type== "Student":
        try:
            data=Student.objects.get(username=uname,password=pword)
            request.session["username"] = uname
        except:
            return render(request, "login.html", {"data": "invalid deatils"})

        if data:
            sd = request.session["username"]
            stu_data = Student.objects.filter(username=sd)
            return render(request,"studentHome.html",{"data1":stu_data})
        else:
            return render(request,"login.html",{"data":"invalid deatils"})
    else:
        return render(request, "login.html", {"data": "invalid deatils"})

def logout(request):

        return redirect('login')

def saveFeedback(request):
    f=request.POST.get("feedback")
    f1=request.POST.get("feedback1")
    f2=request.POST.get("feedback2")
    f3=request.POST.get("feedback3")
    feed_text=request.POST.get("feed-text")
    feedback=Feedback(Sundaram=f,Rejina=f1,Kiranmai=f2,Shilpa=f3,College_feedback_review=feed_text)
    feedback.save()
    messages.success(request,"thanks for your valueable feedback")
    return redirect('logout')

def logoutf(request):

        return redirect('login')

def viewfeedback(request):

    data=Feedback.objects.all()

    c=Feedback.objects.annotate(count=Count("Sundaram")).values("Sundaram",'count').filter(count=1)
    count=0
    count1=0
    count2=0
    for x in c :
        for y in x:
            if x[y]=="Excellent":
                count=count+1
            if x[y]=="Good":
                count1=count1+1
            if x[y]=="Need to improve":
                count2=count2+1
    k = Feedback.objects.annotate(count=Count("Kiranmai")).values("Kiranmai", 'count').filter(count=1)
    kcount = 0
    kcount1 = 0
    kcount2 = 0
    for x in k :
        for y in x:
            if x[y]=="Excellent":
                kcount=kcount+1
            if x[y]=="Good":
                kcount1=kcount1+1
            if x[y]=="Need to improve":
                kcount2=kcount2+1
    r = Feedback.objects.annotate(count=Count("Rejina")).values("Rejina", 'count').filter(count=1)
    rcount = 0
    rcount1 = 0
    rcount2 = 0
    for x in r:
        for y in x:
            if x[y] == "Excellent":
                rcount = rcount + 1
            if x[y] == "Good":
                rcount1 = rcount1 + 1
            if x[y] == "Need to improve":
                rcount2 = rcount2 + 1
    s = Feedback.objects.annotate(count=Count("Shilpa")).values("Shilpa", 'count').filter(count=1)
    scount = 0
    scount1 = 0
    scount2 = 0
    for x in s:
        for y in x:
            if x[y] == "Excellent":
                scount = scount + 1
            if x[y] == "Good":
                scount1 = scount1 + 1
            if x[y] == "Need to improve":
                scount2 = scount2 + 1

    return render(request,"feedback.html",{"data":data,"c1":count,"c2":count1,"c3":count2,"kc1":kcount,"kc2":kcount1,"kc3":kcount2,"rc1":rcount,"rc2":rcount1,"rc3":rcount2,"sc1":scount,"sc2":scount1,"sc3":scount2})




def downloadfeedback(request):
    response=HttpResponse(content_type='text/csv',)
    response['content-disposition']='attachment;filename="feedbacks.csv"'

    writer=csv.writer(response)
    fd=Feedback.objects.all()
    writer.writerow(['Feedback_id', 'sundaram', 'Rejina', 'kiranmai', 'shila', 'college_feedback'])
    for x in fd:
        writer.writerow([x.Feedback_ID,x.Sundaram,x.Rejina,x.Kiranmai,x.Shilpa,x.College_feedback_review])
    return response
def dc(request):
    c = Feedback.objects.annotate(count=Count("Sundaram")).values("Sundaram", 'count').filter(count=1)
    count = 0
    count1 = 0
    count2 = 0
    for x in c:
        for y in x:
            if x[y] == "Excellent":
                count = count + 1
            if x[y] == "Good":
                count1 = count1 + 1
            if x[y] == "Need to improve":
                count2 = count2 + 1
    k = Feedback.objects.annotate(count=Count("Kiranmai")).values("Kiranmai", 'count').filter(count=1)
    kcount = 0
    kcount1 = 0
    kcount2 = 0
    for x in k:
        for y in x:
            if x[y] == "Excellent":
                kcount = kcount + 1
            if x[y] == "Good":
                kcount1 = kcount1 + 1
            if x[y] == "Need to improve":
                kcount2 = kcount2 + 1
    r = Feedback.objects.annotate(count=Count("Rejina")).values("Rejina", 'count').filter(count=1)
    rcount = 0
    rcount1 = 0
    rcount2 = 0
    for x in r:
        for y in x:
            if x[y] == "Excellent":
                rcount = rcount + 1
            if x[y] == "Good":
                rcount1 = rcount1 + 1
            if x[y] == "Need to improve":
                rcount2 = rcount2 + 1
    s = Feedback.objects.annotate(count=Count("Shilpa")).values("Shilpa", 'count').filter(count=1)
    scount = 0
    scount1 = 0
    scount2 = 0
    for x in s:
        for y in x:
            if x[y] == "Excellent":
                scount = scount + 1
            if x[y] == "Good":
                scount1 = scount1 + 1
            if x[y] == "Need to improve":
                scount2 = scount2 + 1
    response = HttpResponse(content_type='text/csv', )
    response['content-disposition'] = 'attachment;filename="feedbackcounts.csv"'

    writer = csv.writer(response)

    writer.writerow(['NAME', 'EXCELENT', 'GOOD', 'NEED TO IMPROVE'])
    writer.writerow(['SUNDARAM',count,count1,count2])
    writer.writerow(['KIRANMAI', kcount, kcount1, kcount2])
    writer.writerow(['REJINA', rcount, rcount1, rcount2])
    writer.writerow(['SHILPA', scount, scount1, scount2])
    return response

def addFaculty(request):
    return render(request,"AddFaculty.html")

def addFaculty1(request):
    fname=request.POST.get("af")
    Feedback.objects.all().annotate(mycolumn=Value(fname, output_field=CharField()))
    return render(request,"AddFaculty.html")