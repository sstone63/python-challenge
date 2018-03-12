import pandas as pd
import os

#How can I organize my directories to make this step simpler?
csv_path = 'budget_data_1.csv'

budget_data = pd.read_csv(csv_path)

Total_Months = budget_data["Date"].nunique()

Total_Revenue = budget_data["Revenue"].sum()

Average_Revenue_Change = round(budget_data["Revenue"].mean())

Greatest_Increase_R = budget_data["Revenue"].max()

Greatest_Decrease_R = budget_data["Revenue"].min()

Date_Max = budget_data.loc[budget_data["Revenue"]==Greatest_Increase_R, "Date"].item()

Date_Min = budget_data.loc[budget_data["Revenue"]==Greatest_Decrease_R, "Date"].item()

print("Financial Analysis") 
print("-------------------")
print("Total Months: " + str(Total_Months))
print("Total Revenue: " + "$" + str(Total_Revenue))
print("Average Reveneue Change: " + "$" + str(Average_Revenue_Change))
print("Greatest Increase in Revenue: " + Date_Max + " " + "$" + str(Greatest_Increase_R))
print("Greatest Decrease in Revenue: " + Date_Min + " " + "$" + str(Greatest_Decrease_R))

budget_to_csv = pd.DataFrame({"Total Months": [Total_Months], "Total Revenue": [Total_Revenue], "Average Revenue Change": [Average_Revenue_Change],
                              "Greatest Increase in Revenue": [Greatest_Increase_R], "Greatest Decrease in Revenue": [Greatest_Decrease_R]})

budget_to_csv.to_csv("new_budget_data.csv", index = False, header = True)
