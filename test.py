from datetime import date
from datetime import timedelta

def get_date_range():
    to= date.today().strftime('%d/%m/%Y') 

    from_date = (date.today() - timedelta(days=10)).strftime('%d/%m/%Y')

