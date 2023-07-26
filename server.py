from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    locations = util.get_location_names()  # Corrected: Call the function to get locations
    response = jsonify({
        'locations': locations
    })
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']  # Corrected: Use 'location' instead of 'locations'
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])  # Corrected: Remove extra parentheses around 'bath'

    # Implement the prediction logic using util module (assuming you have it implemented in 'util')
    predicted_price = util.predict_home_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'predicted_price': predicted_price
    })
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Real Estate Price Prediction")
    util.load_saved_artifacts()
    app.run()
