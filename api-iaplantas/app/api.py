from flask import Flask, request, jsonify
from tensorflow import keras
import tensorflow as tf

from keras.api.models import load_model
from keras.api.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Obtener la ruta absoluta al directorio del script actual
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta absoluta al archivo del modelo
ruta_modelo = r"C:\Users\fuerz\aplicacion-de-plantas\api-iaplantas\model\modelo_plantas.h5"  # Asegúrate de que esta ruta sea correcta

# Verificar si el archivo existe
if not os.path.exists(ruta_modelo):
    raise FileNotFoundError(f"El archivo del modelo no se encuentra en: {ruta_modelo}")

# Intentar cargar el modelo
try:
    print(f"Cargando modelo desde: {ruta_modelo}")
    model = load_model(ruta_modelo)
    print("Modelo cargado exitosamente")
except Exception as e:
    print(f"Error al cargar el modelo: {str(e)}")
    raise

@app.route('/api/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})
    
    img = request.files['file']
    img_path = 'temp/' + img.filename
    img.save(img_path)

    # Preprocesar la imagen
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Realizar la predicción
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions[0])

    return jsonify({'class_index': class_idx})

if __name__ == "__main__":
    app.run(debug=True)
