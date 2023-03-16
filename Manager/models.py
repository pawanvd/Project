from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table="Category"

Status=(
    ("AVB","Available"),
    ("UAVB","Unavailable")
)
class Rooms(models.Model):
    rno=models.IntegerField()
    rimage=models.ImageField(default='abc.jpg',upload_to="Images")
    rprice=models.IntegerField()
    rdescription=models.CharField(max_length=1000)
    rservices=models.CharField(max_length=500)
    ravailability=models.CharField(max_length=20,choices=Status,default="AVB")
    cat=models.ForeignKey(to="Category",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rno)

    class Meta:
        db_table="Rooms"

class Guest(models.Model):
    gname=models.CharField(max_length=20,primary_key=True)
    email=models.EmailField(max_length=20)
    uidno=models.IntegerField()
    contactno=models.IntegerField()
    password=models.CharField(max_length=20)

    class Meta:
        db_table="Guest"


class Booking(models.Model):
    gname=models.ForeignKey(to='Guest',on_delete=models.CASCADE)
    cat=models.ForeignKey(to='Category',on_delete=models.CASCADE)
    rno=models.ForeignKey(to='Rooms',primary_key=True,on_delete=models.CASCADE)
    room_no=models.IntegerField(default=0)
    check_in=models.DateField()
    check_out=models.DateField()
    rprice=models.IntegerField()
    
    class Meta:
        db_table="Booking"


class Bookingss(models.Model):
    gname=models.ForeignKey(to='Guest',on_delete=models.CASCADE)
    cat=models.ForeignKey(to='Category',on_delete=models.CASCADE)
    rno=models.ForeignKey(to='Rooms',on_delete=models.CASCADE)
    room_no=models.IntegerField(default=0)
    check_in=models.DateField()
    check_out=models.DateField()
    rprice=models.IntegerField()
    
    class Meta:
        db_table="Bookingss"


class PaymentMaster(models.Model):
    cardno=models.CharField(max_length=20)
    card_name=models.CharField(max_length=20,default="user")
    cvv=models.CharField(max_length=3)
    expiry=models.CharField(max_length=20)
    balance=models.FloatField(default=10000)

    class Meta:
        db_table="PaymentMaster"

#p p