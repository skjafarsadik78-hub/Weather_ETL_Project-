# 🌦️ Weather ETL Data Engineering Pipeline

A complete End-to-End Data Engineering project that extracts real-time weather data from the Open-Meteo API, transforms the data using Python, stores it in MySQL, and visualizes insights through an interactive Power BI dashboard.

---

# 📌 Project Overview

This project demonstrates the complete ETL (Extract, Transform, Load) process used in modern Data Engineering.

The pipeline automatically:

- Extracts live weather data from multiple Indian cities
- Cleans and transforms the raw JSON data
- Stores the processed data in MySQL
- Generates business insights using Power BI
- Supports repeated execution to collect historical weather data

---

# 🚀 Project Architecture

```
                Open-Meteo API
                       │
                       ▼
             Extract (Python)
                       │
            weather.json (Raw Data)
                       │
                       ▼
            Transform (Python)
                       │
            weather.csv (Cleaned Data)
                       │
                       ▼
              Load into MySQL
                       │
                       ▼
            Power BI Dashboard
```

---

# 📂 Project Structure

```
Weather_ETL_Project/
│
├── data/
│   ├── raw/
│   │     weather.json
│   │
│   └── cleaned/
│         weather.csv
│
├── scripts/
│     extract.py
│     transform.py
│     load.py
│     main.py
│
├── screenshots/
│
├── sql/
│
├── dashboard/
│     Weather_ETL_Dashboard.pbix
│
├── requirements.txt
│
└── README.md
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | ETL Pipeline |
| Requests | API Integration |
| Pandas | Data Cleaning & Transformation |
| MySQL | Data Storage |
| MySQL Connector | Database Connectivity |
| Power BI | Dashboard & Visualization |
| Git & GitHub | Version Control |

---

# 🌍 Weather Data Source

Open-Meteo API

No API key required.

Data includes:

- Temperature
- Humidity
- Wind Speed
- Date & Time

---

# 🏙️ Cities Covered

- Hyderabad
- Bengaluru
- Chennai
- Mumbai
- Delhi
- Kolkata
- Pune
- Visakhapatnam

---

# ⚙️ ETL Workflow

## Step 1 - Extract

Python fetches live weather data from the Open-Meteo API for multiple cities.

Output:

```
weather.json
```

---

## Step 2 - Transform

Transforms JSON into a structured CSV file.

Tasks performed:

- Cleaned records
- Selected required columns
- Standardized data format

Output:

```
weather.csv
```

---

## Step 3 - Load

Loads transformed data into MySQL.

Stored columns:

- City
- Time
- Temperature
- Humidity
- Wind Speed
- Recorded Timestamp

---

# 📊 Dashboard Features

The Power BI dashboard provides:

✅ Average Temperature

✅ Highest Temperature

✅ Average Humidity

✅ Average Wind Speed

✅ Temperature by City

✅ Humidity by City

✅ Wind Speed by City

✅ Temperature Trend

✅ Last Updated Timestamp

✅ City Filter (Slicer)

---

# 📈 Sample Dashboard

> Replace this image after uploading your dashboard screenshot.

```
screenshots/dashboard.png
```

---

# 💾 Database Schema

```sql
CREATE TABLE weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    time VARCHAR(100),
    temperature FLOAT,
    humidity INT,
    wind_speed FLOAT,
    recorded_at DATETIME
);
```

---

# ▶️ How to Run

## Clone Repository

```bash
git clone https://github.com/yourusername/Weather_ETL_Project.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure MySQL

Create a database:

```sql
CREATE DATABASE weather_db;
```

Update database credentials in:

```
scripts/load.py
```

---

## Run ETL Pipeline

```bash
python scripts/main.py
```

The pipeline will:

✔ Extract Data

✔ Transform Data

✔ Load into MySQL

---

# 📷 Project Screenshots

## ETL Pipeline

(Add Screenshot)

---

## MySQL Table

(Add Screenshot)

---

## Power BI Dashboard

(Add Screenshot)

---

# 📌 Future Improvements

- Dockerize the project
- Apache Airflow scheduling
- Historical weather analytics
- Automated email reports
- Cloud deployment (AWS/Azure)
- Data quality checks
- Logging and monitoring

---

# 📚 Learning Outcomes

Through this project I learned:

- Building an ETL pipeline
- API integration using Python
- Data transformation with Pandas
- Loading data into MySQL
- Creating Power BI dashboards
- End-to-End Data Engineering workflow
- Data visualization best practices

---

# 👨‍💻 Author

**Jafar Sadik Shaik**

Final Year B.Tech Student

Aspiring Data Engineer | Python | SQL | Power BI | MySQL


---

# ⭐ If you like this project

<<<<<<< HEAD
Please consider giving this repository a ⭐ on GitHub.
=======
Please consider giving this repository a ⭐ on GitHub.
>>>>>>> 31a44507dc7631eb256b1393642ac3aa8ea0fcc8
