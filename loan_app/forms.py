from django import forms
from django.contrib.auth.models import User
from loan_app.models import UserLoanInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','email','username','password')

class UserLoanInfoForm(forms.ModelForm):
    class Meta():
        model = UserLoanInfo
        fields = ('address',)  #add loan1,loan2,loan3
