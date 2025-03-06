from django.shortcuts import render
from .utils.fetch_data import inventory
from django.http import HttpResponse
from .utils.counters import count
from .utils import make_booking, member_bookings, cancel_booking
# Create your views here.


def homepage(request):
    return render(request, 'home/index.html')


def book(request):
    if request.method == "POST":
        member_id = request.POST.get("member_id")
        itinerary_id = request.POST.get("itinerary_id")
        member_count, itinerary_count =  count(member_id, itinerary_id)

        if member_count == 2 or itinerary_count == 0:
            return HttpResponse(f"Booking not possible")
        else:
            make_booking.make(member_id, itinerary_id)
            return HttpResponse(f"Booking Done!!!")
    
    inventory_table = inventory().to_html()
    tables = [inventory_table]
    return render(request, 'home/book.html', {'tables': tables})


def cancel(request):
    show_extra_field = False  # Default: Hide extra input field
    if request.method == "POST":
        member_id = request.POST.get("member_id")
        booking_id = request.POST.get("booking_id")
        if booking_id is None:
            booking_table = member_bookings.booking_data(member_id).to_html()
            tables = [booking_table]
            show_extra_field = True
            return render(request, 'home/cancel.html', {'tables': tables, 'show_extra_field':show_extra_field})
        
        cancel_booking.cancel(booking_id)
        return HttpResponse(f"Cancellation Done!!!")
        
    return render(request, 'home/cancel.html', {'show_extra_field': show_extra_field})