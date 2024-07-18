from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,MembershipPlan,Trainer
# Create your views here.
def Home(request):
    return render(request,"index.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')
        
        if pass1!=pass2:
            messages.info(request,"Password does not match")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone number is taken")
                return redirect('/signup')
            
        except Exception as identifier:
            pass



        try: 
            if User.objects.get(email=email):
                messages.warning(request,"Email already in use")
                return redirect('/signup')

        except Exception as identifier:
            pass



        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request, "Registration successful! Please log in")
        return redirect('/login')

    return render(request,"signup.html")


def handlelogin(request):
    if request.method =="POST":
        username = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request,"Login successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/login')

    return render(request,"handlelogin.html")


def handlelogout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('/login')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us, we will get back to you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")


def enroll(request):
    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    return render(request,"enroll.html",context)