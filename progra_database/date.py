# -*- coding:utf-8 -*-
# File Name: a1.py
# Created Time: 三 12/ 2 15:47:14 2015
__author__ = 'wangyanwei'
import datetime
import calendar
'''
贷款还款，当天借下个月的前一天还，1号借，当月月底还
'''

def get_next_month(actually_loan_time_limit=3):

    now = datetime.datetime.now()
    day,month,year = now.day,now.month,now.year
    # actually_loan_time_limit = 3
    final = []
    for i in range(1,actually_loan_time_limit+1):


        if day == 1:
            final_year = year + (month+i-2)//12
            final_monty = (month+i-2)%12+1
            next_month_day = calendar.monthrange(year+(month+i-1)//12,(month+i-2)%12+1)[1]
            final_day = next_month_day
        else:
            next_month_day = calendar.monthrange(year+(month+i-1)//12,(month+i-1)%12+1)[1]
            if day <= next_month_day:
                next_month_day  = day - 1
            final_day = next_month_day
            final_year = year + (month+i-1)//12
            final_monty = (month+i-1)%12+1

        time = now.time()

        date1 = datetime.date(final_year,final_monty,final_day)

        final_time = datetime.datetime.combine(date1,time)
        final.append(final_time)

    return final

if __name__ == "__main__":

    a = get_next_month(actually_loan_time_limit=4)
    print(a)
