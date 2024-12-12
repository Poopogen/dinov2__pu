import json
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

dinov2_output_dir = '/home/jovyan/dinov2/output_vitb14_merged_various_dataset_20241127'
json_path= os.path.join(dinov2_output_dir,'training_metrics.json')


file = open(json_path, 'r')#, encoding='utf-8'

i=0
for line in file.readlines():
    dict_data = json.loads(line)
    if i==0:
        keys = dict_data.keys()
        result_df = pd.DataFrame(columns = keys)
    else:
        assert dict_data.keys()==keys, 'not all lines including same keys. '

    result_df = pd.concat([result_df, pd.DataFrame([dict_data])], ignore_index=True)
    
    print(result_df)
    #print(dict_data)
    i+=1

    #break
file.close()

result_df.to_excel(os.path.join(dinov2_output_dir,'training_metrics.xlsx'))




# result_df = pd.read_excel(os.path.join(dinov2_output_dir,'training_metrics.xlsx'),index_col=0,header=0)
print(result_df)
result_df = result_df.set_index(result_df.columns[0])# result_df.columns='iteration'
print(result_df)



# Parameters for subplots
num_cols = 4
num_rows = -(-len(result_df.columns) // num_cols)  # Ceiling division


fig, axes = plt.subplots(num_rows, num_cols, figsize=(16, 4 * num_rows), sharex=True)

# Flatten the axes array for easy iteration
axes = axes.flatten()

# Plot each column
for i, column in enumerate(result_df):
    axes[i].plot(result_df.index, result_df[column], marker="o")
    axes[i].set_title(f"{column}")

    # Use scientific notation for the x-axis
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((-2, 2))  # Adjust limits for when to switch to scientific notation
    axes[i].xaxis.set_major_formatter(formatter)

# Add a shared x-axis label
fig.supxlabel(result_df.index.name, fontsize=14)
# Adjust layout
plt.tight_layout()
plt.savefig(os.path.join(dinov2_output_dir,'training_metrics.jpg'))
