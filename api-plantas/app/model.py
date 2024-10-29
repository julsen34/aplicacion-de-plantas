import tensorflow as tf
from tensorflow.python import keras
from keras.api import layers, models
from keras.src.legacy.preprocessing.image import ImageDataGenerator

# Función para crear el modelo
def create_model():
    model = models.Sequential([
        layers.Input(shape=(150, 150, 3)), 
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(38, activation='softmax')  
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Función para entrenar el modelo
def train_model(model, dataset_path):
    # Rescalado y división de validación (80% entrenamiento, 20% validación)
    train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    
    # Generador para el set de entrenamiento
    train_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=(150, 150),  # Ajustar el tamaño de las imágenes al tamaño esperado por el modelo
        batch_size=32,
        class_mode='sparse',  # 'sparse' para etiquetas enteras en lugar de one-hot
        subset='training'
    )
    
    # Generador para el set de validación
    validation_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=(150, 150),  # Ajustar el tamaño de las imágenes al tamaño esperado por el modelo
        batch_size=32,
        class_mode='sparse',
        subset='validation'
    )
    
    # Entrenamiento del modelo
    model.fit(train_generator, epochs=15, validation_data=validation_generator)
    return model

# Entrenamiento del modelo
if __name__ == "__main__": 
    dataset_path = r'C:\Users\fuerz\aplicacion-de-plantas\.plantas\PlantVillage-Dataset'  # Ruta a tu dataset
    model = create_model()  # Crear el modelo
    model = train_model(model, dataset_path)  # Entrenar el modelo
    model.save('model/modelo_plantas.keras')  # Guardar el modelo entrenado
