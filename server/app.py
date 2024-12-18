# -*- coding: utf-8 -*-
"""app2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UyVxF2OP_J7kCLMGHWZdp16LKsyFb7Ui
"""

from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
from flask_cors import CORS
import csv
import import_ipynb
from mlFunctions import listOfMatchingClubs

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
club_descriptions = [row['description'] for row in organizations_data][0:5]
club_title = [row['name'] for row in organizations_data][0:5]
# Read the event details CSV file
with open('event_details.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    event_details = [row for row in csv_reader]

# Print the event details to verify
event_descriptions = [row['description'] for row in event_details]



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
        ai_result = listOfMatchingClubs(club_title,club_descriptions, user_data.get('teamwork') , user_data.get('community_service') , user_data.get('leadership'), user_data.get('learning'), user_data.get('critical_thinking'), user_data.get('hobbies') , user_data.get('club_preferences'))
        print(ai_result)
        
        if(ai_result == []):
            return jsonify({"error": "No matching clubs found"}), 404
        return "", 200

    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)