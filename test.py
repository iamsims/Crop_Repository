import datetime

def year_choices():
    years = [(r,(r+1)%100) for r in range(1984, datetime.date.today().year+1)]
    actual_value = [int(str(a) + str(b)) for a,b in years] 
    readable_form =['/'.join(map(str,tups)) for tups in years] 
    return list(zip(actual_value, readable_form))

print(year_choices())
