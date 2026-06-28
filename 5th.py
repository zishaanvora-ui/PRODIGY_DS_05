import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import filedialog

print("Select US Accidents CSV file...")
file = filedialog.askopenfilename()
df = pd.read_csv(file)

df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='mixed')
df['Hour']       = df['Start_Time'].dt.hour

plt.figure(figsize=(10, 5))
sns.countplot(x='Hour', data=df, hue='Hour', palette='flare', legend=False)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour (0–23)')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.show()

top_weather = df['Weather_Condition'].value_counts().head(8)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_weather.values, y=top_weather.index,
            hue=top_weather.index, palette='coolwarm', legend=False)
plt.title('Top 8 Weather Conditions During Accidents')
plt.xlabel('Number of Accidents')
plt.tight_layout()
plt.show()
