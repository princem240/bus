from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Bus,book
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import contactform,bform,bookform

# Create your views here.
def home(request):
   
 return render(request,'home.html')

@login_required(login_url='/login')
def view(request):
 return render(request,'view.html')

def filter(request):
 From=request.POST.get('from')
 
 to=request.POST.get('to')
 date=request.POST.get('date')
 
 b=Bus.objects.filter(From=From,To=to,date=date,username_id=1)
 return render(request,'view.html',{'b':b})

def b(request,bus_id):
  if request.method=="POST":
     
     b=Bus.objects.get(id=bus_id)
     user=request.user
     seat = ','.join(request.POST.getlist('check'))
     no=seat.count(",") + 1
     ticket = book(busid=b.id,name=b.name,From=b.From,To=b.To,timefrom=b.timefrom,timeto=b.timeto,date=b.date,duration=b.duration,price=b.price,tp=b.price*no,username=user,seatno=seat)
     ticket.save()
     
     
    
     
    
     

     
     return redirect('/')
  
       
  
 
 
 
 
  else:

   b=book.objects.filter(busid=bus_id)
   
   return render(request,'book.html',{'b':b})


def login(request):
 if  request.method == 'POST':
     u1=request.POST['u1']
     p1=request.POST['p1']
     user=auth.authenticate(username=u1,password=p1)

     if user:
        auth.login(request,user)
        return redirect('/')
     else:
        messages.info(request,"invalid")
        return render(request,'login.html')
 else:
      
   
    return render(request,'login.html')


def register(request):

 if request.method == 'POST':
       n1=request.POST['n1']
      
       u1=request.POST['u1']
       e1=request.POST['e1']
       p1=request.POST['p1']
       
       
       
       if User.objects.filter(username=u1).exists():
             messages.info(request,"username taken")
             return render(request,'register.html')
       elif User.objects.filter(email=e1).exists():
             messages.info(request,"email taken")
             return render(request,'register.html')
       else:
            user=User.objects.create_user(username=u1,email=e1,first_name=n1,password=p1)
            user.save()
            return redirect('/')
   
          
   
 else:
      return render(request,'register.html') 
  
def logout(request):
   auth.logout(request) 
   return redirect('/') 

def about(request):
   
 return render(request,'about.html')



def contact(request):
 
  if request.method=="POST":
   if  request.user.is_authenticated:
     form=contactform(request.POST,request.FILES)

     if form.is_valid():
         form=form.save(commit=False)
         form.username=request.user
         form.save()
         return redirect('/')
     else:
        form=contactform()
        return render(request,'contact.html',{'form':form})
   else:
    return redirect('/login')
  else: 
      form=contactform()
      return render(request,'contact.html',{'form':form})
  

def bookings(request):
 
 if book.objects.filter(username_id=request.user.id).exists():
  b=book.objects.filter(username=request.user)
  name = 'seatno'
  obj = book.objects.first()
  seat= getattr(obj,name)
  name = 'price'
  o= book.objects.first()
  price= getattr(o,name)
#   tp=seat*price
   
  return render(request,'bookings.html',{'b':b})
 else:
    return render(request,'bookings.html')

# def Book(request,bus_id):
  
  
#   if request.method=="POST":
     
#      b=Bus.objects.get(id=bus_id)
    
#      c=book.objects.get(id=3)
#      if book.objects.filter(busid=bus_id,username_id=request.user).exists():
#       c1=book.objects.get(busid=bus_id,username_id=request.user)
#       a=bookform(request.POST,request.FILES,instance=c1)
#      else:
#       a=bookform(request.POST,request.FILES) 
     
#      u=25648
#    #   c.name=b.name
#    #   c.From=b.From
#    #   c.To=b.To
#    #   c.timefrom=b.timefrom
#    #   c.timeto=b.timeto
#    #   c.date=b.date
#    #   c.price=b.price
     

#      if a.is_valid():
#          a=a.save(commit=False)
#          a.username=request.user
         
#          a.busid=b.id
#          a.name=b.name
#          a.From=b.From
#          a.To=b.To
#          a.timefrom=b.timefrom
#          a.timeto=b.timeto
#          a.date=b.date
#          a.price=b.price
#          a.tp=b.price*a.seatno
         



#          a.save()
#          return redirect('/')
#      else:
#         b=Bus.objects.get(id=bus_id)
#         a=book.objects.get()
#         form=bform(instance=b)
#         a=bookform()
#         return render(request,'bookform.html',{'form':form,'a':a})
  
#   else: 
#       b=Bus.objects.get(id=bus_id)
#       form=bform(instance=b)
#       a=bookform()
#       return render(request,'bookform.html',{'form':form,'a':a})
# 
# 
 
 
 
 
 
 
def  cancel(request,bus_id):

   b=book.objects.get(id=bus_id,username_id=request.user)
   b.delete()
   return redirect('/')

   



 
   
 


   
 







