def leap_year(year):
    if year%100!=0 and year%4==0:
        print('leap year')
    elif year%400==0:
        print('leap year') 
    else:
        print('not a leap year')
        
try:
    leap_year(int(input('enter year(in AD): ')))
except ValueError:
    print('please enter valid year')

