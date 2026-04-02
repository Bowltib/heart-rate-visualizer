# 💓 Heart Rate Analyzer Web App

An interactive Heart Rate Analyzer built using Flask, Plotly.js, HTML, CSS, and JavaScript. This application allows users to upload heart rate data, visualize it through an interactive graph, analyze key metrics such as average and peak heart rate, and receive basic health insights.

## 🚀 Features

- Upload CSV files containing Time and BPM values  
- Interactive graph using Plotly with zoom, hover, and pan functionality  
- Automatic calculation of average heart rate  
- Detection and display of peak heart rate with timestamp  
- Color-coded heart rate zones:
  - Low (<60 BPM) → Bradycardia  
  - Normal (60–100 BPM) → Healthy  
  - High (>100 BPM) → Tachycardia  
- Hover tooltips showing time, BPM, and heart rate zone  
- Manual heart rate input with instant health feedback  
- Basic rule-based health suggestions  

## 🛠️ Tech Stack

Backend:
- Python
- Flask
- Pandas

Frontend:
- HTML
- CSS
- JavaScript

Visualization:
- Plotly.js

## 📁 Project Structure

heart-rate-web/
│
├── app.py
├── uploads/
├── templates/
│   └── index.html
└── README.md

## ⚙️ Installation

1. Clone the repository:
git clone <your-repo-link>
cd heart-rate-web

2. (Optional) Create a virtual environment:
python -m venv venv

Activate environment:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3. Install dependencies:
pip install flask pandas

## ▶️ Running the Application

Run the Flask app:
python app.py

Open your browser and go to:
http://127.0.0.1:5000/

## 📄 CSV Format

The CSV file must contain the following format:

Time,BPM
0,72
1,75
2,78
3,80

Time can represent seconds, minutes, or index values.

## 📊 How It Works

1. Upload a CSV file  
2. The backend processes the data using Pandas  
3. Key metrics such as average and peak BPM are calculated  
4. Data is sent to the frontend  
5. Plotly.js renders an interactive graph  
6. Zones are color-coded and annotated  
7. Users can also manually input BPM for quick analysis  

## 🔮 Future Enhancements

- Export graph as image (PNG/PDF)  
- Add min, max, and average summary tables  
- Improve UI/UX with modern styling  
- Add real-time heart rate simulation  
- Store user data and history  
- Integrate AI-based predictions  

## ⚠️ Disclaimer

This project is for educational purposes only. It does not provide medical diagnosis or treatment advice. Always consult a qualified healthcare professional for medical concerns.
 
## 📌 License

This project is open-source and free to use.
