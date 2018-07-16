import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

#plt.xkcd()
#a  = 3
#rand = np.random.rand(1000)
#rand2 = -np.log(1-rand)
#plt.hist(rand2, bins=300, label="test")
##plt.show()
#timex =time.time(tm_year=2018, tm_mon=7, tm_mday=15, 
#                        tm_hour=13, tm_min=32, tm_sec=20, 
#                        tm_wday=6, tm_yday=196, tm_isdst=1)
##print(timex - time.localtime())
#
#
#print(time.strftime("%H:%M:%S", time.gmtime(timex)))

date = datetime.strptime('17 Sep 2018 12', '%d %b %Y %H')
delta_t =  date - datetime.now()
sekunden = delta_t.total_seconds()
if sekunden >=0:
    print("{:1.2f} Wochen".format(delta_t.total_seconds()/(7*24*60*60)))
    print("{:1.2f} Tage".format(delta_t.total_seconds()/(24*60*60)))
else:
    print("schon passiert :-)")
