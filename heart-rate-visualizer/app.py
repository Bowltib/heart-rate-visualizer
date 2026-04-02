from flask import Flask, render_template, request
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_data = None  # Default if no file uploaded

    if request.method == 'POST':
        # Check if file is uploaded
        if 'file' not in request.files:
            return "No file uploaded", 400
        file = request.files['file']
        if file.filename == '':
            return "No file selected", 400

        # Save uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process CSV
        data = pd.read_csv(filepath)

        # Check for required columns
        if 'Time' not in data.columns or 'BPM' not in data.columns:
            return "CSV must have 'Time' and 'BPM' columns", 400

        # Convert columns to plain Python types for JSON serialization
        time = [int(t) for t in data['Time'].tolist()]
        bpm = [int(b) for b in data['BPM'].tolist()]

        # Calculate stats
        avg_bpm = round(float(data['BPM'].mean()), 1)
        peak_bpm = int(data['BPM'].max())
        peak_time = int(data['Time'][data['BPM'].idxmax()])

        # Determine zones for each point
        zones = []
        for value in bpm:
            if value < 60:
                zones.append('low')
            elif value <= 100:
                zones.append('normal')
            else:
                zones.append('high')

        # Prepare data for frontend
        chart_data = {
            'time': time,
            'bpm': bpm,
            'avg': avg_bpm,
            'peak': {'time': peak_time, 'bpm': peak_bpm},
            'zones': zones
        }

    # Render HTML with chart data (None if not uploaded)
    return render_template('index.html', chart_data=chart_data)


if __name__ == '__main__':
    app.run(debug=True)