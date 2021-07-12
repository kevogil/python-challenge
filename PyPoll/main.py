import pandas as pd
import pathlib

csv_path = pathlib.Path("Resources/election_data.csv")
data_df = pd.read_csv(csv_path)

counties = data_df['County']

# Total number of votes cast
voter_ids = data_df['Voter ID']
total_votes = len(voter_ids)
print(f"Total votes: ", "{:,}".format(total_votes))


# Candidate vote analysis
candidates = data_df['Candidate']
candidate_count = candidates.value_counts()
candidate_percent = candidates.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
candidate_analysis = pd.DataFrame({'Percent': candidate_percent, 'Count': candidate_count})

print(candidate_analysis)


# Winner of election
candidate_count = candidate_count.sort_values(ascending=False)
candidate_list = candidate_count.index.tolist()
winner = candidate_list[0]
print(f'Winner: ', winner)


# Wrtie to text file
report = open('Analysis/export.txt','w')

report.write(f"Total votes: " + "{:,}".format(total_votes) + '\n')
report.write(candidate_analysis.to_string() + '\n')
report.write("Winner: " + winner)

report.close()