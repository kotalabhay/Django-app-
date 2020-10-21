
from app.other_constants import *


#====================================================================
# COUNTRY
#====================================================================
country = []

for record in country_list.COUNTRIES_LIST_CHOICES:
    country.append("<li>{} - {}</li>".format(record[0], record[1]))

country = ''.join(country)


#====================================================================
# PREFERRED CURRENCY
#====================================================================
preferred_currency = []

for record in currency_list.CURRENCY_CHOICES:
    preferred_currency.append("<li>{} - {}</li>".format(record[0], record[1]))

preferred_currency = ''.join(preferred_currency)




#====================================================================
# CSV IMPORT DICTIONARY
#====================================================================

