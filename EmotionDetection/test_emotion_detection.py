import unittest
from unittest.mock import patch
from emotion_detection import emotions_detector

# Global mock responses
MOCK_RESPONSES = {
    "joy": {
        "emotionPredictions": [
            {"emotion": {
                'anger': 0.0132405795,
                'disgust': 0.0020517302,
                'fear': 0.009090992,
                'joy': 0.9699522,
                'sadness': 0.054984167
            }}
        ]
    },
    "anger": {
        "emotionPredictions": [
            {"emotion": {
                'anger': 0.8421,
                'disgust': 0.0321,
                'fear': 0.0215,
                'joy': 0.0130,
                'sadness': 0.0913
            }}
        ]
    },
    "disgust": {
        "emotionPredictions": [
            {"emotion": {
                'anger': 0.0211,
                'disgust': 0.8743,
                'fear': 0.0456,
                'joy': 0.0025,
                'sadness': 0.0565
            }}
        ]
    },
    "sadness": {
        "emotionPredictions": [
            {"emotion": {
                'anger': 0.0312,
                'disgust': 0.0121,
                'fear': 0.0245,
                'joy': 0.0045,
                'sadness': 0.9201
            }}
        ]
    },
    "fear": {
        "emotionPredictions": [
            {"emotion": {
                'anger': 0.0152,
                'disgust': 0.0101,
                'fear': 0.8345,
                'joy': 0.0025,
                'sadness': 0.1321
            }}
        ]
    }
}

class TestEmotionDetector(unittest.TestCase):
    @patch('requests.post')
    def test_joy_emotion(self, mock_post):
        # Mock the API response for joy
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = MOCK_RESPONSES["joy"]

        # Call the emotions_detector function
        text = "I love this new technology"
        result = emotions_detector(text)

        # Assert the results
        expected_result = {
            'anger': 0.0132405795,
            'disgust': 0.0020517302,
            'fear': 0.009090992,
            'joy': 0.9699522,
            'sadness': 0.054984167,
            "dominant_emotion": "joy"
        }
        self.assertEqual(result, expected_result)

    @patch('requests.post')
    def test_anger_emotion(self, mock_post):
        # Mock the API response for anger
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = MOCK_RESPONSES["anger"]

        # Call the emotions_detector function
        text = "I am really mad about this"
        result = emotions_detector(text)

        # Assert the results
        expected_result = {
            'anger': 0.8421,
            'disgust': 0.0321,
            'fear': 0.0215,
            'joy': 0.0130,
            'sadness': 0.0913,
            "dominant_emotion": "anger"
        }
        self.assertEqual(result, expected_result)

    @patch('requests.post')
    def test_disgust_emotion(self, mock_post):
        # Mock the API response for disgust
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = MOCK_RESPONSES["disgust"]

        # Call the emotions_detector function
        text = "I feel disgusted just hearing about this"
        result = emotions_detector(text)

        # Assert the results
        expected_result = {
            'anger': 0.0211,
            'disgust': 0.8743,
            'fear': 0.0456,
            'joy': 0.0025,
            'sadness': 0.0565,
            "dominant_emotion": "disgust"
        }
        self.assertEqual(result, expected_result)

    @patch('requests.post')
    def test_sadness_emotion(self, mock_post):
        # Mock the API response for sadness
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = MOCK_RESPONSES["sadness"]

        # Call the emotions_detector function
        text = "I am so sad about this"
        result = emotions_detector(text)

        # Assert the results
        expected_result = {
            'anger': 0.0312,
            'disgust': 0.0121,
            'fear': 0.0245,
            'joy': 0.0045,
            'sadness': 0.9201,
            "dominant_emotion": "sadness"
        }
        self.assertEqual(result, expected_result)

    @patch('requests.post')
    def test_fear_emotion(self, mock_post):
        # Mock the API response for fear
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = MOCK_RESPONSES["fear"]

        # Call the emotions_detector function
        text = "I am really afraid that this will happen"
        result = emotions_detector(text)

        # Assert the results
        expected_result = {
            'anger': 0.0152,
            'disgust': 0.0101,
            'fear': 0.8345,
            'joy': 0.0025,
            'sadness': 0.1321,
            "dominant_emotion": "fear"
        }
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
