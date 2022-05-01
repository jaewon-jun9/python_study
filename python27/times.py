import datetime
nowtime = datetime.datetime.now()
strtime = nowtime.strftime('%Y-%m-%d %H:%M:%S')
print(strtime)
print(strtime[0:4])
print(strtime[5:7])
print(strtime[8:10])
print(strtime[11:13])
print(strtime[14:16])
print(strtime[17:19])
d = datetime.date(2009,5,23)
t = datetime.time(17,5,9)
newtime = datetime.datetime.combine(d,t)
strtime2 = newtime.strftime('%Y-%m-%d %H:%M:%S')
print(strtime2)
diff_days = datetime.timedelta(days=50)
newtime2 = newtime + diff_days
strtime3 = newtime2.strftime('%Y-%m-%d %H:%M:%S')
print(strtime3)
# result
# 2022-05-01 23:34:53
# 2022
# 05
# 01
# 23
# 34
# 53
# 2009-05-23 17:05:09
# 2009-07-12 17:05:09
