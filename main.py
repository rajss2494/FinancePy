import os, sys
for item in sys.path:
    print (item)
from financepy.utils import date, frequency, day_count
from financepy.products.bonds import  Bond

sys.path.append(r'C:\Users\avsre\PycharmProjects\Pythonfunctions\venv\Lib\site-packages')
sys.path.append(r'C:\Users\avsre\python\repos\FinancePy\financepy\utils')

import numpy as np

import traceback
import datetime


# dt1= datetime.datetime(2023, 3, 20)
# dt2= datetime.datetime(2026, 4, 20)
dt1= date.Date(20,3, 2023)
dt2= date.Date(20,4, 2026)
couponfreq = frequency.FrequencyTypes.QUARTERLY
daycounttype = day_count.DayCountTypes.ACT_ACT_ISDA

b1 = Bond(dt1, dt2, .03, couponfreq,daycounttype)

print(b1._calculate_payment_dts())
print(b1.payment_dts)
print(b1.cpn_dts)
b1._calculate_flows()
b1.flow_amounts


print(b1.dirty_price_from_discount_curve(dt2))