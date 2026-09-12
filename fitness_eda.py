# Fitness Business Data Analysis - Python EDA
# Data Analyst Capstone | December 2020
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "PowerBI_Dataset.xlsx"

df = pd.read_excel(INPUT_FILE)
df["Date"] = pd.to_datetime(df["Date"])

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nDescriptive statistics:\n", df.describe(include="all"))

# Calculated field validation
df["Calculated_Cal_per_Min"] = df["Calories"] / df["Duration"]
print("\nCal_per_Min validation (first 10 rows):")
print(df[["Calories", "Duration", "Cal_per_Min", "Calculated_Cal_per_Min"]].head(10))

# KPI summary
kpis = {
    "Total Sessions": len(df),
    "Total Calories": df["Calories"].sum(),
    "Average Calories / Session": df["Calories"].mean(),
    "Average Calories / Minute": df["Cal_per_Min"].mean(),
    "Average Duration (min)": df["Duration"].mean(),
    "Average Pulse": df["Pulse"].mean(),
    "Maximum Maxpulse": df["Maxpulse"].max(),
}
print("\nKPIs:")
for k, v in kpis.items():
    print(f"{k}: {v:.2f}" if isinstance(v, float) else f"{k}: {v}")

# Grouped analysis
print("\nIntensity analysis:")
print(df.groupby("Intensity").agg(
    Sessions=("Intensity", "size"),
    Total_Calories=("Calories", "sum"),
    Avg_Calories=("Calories", "mean"),
    Avg_Cal_per_Min=("Cal_per_Min", "mean"),
    Avg_Duration=("Duration", "mean")
).round(2))

print("\nWeekday analysis:")
print(df.groupby("Weekday").agg(
    Sessions=("Weekday", "size"),
    Total_Calories=("Calories", "sum"),
    Avg_Calories=("Calories", "mean")
).round(2))

print("\nWeekly analysis:")
print(df.groupby("Week").agg(
    Sessions=("Week", "size"),
    Total_Calories=("Calories", "sum"),
    Avg_Calories=("Calories", "mean")
).round(2))

# Charts
plt.figure(figsize=(10, 5))
plt.plot(df.sort_values("Date")["Date"], df.sort_values("Date")["Calories"], marker="o")
plt.title("Daily Calories Burned")
plt.xlabel("Date")
plt.ylabel("Calories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_calories.png", dpi=160)
plt.close()

intensity_avg = df.groupby("Intensity")["Calories"].mean().reindex(["Low","Medium","High"])
plt.figure(figsize=(7, 5))
intensity_avg.plot(kind="bar")
plt.title("Average Calories by Intensity")
plt.xlabel("Intensity")
plt.ylabel("Average Calories")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("avg_calories_by_intensity.png", dpi=160)
plt.close()

print("\nEDA completed successfully.")
