import random
import matplotlib.pyplot as plt
import numpy as np

# Lists of dishes for breakfast, lunch, and dinner
indian_breakfast_ideas = [
    'AlooParatha', 'Poha', 'Soya Methi Paratha', 'Kala chana chaat',
    'Dosa', 'poori sabji', 'Vermicilli', 'Besan ka chilla', 'Sooji Chilla',
    'Idli', 'Moon Dal Chilla'
]

lunch_menu = ['rajma-rice', 'Malai Kofta', 'Kadhai Paneer','Kale-Channe','Safed Matar ki Sabji','Aloo Dum', 'Palak Paneer',
              'chole-rice', 'kadhi-rice', 'mix-veg', 'Gobhi Aloo', 'Taroi', 'Bhindi', 'Bharta-Baigan', 'Nutri-Aloo']

dal_menu = ['Chane ki Daal', 'Moong ki daal', 'Arhar ki daal','Arhar ki daal','Arhar ki daal','Arhar ki daal', 'Dal Makhni', 'Masoor ki daal', 'Dal Palak']

dinner_menu = ['Chole-Bhature', 'Matar-Paneer', 'Kadhai-Paneer', 'Malai-Kofta',
               'Sambhar-Rice', 'Tehri', 'Gobhi- Aloo', 'Mix-Veg', 'Biryani',
               'Aloo-Methi','Pav-Bhaji', 'Baigan-Aloo', 'Nutri-Matar', 'Chole-Rice',
               'Lauki-Kofta','Dum Aloo','Idli-Sambhar']

# Randomly select 7 unique dishes for the week
selected_breakfast = random.sample(indian_breakfast_ideas, 7)
selected_lunch = random.sample(lunch_menu, 7)
selected_dal = random.sample(dal_menu, 7)
selected_dinner = random.sample(dinner_menu, 7)

# Days of the week
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create and print the table
fig, ax = plt.subplots(figsize=(14, 3))
ax.axis('off')

data =[]
# Create the table
col_labels = ['Day', 'Breakfast', 'Lunch', 'Dinner']
col_widths = [0.1, 0.25, 0.35, 0.3]  # Adjust column widths

for day, breakfast, lunch, dal, dinner in zip(week_days, selected_breakfast, selected_lunch, selected_dal, selected_dinner):
    combined_lunch_dal = f"{lunch} + {dal}"
    data.append([day, breakfast, combined_lunch_dal, dinner])

# Create the table
table = ax.table(cellText=data,
                 colLabels=['Day', 'Breakfast', 'Lunch', 'Dinner'],
                 loc='center', cellLoc='center')

# Set font size
table.auto_set_font_size(False)
table.set_fontsize(12)

# Random colors for table heading
heading_colors = [plt.cm.jet(np.random.rand()) for _ in range(len(data[0]))]
for i, color in enumerate(heading_colors):
    table[(0, i)].set_facecolor(color)

# Add footer
footer_text = "Your Weekly Food Chart - created by Aakash Saxena"
footer = fig.text(0.99, 0.01, footer_text, horizontalalignment='right', verticalalignment='bottom', fontsize=10)

plt.savefig('weekly_menu.png')
plt.show()
