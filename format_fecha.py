# Formatear fecha

s = '06:40:03AM'

def timeConversion(s):
    # Write your code here
    hours = int(s[0:2])
    
    if s[8:10] == 'PM' and hours != 12:
        hours += 12
        print(str(hours) + s[2:8])
    elif s[8:10] == 'PM' and hours == 12:
        print('12' + s[2:8])
    elif s[8:10] == 'AM' and hours == 12:
        print('00' + s[2:8])
    else:
        print(s[0:8])

timeConversion(s)