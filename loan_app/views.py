from django.shortcuts import render
from loan_app.forms import UserForm, UserLoanInfoForm
from loan_app.models import LoanInfo
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request,'loan_app/index.html')

def home(request):
    if request.method == 'POST' :
        loanamtinput = request.POST.get('loanamtinput',None)
        loaninstallment = request.POST.get('loaninstallment',None)
        loantype = request.POST.get('loanlist',None)
        print(loanamtinput)
        print(loaninstallment)
        print(loantype)
        return HttpResponse("Loan edukand pani eduth paisa undaku malaree")
    else:
        loanlist = LoanInfo.objects.values_list('loantype',flat=True).distinct()
        #print(loanlist)
        return render(request,'loan_app/home.html',{'loanlist':loanlist})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account Not Active")
        else:
            return HttpResponse("Invalid Login Credentials")
    else:
        return render(request,'loan_app/login.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def signup(request):
    registered = False
    if(request.method == "POST"):
        user_form = UserForm(data=request.POST)
        loaninfo_form = UserLoanInfoForm(data=request.POST)

        if(user_form.is_valid() and loaninfo_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            loaninfo = loaninfo_form.save(commit=False)
            loaninfo.user = user
            loaninfo.save()

            registered = True
            return  HttpResponse("Successfully Registered")
            return HttpResponseRedirect(reverse('index'))

        else:
            print(user_form.errors,loaninfo_form.errors)

    else:
        user_form = UserForm()
        loaninfo_form = UserLoanInfoForm()

    return render(request,'loan_app/signup.html',
                            {'user_form':user_form,
                              'loaninfo_form':loaninfo_form,
                              'registered':registered})
