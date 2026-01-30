🎓 Student Performance Prediction – Production Ready ML System

A production-ready Machine Learning web application that predicts a student’s Maths score based on demographic and academic features.
The system is built using Python, Flask, Scikit-learn, CatBoost, and deployed on Render Cloud.

🔗 Live Demo
👉 https://production-ready-ml-system.onrender.com

📌 Features
- Predicts Maths score using trained ML model
- User-friendly web interface (Flask + HTML + Bootstrap)
- End-to-end ML pipeline (data ingestion → transformation → training → prediction)
- Custom exception handling and logging
- Production-ready project structure
- Deployed on Render with Gunicorn

🧠 Machine Learning Workflow
- Data Ingestion
- Data Transformation (encoding, scaling)
- Model Training 
- Model Evaluation
- Model Serialization
- Prediction Pipeline
- Web Deployment

🏗️ Tech Stack
- Python
- Flask
- NumPy
- Scikit-learn
- Gunicorn
- HTML, CSS, Bootstrap
- Render Cloud

📂 Project Structure

MLProject
│
├── app.py
├── requirements.txt
├── templates/
│   ├── home.html
│   └── index.html
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── notebook/
│   ├── 1_EDA_STUDENT_PERFORMANCE.ipynb
│   └── 2_MODEL_TRAINING.ipynb
│
└── README.md


📊 Input Parameters
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

🎯 Output
Predicted Maths Score

🚀 Deployment
The application is deployed on Render using: gunicorn app:app

📈 Future Improvements
- Add user authentication
- Store predictions in database
- Add model monitoring
- Improve UI with charts
- Add API endpoint

👨‍💻 Author
Kashish Raj
Machine Learning & Software Enthusiast
