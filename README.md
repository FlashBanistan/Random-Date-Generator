# Random-Date-Generator
## Python module to randomly generate a date in a variety of formats.

### Exposes 4 main functions:

1) get_random_date(pattern_num, yr_start, yr_end)
2) get_random_day(fmt)
3) get_random_month(fmt)
4) get_random_year(fmt, start, end)

### Possible formats include:
'd'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1  
'dd'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;01  
'weekday'&nbsp;&nbsp;Monday  
'weekday_short'&nbsp;&nbsp;Mon  
'm'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1  
'mm'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;01  
'mmm'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jan  
'mmmm'&nbsp;&nbsp;&nbsp;&nbsp;January  
'yy'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16  
'yyyy'&nbsp;&nbsp;&nbsp;&nbsp;2016  

### Premade patterns with corresponding numbers:
1)	**'dd/mm/yy'**,	03/08/06
2)	**'dd/mm/yyyy'**,	03/08/2006
3)	**'d/m/yy'**,	3/8/06
4)	**'d/m/yyyy'**,	3/8/2006
5)	**'dd-mmm-yy'**,	03-Aug-06
6)	**'dd-mmm-yyyy'**,	03-Aug-2006
7)	**'d-mmm-yy'**,	3-Aug-06
8)	**'d-mmm-yyyy'**,	3-Aug-2006
9)	**'d-mmmm-yy'**,	3-August-06
10)	**'d-mmmm-yyyy'**,	3-August-2006
11)	**'yy/mm/dd'**,	06/08/03
12)	**'yyyy/mm/dd'**,	2006/08/03
13)	**'mm/dd/yy'**,	08/03/06
14)	**'mm/dd/yyyy'**,	08/03/2006
15)	**'mmm-dd-yy'**,	Aug-03-06
16)	**'mmm-dd-yyyy'**,	Aug-03-2006
17)	**'yyyy-mm-dd'**,	2006-08-03
18)	**'weekday, dth mmmm yyyy'**,	Monday, 3 of August 2006
19)	**'weekday'**,	Monday
20)	**'mmm-yy'**,	Aug-06
21)	**'yy'**,	06
22)	**'yyyy'**,	2006
23) **'mmmm yyyy'**, August 2017

### Pull requests welcome :)