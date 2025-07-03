''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_emotion_detector():
    '''This code receives the text from the HTML interface and
    runs emotion detection over it using emotion_detector() function. 
    The output returned shows the emotions anger, disgust, fear, joy, sadness 
    and dominant emotion.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"]:
        formatted_response = "For the given statement, the system response is "
        for index, (key, value) in enumerate(response.items()):
            if index == len(response.items()) - 2:
                formatted_response += f"'{key}': {value}. "
            elif index == len(response.items()) - 1:
                formatted_response += f"The dominant emotion is <b>{value}.</b>"
            else:
                formatted_response += f"'{key}': {value}, "

        return formatted_response
    return "Invalid text! Please try again!."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
