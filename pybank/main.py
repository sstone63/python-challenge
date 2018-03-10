import pandas as pd
import os

#How can I organize my directories to make this step simpler?
csv_path = os.path.join(os.path.dirname("pybank"), "budget_data_1.csv")

budget_data = pd.read_csv(csv_path)

Total_Months = budget_data["Date"].nunique()

Total_Revenue = budget_data["Revenue"].sum()

Average_Revenue_Change = budget_data["Revenue"].mean()

Greatest_Increase_R = budget_data["Revenue"].max()

Greatest_Decrease_R = budget_data["Revenue"].min()

print("Financial Analysis") 
print("-------------------")
print("Total Months: " + str(Total_Months))
print("Total Revenue: " + str(Total_Revenue))
print("Average Reveneue Change: " + str(Average_Revenue_Change))
print("Greatest Increase in Revenue: " + str(Greatest_Increase_R))
print("Greatest Decrease in Revenue: " + str(Greatest_Decrease_R))

budget_data.to_csv("new_budget_data.csv", index = False, header = True)

       