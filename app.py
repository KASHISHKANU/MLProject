from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)
app = application

# Home Page
@app.route('/')
def index():
    return render_template('home.html')

# Prediction Route
@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'POST':

        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=int(request.form.get('reading_score')),
            writing_score=int(request.form.get('writing_score'))
        )

        final_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        preds = predict_pipeline.predict(final_df)

        return render_template('home.html', results=round(preds[0],2))

    return render_template('home.html')


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

