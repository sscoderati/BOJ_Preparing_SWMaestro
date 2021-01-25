import calendar

day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
date, month = map(int, input().split())

tday = calendar.weekday(2007, date, month)
print(day[tday])
