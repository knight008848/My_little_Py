#! python2.7
# -*- coding: utf-8 -*-

"""
A Chinese Calendar Library in Pure Python(1901~2100)
====================================================

Usage: SLcalendar Month [4-Digit-Year]
   or: SLcalendar 4-Digit-Year Month

This Python script is to show Solar an Lunar calendar at the
same time. You need to have Python (3.0 or above) installed.

Acceptable date range:  1901/01 -- 2100/12 

Chinese Calendar: http://en.wikipedia.org/wiki/Chinese_calendar

License: 
    GNU General Public License (GPL, see [url]http://www.gnu.org[/url]).
    In short, users are free to use and distribute this program
    in whole. If users make revisions and distribute the revised
    one, they are required to keep the revised source accessible
    to the public.

Version:

0.1.0 Alpha Version
"""
#Test:
#"鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡","狗", "猪"
#阳历与阴历我国通常使用的纪年方法。阳历又叫公历，阴历又叫农历。外事用阳历，以与国际接轨，内事用阴历，以合国人习惯。不过现在农历大只使用在一些节日和祭祀活动中，而公历的应用却越来越广泛。由于地球绕太阳转一周是365.2422，如果按公转一圈为一年，那么无论公历还是农历都无法非常精确的表示一年。所以农历平年十二个月，大月三十天，小月二十九天，全年354天或355天（一年中哪个月大，哪个月小，年年不同）。由于每年的天数比太阳年约差十一天，所以在十九年里设置七个闰月，有闰月的年份全年383天或384天。而阳历却比较简单，平年365天，四年一闰，闰年366天。他们表达都不如干支纪年表示准确，因为干支纪年是按照二十四节气来划分的，而二十四节又是地球公转轨道的360度按二十四份等分得来。由于农历自身的特点，所以农历大约只使用在节日或者祭祀活动中。同样由于相同的原因，公历和农历的转换比较麻烦，因为农历闰月实在太不固定了，一般是国家机构或者天文台推算一百到二百年的公历农对应历信息供人参考使用。这里使用台湾一家天文台提供的换算信息，我把他处理成数组，以供调用。该数组使用17个BIT来表示阴历每年信息。最低四个BIT表示该年闰月是闰哪个月，接下来的中间12个BIT表示每月是大月还是小月，第十七个BIT表示该年有没有闰年(闰月大小)。转换算法也很简单，公历转农历，计算阳历某年月日到1900年的天数，然后推算出阴历哪个日期与1900相差的天数与阳历相同，两者即为同一天。

#remember, in this program:
#   month=0 means Januaray, month=1 means February ...;
#   day=0 means the first day of a month, day=1 means the second day,
#       so as to easy to manipulate Python lists.
#   year=0 is 1900, year=1 is 1901,until the last step to output
#   weekday =0 is Sunday.

daysInSolarMonth= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]              
lunarMonthDays  = [29,30] # a short (long) lunar month has 29 (30) days */      
                                                                                
shengXiaoEn     = ["Mouse", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",         
                   "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
                            
shengXiaoGB     = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡",  
                   "狗", "猪"]
                                                                     
zhiGB           = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉",  
                   "戌", "亥"]
                                                                     
ganGB           = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]  
                                                                                
monthEn         = ['January', 'February', 'March', 'April', 'May', 'June',      
                   'July', 'August', 'September', 'October', 'November',        
                   'December']
                   
monthGB         = ["正","二", "三", "四", "五", "六", "七", "八", "九",  
                   "十","十一","腊"]
                                                                               
weekdayEn       = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday",
                   "Friday", "Saturday"]
                                                 
weekdayGB       = ["日", "一", "二", "三", "四", "五", "六"]
                    
numGB           = ["○", "一", "二", "三", "四", "五", "六", "七", "八", "九",  
                   "十"]
                   
tenGB           = ["初","十", "廿", "卅"]
                                                                           
lunarHolidays   = {(0,0):'春节', (4,4):'端午节', (7,14):'中秋节',(0,14):'元宵节'}
                   
solarHolidays   = {(0,0):'元旦', (4,0):'劳动节', (9,0):'国庆节',(6,0):'建党节',(7,0):'建军节'} 

solarTerms      = {}
                   
#   encoding:                                                                  
#               b bbbbbbbbbbbb bbbb                                             
#      bit#     1 111111000000 0000                                             
#               . ............ ....                                             
#      month#     000000000111                                                  
#               M 123456789012   L                                             
#                                                                              
#   b_j = 1 for long month, b_j = 0 for short month                             
#   L is the leap month of the year if 1<=L<=12; NO leap month if L = 0.        
#   The leap month (if exists) is long one if M = 1. 
#   
yearCode = [                                                                    
                                                                                 0x04bd8, # 1900 
0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950, 0x16554, 0x056a0, 0x09ad0, 0x055d2, 0x04ae0, # 1910 
0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540, 0x0d6a0, 0x0ada2, 0x095b0, 0x14977, 0x04970, # 1920 
0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54, 0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566, # 1930 
0x0d4a0, 0x0ea50, 0x06e95, 0x05ad0, 0x02b60, 0x186e3, 0x092e0, 0x1c8d7, 0x0c950, 0x0d4a0, # 1940 
0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0, 0x092d0, 0x0d2b2, 0x0a950, 0x0b557, 0x06ca0, # 1950 
0x0b550, 0x15355, 0x04da0, 0x0a5d0, 0x14573, 0x052d0, 0x0a9a8, 0x0e950, 0x06aa0, 0x0aea6, # 1960 
0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260, 0x0f263, 0x0d950, 0x05b57, 0x056a0, 0x096d0, # 1970 
0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250, 0x0d558, 0x0b540, 0x0b5a0, 0x195a6, 0x095b0, # 1980 
0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50, 0x06d40, 0x0af46, 0x0ab60, 0x09570, 0x04af5, # 1990 
0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58, 0x055c0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960, # 2000 
0x0d954, 0x0d4a0, 0x0da50, 0x07552, 0x056a0, 0x0abb7, 0x025d0, 0x092d0, 0x0cab5, 0x0a950, # 2010 
0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0, 0x0a5b0, 0x15176, 0x052b0, 0x0a930, 0x07954, # 2020 
0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6, 0x0a4e0, 0x0d260, 0x0ea65, 0x0d530, 0x05aa0, # 2030 
0x076a3, 0x096d0, 0x04bd7, 0x04ad0, 0x0a4d0, 0x1d0b6, 0x0d250, 0x0d520, 0x0dd45, 0x0b5a0, # 2040 
0x056d0, 0x055b2, 0x049b0, 0x0a577, 0x0a4b0, 0x0aa50, 0x1b255, 0x06d20, 0x0ada0, 0x14b63, # 2050 
0x09370, 0x049f8, 0x04970, 0x064b0, 0x168a6, 0x0ea50, 0x06b20, 0x1a6c4, 0x0aae0, 0x092e0, # 2060 
0x0d2e3, 0x0c960, 0x0d557, 0x0d4a0, 0x0da50, 0x05d55, 0x056a0, 0x0a6d0, 0x055d4, 0x052d0, # 2070 
0x0a9b8, 0x0a950, 0x0b4a0, 0x0b6a6, 0x0ad50, 0x055a0, 0x0aba4, 0x0a5b0, 0x052b0, 0x0b273, # 2080 
0x06930, 0x07337, 0x06aa0, 0x0ad50, 0x14b55, 0x04b60, 0x0a570, 0x054e4, 0x0d260, 0x0e968, # 2090 
0x0d520, 0x0daa0, 0x16aa6, 0x056d0, 0x04ae0, 0x0a9d4, 0x0a4d0, 0x0d150, 0x0f252, 0x0d520  # 2100 
]
yearsCoded = len(yearCode)

import os
from sys import argv, exit, stdout
from time import time, localtime
ow=stdout.write


class LunarYearInfo:
    def __init__(self):
        self.yearDays = 0
        self.monthDays = [0]*13
        self.leapMonth = -1  # -1 means no lunar leap month

yearInfo = [0]*yearsCoded #global variable
for i in range(yearsCoded):
    yearInfo[i] = LunarYearInfo()
    
class Date:
    def __init__(self,year,month,day,weekday=-1,gan=-1,zhi=-1,info=''):
        self.year     = year
        self.month    = month
        self.day      = day
        self.weekday  = weekday
        self.gan      = gan
        self.zhi      = zhi
        self.info     = info

solar1st = Date (0, 0, 30, 3) # Wednesday, January 31, 1900 
lunar1st = Date (0, 0, 0, 3, 6, 0) # First day, First month, 1900, 庚/子年

def error(msg):
    print('Error:',msg);
    exit(1)
    
def isSolarLeapYear (year):
    year=year+1900
    return (year%4 == 0) and (year%100 != 0) or (year%400 == 0)

baseYear=1601 - 1900
# in fact, real baseYear=1201 or 1601 ...  In order to ease calculation of
# leap years. real baseYear must conform to:
#   realBaseYear%4==1 and realBaseYear%400==1.
# Assert realBaseYear < solar1st.year .

# Compute the number of days from the Solar First Date
# month=0 means January, ... 
def solarDaysFromBaseYear(d):
    delta = d.year - baseYear
    offset = delta*365 + delta//4 - delta//100 + delta//400 # Floor除法
    for i in range(d.month):
        offset += daysInSolarMonth[i]; 
    if d.month>1 and isSolarLeapYear(d.year):
        offset += 1
    offset += d.day
    #print ('offset=',offset)
    return offset

# Compute the number of days from the Solar First Date
# month=0 means January, ..., year=0 means 1900, ...
def solarDaysFromFirstDate (d): #d is a Date class
    return solarDaysFromBaseYear (d) - solarDaysFromBaseYear (solar1st)

def calcLunarDaysPerMonth(iYear):
    code = yearCode[iYear]
    leapMonth = code&0xf #leapMonth==0 means no lunar leap month

    code >>= 4
    for iMonth in range(12):
        yearInfo[iYear].monthDays[11-iMonth] = lunarMonthDays [code&0x1]
        code >>= 1

    if leapMonth>0:
        yearInfo[iYear].leapMonth = leapMonth-1
        yearInfo[iYear].monthDays.insert (leapMonth,lunarMonthDays [code&0x1])
        
#初始化阴历各年的总天数
def calcAllLunarYearsInfo():
    for iYear in range(yearsCoded):
        calcLunarDaysPerMonth(iYear)
        for iMonth in range(13):
            yearInfo[iYear].yearDays += yearInfo[iYear].monthDays[iMonth]
            
def lunarDate2GB(year, month, day):
    if (month,day) in lunarHolidays:
        info = lunarHolidays[(month,day)]
    else:
        day += 1#方便转换1~30
        if day == 1:
            info = '闰' * (month//100) + monthGB[month%100] + '月'
        elif day == 10:
            info = '初十'
        elif day == 20:
            info = '二十'
        elif day == 30:
            info = '三十'
        else:
            info = tenGB[day//10] + numGB[day%10]
        
    return info

#input dateSolar, return (dateLunar, isLunarMonthOrNot)
def solar2Lunar(d): #d is a Date class
    dLunar = Date(-1, -1, -1) #unknown lunar Date class 
    
    offset = solarDaysFromFirstDate(d)
    
    dLunar.weekday = (offset + solar1st.weekday) % 7
    
    for iYear in range(yearsCoded):
        if offset < yearInfo[iYear].yearDays:
            dLunar.year = iYear; break
        offset -= yearInfo[iYear].yearDays
    if dLunar.year == -1:
        error("Date out of range.")
        
    dLunar.gan = (dLunar.year + lunar1st.gan) % 10
    dLunar.zhi = (dLunar.year + lunar1st.zhi) % 12
    
    for iMonth in range(13):
        if offset< yearInfo[dLunar.year].monthDays[iMonth]:
            dLunar.month = iMonth; break
        offset -= yearInfo[dLunar.year].monthDays[iMonth]
        
    dLunar.day = offset

    isLeapMonth=0
    if yearInfo[dLunar.year].leapMonth >=0:
        if dLunar.month ==  yearInfo[iYear].leapMonth + 1:
            isLeapMonth=1
        if dLunar.month > yearInfo[dLunar.year].leapMonth:
            dLunar.month -= 1
            
    if isLeapMonth == 1:
        dLunar.month += 100
    
    #查公历节日字典
    if (d.month,d.day) in solarHolidays:
        dLunar.info = solarHolidays[(d.month,d.day)]
    else:
        dLunar.info = lunarDate2GB(dLunar.year, dLunar.month, dLunar.day)
    
    #dLunar.info = ''
    
    return dLunar

def getSolarDaysInMonth (year,month):
    if month==1:
        if (((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)):
            return 29
        else:
            return 28
    else: 
        return daysInSolarMonth[month]

def lunarMonth2GB(month):
    if month > 99: # It's a leap month
        month -= 100
        return '闰' + monthGB[month]
    else:
        return monthGB[month]

#输出当月月历
def outputCalendar(year,month):
    dLunar = Date(-1,-1,-1)
    ow ('\n     公元%d年%d月(%s)' % (year+1900, month+1,monthEn[month] ) )
    ow(' '*(28-len(monthEn[month])))
    
    for iDay in range(getSolarDaysInMonth(year,month)):
        dSolar = Date(year,month,iDay)
        dLunar = solar2Lunar(dSolar)
        
        if iDay==0:
            ow ('%s%s年%s月 (生肖属%s)\n' %(ganGB[dLunar.gan], zhiGB[dLunar.zhi], lunarMonth2GB(dLunar.month), shengXiaoGB[dLunar.zhi]))
            ow ('='*74 + '\n')
            for i in range(7):
                ow ("%3s%2s     " % (weekdayEn[i][:3],weekdayGB[i]))
            ow('\n\n')
            for i in range(dLunar.weekday):
                ow(' '*11)
        elif dLunar.weekday == 0:
            ow('\n')
            
        ow ( "%2d %s" %(iDay+1,dLunar.info+' '*(8-2*len(dLunar.info))))
    ow('\n\n')

def checkArgv(argv):
    argc = len(argv)
    if argc==1 or argv[1] in ('-h','-help','/h','/help'):
        print(__doc__);
        exit(0)
        
    #in case people input arguments as "4-digit-year month"
    if argc==3 and len(argv[1]) == 4:
        argv[1], argv[2] = argv[2], argv[1]
        
    #argv[1] is Month, argv[2] is Year.
        
    #Get mounth(number, English or abbr.)
    month = -1
    for iMonth in range(12):
        if argv[1].lower() == monthEn[iMonth].lower() or argv[1].lower() == monthEn[iMonth][:3].lower():
            month = iMonth+1;
            break
    if month == -1:
        try: #异常处理
            month = int(argv[1])
        except ValueError:
            error ('You did not input an integer for month, try again ...' )
    if month<1 or month>12:
        error("Month not within 01--12")
    
    #Get year, if no argv[2], use current year.
    if argc == 2:
        year = localtime(time())[0]
    else:
        if len(argv[2])!=4:
            error("Year must be 4 digits.")
        else:
            try: #异常处理
                year = int(argv[2])
            except ValueError:
                error ('You did not input an integer for year, try again ... ')
        if year<1901 or year>=1900+yearsCoded:
            error ("Year must be within %d--%d" % (1901, 1900+yearsCoded-1))

    return year-1900, month-1

if __name__ == "__main__":
    year,month = checkArgv(argv)
    calcAllLunarYearsInfo()
    outputCalendar(year,month)