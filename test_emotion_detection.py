import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion detector."""

    def test_joy(self):
        """Test that a positive sentence returns joy."""
        result = emotion_detector("I love this new technology.")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Test that an angry sentence returns anger."""
        result = emotion_detector("I am very angry and frustrated.")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_fear(self):
        """Test that a fearful sentence returns fear."""
        result = emotion_detector("I am afraid and scared.")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_disgust(self):
        """Test that a disgusting sentence returns disgust."""
        result = emotion_detector("This is disgusting.")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Test that a sad sentence returns sadness."""
        result = emotion_detector("I am feeling very sad today.")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()