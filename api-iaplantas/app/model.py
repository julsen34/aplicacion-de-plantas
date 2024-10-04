import tensorflow as tf
from tensorflow import keras
from keras.api import layers
from keras.src.legacy.preprocessing.image import ImageDataGenerator

# Función para crear el modelo
def create_model():
    model = keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(38, activation='softmax')  # PlantVillage tiene 38 categorías
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Función para entrenar el modelo
def train_model(model, dataset_path):
    train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    
    train_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=(150, 150),
        batch_size=32,
        class_mode='sparse',
        subset='training'
    )
    
    validation_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=(150, 150),
        batch_size=32,
        class_mode='sparse',
        subset='validation'
    )
    
    model.fit(train_generator, epochs=15, validation_data=validation_generator)
    return model

# Entrenamiento del modelo
if __name__ == "__main__":
    dataset_path = r'C:\Users\fuerz\Plantas'  # Cambiar a la ruta local
    model = create_model()
    model = train_model(model, dataset_path)
    model.save('model/modelo_plantas.keras')
