# <span style="font-family: Arial; font-size: 30px;">Hate Speech Classification Web App</span>

## <span style="font-family: Georgia;">Description</span>
This project is a web-based application designed to classify text comments into one of three categories:
- **Hate Speech**
- **Offensive Speech**
- **No Hate**

The system uses a machine learning model trained on a labeled dataset of text comments. The model employs **Natural Language Processing (NLP)** techniques such as **TF-IDF vectorization** and **Logistic Regression** for text classification. The web application is built using **Flask**, providing a user-friendly interface to input comments and view classification results.

---

## <span style="font-family: Verdana;">Features</span>
- **Classifies comments** into Hate Speech, Offensive Speech, or No Hate.
- Provides instant predictions with a clear explanation of the class.
- Handles input validation and displays error messages for invalid or empty comments.
- Modular code structure for easy maintenance and future improvements.

---

## <span style="font-family: Tahoma;">Tech Stack</span>

### Programming Languages & Frameworks
- **Python**
- **Flask (Web Framework)**

### Libraries & Tools
- **scikit-learn**: For machine learning model training and evaluation.
- **TfidfVectorizer**: For text feature extraction.
- **Pickle**: For saving and loading the trained model and vectorizer.
- **HTML/CSS**: For the user interface.

---

## <span style="font-family: Courier New;">Installation and Setup</span>

### Clone the Repository
```bash
git clone https://github.com/your-username/hate-speech-classification.git
cd hate-speech-classification

Run the Flask Application
bash
Copier le code
python app.py
Access the Web Application
Open your browser and navigate to http://127.0.0.1:5000/.
