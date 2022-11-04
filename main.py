import phonenumbers

#import geocoder
from phonenumbers import geocoder

#specify then phone number
a = input("Enter the Phone Number: ")
#clcoding.com
phonenumber = phonenumbers.parse(a)

#display the location of phone number
print(geocoder.description_for_number(phonenumber,'en'))
