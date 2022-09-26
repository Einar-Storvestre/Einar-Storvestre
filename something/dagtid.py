import datetime
import pytz
#dagens dato
today=datetime.date.today()
print(today)

#bursdags dato
birthday=datetime.date(2003, 7,12)
print(birthday)

#datoen i dag - bursdagsdato= hvor mange dager du har levd!
days_since_birth=(today-birthday).days
print(days_since_birth )

#hvis du legge til eller trekke fra dager: days= n dager
pluss_minus_dager=datetime.timedelta(days=45)
print(today+pluss_minus_dager)

#hvilken dag det er i dag 0=mandag 6=søndag
print(today.weekday())

# datetime.date (Y, M, D)
#datetime.time (h, m , s , ms)
#datetime.datetime( Y, M, D, H, M, S, ms)

#tiden akkurat nå!
print(datetime.datetime.now())

print(pytz.utc)