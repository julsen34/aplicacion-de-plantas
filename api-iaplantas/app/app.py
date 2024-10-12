from flask import Flask, request, jsonify
from tensorflow.python.keras.models import load_model
from keras.api.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Cargar el modelo entrenado
try:
    model = load_model('model/modelo_plantas.keras')
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    model = None

# Diccionario con las clases del PlantVillage Dataset 
class_labels = ['Apple_scab', 'Apple_black_rot', 'Apple_healthy', 'Corn_healthy', 'Corn_blight']

# Función para preprocesar la imagen
def preprocess_image(img_path):
    try:
        # Asegúrate de que el tamaño de la imagen sea el esperado por tu modelo (ajústalo según tu modelo)
        img = image.load_img(img_path, target_size=(224, 224))  # Usa el tamaño correcto para tu modelo
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalización
        return img_array
    except Exception as e:
        print(f"Error al preprocesar la imagen: {e}")
        return None

# Ruta para hacer predicciones
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha cargado una imagen'}), 400
    
    file = request.files['file']
    
    # Guardar la imagen temporalmente para procesarla
    img_path = './temp_image.jpg'
    file.save(img_path)
    
    # Preprocesar la imagen
    img_array = preprocess_image(img_path)
    
    if img_array is None:
        return jsonify({'error': 'No se pudo procesar la imagen'}), 500
    
    try:
        # Hacer la predicción
        predictions = model.predict(img_array)
        predicted_class = class_labels[np.argmax(predictions[0])]
        
        # Eliminar la imagen temporal
        os.remove(img_path)
        
        # Devolver la predicción en formato JSON
        return jsonify({'prediction': predicted_class})
    
    except Exception as e:
        print(f"Error al hacer la predicción: {e}")
        return jsonify({'error': 'Ocurrió un error durante la predicción'}), 500

if __name__ == '__main__':
    if model is None:
        print("No se pudo cargar el modelo. Revisa el archivo del modelo y vuelve a intentarlo.")
    else:
        app.run(debug=True)

