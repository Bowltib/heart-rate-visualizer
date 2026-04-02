# Heart Rate Analyzer 💓

A web-based interactive heart rate analyzer built with **Flask**, **Plotly.js**, **HTML/CSS/JS**, and **Pandas**.  

This app allows users to **upload heart rate data** via CSV, visualize it in an interactive graph, check average and peak heart rates, view heart rate zones, and even **manually input heart rate values** for instant health insights.

---

## Features

1. **CSV Upload & Visualization**  
   - Upload CSV files containing `Time` and `BPM` columns.  
   - Interactive Plotly graph showing heart rate over time.  
   - Color-coded heart rate zones:  
     - **Blue**: Bradycardia (<60 BPM)  
     - **Green**: Normal (60–100 BPM)  
     - **Red**: Tachycardia (>100 BPM)  

2. **Hover Tooltips**  
   - Each point on the graph displays Time, BPM, and Zone when hovered.  

3. **Analysis Metrics**  
   - Displays **Average BPM**  
   - Displays **Peak BPM** with time of occurrence  

4. **Manual Heart Rate Input**  
   - Users can enter a BPM value manually and receive instant health advice.  

---

## Tech Stack

- **Backend**: Python 3.x, Flask  
- **Data Processing**: Pandas  
- **Visualization**: Plotly.js  
- **Frontend**: HTML, CSS, JavaScript  

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-link>
cd heart-rate-analyzer
