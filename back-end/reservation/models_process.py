# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv
import math
import pandas as pd
from dateutil.relativedelta import relativedelta
from jeju_schedule.models import JejuSchedule
from reservation.models import Reservation
from jeju_data.models import Accommodation, Plane, Activity
from common.models import ValueObject, Reader, Printer


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'reservation/data/'
        vo.fname = 'price.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_reservation()

    def pre_process(self, p):
        arr = []
        pr = JejuSchedule.objects.get(id=p)
        print(pr)
        plane = Plane.objects.filter(id__in=pr.plane).values()
        print(plane)
        acc_pr = Accommodation.objects.get(id=pr.acc_id)
        print(acc_pr)
        activity = Activity.objects.filter(id__in=pr.activity).values()
        print(activity)
        people = pr.people
        day = pr.day
        unit = acc_pr.standard_number
        print(people/unit)
        acc_price = math.ceil(people/unit) * acc_pr.price * day
        print(acc_price, unit, p, acc_pr.price, day)
        reg_date = pr.reg_date.date()
        price = (plane.economyCharge * people) + acc_price + activity.price
        tax = price * 0.1
        subtotal = price + tax
        fee = subtotal * 0.2
        total_price = subtotal + fee
        jeju_schedule_id = p
        arr.append(reg_date)
        arr.append(people)
        arr.append(day)
        arr.append(price)
        arr.append(int(tax))
        arr.append(int(subtotal))
        arr.append(int(fee))
        arr.append(int(total_price))
        arr.append(jeju_schedule_id)
        n = 9
        result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
        df = pd.DataFrame(result, columns=['reg_date', 'people', 'day', 'price', 'tax', 'subtotal', 'fees', 'total_price', 'jeju_schedule_id'])
        print(df)
        df.to_csv(self.csvfile + 'price.csv')

    def insert_reservation(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                reservation = Reservation.objects.create(reg_date=row['reg_date'],
                                                         price=row['price'],
                                                         tax=row['tax'],
                                                         subtotal=row['subtotal'],
                                                         fees=row['fees'],
                                                         total_price=row['total_price'],
                                                         jeju_schedule_id=row['jeju_schedule_id'])
                print(f'2 >>>> {reservation}')
            print('DATA UPLOADED SUCCESSFULLY!')
