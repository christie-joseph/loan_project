from django.contrib import admin
from loan_app.models import LoanInfo,UserLoanInfo

# Register your models here.

admin.site.register(LoanInfo)
admin.site.register(UserLoanInfo)
