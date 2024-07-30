from django.shortcuts import render,HttpResponse,redirect
from messageapp.models import Msg

# Create your views here.

def testing(request):
    return HttpResponse("hello welcome to messaging app")
    
def create(request):
    print("requst is :" , request.method)
    if request.method== "GET":
        return render(request,'create.html')
    else:
        # FETCH DATA
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        m_num = request.POST['number']
        e_mail = request.POST['email']
        # pass_word = request.POST['password']
        # print("first_name :", f_name)
        # print("last_name :", l_name)
        # print("mob_num :", m_num)
        # print("e_mail :", e_mail)
        # print("pass_word :", pass_word)        
        # insert>>
        m = Msg.objects.create(fname=f_name,lname=l_name,mobile=m_num,email=e_mail)
        m.save()
        # return HttpResponse("data inserted successfully")
        return redirect('/dashboard')
def dashboard(request):
    m=Msg.objects.all()  #to fetch all query set
    print(m)
    context = {}
    context['data']= m
    # return HttpResponse("data fetched successfully")
    return render(request,'dashboard.html',context)

def delete(requset,rid):
    # print('id to be deleted :' , rid)
    # return HttpResponse("'id to be deleted :'" + rid)
    m = Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')

def edit(request,rid):
        # return HttpResponse("data inserted successfully")
        # return HttpResponse("'id to be edited :'" + rid)
         
    d = Msg.objects.get(id=rid)
    if request.method=='POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        m_num = request.POST['number']
        e_mail = request.POST['email']
        s=Msg.objects.filter(id=rid).update(fname=f_name,lname=l_name,mobile=m_num,email=e_mail)
        # return HttpResponse("data inserted successfully")
        return redirect('/dashboard')
    context = {}
    context['data'] = d
    return render(request,'edit.html',context)