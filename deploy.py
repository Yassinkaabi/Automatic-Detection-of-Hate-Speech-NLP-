from flask import Flask, request, render_template, jsonify, flash, redirect, url_for
import pickle
from bson.objectid import ObjectId
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient

# Flask app initialization
app = Flask(__name__)
app.secret_key = "your_secret_key"

# MongoDB setup
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client['comments_database']
comments_collection = db['comments']

# Load the hate speech classification model and vectorizer
model_path = 'logistic_regression_model.pkl'
vectorizer_path = 'tfidf_vectorizer.pkl'

try:
    model = pickle.load(open(model_path, 'rb'))
    vectorizer = pickle.load(open(vectorizer_path, 'rb'))
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()
except pickle.UnpicklingError as e:
    print(f"Pickle Load Error: {e}")
    exit()

# Class mapping dictionary
class_mapping = {
    0: "Hate Speech", 1: "Offensive Speech", 2: "No Hate", 
    "Hate Speech": "Hate Speech", 
    "Offensive Speech": "Offensive Speech", 
    "No Hate": "No Hate"
}

# Helper function to classify text
def classify_text(comment):
    try:
        if not comment:
            return "Error: Comment is empty."

        vectorized_comment = vectorizer.transform([comment])
        prediction = model.predict(vectorized_comment)[0]
        return class_mapping.get(prediction, "Unknown Class")
    except Exception as e:
        print(f"Exception: {e}")
        return "Error during classification."

# Home route to display all comments
@app.route("/")
def index():
    comments = comments_collection.find()
    return render_template("index.html", comments=comments)

# Create a new comment
@app.route("/create", methods=["GET"])
def create():
    return render_template("create.html")


@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        comment = request.form.get('comment', '').strip()
        if not comment:
            flash("Please enter a valid comment.", "danger")
            return redirect(url_for('create'))  # Redirect back to the create page

        predicted_class = classify_text(comment)

        if predicted_class == "No Hate":
            comments_collection.insert_one({"text": comment})
            flash("Comment successfully stored as 'No Hate'.", "success")
            return redirect(url_for('index'))
        elif predicted_class in ["Hate Speech", "Offensive Speech"]:
            flash(f"Alert: This is {predicted_class}.", "danger")
            return redirect(url_for('index'))

        flash("An unexpected error occurred during classification.", "danger")
        return redirect(url_for('index'))

# Read a specific comment by ID
@app.route('/comment/<comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = comments_collection.find_one({"_id": ObjectId(comment_id)})
    return render_template('comment.html', comment=comment)

# Delete a specific comment by ID
@app.route('/comment/<comment_id>', methods=['POST'])
def delete_comment(comment_id):
        comments_collection.delete_one({"_id": ObjectId(comment_id)})
        flash("Comment deleted successfully.", "success")
        return redirect(url_for('index'))

# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True)
