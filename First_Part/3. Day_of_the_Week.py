def main():
      
      #to enter the year until the value is right
      year = int(input("Enter year: "))
      while ( (year < 1900) or (year > 2100) ):
           year = int(input("Enter the correct year: "))
            
      #to enter the month until the value is right
      m = int(input("Enter month: "))
      while ( (m < 1) or ( m > 12) ):
            m = int(input("Enter the correct month: "))
      
      #to enter the day 
      b = int(input("Enter day: "))
      if ( (year %400 == 0) or ( (year %4 == 0)and(year %100 != 0) ) ) and (m == 2):
            if ( b >= 1) and (b <= 29):
                  flag = True
            else:
                  flag = False
      # check the February in not the leap
      elif (m == 2):
            if ( b >= 1) and (b <= 28):
                  flag = True
            else:
                  flag = False
      # check the not month with 31 days
      elif (m == 1, m == 3, m == 5, m == 7,m == 8, m == 10, m == 12):
            if ( b >= 1) and (b <= 31):
                  flag = True
            else:
                  flag = False
      # check the month with 30 days
      elif (m == 4, m == 6, m == 9, m == 11):
            if ( b >= 1) and (b <= 30):
                  flag = True
            else:
                  flag = False
                  
      #use the while loop to prompt the user to re-enter the day when the value was wrong
      while (flag != True):
            b = int(input("Enter the correct day: "))
            # use the conditonal statement to check the value of the day
            # based on the value of year and month
      
            # check the leap year and February
            if ( (year %400 == 0) or ( (year %4 == 0)and(year %100 != 0) ) ) and (m == 2):
                  if ( b >= 1) and (b <= 29):
                        flag = True
                  else:
                        flag = False
            # check the February in not the leap
            elif (m == 2):
                  if ( b >= 1) and (b <= 28):
                        flag = True
                  else:
                        flag = False
            # check the not month with 31 days
            elif (m == 1, m == 3, m == 5, m == 7,m == 8, m == 10, m == 12):
                  if ( b >= 1) and (b <= 31):
                        flag = True
                  else:
                        flag = False
            # check the month with 30 days
            elif (m == 4, m == 6, m == 9, m == 11):
                  if ( b >= 1) and (b <= 30):
                        flag = True
                  else:
                        flag = False
      
      #adjust the month value for the calculation          
       
      if (m>2):
            a = m - 2
      elif m == 1:
            a = m + 10
            year -= 1
      elif m == 2:
            a = m + 10
            year -= 1
            
      #compute the century
      d = year//100
            
      #adjust the year to the century year
      c = year - d*100
      
      #use the algorithm provided to compute the day of the week      
      w = (13 * a - 1 ) // 5 
      x = c // 4 
      y = d // 4 
      z = w + x + y + b + c - 2 * d 
      r = z % 7 
      r = (r + 7) % 7
      
      daylist = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
      str_day = daylist[r]
      
      print("The day is %s."%(str_day))
      
      
main()