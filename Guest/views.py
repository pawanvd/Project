from django.shortcuts import render,redirect,HttpResponse
from Manager.models import Category,Rooms,Guest,PaymentMaster,Bookingss
from datetime import datetime,timedelta
from django.contrib import messages

# Create your views here.
def homepage(request):
    cats=Category.objects.all()                             #fetch all records
    rooms=Rooms.objects.all()
    return render(request,"homepage.html",{"cats":cats,"rooms":rooms})



def login(request):
    cats=Category.objects.all()    
    if(request.method=="GET"):
        return render(request,"login.html",{"cats":cats})
    else:
        gname=request.POST["gname"]
        password=request.POST["password"]
        try: 
            guest=Guest.objects.get(gname=gname,password=password)                  #here cheking of username and password 
           
        except:
            messages.error(request,'  !!Invalid Credentials!!')
            return redirect(login)
        else:
            request.session["gname"]=gname  
            return redirect(homepage)



def signup(request):
    cats=Category.objects.all()
    if (request.method=="GET"):
        return render(request,"signup.html",{"cats":cats})                     #cats pass to show navbar
    else:
        gname=request.POST["gname"]
        email=request.POST["email"]
        uidno=request.POST["uidno"]
        contactno=request.POST["contactno"]
        password=request.POST["password"]
        guest=Guest(gname,email,uidno,contactno,password)                            #we are passint it to database
        guest.save()
        return redirect(homepage)



def signout(request):
    request.session.clear()
    return redirect(homepage)



def showrooms(request,id):
    id=Category.objects.get(id=id)
    rooms=Rooms.objects.filter(cat=id)
    cats=Category.objects.all()
    return render(request,"showrooms.html",{"cats":cats,"rooms":rooms})



def viewdetails(request,id):
    cats=Category.objects.all()
    room=Rooms.objects.get(id=id)
    return render(request,"viewdetails.html",{"room":room,"cats":cats},)



def searchavailability(request):
    if(request.method=="POST"):
        cats=Category.objects.all()
        rno=request.POST["rno"]
        room = Rooms.objects.get(rno=rno)
        check_in=request.POST["check_in"] 
        check_out=request.POST["check_out"]
        if check_out<check_in:
            messages.error(request,'!! Invalid Check_Out date !!')
            return redirect(viewdetails,id=room.id)
        #else:

        is_available_1=Bookingss.objects.filter(rno=room,check_in=check_in,check_out=check_out).exists()      #exits return true if present
        is_available_2=Bookingss.objects.filter(rno=room,check_in__lte=check_in ,check_out__gte=check_in).exists() #(<...>)
        is_available_3=Bookingss.objects.filter(rno=room,check_in__lte=check_out,check_out__gte=check_out).exists()
        is_available_4=Bookingss.objects.filter(rno=room,check_in__gte=check_in,check_out__lte=check_out).exists()
        #is_available_2=Booking.objects.filter(rno=room,check_in__gte=check_in ,check_in__gte=check_out).exists() #(<...>)
        #is_available_3=Booking.objects.filter(rno=room,check_out__lte=check_in,check_out__lte=check_out).exists()
        print(rno," ",check_in," ",check_out)
        print(is_available_2)
        
        if is_available_1 or is_available_2 or is_available_3 or is_available_4:
            return render(request,"pop.html",{"id":room.id})
        else:
            return render(request,"booking.html",{"room":room,"check_in":check_in,"check_out":check_out,"cats":cats})


def booknow(request):
     if(request.method=="POST"):
        if("gname" in request.session):
            cats=Category.objects.all()
            rno=request.POST["rno"]
            room = Rooms.objects.get(rno=rno)
            check_in=request.POST["check_in"]
            check_out=request.POST["check_out"]
            rprice=request.POST["rprice"]

            check_in=datetime.strptime(check_in,'%Y-%m-%d')
            check_out=datetime.strptime(check_out,'%Y-%m-%d')
            num_days=(check_out-check_in).days
            print(num_days)
            total=num_days*int(rprice)
            print(total)

            #tax=rprice*0.18
           # rtotal=rprice+tax
            return render(request,"makepayment.html",{"rno":rno,"check_in":check_in,"check_out":check_out,"price":total,"id":room.id,"room":room,"cats":cats})
        else:
            check_in=request.POST["check_in"]
            check_out=request.POST["check_out"]
            request.session["check_in"]=check_in
            request.session["check_out"]=check_out
            return redirect(login)



def makepayment(request):
    if(request.method=="POST"):
        rno=request.POST["rno"]
        check_in=request.POST["check_in"]
        check_out=request.POST["check_out"]
        price=request.POST["price"]
        room = Rooms.objects.get(rno=rno)
        return render(request,"payment.html",{"rno":rno,"check_in":check_in,"check_out":check_out,"price":price,"id":room.id,"room":room})




def payment(request):
    if(request.method=="GET"):
        return render(request,"payment.html",{})
    else:
        gname=request.session["gname"]
        catk=request.POST["catk"]
        print(catk)
        rno=request.POST["rno"]
        check_in=request.POST["check_in"]
        check_out=request.POST["check_out"]
        price=request.POST["price"]
        ex=Rooms.objects.get(rno=rno)
        cardno=request.POST["cardno"]
        card_name=request.POST["card_name"]
        cvv=request.POST["cvv"]
        expiry=request.POST["expiry"]
        try:
            buyer=PaymentMaster.objects.get(cardno=cardno,card_name=card_name,cvv=cvv,expiry=expiry)
        except:
            return redirect(payment)
        else:
            #its match
            owner=PaymentMaster.objects.get(cardno='1111',card_name="Owner",cvv='123',expiry='12/2024')
            owner.balance+=int(price)
            buyer.balance-=int(price)
            owner.save()
            buyer.save()
            book=Bookingss(gname_id=gname,cat_id=catk,rno_id=ex.id,room_no=rno,check_in=check_in,check_out=check_out,rprice=price)
            #gname_id=gname,cat_id=cat,rno_id=rno,check_in=check_in,check_out=check_out,rprice=rprice
            '''book.gname_id=gname
            book.cat_id=catk
            book.rno_id=ex.id
            book.room_no=rno
            book.check_in=check_in
            book.check_out=check_out
            book.rprice=rprice'''
            book.save()
            return redirect(homepage)


'''def booking(request):
    if(request.method=="POST"):
        if("gname" in request.session):
            gname=request.session["gname"]
            catk=request.POST["catk"]
            rno=request.POST["rno"]
            check_in=request.POST["check_in"]
            check_out=request.POST["check_out"]
            rprice=request.POST["rprice"]
            ex=Rooms.objects.get(rno=rno)
            book=Booking()
            #gname_id=gname,cat_id=cat,rno_id=rno,check_in=check_in,check_out=check_out,rprice=rprice
            book.gname_id=gname
            book.cat_id=catk
            book.rno_id=ex.id
            book.check_in=check_in
            book.check_out=check_out
            book.rprice=rprice
            book.save()
            return redirect(homepage) 
        else:
            return render(request,"login.html",{})'''   


def mybooking(request):
    cats=Category.objects.all()
    gname=request.session["gname"]
    guest=Guest.objects.get(gname=gname)
    if (request.method=="GET"):
        bookings=Bookingss.objects.filter(gname=gname)
        return render(request,"mybooking.html",{"booking":bookings,"cats":cats})

    else:
        #action=request.POST["action"]
        rno=request.POST["rno"]
        iid=request.POST["iid"]
        room=Rooms.objects.get(rno=rno)
        book=Bookingss.objects.get(gname=gname,rno=room.id,id=iid)
        #if(action=="remove"):
        book.delete()
        return redirect(mybooking) 