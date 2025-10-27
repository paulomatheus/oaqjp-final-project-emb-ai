from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.pop('dominant_emotion')
    scores_list = []
    for emotion, score in response.items():
        scores_list.append(f"'{emotion}': {score}")
    scores_string = ", ".join(scores_list[:-1]) + f" and {scores_list[-1]}"

    return f"For the given statement, the system response is {scores_string}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=5000)