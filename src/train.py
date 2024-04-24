import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from models.custom_model import custom_model
from src.data_loader import load_data

def train_model(input_dir='data/raw_images', output_dir='data/processed_images'):
    # Load data
    X_train, y_train = load_data(input_dir, output_dir)
    
    # Normalize images
    X_train = X_train.astype('float32') / 255.0
    y_train = y_train.astype('float32') / 255.0
    
    # Define the input shape based on the first image's shape
    input_shape = X_train[0].shape
    
    # Create model
    model = custom_model(input_shape)
    
    # Compile model
    optimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='mse')
    
    # Train model
    model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)
    
    # Save model
    model.save('custom_model.h5')

if __name__ == '__main__':
    train_model()