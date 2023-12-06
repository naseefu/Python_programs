

from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier


phonenum = input("Enter the phone number with Country code:")
pn = phonenumbers.parse(phonenum)

#printing the time zone

tz = timezone.time_zones_for_number(pn)
print("Time zone :",tz)

gc = geocoder.description_for_number(pn,"en")
print("Country name :",gc)

cr = carrier.name_for_number(pn,'en')
print("service provider :",cr)