hours=input('How many hours do you work weekly? ')
rate=input('How much do you earn per hour? ')
from decimal import Decimal
print('Your weekly gross pay is $', (Decimal(hours))*(Decimal(rate)))