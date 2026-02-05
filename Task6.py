# Task 6: Integrate Pandas and NumPy: Analyze a dataset (e.g., from Kaggle), compute statistics,
# and visualize with Matplotlib in a Flask dashboard.

from flask import Flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def dashboard():

    # 1. Load CSV
    df = pd.read_csv('data.csv')

    # 2. Compute statistics
    avg = np.mean(df['Score'])
    mx = np.max(df['Score'])
    mn = np.min(df['Score'])

    # 3. Draw chart
    plt.figure()
    plt.plot(df['Name'], df['Score'])
    plt.title('Student Scores')
    plt.savefig('static/chart.png')
    plt.close()

    # 4. Show dashboard
    return f'''
    <h1>Flask Data Dashboard</h1>
    <p><b>Average Scores:</b> {avg}</p>
    <p><b>Highest Scores:</b> {mx}</p>
    <p><b>Lowest Scores:</b> {mn}</p>
    <img src="/static/chart.png" width="400">
    '''

if __name__ == '__main__':
    app.run(debug=True)

