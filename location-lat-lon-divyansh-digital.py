import phonenumbers

from phonenumbers import geocoder

number = "+country-dialing-code&then-your-number"
# In case you didn't understand, I meant to say that to see output enter your country dialing code with "+" on starting and without any space enter your number. 

ch_num = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_num, "en"))

from phonenumbers import carrier

service_company = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_company,"en"))
# Result will be Country /n Internet Service Provider.
