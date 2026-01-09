from django.contrib.auth.models import User
from Professor.models import Professor
from Student.models import Department

# Get departments
cs_dept = Department.objects.get(Department_Code='CS')
bis_dept = Department.objects.get(Department_Code='BIS')

# Professor data
professors = [
    {'username': 'smith1j', 'first': 'John', 'last': 'Smith', 'dept': cs_dept, 'email': 'smith1j@cmich.edu', 'phone': 9897741001, 'office': 'Pearce Hall 201'},
    {'username': 'johnson2m', 'first': 'Mary', 'last': 'Johnson', 'dept': cs_dept, 'email': 'johnson2m@cmich.edu', 'phone': 9897741002, 'office': 'Pearce Hall 203'},
    {'username': 'williams3r', 'first': 'Robert', 'last': 'Williams', 'dept': bis_dept, 'email': 'williams3r@cmich.edu', 'phone': 9897741003, 'office': 'Grawn Hall 305'},
    {'username': 'davis4s', 'first': 'Sarah', 'last': 'Davis', 'dept': cs_dept, 'email': 'davis4s@cmich.edu', 'phone': 9897741004, 'office': 'Pearce Hall 205'},
    {'username': 'brown5m', 'first': 'Michael', 'last': 'Brown', 'dept': bis_dept, 'email': 'brown5m@cmich.edu', 'phone': 9897741005, 'office': 'Grawn Hall 310'},
]

created = []
for prof in professors:
    try:
        user = User.objects.create_user(username=prof['username'], email=prof['email'], password='password')
        professor = Professor.objects.create(
            user=user,
            First_Name=prof['first'],
            Last_Name=prof['last'],
            Department_id=prof['dept'],
            Email=prof['email'],
            Phone=prof['phone'],
            Office=prof['office'],
            created_by='admin2'
        )
        created.append(f"{prof['first']} {prof['last']} ({prof['username']})")
        print(f"✓ Created: {prof['first']} {prof['last']} ({prof['username']})")
    except Exception as e:
        print(f"✗ Error creating {prof['username']}: {e}")

print(f"\nSuccessfully created {len(created)} professors!")
