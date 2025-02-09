from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = models.Manager()

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
    
class Employee(models.Model):
    name = models.CharField(max_length = 300)
    id_number = models.CharField(max_length = 300)
    rate = models.FloatField(null=0)
    overtime_pay = models.FloatField(null=0)
    allowance = models.FloatField(null=0) 
    objects = models.Manager()
    def getName(self):
        return self.name 
    
    def getID(self):
        return self.id_number
    
    def getRate(self):
        return self.rate
    
    def getOvertime(self):
        return self.overtime_pay
    
    def resetOvertime(self):
        self.overtime_pay = 0
        return self.overtime_pay

    def getAllowance(self):
        return self.allowance
    
    def __str__(self):
        return "pk: " + self.id_number + ", rate: " + str(self.rate)
    
class Payslip(models.Model):
    id_number = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length = 300)
    date_range = models.CharField(max_length = 300)
    year = models.CharField(max_length = 300)
    pay_cycle = models.IntegerField(null=0)
    rate = models.FloatField(null=0)
    earnings_allowance = models.FloatField(null=0)
    deductions_tax = models.FloatField(null=0)
    deductions_health = models.FloatField(null=0)
    pag_ibig = models.FloatField(null=0)
    sss = models.FloatField(null=0)
    overtime = models.FloatField(null=0)
    total_pay = models.FloatField(null=0)
    objects = models.Manager()

    def getIDNumber(self):
        return self.id_number
    
    def getMonth(self):
        return self.month
    
    def getDate_range(self):
        return self.date_range
    
    def getYear(self):
        return self.year
    
    def getPay_cycle(self):
        return self.pay_cycle
    
    def getRate(self):
        return self.rate
    
    def getCycleRate(self):
        return self.rate/2
    
    def getEarnings_allowance(self):
        return self.earnings_allowance
    
    def getDeductions_tax(self):
        return self.deductions_tax
    
    def getDeductions_health(self):
        return self.deductions_health
    
    def getPag_ibig(self):
        return self.pag_ibig
    
    def getSSS(self):
        return self.sss
    
    def getOvertime(self):
        return self.overtime
    
    def getTotal_pay(self):
        return self.total_pay
    
    def __str__(self):
        return "pk: " + str(self.pk) + ", Employee: " + str(self.id_number) + ", Period: " + str(self.month) + " " + str(self.date_range) + ", " + str(self.year) + ", Cycle: " + str(self.pay_cycle) + ", Total Pay: " + str(self.total_pay)