import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(2, activation='softmax')  # Cambia el número de clases según tu dataset
    ])
    
    model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy'])
    
    return model

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
    
    model.fit(train_generator, epochs=10, validation_data=validation_generator)

# Ejemplo de uso
if __name__ == "__main__":
    model = create_model()
    train_model(model, r'C:\Users\fuerz\Plantas') 
    model.save('model/modelo_plantas.h5')  # Guarda el modelo entrenado
