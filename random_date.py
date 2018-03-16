import random

DAYS_OF_MONTH = [x for x in range(1, 32)]
MONTHS = (
  (('January'), ('Jan'), ('01'), ('1')),
  (('February'), ('Feb'), ('02'), ('2')),
  (('March'), ('Mar'), ('03'), ('3')),
  (('April'), ('Apr'), ('04'), ('4')),
  (('May'), ('May'), ('05'), ('5')),
  (('June'), ('June'), ('06'), ('6')),
  (('July'), ('July'), ('07'), ('7')),
  (('August'), ('Aug'), ('08'), ('8')),
  (('September'), ('Sept'), ('09'), ('9')),
  (('October'), ('Oct'), ('10'), ('10')),
  (('November'), ('Nov'), ('11'), ('11')),
  (('December'), ('Dec'), ('12'), ('12')),
)
WEEKDAYS = (
  (('Monday'), ('Mon')),
  (('Tuesday'), ('Tue')),
  (('Wednesday'), ('Wed')),
  (('Thursday'), ('Thu')),
  (('Friday'), ('Fri')),
  (('Saturday'), ('Sat')),
  (('Sunday'), ('Sun')),
)

def get_random_day(fmt):
  ran_num = random.randint(0, 30)
  day = DAYS_OF_MONTH[ran_num]
  if fmt == 'd':
    return str(day)
  elif fmt == 'dd':
    return str(day) if day > 9 else "0" + str(day)
  elif fmt == 'weekday':
    return WEEKDAYS[random.randint(0, 6)][0]
  elif fmt == 'weekday_short':
    return WEEKDAYS[random.randint(0, 6)][0]
  else:
    raise ValueError('"{0}" is not a valid format.'.format(fmt))

def get_random_month(fmt):
  ran_num = random.randint(0, 11)
  if fmt == 'm':
    return MONTHS[ran_num][3]
  elif fmt =='mm':
    return MONTHS[ran_num][2]
  elif fmt == 'mmm':
    return MONTHS[ran_num][1]
  elif fmt == 'mmmm':
    return MONTHS[ran_num][0]
  else:
    raise ValueError('"{0}" is not a valid format.'.format(fmt))

def get_random_year(fmt, start, end):
  if end < start:
    raise ValueError('Start date must come before end date.')
  if start < 1000 or end > 9999:
    raise ValueError('Year must be a value between 1000 and 9999')
  ran_num = random.randint(start, end)
  if fmt == 'yy':
    return str(ran_num)[2:4]
  elif fmt == 'yyyy':
    return str(ran_num)
  else:
    raise ValueError('"{0}" is not a valid format.'.format(fmt))

"""PREMADE PATTERNS"""
""""""""""""""""""""""""
def one(yr_start, yr_end):
  # dd/mm/yy	03/08/06
  day = get_random_day('dd')
  month = get_random_month('mm')
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}/{1}/{2}'.format(day, month, year)
  
def two(yr_start, yr_end):
  # dd/mm/yyyy	03/08/2006
  day = get_random_day('dd')
  month = get_random_month('mm')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}/{1}/{2}'.format(day, month, year)

def three(yr_start, yr_end):
  # d/m/yy	3/8/06
  day = get_random_day('d')
  month = get_random_month('m')
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}/{1}/{2}'.format(day, month, year)

def four(yr_start, yr_end):
  # d/m/yyyy	3/8/2006
  day = get_random_day('d')
  month = get_random_month('m')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}/{1}/{2}'.format(day, month, year)

def five(yr_start, yr_end):
  # dd-mmm-yy 03-Aug-06
  day = get_random_day('dd')
  month = get_random_month('mmm')
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}-{1}-{2}'.format(day, month, year)

def six(yr_start, yr_end):
  # dd-mmm-yyyy	03-Aug-2006
  day = get_random_day('dd')
  month = get_random_month('mmm')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}-{1}-{2}'.format(day, month, year)

def seven(yr_start, yr_end):
  # d-mmm-yy	3-Aug-06
  day = get_random_day('d')
  month = get_random_month('mmm')
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}-{1}-{2}'.format(day, month, year)

def eight(yr_start, yr_end):
  # d-mmm-yyyy	3-Aug-2006
  day = get_random_day('d')
  month = get_random_month('mmm')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}-{1}-{2}'.format(day, month, year)

def nine(yr_start, yr_end):
  # d-mmmm-yy	3-August-06
  day = get_random_day('d')
  month = get_random_month('mmmm')
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}-{1}-{2}'.format(day, month, year)

def ten(yr_start, yr_end):
  # d-mmmm-yyyy	3-August-2006
  day = get_random_day('d')
  month = get_random_month('mmmm')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}-{1}-{2}'.format(day, month, year)

def eleven(yr_start, yr_end):
  # yy/mm/dd	06/08/03
  day = get_random_day('dd')
  month = get_random_month('mm')
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}/{1}/{2}'.format(year, month, day)

def twelve(yr_start, yr_end):
  # yyyy/mm/dd	2006/08/03
  day = get_random_day('dd')
  month = get_random_month('mm')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}/{1}/{2}'.format(year, month, day)

def thirteen(yr_start, yr_end):
  # mm/dd/yy	08/03/06
  day = get_random_day('dd')
  month = get_random_month('mm')
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}/{1}/{2}'.format(month, day, year)

def fourteen(yr_start, yr_end):
  # mm/dd/yyyy	08/03/2006
  day = get_random_day('dd')
  month = get_random_month('mm')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}/{1}/{2}'.format(month, day, year)

def fifteen(yr_start, yr_end):
  # mmm-dd-yy	Aug-03-06
  day = get_random_day('dd')
  month = get_random_month('mmm')
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}-{1}-{2}'.format(month, day, year)

def sixteen(yr_start, yr_end):
  # mmm-dd-yyyy	Aug-03-2006
  day = get_random_day('dd')
  month = get_random_month('mmm')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}-{1}-{2}'.format(month, day, year)

def seventeen(yr_start, yr_end):
  # yyyy-mm-dd	2006-08-03
  day = get_random_day('dd')
  month = get_random_month('mm')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}-{1}-{2}'.format(year, month, day)

def eighteen(yr_start, yr_end):
  # weekday, dth mmmm yyyy	Monday, 3 of August 2006
  weekday = get_random_day('weekday')
  day = get_random_day('d')
  month = get_random_month('mmmm')
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}, {1} of {2} {3}'.format(weekday, day, month, year)

def nineteen():
  # weekday	Monday
  weekday = get_random_day('weekday')
  return '{}'.format(weekday)

def twenty(yr_start, yr_end):
  # mmm-yy	Aug-06
  month = get_random_month('mmm')
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}-{1}'.format(month, year)

def twenty_one(yr_start, yr_end):
  # yy	06
  year = get_random_year('yy', yr_start, yr_end)
  return '{0}'.format(year)

def twenty_two(yr_start, yr_end):
  # yyyy	2006
  year = get_random_year('yyyy', yr_start, yr_end)
  return '{0}'.format(year)

def get_random_date(fmt, yr_start, yr_end):
    return {
        1: one(yr_start, yr_end),
        2: two(yr_start, yr_end),
        3: three(yr_start, yr_end),
        4: four(yr_start, yr_end),
        5: five(yr_start, yr_end),
        6: six(yr_start, yr_end),
        7: seven(yr_start, yr_end),
        8: eight(yr_start, yr_end),
        9: nine(yr_start, yr_end),
        10: ten(yr_start, yr_end),
        11: eleven(yr_start, yr_end),
        12: twelve(yr_start, yr_end),
        13: thirteen(yr_start, yr_end),
        14: fourteen(yr_start, yr_end),
        15: fifteen(yr_start, yr_end),
        16: sixteen(yr_start, yr_end),
        17: seventeen(yr_start, yr_end),
        18: eighteen(yr_start, yr_end),
        19: nineteen(),
        20: twenty(yr_start, yr_end),
        21: twenty_one(yr_start, yr_end),
        22: twenty_two(yr_start, yr_end),
    }.get(fmt, 14)    # 14 is default if x not found
