# app.api

from flask import Flask, request, jsonify
from tensorflow import keras
from keras.api.models import load_model
from keras.api.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Cargar el modelo entrenado
model = None
try:
    model = load_model('model/modelo_plantas.keras')  # Asegúrate del formato correcto
    print("Modelo cargado correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")

# Diccionario con las clases del PlantVillage Dataset 
class_labels = ['Apple_scab', 'Apple_black_rot', 'Apple_healthy', 
                'Corn_healthy', 'Corn_blight', 'Tomato_bacterial_spot', 
                'Tomato_early_blight', 'Tomato_late_blight', 
                'Tomato_healthy', 'Tomato_mosaic_virus', 
                'Tomato_target_spot', 'Potato_early_blight', 
                'Potato_late_blight', 'Potato_healthy', 'Pepper_bacterial_spot', 
                'Pepper_healthy', 'Grape_black_rot', 'Grape_healthy', 
                'Grape_leaf_blight', 'Orange_greening', 
                'Strawberry_healthy', 'Strawberry_leaf_scorch', 
                'Peach_healthy', 'Peach_bacterial_spot', 
                'Peach_black_spot', 'Cucumber_healthy', 
                'Cucumber_downey_mildew', 'Cucumber_fusarium_wilt', 
                'Lettuce_healthy', 'Lettuce_downy_mildew', 
                'Soybean_healthy', 'Soybean_bacterial_spot', 
                'Soybean_frogeye_leaf_spot']

# Función para preprocesar la imagen
def preprocess_image(img_path):
    try:
        img = image.load_img(img_path, target_size=(150, 150))  # Cambia según tu modelo
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
    
    img_path = './temp_image.jpg'
    file.save(img_path)
    
    img_array = preprocess_image(img_path)
    
    if img_array is None:
        return jsonify({'error': 'No se pudo procesar la imagen'}), 500
    
    try:
        predictions = model.predict(img_array)
        predicted_class = class_labels[np.argmax(predictions[0])]
        
        os.remove(img_path)
        
        return jsonify({'prediction': predicted_class})
    
    except Exception as e:
        print(f"Error al hacer la predicción: {e}")
        return jsonify({'error': 'Ocurrió un error durante la predicción'}), 500

if __name__ == '__main__':
    if model is None:
        print("No se pudo cargar el modelo. Revisa el archivo del modelo y vuelve a intentarlo.")
        exit(1)
    else:
        app.run(debug=True)
