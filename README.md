# 🌍 Global Earthquake Analytics Project

## 📌 Project Overview

The **Global Earthquake Analytics Project** focuses on analyzing earthquake data collected from the United States Geological Survey (USGS).

The objective is to explore global earthquake patterns, understand earthquake magnitude and depth distributions, identify trends over time, and analyze tsunami-related events using Python, SQL concepts, data visualization, and an interactive Streamlit dashboard.

## 🎯 Project Objectives

- Collect earthquake data from the USGS API.
- Perform data cleaning and preprocessing.
- Handle missing values and duplicate records.
- Perform feature engineering.
- Conduct Exploratory Data Analysis (EDA).
- Analyze earthquake magnitude, depth, frequency, and geographical distribution.
- Identify significant earthquake events and tsunami-related patterns.
- Build an interactive dashboard using Streamlit.

## 📂 Project Structure

```text
Earthquake-Analytics-Project/
│
├── Earthquake_analysis.ipynb
├── earthquake.py
├── earthquake_cleaned.zip
├── requirements.txt
└── README.md
```

## 📊 Dataset Information

**Data Source:** USGS Earthquake API

https://earthquake.usgs.gov/fdsnws/event/1/

**Data Period:** January 2021 – December 2025

The dataset contains earthquake information such as:

- Earthquake ID
- Date and Time
- Latitude and Longitude
- Magnitude
- Depth
- Location
- Magnitude Type
- Tsunami Indicator
- Significance Score

The cleaned dataset is provided as a compressed ZIP file containing the CSV data.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook
- SQL
- USGS API
- Visual Studio Code
- GitHub

## 🔍 Project Workflow

1. Data Collection – Retrieved earthquake data using the USGS API.
2. Data Cleaning – Processed missing values, duplicates, and inconsistent data.
3. Feature Engineering – Extracted year, month, day, and other time-related features.
4. Exploratory Data Analysis – Analyzed earthquake magnitude, depth, and time-based patterns.
5. Data Visualization – Created charts to understand earthquake distributions and trends.
6. Dashboard Development – Built an interactive Streamlit dashboard.

## 📈 Streamlit Dashboard Features

The interactive dashboard includes:

- Dataset Overview
- Total Earthquake Records
- Average Earthquake Magnitude
- Maximum Magnitude
- Average Earthquake Depth
- Magnitude Distribution
- Depth Distribution
- Year-wise Earthquake Trends
- Global Earthquake Map
- Tsunami Analysis
- Business Insights
- Interactive Filters for Year, Magnitude, and Depth

## 💻 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/JamunaSengodan/Earthquake-Analytics-Project.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Earthquake-Analytics-Project
```

### Step 3: Create a Virtual Environment (Optional)

```bash
python -m venv env
```

Activate it on Windows:

```bash
env\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Streamlit Dashboard

```bash
python -m streamlit run earthquake.py
```

The dashboard will open in your browser at:

http://localhost:8501

## 📓 Jupyter Notebook

The `Earthquake_analysis.ipynb` notebook contains the data collection, data cleaning, feature engineering, exploratory data analysis, and visualization steps.

## 📌 Key Outcomes

- Explored global earthquake patterns over the selected five-year period.
- Identified magnitude and depth distributions.
- Analyzed earthquake frequency across different years.
- Visualized geographical earthquake locations.
- Examined tsunami-related earthquake events.
- Developed an interactive dashboard to support data exploration and insights.

## 👩‍💻 Author

**Jamuna Sengodan**

GitHub: https://github.com/JamunaSengodan

---

*This project was developed as part of a Data Analytics learning and portfolio project.*
