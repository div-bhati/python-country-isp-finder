import phonenumbers
#from location import number

from phonenumbers import geocoder

number = "+916377418515"

ch_num = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_num, "en"))

from phonenumbers import carrier

service_company = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_company,"en"))
# Result will be Country /n Internet Service Provider.