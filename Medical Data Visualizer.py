import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the data
df = pd.read_csv('medical_examination.csv')

# Create the overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize data
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Clean the data
df = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

# Convert data into long format for catplot
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

# Group and reformat data for catplot
df_cat['total'] = 1
df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

# Rename columns
df_cat = df_cat.rename(columns={'variable': 'variable', 'value': 'value', 'total': 'total'})

# Draw the Categorical Plot
def draw_cat_plot():
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')
    fig.set_axis_labels('variable', 'total')
    plt.show()
    return fig

# Draw the Heat Map
def draw_heat_map():
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True, linewidths=.5, ax=ax, cmap="coolwarm")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

# Draw the Categorical Plot
draw_cat_plot()

# Draw the Heat Map
draw_heat_map()
