"""
This module provides a Flask application for emotion detection.
It includes a route for analyzing text and returning emotional analysis.
"""
from flask import Flask  # Only import the necessary modules
from EmotionDetection.emotion_detection import emotions_detector

# Create an instance of the Flask class
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detection():
    """
    This route processes the input text and returns the dominant emotion.
    If no dominant emotion is detected, it returns an error message.
    """
    # Call the emotions_detector function
    response = emotions_detector('I love my life')

    # Check if the response contains None for dominant_emotions
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!\n'

    return response

if __name__ == "__main__":
    # Run the Flask application on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)  # Use host="0.0.0.0" to make it accessible
