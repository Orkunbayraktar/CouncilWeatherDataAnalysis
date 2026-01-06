# 📊 Council Weather Data Analysis

A Python-based weather data analysis application that uses **web scraping**, **data cleaning**, **statistical analysis**, **anomaly detection**, and **visualization** to explore real-world weather trends and conditions. :contentReference[oaicite:0]{index=0}

---

## 🚀 Overview

This project demonstrates how to gather weather data from a public source, preprocess it, analyze key patterns, classify daily weather conditions, and generate insightful visualizations.

It’s ideal for developers and data enthusiasts who want a hands-on example of Python-driven **data engineering + analytics** workflows. :contentReference[oaicite:1]{index=1}

---

## 🔍 Key Features

✅ **Web Scraping** – Collect weather data from a website using HTTP requests and HTML parsing. :contentReference[oaicite:2]{index=2}  
✅ **Data Cleaning & Preparation** – Handle missing values, normalize formats, and clean dataset inconsistencies. :contentReference[oaicite:3]{index=3}  
✅ **Statistical Insights** – Compute mean, min, max, quartiles, and rolling averages. :contentReference[oaicite:4]{index=4}  
✅ **Anomaly Detection** – Detect unusually high or low temperatures. :contentReference[oaicite:5]{index=5}  
✅ **Weather Classification** – Label daily conditions (Very Cold → Very Hot). :contentReference[oaicite:6]{index=6}  
✅ **Visualizations** – Generate plots that visualize time series trends and distributions. :contentReference[oaicite:7]{index=7}

---

## 🔧 Technologies

- Python 3.x  
- `requests`, `BeautifulSoup` for web scraping  
- `pandas` for data cleaning & analysis  
- `matplotlib`, `seaborn` for plotting and visualization :contentReference[oaicite:8]{index=8}

---

## 📦 Installation

1. **Clone the Repo**

   ```bash
   git clone https://github.com/Orkunbayraktar/CouncilWeatherDataAnalysis.git
   cd CouncilWeatherDataAnalysis

2.  **Create a Virtual Environment (optional but recommended)**

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3.  **Install Dependencies**

pip install -r requirements.txt

4. **Run the Application**

python main.py



## ⚙️ What Happens Next?
Once started, the program automatically:
- Scrapes weather data from the source
- Cleans and preprocesses the dataset
- Performs statistical analysis and anomaly detection
- Classifies daily weather conditions
- Generates visualizations and outputs results


## 📈 Expected Output

After running the application, the user can expect the following outputs:

### Console Output
- Summary statistics such as **average, minimum, and maximum temperatures**
- Detection of **anomalous temperature values**
- Printed classification of daily weather conditions

### Visual Output
The program generates several plots to help interpret the data, including:
- **Temperature trends over time**
- **Distribution plots** showing temperature spread
- **Box plots** highlighting outliers and anomalies

These visualizations provide insights into seasonal patterns, temperature variability, and unusual weather behavior.


## 📁 Project Structure
.
├── analysis.py         # Statistical analytics
├── datacleaning.py     # Cleaning & formatting
├── main.py             # Entry point
├── visualization.py    # Plots & charts
├── webscraping.py      # Data collection logic
├── requirements.txt    # Dependencies
├── README.md           # Project overview
└── LICENSE             # MIT License


## 📝 License

This project is licensed under the MIT License.


## 📬 Contact

Created by Council Team — feel free to reach out or fork the repo ⭐.








