from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
from flask_cors import CORS 
# Initialize Flask app
app = Flask(__name__)

# Firebase Admin SDK initialization
# cred = credentials.Certificate("path/to/your/firebase-service-account.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://your-database-name.firebaseio.com/'
# })
CORS(app) 
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
        
        # Validate user data fields
        required_fields = ['teamwork', 'community_service', 'leadership', "learning", "critical_thinking", "hobbies", "club_wants"]
        schema = {
            "user_id": int,
            "teamwork": bool,
            "community_service": bool,
            "leadership": bool,
            "learning": bool,
            "critical_thinking": bool,
            "hobbies": str,
            "club_wants": str
        }
        
        schema.teamwork = user_data.get("teamwork")
        schema.community_service = user_data.get("community_service")
        schema.leadership = user_data.get("leadership")
        schema.learning = user_data.get("learning")
        schema.critical_thinking = user_data.get("critical_thinking")
        schema.hobbies = user_data.get("hobbies")
        schema.club_wants = user_data.get("club_wants")
        
        print(schema)
        
    

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