from flask import Flask, request, jsonify
from tensorflow.python.keras.models import load_model
from keras.api.preprocessing import image
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado
model = load_model('model/modelo_plantas.keras')

# Diccionario con las clases del PlantVillage Dataset (puedes agregar las clases según tu dataset)
class_labels = ['Apple_scab', 'Apple_black_rot', 'Apple_healthy', 'Corn_healthy', 'Corn_blight', ...]  # Completa con todas las clases

# Función para preprocesar la imagen
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.  # Normalización
    return img_array

# Ruta para hacer predicciones
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha cargado una imagen'}), 400
    
    file = request.files['file']
    img_path = './temp_image.jpg'
    file.save(img_path)
    
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    predicted_class = class_labels[np.argmax(predictions[0])]
    
    return jsonify({'prediction': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)
