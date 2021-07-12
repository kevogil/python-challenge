import pandas as pd
import pathlib

csv_path = pathlib.Path("Resources/budget_data.csv")
data_df = pd.read_csv(csv_path)

dates = data_df["Date"]
profits_losses = data_df["Profit/Losses"].astype('float32')

num_of_months = int(len(dates))
total = profits_losses.sum()

# Add list of all variances into an array
total_variance = 0
all_variance = []
for i in range(1, len(profits_losses)):
    prev_row = i - 1
    variance = profits_losses[i] - profits_losses[prev_row]
    all_variance.append(variance)

# Average value of variances
avg_value = round(sum(all_variance)/len(all_variance),2)

# Greatest value of variance and identify position in variance array
max_value = max(all_variance)
max_value_index = all_variance.index(max_value) + 1

# Smallest value of variance and identify position in variance array
min_value = min(all_variance)
min_value_index = all_variance.index(min_value) + 1



# Print to terminal
print(f"Total Months: ", num_of_months)
print(f"Total: ", "${:,.2f}".format(total))
print(f"Average change: ", "${:,.2f}".format(avg_value))
print(f"Greatest increase in profits: ", dates[max_value_index], "${:,.2f}".format(max_value))
print(f"Greatest decrease in profits: ", dates[min_value_index], "${:,.2f}".format(min_value))

# Wrtie to text file
report = open('Analysis/export.txt','w')

report.write(f"Total Months: " + str(num_of_months) + '\n')
report.write(f"Total: " + "${:,.2f}".format(total) + '\n')
report.write(f"Average change: " + "${:,.2f}".format(avg_value) + '\n')
report.write(f"Greatest increase in profits: " + dates[max_value_index] + " " + "${:,.2f}".format(max_value) + '\n')
report.write(f"Greatest decrease in profits: " + dates[min_value_index] + " " + "${:,.2f}".format(min_value) + '\n')

report.close()