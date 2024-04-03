import random
import matplotlib.pyplot as plt

indian_breakfast_ideas = [
    'AlooParatha', 'Poha', 'Soya Methi Paratha', 'Kala chana chaat',
    'Dosa', 'poori sabji', 'Vermicilli', 'Besan ka chilla', 'Sooji Chilla',
    'Idli', 'Moon Dal Chilla'
]

lunch_menu = ['rajma-rice', 'Malai Kofta', 'Kadhai Paneer', 'Aloo Dum', 'Palak Paneer',
              'chole-rice', 'kadhi-rice', 'mix-veg', 'Gobhi Aloo', 'Taroi', 'Bhindi', 'Bharta-Baigan', 'Nutri-Aloo']

dal_menu = ['Chane ki Daal', 'Moong ki daal','Arhar ki daal' ,'Arhar ki daal','Arhar ki daal', 'Dal Makhni', 'Masoor ki daal', 'Dal Palak']

# Randomly select 7 unique dishes for the week
selected_breakfast = random.sample(indian_breakfast_ideas, 7)
selected_lunch = random.sample(lunch_menu, 7)
selected_dal = random.sample(dal_menu, 7)

# Days of the week
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create and print the table
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# Prepare data for the table
data = []
for day, breakfast, lunch, dal in zip(week_days, selected_breakfast, selected_lunch, selected_dal):
    combined_lunch_dal = f"{lunch} + {dal}"
    data.append([day, breakfast, combined_lunch_dal])


# Create the table
table = ax.table(cellText=data,
                 colLabels=['Day', 'Breakfast','Lunch'],
                 loc='center', cellLoc='center', colWidths=[0.2, 0.3, 0.6])

# Remove the axis and set font size
ax.axis('off')
table.auto_set_font_size(False)
table.set_fontsize(12)

plt.savefig('weekly_menu.png')
plt.show()
