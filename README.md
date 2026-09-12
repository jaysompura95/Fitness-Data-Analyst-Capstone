# Fitness Business Data Analysis — Data Analyst Capstone

## Project
End-to-End analysis of a December 2020 fitness-session dataset using Python/Pandas, Excel, and Power BI.

## Assignment alignment
The Week 4 brief requires:
- clean and explore the dataset in Python;
- analyze using SQL or Pandas;
- visualize using Excel and a BI tool;
- compile a final report with charts, findings, and recommendations;
- submit complete code and a demo recording or PDF explanation report.

## Files
- `Fitness_EDA_Notebook.ipynb` — executable Python EDA notebook.
- `fitness_eda.py` — standalone Python EDA script.
- `PowerBI_Dataset.xlsx` — source dataset.
- `Fitness_Analysis.xlsx` — analysis workbook with raw data and grouped summaries.
- `PowerBI_Dashboard_Layout_and_DAX.txt` — exact Power BI build specification and DAX.
- `Fitness_Final_Report.pdf` — final stakeholder-style report.
- `README.md` — project guide.

## Python setup
```bash
pip install pandas openpyxl matplotlib jupyter
jupyter notebook Fitness_EDA_Notebook.ipynb
```

Place `PowerBI_Dataset.xlsx` in the same folder before running the notebook/script.

## Power BI setup
1. Open Power BI Desktop.
2. Get Data → Excel → `PowerBI_Dataset.xlsx`.
3. Load `Sheet1`.
4. Rename the table to `Fitness`.
5. Set `Date` to Date type; numeric columns to appropriate numeric types.
6. Add the DAX measures from `PowerBI_Dashboard_Layout_and_DAX.txt`.
7. Build the dashboard using the exact layout in that file.
8. Add slicers for Intensity and Weekday.
9. Format the page for a clean stakeholder presentation.

## Headline KPIs
- Total Sessions: 30
- Total Calories: 9,218.7
- Average Calories / Session: 307.29
- Average Calories / Minute: 5.55
- Average Duration: 55.5 minutes
- Average Pulse: 102.8
- Maximum Maxpulse: 175

## Notes
The Power BI page is designed to reproduce the structure of the supplied interactive dashboard prototype: filter controls, four KPI cards, daily calorie trend, average calories by intensity, and a session-detail table.
