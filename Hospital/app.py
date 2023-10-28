# Import necessary modules from the Flask library
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# Initialize Flask app and set the secret key for session handling
app = Flask(__name__)
app.secret_key = "secretkey"

# Data for diagnostic tests and emergency services, categorized by type
diagnostic_tests = {
    "Laboratory tests": {
        "Blood Test": {"cost": 55, "room": "201"},
        "Urine Test": {"cost": 35, "room": "202"},
        "Liver Function Test": {"cost": 60, "room": "203"},
        "Thyroid Test": {"cost": 50, "room": "204"},
        "Kidney Function Test": {"cost": 65, "room": "205"},
    },
    "Scanning tests": {
        "MRI": {"cost": 250, "room": "301"},
        "CT Scan": {"cost": 120, "room": "302"},
        "PET Scan": {"cost": 350, "room": "303"},
        "X-Ray": {"cost": 75, "room": "304"},
        "Ultrasound": {"cost": 80, "room": "305"},
    },
    "Vision tests": {
        "Eye Examination": {"cost": 55, "room": "401"},
        "Macular Degeneration Test": {"cost": 100, "room": "402"},
        "Color Blindness Test": {"cost": 25, "room": "403"},
        "Glaucoma Test": {"cost": 80, "room": "404"},
        "Peripheral Vision Test": {"cost": 60, "room": "405"},
    },
    "Respiratory tests": {
        "Lung Volume Test": {"cost": 85, "room": "501"},
        "Spirometry": {"cost": 65, "room": "502"},
        "Peak Flow Test": {"cost": 70, "room": "503"},
        "Gas Diffusion Test": {"cost": 95, "room": "504"},
        "Oxygen Saturation Test": {"cost": 45, "room": "505"},
    },
    "Hearing tests": {
        "Tympanometry": {"cost": 55, "room": "601"},
        "Audiometry Test": {"cost": 50, "room": "602"},
        "Speech Test": {"cost": 70, "room": "603"},
        "Pure Tone Test": {"cost": 60, "room": "604"},
        "Otoacoustic Emission Test": {"cost": 75, "room": "605"},
    },
    "Bio-metric tests": {
        "Heartbeat Monitoring": {"cost": 20, "room": "701"},
        "Cholesterol Test": {"cost": 70, "room": "702"},
        "Bone Density Test": {"cost": 90, "room": "703"},
        "Blood Pressure Test": {"cost": 25, "room": "704"},
        "Glucose Test": {"cost": 30, "room": "705"},
    }

}

# Define emergency services with their respective details
emergency_services = {
    "Ambulance": {"cost": 150, "ETA": "10 minutes"},
    "Paramedics": {"cost": 50, "ETA": "15 minutes"}

}


# Define the route for the homepage
@app.route('/')
def index():
    """Render the homepage."""
    return render_template("index.html")


@app.route('/diagnostics', methods=['GET', 'POST'])
def diagnostics():
    """Handle and render the diagnostics page.

    For POST requests, filter the diagnostic tests based on the submitted category and search query.
    For GET requests, display the list of available diagnostic categories.
    """
    if request.method == 'POST':
        category = request.form.get('category')
        search_query = request.form.get('search_query').lower()

        if category and category in diagnostic_tests:
            tests = {
                test_name: details for test_name, details in diagnostic_tests[category].items()
                if search_query in test_name.lower()
            }
            return render_template('diagnostics_detail.html', tests=tests, category=category)

    return render_template('diagnostics.html', categories=diagnostic_tests.keys())


@app.route('/search', methods=['GET', 'POST'])
def search():
    """Render search results based on the query.

    The search function checks all diagnostic test names against the query and displays matching tests.
    """
    query = request.form.get('query')
    results = {}

    # Search through all diagnostic tests
    for category, tests in diagnostic_tests.items():
        matching_tests = {
            test_name: details for test_name, details in tests.items()
            if query.lower() in test_name.lower()
        }
        if matching_tests:
            results[category] = matching_tests

    return render_template('search_results.html', results=results)


@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    """Handle and render the emergency services page.

    For POST requests, process the form submission and either confirm the service request or
    display a confirmation page for user verification.
    For GET requests, render the emergency service request form.
    """
    # Extracting form details
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        nid = request.form.get('nid')
        phone = request.form.get('phone')
        service_type = request.form.get('service_type')

        if 'confirm' in request.form:
            flash(
                f"Request confirmed! {name}, your {service_type} will arrive in {emergency_services[service_type]['ETA']}.",
                "success"
            )
            return redirect(url_for('emergency'))
        else:
            return render_template(
                "confirm.html", name=name, age=age, nid=nid, phone=phone, service_type=service_type,
                service_details=emergency_services[service_type]
            )

    return render_template("emergency.html", services=emergency_services)


# Main execution point of the script
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask development server in debug mode
