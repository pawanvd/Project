from django.contrib import admin
from .models import Category,Rooms,Booking,PaymentMaster,Bookingss
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):                      #a classs is made inherited from model Admin
    list_display=("id","category_name")


class RoomsAdmin(admin.ModelAdmin):
    list_display=["id","rno","rimage","rprice","rdescription","rservices","ravailability","cat"]


class BookingAdmin(admin.ModelAdmin):
    list_display = ['gname','cat','rno','room_no','check_in','check_out','rprice']

class BookingssAdmin(admin.ModelAdmin):
    list_display = ['id','gname','cat','rno','room_no','check_in','check_out','rprice']

class PaymentMasterAdmin(admin.ModelAdmin):
    list_display=("cardno","card_name","cvv","expiry","balance")

admin.site.register(Booking,BookingAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Rooms,RoomsAdmin)
admin.site.register(PaymentMaster,PaymentMasterAdmin)