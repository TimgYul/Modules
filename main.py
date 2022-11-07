from application import salary
from application.db import pepole
import datetime

if __name__ == '__main__':
    now = datetime.datetime.now()
    print( now.strftime("%d-%m-%Y %H:%M") )
    salary.calculate_salary()
    pepole.get_employees()
    