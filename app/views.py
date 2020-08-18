from django.shortcuts import render
from. models import Login,Category,Staff,Room,Customer,Booking,Service,Custservice
from.forms import ProfileForm,ServiceForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    Lusername=request.POST['username']
    Lpassword=request.POST['pass']
    m=Login.objects.get(username=Lusername)
    if m.password==Lpassword:
        return render(request,'savecustomer.html')
    else:
        return render(request,'index.html',{'error':"incorrect password" })

def add_staff(request):
    return render(request,"staff.html")

def save_detail(request):
    s1=Staff()
    l1=Login()
    s1.name=request.POST['name']
    s1.email=request.POST['email']
    s1.phone=request.POST['phone']
    s1.address=request.POST['address']
    s1.gender=request.POST['gender']
    s1.salary=request.POST['salary']
    s1.designation=request.POST['designation']
    l1.username=s1.email
    l1.password=request.POST['pass']
    l1.save()
    s1.staffs=l1
    s1.save()
    return render(request,'index.html')

def add_category(request):
    return render(request,'category.html')
    
def save_category(request):
    c=Category()
    c.cname=request.POST['category']
    c.description=request.POST['description']
    #new
    c.charges=request.POST['charge'] 
    c.save()
    return render(request,'savecustomer.html',{'error':'category_added'})  

def rooms(request):
    s=Category.objects.all()
    return render(request,'room.html',{'list1':s})


def save_room(request):
    rom=Room( )
    rom.room_no=request.POST['room_no']
    rom.description=request.POST['description']
    k=request.POST.getlist('checks')
    print(k,"hello")
    for items in k:
        blue=Category.objects.get(id=items)
        rom.categories=blue
    rom.save()
    return render(request,'savecustomer.html',{'error':'rooms_added'})  


def saveprofile(request):
        pf=ProfileForm()
        return render(request,"customer.html",{'form':pf})    

def dataadd(request): 
  print("hello")  
  profile_form=ProfileForm(request.POST,request.FILES)
  print("hello")
  if profile_form.is_valid():
            print("hello")
            p=Customer()
            selected_room=profile_form.cleaned_data["room_display"]
            p.name=profile_form.cleaned_data["name"]
            p.email=profile_form.cleaned_data["email"]
            p.phone=profile_form.cleaned_data["phone"]
            p.address=profile_form.cleaned_data["address"]
            p.adhaar=profile_form.cleaned_data["adhaar"]       
            p.save()
            b=Booking() 
            b.chechin_date=request.POST['checkin']
            b.chechout_date=request.POST['checkout'] 
            b.no_of_person=request.POST['num']
            b.cust=p
            print("hello",b.cust)
            for r in selected_room:
                z=str(r)
                k=z.split()
                am=k[0]    
            booking_list=Booking.objects.all()
            
            for items in booking_list:
                print(items.rom.room_no,'hi')
                if items.rom.room_no in am:    
                      return render(request,"savecustomer.html",{'error':"room addition operation  failed try adding different room"})
                else:  
                      b.rom=Room.objects.get(room_no=am)    
                      b.save()
                      print("hello ji",p.id)
                      s=Service()
                      for item in booking_list:
                              s.name=item.rom.categories.cname
                              s.description=item.rom.categories.description
                              s.charges=item.rom.categories.charges
                              s.save() 
                              pin=Custservice()
                              pin.customers=p
                              pin.services=s
                              pin.save()       
                              return render(request,'savecustomer.html',{'error':'customer_added and charge'})
                      return render(request,'savecustomer.html',{'error':'customer_added'})
            b.rom=Room.objects.get(room_no=am)    
            b.save()
            return render(request,'savecustomer.html',{'error':'customer_added'})      
  else:
        return render(request,'savecustomer.html',{'error':'customer_not_valid'})               
                  
                 
    
def addbook(request):
    b=Booking() 
    b.chechin_date=request.POST['checkin']
    b.chechout_date=request.POST['checkout'] 
    b.no_of_person=request.POST['num']
    m=request.POST.getlist('checks')
    
def services(request):
    return render(request,'addservice.html')
    
def addservice(request):
    s=Service()
    s.name=request.POST['name']
    s.description=request.POST['description']
    s.charges=request.POST['charges']
    s.save()
    return render(request,'savecustomer.html',{'error':'service_added'})

def custservice(request):
    pf=ServiceForm()
    return render(request,"service.html",{'form':pf}) 

def addservice_cust(request):
  service_form=ServiceForm(request.POST)
  if service_form.is_valid():
            p=Custservice()
            name=service_form.cleaned_data["cust_display"]
            service_=service_form.cleaned_data["service_display"]   
            for i in name:
                tu=str(i)
                sh=tu.split()
            n=sh[0] 
            print("hi",n)  
            for e in service_:
                tus=str(e)
                sha=tus.split()
            nn=sha[0]
             
            p.customers=Customer.objects.get(name=n)
            p.services=Service.objects.get(name=nn)
            p.save()
            return render(request,'savecustomer.html',{'error':'service_added'})
        
def customerview(request):
    m=Customer.objects.all() 
    return render(request,'customerview.html',{'list1':m})       

def bill(request,id):
    l=Custservice.objects.all()
    b=Booking.objects.all()
    s=Service()
    cust_id=id      
    list2=list()
    for item in l:
        if cust_id==item.customers.id:
            list2.append(item.services)
    sum=0
    for item in list2:
        sum=sum+item.charges      
    list2.append(sum)         
    return render(request,'bill.html',{'list3':list2})

def delete(request,id):
    p=Customer.objects.get(id=id)
    p.delete()
    m=Customer.objects.all() 
    return render(request,'customerview.html',{'list1':m})        
