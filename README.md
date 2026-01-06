Council-
Weather Data Analysis with Web Scraping
📌 Project Overview
This project is a Python-based application that collects weather data using web scraping, cleans and processes real-world data, performs statistical analysis, detects anomalous temperature values, classifies daily weather conditions, and visualizes the results.

The main goal of the project is to demonstrate the use of Python fundamentals together with data analysis and visualization techniques.

🛠 Technologies Used
Python 3
Requests & BeautifulSoup (Web Scraping)
Pandas (Data Cleaning and Analysis)
Matplotlib & Seaborn (Data Visualization)
🌐 Data Collection
Weather data is collected from a public website using HTTP requests and HTML parsing.
The raw data may include:

missing temperature values
non-numeric entries
inconsistent date formats
These issues are handled during the data cleaning phase.

🧹 Data Cleaning
The following steps are applied to the raw dataset:

Conversion of temperature values to numeric format
Removal of missing or invalid temperature entries
Conversion of date strings to datetime objects
Removal of rows with invalid dates
This ensures the dataset is suitable for analysis.

📊 Data Analysis
The project performs several statistical analyses:

Mean, minimum, and maximum temperature calculation
Quartile analysis (25%, 50%, 75%)
Rolling average calculation
Anomaly detection using mean and standard deviation
Anomalous values are classified as:

High anomaly
Low anomaly
Normal
🌤 Weather Classification
Each day’s weather condition is classified using conditional logic based on temperature ranges:

Very Cold
Cold
Mild
Hot
Very Hot
This provides a human-readable interpretation of numerical data.

📈 Visualization
The program generates multiple plots:

Scatter plot showing temperature changes over time
Color-coded visualization of weather conditions
Box plot displaying temperature distribution and outliers
▶ How to Run the Project

Follow the steps below to run the project on your local machine.

1️⃣ Clone the repository git clone https://github.com/Orkunbayraktar/CouncilWeatherDataAnalysis.git

2️⃣ Navigate into the project folder cd CouncilWeatherDataAnalysis

3️⃣ Install required dependencies

Make sure you have Python 3 installed, then run:

pip install -r requirements.txt

4️⃣ Run the program

The main entry point of the project is main.py, which is located in the root directory.

python main.py
