from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from Professor.models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def Students(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'students/students.html',context)

@login_required(login_url='login')
def Profile(request):
    user=User.objects.get(username=request.user)
    if Student.objects.filter(user=user).exists():
        profile=Student.objects.get(user=user)
        role='student'
        context={'profile':profile,'role':role}
        return render(request,'profile.html',context)
    else:
        profile=Professor.objects.get(user=user)
        role='professor'
        officehours=OfficeHours.objects.filter(Professor=profile)
        context={'profile':profile,'role':role,'officehours':officehours}
        return render(request,'profile.html',context)
    
@login_required(login_url='login')
def ViewAppointments(request,pk):
    user=User.objects.get(username=pk)
    professor=Professor.objects.get(user=user)
    appointments=Appointment.objects.filter(Professor=professor)
    context={'appointments':appointments,'professor':professor}
    return render(request,'students/viewappointments.html',context)

@login_required(login_url='login')
def ConfirmAppointment(request, appointment_id):
    try:
        appointment = Appointment.objects.get(AppointmentId=appointment_id)
        student = Student.objects.get(user=request.user)
        
        # Check if appointment is already confirmed
        if appointment.Confirmed:
            messages.error(request, 'This appointment slot is already booked.')
            return redirect('viewappointments', pk=appointment.Professor.user.username)
        
        # Confirm the appointment
        appointment.Confirmed = True
        appointment.Student = student
        appointment.updated_by = request.user.username
        appointment.save()
        
        # Send confirmation email to student
        try:
            send_mail(
                subject=f'Appointment Confirmation with {appointment.Professor.First_Name} {appointment.Professor.Last_Name}',
                message=f'''Dear {student.First_Name} {student.Last_Name},

Your appointment has been confirmed!

Details:
Professor: {appointment.Professor.First_Name} {appointment.Professor.Last_Name}
Date: {appointment.Date}
Day: {appointment.Day}
Time: {appointment.Time}
Office: {appointment.Professor.Office}

Please arrive on time for your appointment.

Best regards,
Appointment Scheduler Team''',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[student.Email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email sending failed: {e}")
        
        messages.success(request, f'Appointment confirmed for {appointment.Date} at {appointment.Time}')
        
    except Appointment.DoesNotExist:
        messages.error(request, 'Appointment not found.')
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found.')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    
    return redirect('viewappointments', pk=appointment.Professor.user.username)

