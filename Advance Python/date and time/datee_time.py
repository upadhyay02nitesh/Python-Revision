from datetime import datetime, timedelta
print("Current Date and Time:", datetime.now())
print("Current Date:", datetime.now().date())
print("Current Time:", datetime.now().time())

print("Time after 1 hour:", datetime.now() + timedelta(hours=1))
print("Time after 30 minutes:", datetime.now() + timedelta(minutes=30))
print("Time after 15 seconds:", datetime.now() + timedelta(seconds=15))
print("Date after 10 days:", datetime.now().date() + timedelta(days=10))

# Convert datetime to string
print("Formatted Date:", datetime.now().strftime("%Y-%m-%d"))
print("Formatted Time:", datetime.now().strftime("%H:%M:%S"))


# Convert string to datetime
d="2023-10-05"
dt = datetime.strptime(d, "%Y-%m-%d")
print("Parsed Date:", dt)


# datetime_demo.py
import datetime
from datetime import date, time, datetime, timedelta

# -------------------------
# 1. Working with date
# -------------------------
print("\n--- DATE ---")
today = date.today()                       # Current date
print("Today:", today)

d = date(2025, 8, 23)                      # Specific date
print("Specific date:", d)

print("Year:", d.year)
print("Month:", d.month)
print("Day:", d.day)

print("Weekday (0=Monday):", d.weekday())
print("ISO Weekday (1=Monday):", d.isoweekday())

# -------------------------
# 2. Working with time
# -------------------------
print("\n--- TIME ---")
t = time(14, 30, 15, 500000)              # hour, minute, second, microsecond
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

# -------------------------
# 3. Working with datetime
# -------------------------
print("\n--- DATETIME ---")
dt = datetime.now()                         # Current datetime
print("Now:", dt)

dt2 = datetime(2025, 8, 23, 14, 30, 15)    # Specific datetime
print("Specific datetime:", dt2)

print("Year:", dt2.year)
print("Month:", dt2.month)
print("Day:", dt2.day)
print("Hour:", dt2.hour)
print("Minute:", dt2.minute)
print("Second:", dt2.second)

# -------------------------
# 4. Formatting datetime (strftime)
# -------------------------
print("\n--- STRFTIME (Formatting) ---")
print("YYYY-MM-DD:", dt2.strftime("%Y-%m-%d"))
print("DD/MM/YYYY:", dt2.strftime("%d/%m/%Y"))
print("Full:", dt2.strftime("%A, %d %B %Y %I:%M:%S %p"))

# -------------------------
# 5. Parsing datetime from string (strptime)
# -------------------------
print("\n--- STRPTIME (Parsing) ---")
date_str = "2025-08-23 14:30:15"
parsed_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_dt)

# -------------------------
# 6. Timedelta (date/time difference)
# -------------------------
print("\n--- TIMEDELTA ---")
delta = timedelta(days=10, hours=5, minutes=30)
future = dt + delta
past = dt - delta
print("10 days, 5 hours, 30 minutes later:", future)
print("10 days, 5 hours, 30 minutes earlier:", past)

# Difference between two dates
diff = future - dt
print("Difference:", diff)
print("Total seconds:", diff.total_seconds())

# -------------------------
# 7. Date arithmetic
# -------------------------
print("\n--- DATE ARITHMETIC ---")
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)

# -------------------------
# 8. Combining date and time
# -------------------------
print("\n--- COMBINE DATE & TIME ---")
d = date(2025, 8, 23)
t = time(15, 45, 30)
dt_combined = datetime.combine(d, t)
print("Combined datetime:", dt_combined)

# -------------------------
# 9. Replacing parts of datetime
# -------------------------
print("\n--- REPLACE ---")
dt_new = dt.replace(year=2030, month=1, day=1)
print("Replaced datetime:", dt_new)

# -------------------------
# 10. Timestamp and fromtimestamp
# -------------------------
print("\n--- TIMESTAMP ---")
ts = dt.timestamp()                     # Seconds since epoch
print("Timestamp:", ts)
dt_from_ts = datetime.fromtimestamp(ts)
print("Datetime from timestamp:", dt_from_ts)

# -------------------------
# 11. UTC datetime
# -------------------------
print("\n--- UTC DATETIME ---")
utc_now = datetime.utcnow()
print("UTC now:", utc_now)

# -------------------------
# 12. Comparing dates
# -------------------------
print("\n--- COMPARISON ---")
print("dt2 > dt:", dt2 > dt)
print("today == dt.date():", today == dt.date())


dob_str = "8-2-2001"  

# Convert string → datetime object
dob = datetime.strptime(dob_str, "%d-%m-%Y").date()
print(today.year-dob.year-((today.month,today.day)<(dob.month,dob.day)))

from datetime import date, datetime
from dateutil.relativedelta import relativedelta

dob_str = "8-2-2001"
dob = datetime.strptime(dob_str, "%d-%m-%Y").date()
diff = relativedelta(date.today(), dob)

print(diff.years, "years", diff.months, "months", diff.days, "days")
