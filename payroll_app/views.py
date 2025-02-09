from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Employee, Payslip
from django.contrib import messages

# Create your views here.

id = 0

def View_main(request):
    return render(request, 'LazapeeApp/base.html')

def Welcome(request):
    return render(request, 'LazapeeApp/welcome.html')

# Account
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(Account.objects.filter(username=username, password=password)):
            global id
            id = username
            return redirect('employeelist')
        else:
            messages.error(request, 'Invalid login')
            return render(request, 'LazapeeApp/login.html')
    else:
        # Render the login form when the request method is GET
        return render(request, 'LazapeeApp/login.html')

def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if Account.objects.filter(username=username).exists():
            messages.error(request, 'Account already exists')
            return redirect('signup')
        
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
        
        else:
            Account.objects.create(username=username, password=password)
            messages.success(request, 'Account created successfully')
            return redirect('login') 
    else:
        return render(request, 'LazapeeApp/signup.html')

# this works properly
def Logout(request):
    return redirect('LazapeeApp/login.html')


# EMPLOYEES 
def EmployeeList(request):
    employees = Employee.objects.all()
    return render(request, 'LazapeeApp/employeelist.html', {'employees': employees})

def Add_employees(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        id_number = int(request.POST.get('id_number'))
        if id_number < 0:
            messages.error(request, 'Invalid ID number.')
            return redirect ('add_employees')
        else:
            pass
        rate = float(request.POST.get('rate'))
        if rate < 0:
            messages.error(request, 'Invalid Rate.')
            return redirect ('add_employees')
        else:
            pass
        allowance = float(request.POST.get('allowance'))
        if allowance < 0:
            messages.error(request, 'Invalid Allowance.')
            return redirect ('add_employees')
        else:
            pass
    
        if(allowance == ''):
            allowance = 0

        if Employee.objects.filter(id_number=id_number).exists():
            messages.error(request, 'An employee with this ID already exists')
            return redirect('add_employees')

        Employee.objects.create(
            name=name,
            id_number=id_number,
            rate=rate,
            allowance=allowance,
            overtime_pay=0
        )
        return redirect('employeelist')

    else: 
        return render(request, 'LazapeeApp/add_employees.html')

def Update_employee(request, pk):
    
    if request.method =='POST':
        rate = request.POST.get('update_rate')
        allowance = request.POST.get('update_allowance')
        Employee.objects.filter(pk=pk).update(rate=rate, allowance=allowance)
        messages.success(request, "Employee Information Has Been Updated.", extra_tags='alert-success')
        return redirect('employeelist')
    else:
        emp = get_object_or_404(Employee, pk=pk)
        return render(request, 'LazapeeApp/update_employee.html', {'employees': emp})
    
def Delete_employee(request, pk):
    Employee.objects.filter(pk=pk).delete()
    return redirect('employeelist')

def Overtime(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method=='POST':
        overtime = float(request.POST.get('overtime_hours'))
        if overtime < 0:
            messages.error(request, 'Invalid Hour Input.')
            return redirect ('employeelist')
        else:
            pass
        emp.overtime_pay += round((emp.rate/160) * 1.5 * overtime, 2)
        Employee.objects.filter(pk=pk).update(overtime_pay=emp.overtime_pay)
        return redirect('employeelist')
    else:
        return redirect(request, 'LazapeeApp/employeelist.html')



# PAYROLL : creation + list
def Payroll(request):
    global id
    if (request.method == 'POST'):
        employees_id = request.POST.get('employeeid')
        if employees_id == "Select employee":
            messages.error(request, 'Please Select Employee.')
            return redirect('payroll')
        else:
        
            try: 
                if employees_id == 'ALL':
                    list_convert = list(Employee.objects.all().values_list('id_number', flat=True))
                    
                else:
                    list_convert = []
                    list_convert.append(employees_id)

            except Employee.DoesNotExist:
                return redirect('employeelist')
            
            for i in list_convert:
                month = request.POST.get('month')
                year = request.POST.get('year')
                if year == '':
                    messages.error(request, 'Please Input Year.')
                    return redirect ('payroll')
                else:
                    pass
                cycle = request.POST.get('cycle')
                if cycle == 'Select cycle':
                    messages.error(request, 'Please Select Cycle.')
                    return redirect ('payroll')
                else:
                    cycle = int(cycle)

                emp = get_object_or_404(Employee, id_number=i)
                xid = emp.id_number
                rate = emp.rate
                allowances = emp.allowance
                overtime = emp.overtime_pay
                payslip_list = list(Payslip.objects.filter(id_number=emp))
                #print(payslip_list)

                for empps in payslip_list:
                    if empps.month == month and empps.year == year and empps.pay_cycle == cycle:
                        messages.error(request, 'Payslip already exists.')
                        return redirect('payroll')
                    else:
                        pass
        
                if cycle == 1:
                    tax = ((rate/2) + allowances + overtime - 100) * 0.2
                    total = round(((rate/2) + allowances + overtime -100) - tax, 2)

                    payslip = Payslip.objects.create(
                        id_number = emp,
                        month=month,
                        date_range = '1-15',
                        year=year,
                        pay_cycle = cycle,
                        rate=rate,
                        earnings_allowance = allowances,
                        deductions_tax = tax,
                        deductions_health = 0,
                        pag_ibig=100,
                        sss=0,
                        overtime = overtime,
                        total_pay = total
                    )
                    
                    payslip.save()
                    Employee.objects.filter(id_number=xid).update(overtime_pay=0)
                    messages.success(request, "Payslip created successfully.")
                    
                elif cycle == 2:
                    PhilHealth = rate * 0.04
                    SSS = rate * 0.045
                    tax = ((rate/2) + allowances + overtime - PhilHealth - SSS) * 0.2
                    total = round(((rate/2) + allowances + overtime - PhilHealth - SSS) - tax, 2)

                    if month in ["1", "3", "5", "7", "8", "10", "12"]:
                        date_range = "16-31"
                    elif month =="2":
                        date_range = "16-28"
                    else:
                        date_range = "16-30"

                    payslip = Payslip.objects.create(
                        id_number = emp,
                        month=month,
                        date_range = date_range,
                        year=year,
                        pay_cycle = cycle,
                        rate=rate,
                        earnings_allowance = allowances,
                        deductions_tax = round(tax, 2),
                        deductions_health = PhilHealth,
                        pag_ibig=100,
                        sss=SSS, #capital S
                        overtime = overtime,
                        total_pay = total
                    )

                    payslip.save()
                    Employee.objects.filter(id_number=xid).update(overtime_pay=0)
                    messages.success(request, "Payslip created successfully.")
                    
            employees = Employee.objects.all()
            payslips = Payslip.objects.all()
            return render(request, 'LazapeeApp/payroll.html', {'employees': employees, 'payslips': payslips})
    else:
        employees = Employee.objects.all()
        payslips = Payslip.objects.all()
        return render(request, 'LazapeeApp/payroll.html', {'employees': employees, 'payslips': payslips})


# PAYSLIP : view -> receipt
def Payslips(request, pk):
    #payslip = Payslip.objects.get(pk=pk)
    payslip = get_object_or_404(Payslip,pk=pk)
    gross = payslip.getCycleRate() + payslip.earnings_allowance + payslip.overtime

    if(payslip.pay_cycle == 1):
        payslip.deductions_health = 0
        payslip.sss = 0
        total_deduct = round(payslip.deductions_tax + payslip.pag_ibig, 2)
        return render(request, 'LazapeeApp/payslip.html', {'payslip':payslip, 'gross':gross, 'total_deduct':total_deduct, 'pag_ibig':'PAGIBIG'})

    elif(payslip.pay_cycle == 2):
        total_deduct = round(payslip.deductions_tax + payslip.deductions_health + payslip.sss, 2)
        return render(request, 'LazapeeApp/payslip.html', {'payslip':payslip, 'gross':gross, 'total_deduct':total_deduct, 'philhealth': 'PHILHEALTH', 'sss': 'SSS'})
    return render(request, 'LazapeeApp/payslip.html', {'payslip': payslip, 'pk': pk, 'gross': gross})