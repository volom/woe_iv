import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')
# Select data for the specific feature
selected_feature = 'FEATURE_NAME'
selected_data = woe_iv[woe_iv['feature'] == selected_feature][['sample_class', 'woe']].dropna()

# Plotting a bar chart
ax = selected_data.plot.bar(x='sample_class', y='woe', color=['#006400' if val > 0 else '#8B0000'  for val in selected_data['woe']], legend=False)
plt.title(f"WOE for {selected_feature}, IV - {round(woe_iv[woe_iv['feature'] == selected_feature]['iv'].sum(),2)}")
plt.ylabel('Weight of Evidence (WOE)')
plt.xlabel('Events Count')

# Add data signatures (annotations) on top of each bar
for i, value in enumerate(selected_data['woe']):
    ax.annotate(f'{value:.2f}', (i, value), ha='center', va='bottom')

#plt.savefig(f'woe_events_result/{n+1}_{selected_feature}.png')
plt.show()
