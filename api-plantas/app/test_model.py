import unittest
from app import predict

class TestModel(unittest.TestCase):

    def test_predict_healthy(self):
        # Simula la entrada de una imagen de una planta sana
        result = predict("test_images/healthy.jpg")
        self.assertEqual(result, 'Healthy')

    def test_predict_diseased(self):
        # Simula la entrada de una imagen de una planta enferma
        result = predict("test_images/diseased.jpg")
        self.assertEqual(result, 'Diseased')

if __name__ == '__main__':
    unittest.main()
