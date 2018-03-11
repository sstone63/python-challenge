#Read in CSV
import pandas as pd

csv_path = "python-challenge/election_data_2.csv"

election_data = pd.read_csv(csv_path)

#Total Number of Votes Cast
Total_Votes = election_data["Voter ID"].nunique()

#List of Candidates receiving votes
election_results = pd.DataFrame(election_data["Candidate"].value_counts().reset_index())

election_results = election_results.rename(columns={"index": "Candidate", "Candidate": "Votes"})

#Create Column with Percentage of Votes
Vote_Percentage = round((election_results["Votes"]/Total_Votes)*100)
election_results["Percentage of Votes"] = Vote_Percentage

#Find Winner
Max_Votes = election_results["Votes"].max()

Winner = election_results.loc[election_results["Votes"]==Max_Votes, "Candidate"].item()

print("Election Results")
print("------------------")
print("Total Votes: " + str(Total_Votes))
print("------------------")
print(election_results.to_string(index=False))
print("------------------")
print("Winner:" + " " + Winner)

election_results.to_csv("Election_Results.csv", index = False, header = True)