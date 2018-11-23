from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LoanInfo(models.Model):
    loanno = models.CharField(max_length=6,unique=True)
    loantype = models.CharField(max_length=20)
    loanprovider = models.CharField(max_length=30)
    loanamt = models.DecimalField(max_digits=10,decimal_places=2)
    loanduration = models.DurationField()
    loanintr = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return self.loanno+",Type =  "+self.loantype

class UserLoanInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    address = models.CharField(max_length=264)
    #loan1 = models.ForeignKey(LoanInfo,blank=True,on_delete=models.PROTECT)
    #loan2 = models.ForeignKey(LoanInfo,blank=True,on_delete=models.PROTECT)
    #loan3 = models.ForeignKey(LoanInfo,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username
