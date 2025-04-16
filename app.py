from flask import Flask, jsonify
import random
import statistics

app = Flask(__name__)

# Initial base wait times
hospitals = [
    {"name": "General Hospital", "base_wait_time": random.randint(20, 100)},
    {"name": "City Medical Center", "base_wait_time": random.randint(20, 100)},
    {"name": "Downtown ER", "base_wait_time": random.randint(20, 100)}
]

# Function to simulate 20 reports and average them
def update_wait_times():
    for hospital in hospitals:
        base = hospital["base_wait_time"]
        # Simulate 20 reported wait times within ±15 minutes
        reported_times = [max(0, base + random.randint(-15, 15)) for _ in range(20)]
        average_wait_time = round(statistics.mean(reported_times))
        hospital["wait_time"] = average_wait_time

@app.route('/wait-times', methods=['GET'])
def get_wait_times():
    update_wait_times()
    # Return only name and averaged wait_time
    response = [{"name": h["name"], "wait_time": h["wait_time"]} for h in hospitals]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
