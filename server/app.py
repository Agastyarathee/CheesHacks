from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
from flask_cors import CORS 
import csv
# Initialize Flask app
app = Flask(__name__)

# Firebase Admin SDK initialization
# cred = credentials.Certificate("path/to/your/firebase-service-account.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://your-database-name.firebaseio.com/'
# })
CORS(app) 

# Read the organizations data CSV file
with open('organizations_data.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    organizations_data = [row for row in csv_reader]


# Extract only the descriptions from the organizations data
club_descriptions = [row['description'] for row in organizations_data]
club_title = [row['name'] for row in organizations_data]
# Read the event details CSV file
with open('event_details.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    event_details = [row for row in csv_reader]

# Print the event details to verify
event_descriptions = [row['description'] for row in event_details]
event_title = [row['name'] for row in event_details]

# Print the event details to verify
print(event_details)
# Dummy AI model function
def dummy_ai_model(user_data):
    """
    Placeholder function for AI model processing.
    Takes user data as input and returns a dummy result.
    """
    # Replace this with your actual AI model logic
    return {"prediction": "success", "confidence": 0.95}

@app.route('/submit', methods=['POST'])
def submit_user_data():
    try:
        # Get JSON data from the request
        user_data = request.json
        print(user_data)
        # # Send schema to Firebase
        # ref = db.reference('users')  # Creates a 'schemas' node in the Firebase DB
        # ref.push(schema)  # Pushes the schema to the database
        
       
        # Run the AI model on the user data
        ai_result = dummy_ai_model(user_data)

        # Combine and return the results
        response = {
            "firebase_status": "User data sent successfully",
            "ai_result": ai_result
        }

        return jsonify(schema), 200

    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)