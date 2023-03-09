import re, datetime

date_str = '09/03/2023'

# regular expression for dates in DD/MM/YYYY format
# years range from 1000 to 2999
match = re.match(r'^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/([1-2][0-9]{3})$', date_str)
if match:
    day = match.group(1)
    month = match.group(2)
    year = match.group(3)
    print(f'Day: {day}, Month: {month}, Year: {year}')

# is using this module cheating?
try:
    day = int(day)
    month = int(month)
    year = int(year)
    date_obj = datetime.date(year, month, day) # date_obj is not used explicitly
    
    # Add the "th" suffix to the correct days of the month
    if int(day) in range(11, 14):
        date_formatted = date_obj.strftime("%B %d, %Y")
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(int(day) % 10, "th")
        # %e specifier formats day of the month as single digit with leading space instead of a leading zero like %d does
        date_formatted = date_obj.strftime("%B %e" + suffix + ", %Y")
    print(date_formatted)

    print("Valid date")
except ValueError:
    print("Invalid date")