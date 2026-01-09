from django.contrib.auth.models import User
from Professor.models import Professor
from Student.models import Department

# Get departments
cs_dept = Department.objects.get(Department_Code='CS')
bis_dept = Department.objects.get(Department_Code='BIS')

# Professor data
professors = [
    {'username': 'boasson1e', 'first': 'Emil', 'last': 'Boasson', 'dept': cs_dept, 'email': 'boasson1e@cmich.edu', 'phone': 9897741006, 'office': 'Pearce Hall 207'},
    {'username': 'lawrance2f', 'first': 'Fredrik', 'last': 'Lawrance', 'dept': cs_dept, 'email': 'lawrance2f@cmich.edu', 'phone': 9897741007, 'office': 'Pearce Hall 209'},
    {'username': 'peales3j', 'first': 'Jared', 'last': 'Peales', 'dept': bis_dept, 'email': 'peales3j@cmich.edu', 'phone': 9897741008, 'office': 'Grawn Hall 315'},
    {'username': 'macaron4k', 'first': 'Kevin', 'last': 'Macaron', 'dept': bis_dept, 'email': 'macaron4k@cmich.edu', 'phone': 9897741009, 'office': 'Grawn Hall 320'},
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
