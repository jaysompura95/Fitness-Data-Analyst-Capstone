# 🏋️ Fitness Business Data Analysis & Performance Dashboard

## 📌 Project Overview

This project is an end-to-end **Data Analyst Capstone Project** focused on analyzing fitness business performance data and creating an interactive dashboard for business insights.

The project covers the complete data analytics workflow:

**Data → Cleaning → Exploratory Data Analysis → Analysis → Visualization → Dashboard → Insights → Recommendations**

---

## 🎯 Project Objective

The main objective of this project is to analyze fitness session data and identify meaningful patterns in:

* Workout sessions
* Calories burned
* Workout intensity
* Session duration
* Pulse and maximum pulse
* Calories burned per minute
* Weekly and weekday performance

The analysis is designed to help stakeholders understand fitness activity and make data-driven decisions.

---

## 📊 Dataset

The dataset contains **30 fitness session records** with the following variables:

| Column      | Description                  |
| ----------- | ---------------------------- |
| Duration    | Workout duration in minutes  |
| Date        | Session date                 |
| Pulse       | Average pulse during session |
| Maxpulse    | Maximum recorded pulse       |
| Calories    | Calories burned              |
| Cal_per_Min | Calories burned per minute   |
| Intensity   | Workout intensity            |
| Week        | Week number                  |
| Month       | Month of activity            |
| Weekday     | Day of the week              |

---

## 🛠️ Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Jupyter Notebook**
* **Microsoft Excel**
* **Power BI**
* **DAX**
* **GitHub**

---

## 🔍 Data Analysis Process

### 1. Data Cleaning

The dataset was checked for:

* Missing values
* Duplicate records
* Data types
* Numerical consistency
* Date formatting

The cleaned dataset was then used for further analysis.

### 2. Exploratory Data Analysis

Python and Pandas were used to analyze:

* Total workout sessions
* Total calories burned
* Average calories per session
* Average calories per minute
* Average workout duration
* Average pulse
* Maximum recorded pulse
* Performance by workout intensity
* Weekday performance
* Weekly trends

---

## 📈 Key Performance Indicators

| KPI                        |    Value |
| -------------------------- | -------: |
| Total Sessions             |       30 |
| Total Calories Burned      |  9,218.7 |
| Average Calories / Session |   307.29 |
| Average Calories / Minute  |     5.55 |
| Average Duration           | 55.5 min |
| Average Pulse              |    102.8 |
| Maximum Recorded Maxpulse  |      175 |

---

## 📊 Power BI Dashboard

The Power BI dashboard provides an interactive view of fitness business performance.

### Dashboard Components

**Filters / Slicers**

* Intensity
* Weekday

**KPI Cards**

* Total Sessions
* Total Calories
* Average Calories / Session
* Average Calories / Minute

**Charts**

* Daily Calories Trend
* Average Calories by Intensity

**Detailed Table**

* Date
* Weekday
* Duration
* Pulse
* Calories
* Calories / Minute
* Intensity

---

## 🧮 DAX Measures

```DAX
Total Sessions =
COUNTROWS(Fitness)

Total Calories =
SUM(Fitness[Calories])

Avg Calories per Session =
DIVIDE([Total Calories], [Total Sessions])

Avg Calories per Minute =
AVERAGE(Fitness[Cal_per_Min])

Avg Duration =
AVERAGE(Fitness[Duration])

Avg Pulse =
AVERAGE(Fitness[Pulse])

Max Recorded Maxpulse =
MAX(Fitness[Maxpulse])
```

---

## 💡 Key Insights

The analysis provides visibility into:

1. Overall fitness session volume and calorie expenditure.
2. Differences in calorie performance across workout intensity levels.
3. Daily changes in calories burned.
4. Relationship between workout duration and calorie expenditure.
5. Variation in performance across weekdays.
6. Workout efficiency using calories burned per minute.

---

## 📌 Business Recommendations

Based on the analysis, stakeholders can:

* Monitor workout intensity and session performance.
* Identify high-performing workout patterns.
* Encourage consistent workout schedules.
* Track calories burned per minute as an efficiency metric.
* Use dashboard filters to compare different workout segments.
* Use weekly and daily trends for performance monitoring.

---

## 📁 Project Structure

```text
Fitness-Data-Analyst-Capstone/
│
├── README.md
├── fitness_eda.py
├── Fitness_EDA_Notebook.ipynb
├── PowerBI_Dataset.xlsx
├── Fitness_Analysis.xlsx
├── Fitness_Final_Report.pdf
├── Fitness_Project_Executive_Summary.txt
├── PowerBI_Dashboard_Layout_and_DAX.txt
└── Fitness_Business_Dashboard.pbix
```

---

## 🚀 How to Run the Project

### Python Analysis

Install the required libraries:

```bash
pip install pandas numpy matplotlib openpyxl
```

Run:

```bash
python fitness_eda.py
```

Or open:

```text
Fitness_EDA_Notebook.ipynb
```

using Jupyter Notebook or JupyterLab.

### Power BI

1. Open **Power BI Desktop**.
2. Select **Get Data → Excel**.
3. Import `PowerBI_Dataset.xlsx`.
4. Load the dataset.
5. Create the DAX measures provided above.
6. Build the dashboard using the documented layout.
7. Save the Power BI file as `.pbix`.

---

## 📄 Project Deliverables

This repository contains:

* ✅ Python EDA code
* ✅ Jupyter Notebook
* ✅ Excel analysis
* ✅ Dataset
* ✅ Power BI dashboard specification
* ✅ Power BI dashboard file
* ✅ Final PDF report
* ✅ Executive summary
* ✅ Project documentation

---

## 🎓 Course Alignment

This project demonstrates:

* Data Cleaning
* Exploratory Data Analysis
* Pandas-based Analysis
* Excel Data Analysis
* Data Visualization
* Power BI Dashboard Development
* DAX Measures
* Business Insights
* Data Storytelling
* Business Recommendations

---

## 👤 Author

**Jay Sompura**

**Data Science / Data Analytics Student**

---

## ⭐ Project Outcome

This project demonstrates an end-to-end approach to transforming raw fitness data into **actionable business insights through Python, Excel and Power BI**.

**From raw data to business decisions — Data → Insights → Action.**
