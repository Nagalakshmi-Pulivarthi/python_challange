import csv
import os
#input ,output files path in dictionary
file_dictionary={"budget_data_1.csv":"budgetdata1.txt","budget_data_2.csv":"budgetdata2.txt"}
for key,value in file_dictionary.items():
    print("Input File:" + key  )
    #variable initialization
    total_revenue=0
    total_months=0
    revenue_change=0
    prev_revenue=0
    greatest_increase=["",0]
    greatest_decrease=["",99999999999]
    revenue_changes=[]
    csvpath=os.path.join("../PyBank",key)
    file_text=os.path.join("../PyBank",value)
   #reading csv file
    with open(csvpath) as csvfile1:
        reader1=csv.DictReader(csvfile1)

        #loop through each csv file
        for row in reader1:
            total_months=total_months+1
            total_revenue=total_revenue+int(row["Revenue"])
            revenue_change=int(row["Revenue"])-prev_revenue
            #print(revenue_change)
            prev_revenue=int(row["Revenue"])
            if (revenue_change > greatest_increase[1]):
                greatest_increase[1] = revenue_change
                greatest_increase[0] = row["Date"]

            if (revenue_change < greatest_decrease[1]):
                greatest_decrease[1] = revenue_change
                greatest_decrease[0] = row["Date"]


        
            revenue_changes.append(int(row["Revenue"]))

        # Set the Revenue average
        revenue_avg = round((sum(revenue_changes) / len(revenue_changes)),2)
        
            #print(prev_revenue)
        
        print("Total Months: " + str(total_months))
        print("Total Revenue: " +"$"+ str(total_revenue))
        print("Greatest Increase: "+"$" + str(greatest_increase[1]) + " in " + str(greatest_increase[0]))
        print("Greatest Decrease: "+"$" + str(greatest_decrease[1]) + " in " + str(greatest_decrease[0]))
        print("Average Change: " + str(revenue_avg))
        print("*************************")
        # a = int(row[1])
        with open(file_text, "w") as txt_file:
            txt_file.write("Final Analysis")
            txt_file.write("\n")
            txt_file.write("**********************************")
            txt_file.write("\n")
            txt_file.write("Total Months: " + str(total_months))
            txt_file.write("\n")
            txt_file.write("Total Revenue: "+ "$"+ str(total_revenue))
            txt_file.write("\n")
            txt_file.write("Greatest Increase: " + str(greatest_increase[1]) + " in " + str(greatest_increase[0]))
            txt_file.write("\n")
            txt_file.write("Greatest Decrease: " + str(greatest_decrease[1]) + " in " + str(greatest_decrease[0]))
            txt_file.write("\n")
            txt_file.write("Average Change: " + str(revenue_change)) 
        