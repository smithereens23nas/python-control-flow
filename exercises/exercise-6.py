# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

mo = input('Enter the month of the year (Jan - Dec): ')
day = int(input('Enter the day of the month: '))
if mo in ('Dec', 'Jan', 'Feb'):
  season = 'Fall' if mo == 'Dec' and day < 21 else 'Winter'
elif mo in ('Mar', 'Apr', 'May'):
  season = 'Winter' if mo == 'Mar' and day < 20 else 'Spring'
elif mo in ('Jun', 'Jul', 'Aug'):
  season = 'Spring' if mo == 'Jun' and day < 21 else 'Summer'
else:
  season = 'Summer' if mo == 'Sep' and day < 22 else 'Fall'
print(f'{mo} {day} is in {season}')