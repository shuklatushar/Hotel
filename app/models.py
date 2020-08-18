from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    
    class Meta:
        db_table='Login'    
    
class Staff(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=100) 
    salary=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    staffs=models.OneToOneField(Login,on_delete=models.CASCADE)
    def __str__(self):
        return self.name+" "+self.email+" "+self.phone+" "+self.address+" "+self.gender+" "+self.salary+" "+self.designation
    class Meta:
        db_table='Staff'
    
class Category(models.Model):
    cname=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    #new
    charges=models.CharField(max_length=100)
    class Meta:
        db_table='category'
    
class Room(models.Model):
    room_no=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    categories=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.room_no+" "+self.description
    class Meta:
        db_table='room'
        
class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    adhaar=models.ImageField(upload_to='pictures') 
    class Meta:
        db_table='customer'
    def __str__(self):
        return self.name+" "+self.email    
            
class Booking(models.Model):
    cust=models.ForeignKey(Customer,on_delete=models.CASCADE) 
    rom=models.ForeignKey(Room,on_delete=models.CASCADE) 
    chechin_date=models.DateField()
    chechout_date=models.DateField()
    no_of_person=models.CharField(max_length=100)
    class Meta:
        db_table='booking'   
    def __str__(self):
        return self.chechin_date+" "+self.chechout_date+" "+self.no_of_person       
    
class Service(models.Model): 
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    charges=models.IntegerField()
    class Meta:
        db_table='service'
    def __str__(self):
        return self.name+" "+str(self.charges)    

class Custservice(models.Model):
    customers=models.ForeignKey(Customer,on_delete=models.CASCADE) 
    services=models.ForeignKey(Service,on_delete=models.CASCADE)
    class Meta:
        db_table='custservice'   
    def __str__(self):
        return self.name+" "+str(self.charges)      
          
    
       