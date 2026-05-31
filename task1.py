import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male"],
    "Age": [18, 20, 22, 21, 19, 23, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

# ---------------- BAR CHART ----------------
gender_count = df["Gender"].value_counts()

plt.figure(figsize=(5,5))
plt.bar(gender_count.index, gender_count.values)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# ---------------- HISTOGRAM ----------------
plt.figure(figsize=(5,5))
plt.hist(df["Age"], bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()