from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import preprocess_input

def fine_tune_model(train_dir, val_dir, test_dir):
    # Load pre-trained ResNet50 model
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    # Freeze pre-trained layers
    for layer in base_model.layers[:-4]:
        layer.trainable = False

    # Define custom classification layers
    flat = Flatten()(base_model.output)
    output = Dense(1, activation='sigmoid')(flat)

    # Create the fine-tuned model
    fine_tuned_model = Model(inputs=base_model.inputs, outputs=output)

    # Compile the model
    fine_tuned_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Define data generators
    train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
    val_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
    test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

    # Fine-tune the model
    train_generator = train_datagen.flow_from_directory(
        train_dir, target_size=(224, 224), batch_size=32, class_mode='binary', classes=['Normal_Eyes', 'drugged_eyes']
    )
    val_generator = val_datagen.flow_from_directory(
        val_dir, target_size=(224, 224), batch_size=32, class_mode='binary', classes=['Normal_Eyes', 'drugged_eyes']
    )
    test_generator = test_datagen.flow_from_directory(
        test_dir, target_size=(224, 224), batch_size=32, class_mode='binary', classes=['Normal_Eyes', 'drugged_eyes']
    )

    # Train the model
    fine_tuned_model.fit(train_generator, validation_data=val_generator, epochs=15)

    # Evaluate the model on the test set
    test_loss, test_accuracy = fine_tuned_model.evaluate(test_generator)
    print(f'Test accuracy: {test_accuracy:.2f}')

    # Save the model
    fine_tuned_model.save('trained.h5')

