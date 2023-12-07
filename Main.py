
    
import csv
import datetime
month=0
total=0
numbers=0
avg=0
i=0
increase=[]
decrease=[]
profit_sum=[]
# opening the CSV file

with open('Resources/budget_data.csv', mode ='r')as file:
   
  # reading the CSV file
  csvfile = csv.reader(file)
 
  csv_header = next(csvfile)
  print(f"CSV Header: {csv_header}")

  # displaying the contents of the CSV file
  for lines in csvfile:
        print(lines)

        month=( month + 1 )
        
        print(month)
        print(lines[1])
        print(lines[0])
        
        profit_sum.append(int(lines[1]))
         
  print (profit_sum)
  print (len(profit_sum))
  print ("there is a total of "+(str(sum((profit_sum)))))
  while i < len(profit_sum):
      total += profit_sum[i]
      i += 1
  avg = total / len(profit_sum)
  print(avg)
 ``

  


  #for row in csvfile:
    #print(row[1])    


  # display the number of months included in the data set

# display the total Profit Losses





   


        
    
