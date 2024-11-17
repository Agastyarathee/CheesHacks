
# **ClubMatch: AI-Driven Club Recommendation System**

ClubMatch is a machine learning-based system designed to recommend campus clubs and organizations to students based on their personality traits and preferences. By analyzing club descriptions and user-provided personality scores, the system provides highly personalized and inclusive recommendations.

---

## **Getting Started**

These instructions will help you set up and run the project locally for development and testing. For details on deploying or expanding the project, see the **Deployment** section.

---

### **Prerequisites**

Before running the project, ensure you have the following installed:

- **Python 3.x** - [Download Python](https://www.python.org/downloads/)
- **Flask** for backend API development  
  Install via pip:  
  ```bash
  pip install flask
  ```
- **Pandas** for data manipulation  
  Install via pip:  
  ```bash
  pip install pandas
  ```
- **Scikit-learn** for implementing the recommendation system  
  Install via pip:  
  ```bash
  pip install scikit-learn
  ```
- **Node.js** (for the frontend) - [Download Node.js](https://nodejs.org/)
- **React.js** for building the frontend

---

### **Installing**

Follow these steps to get the project up and running:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/clubmatch.git
   cd clubmatch
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install backend dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the frontend:**
   Navigate to the `frontend/` directory and install React dependencies:
   ```bash
   cd frontend
   npm install
   ```

5. **Prepare your data:**
   - The project uses club data scraped from the **UW-Madison Clubs Directory**. Ensure the `clubs.csv` file (containing club names and descriptions) is located in the `data/` directory.

---

### **Usage**

1. **Run the Flask backend:**
   Start the backend server to handle personality scores and club matching.
   ```bash
   python app.py
   ```

2. **Run the React frontend:**
   Navigate to the `frontend/` directory and start the development server:
   ```bash
   npm start
   ```

3. **Access the application:**
   Open your browser and navigate to `http://localhost:3000` to use the app.

4. **Data Flow:**
   - **Frontend (React):** Users fill out a personality survey through an interactive form.
   - **Backend (Flask):** Flask processes survey data, computes a personality score, and matches it to clubs using a keyword-based algorithm.
   - **Recommendations:** The app displays a list of recommended clubs ranked by relevance.

---

## **Running Tests**

To validate the system's functionality:

1. **Backend Tests:**
   - Use provided test data in `test_data.csv` to ensure club matching works as expected.  
   - Run:  
     ```bash
     python tests/test_recommendations.py
     ```

2. **Frontend Tests:**
   - Run React testing suite to ensure UI components function correctly:  
     ```bash
     npm test
     ```

3. **Coding Style Tests:**
   - Ensure backend code adheres to PEP 8 standards using a linter like `flake8`:  
     ```bash
     pip install flake8
     flake8 .
     ```

---

## **Deployment**

1. **Deploy the Flask Backend:**
   - Deploy Flask on platforms like Heroku, AWS, or any hosting provider supporting Python.
   - Prepare for deployment by creating a `Procfile` for Heroku.

2. **Deploy the React Frontend:**
   - Build the React app for production:  
     ```bash
     npm run build
     ```
   - Deploy on platforms like Netlify or Vercel.

---

## **Built With**

- **Python** - Main programming language
- **Flask** - For backend API development
- **Pandas** - For data analysis and manipulation
- **Scikit-learn** - For implementing the recommendation algorithm
- **React.js** - For building the frontend user interface

---

## **Contributing**

We welcome contributions! Please read `CONTRIBUTING.md` for details on our code of conduct and how to submit pull requests.

---

## **Versioning**

We use **SemVer** for versioning. For available versions, see the [tags on this repository](https://github.com/yourusername/clubmatch/tags).  
Current version: **v1.0.0**

---

## **Authors**

- **Agastya Rathee**
- **Ethan Feiges**
- **Abhijeet Beedikar**
- **Nishith Shankar**

---

## **License**

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

---

## **Acknowledgments**

- **UW-Madison Clubs Directory** for club data.
- Hat tip to open-source libraries and tools.
- Inspiration from recommendation systems and machine learning.

---
