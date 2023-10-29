from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name)

# Sample data structures to simulate database functionality
blood_bank = {'A+': 10, 'B+': 15, 'O+': 5,'AB+': 20, 'A-': 10, 'B-': 15, 'O-': 5,'AB-': 20,}
appointments = []
announcements = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request_blood', methods=['POST'])
def request_blood():
    name = request.form['name']
    blood_type = request.form['blood_type']
    pickup_time = request.form['pickup_time']
    
    if blood_type in blood_bank and blood_bank[blood_type] > 0:
        blood_bank[blood_type] -= 1
        return f"Blood request for {name} ({blood_type}) submitted successfully! Pickup time: {pickup_time}"
    else:
        return "Blood type not available in the blood bank."

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/cancel_appointment', methods=['POST'])
def cancel_appointment():
    appointment_id = request.form['appointment_id']
    
    # Implement cancellation logic here
    # You can remove the appointment with the given ID from the 'appointments' list
    
    return "Appointment canceled successfully!"

@app.route('/add_announcement', methods=['POST'])
def add_announcement():
    announcement = request.form['announcement']
    announcements.append(announcement)
    return "Announcement added successfully!"

if __name__ == '__main__':
    app.run(debug=True)
