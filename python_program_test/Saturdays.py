import datetime
from calendar import SATURDAY


class IsSecondSaturday:
    ''' identifies given date is saturday or not 
    '''
    def second_saturday(self,date):
        if date.weekday() != SATURDAY:
            return False
        day = date.day
        if (day in range(8, 14 + 1) or day%5 ==0):
            return True
    '''Extracts  all the dates between pased dates
    '''
    def Get_Saturdays(self,start,end):
        start_date  = datetime.datetime.strptime(start, '%d%m%Y')
        end_date    = datetime.datetime.strptime(end, '%d%m%Y')
        diff = end_date - start_date
        saturday_list=[]
        for i in range(diff.days + 1):
            date = start_date + datetime.timedelta(i)
            is_saturday=self.second_saturday(date)
            if is_saturday:
                saturday_list.append((date.strftime('%d%m%Y')))
        
        return saturday_list
## creating class object
is_second_saturday_obj =IsSecondSaturday()
## Call the function to get all saturdays date formate == ddmmyyyy
intervel_Dates= is_second_saturday_obj.Get_Saturdays("01062020","21062021")
## print all saturdays along with saturdays which are multiples of 5
print(*intervel_Dates, sep = "\n")
