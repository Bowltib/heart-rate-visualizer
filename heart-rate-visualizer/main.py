import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv("heart_rate.csv")

# Extract columns
time = data["Time"]
bpm = data["BPM"]

# Plot graph with markers
plt.plot(time, bpm, marker='o')
# Highlight heart rate zones
plt.fill_between(time, bpm, where=(bpm < 60), interpolate=True, alpha=0.3)
plt.fill_between(time, bpm, where=((bpm >= 60) & (bpm <= 100)), interpolate=True, alpha=0.3)
plt.fill_between(time, bpm, where=(bpm > 100), interpolate=True, alpha=0.3)

# Titles and labels
plt.title("Heart Rate Over Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Beats Per Minute (BPM)")

# Add grid
plt.grid()
# Calculate average BPM
avg_bpm = bpm.mean()

# Draw average line
plt.axhline(y=avg_bpm, linestyle='--')

# Label the average line
plt.text(time.iloc[-1], avg_bpm, f'Avg: {avg_bpm:.1f}')
# Find peak heart rate
max_bpm = bpm.max()
max_index = bpm.idxmax()
max_time = time[max_index]

# Mark peak point
plt.scatter(max_time, max_bpm)

# Label peak
plt.text(max_time, max_bpm, f'Peak: {max_bpm}')
# Show graph
plt.show()