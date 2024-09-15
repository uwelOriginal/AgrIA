import numpy as np
from PIL import Image
import openvino.runtime as ov

def preprocess_image(img_path):
    # Cargar la imagen
    image = Image.open(img_path)

    # Redimensionar la imagen a 150x150 (lo mismo que haces con torchvision.transforms)
    image = image.resize((150, 150))

    # Convertir la imagen a un array NumPy y escalar los valores de píxeles a [0, 1]
    image_array = np.array(image) / 255.0

    # Si la imagen es RGB (3 canales), asegurarse de que esté en la forma (3, 150, 150)
    if image_array.shape[-1] == 3:  # Si tiene 3 canales (RGB)
        image_array = np.transpose(image_array, (2, 0, 1))  # Cambiar la forma a (C, H, W)

    # Normalizar manualmente como lo harías con torchvision.transforms.Normalize
    mean = np.array([0.5, 0.5, 0.5])
    std = np.array([0.5, 0.5, 0.5])
    image_array = (image_array - mean[:, None, None]) / std[:, None, None]

    # Agregar una dimensión para el batch (1, C, H, W)
    image_array = np.expand_dims(image_array, axis=0)

    return image_array

def run(img_path):
    # Preprocesar la imagen manualmente
    input_image = preprocess_image(img_path)

    # Cargar el modelo IR (XML y BIN ya preconvertidos)
    core = ov.Core()
    ov_model = core.read_model("/workspaces/AgrIA/Preprocesamiento/simple_cnn.xml")

    # Compilar el modelo para el dispositivo deseado (CPU)
    compiled_model = core.compile_model(ov_model, 'CPU')

    # Crear una solicitud de inferencia
    infer_request = compiled_model.create_infer_request()

    # Realizar la inferencia
    output = infer_request.infer({0: input_image})

    # Procesar la salida
    output_data = output[compiled_model.output(0)]

    # Asumiendo que 'predicted_class' es el índice de la clase predicha
    predicted_class = np.argmax(output_data)  # Este es el índice que predice el modelo
    class_names = ['Black Soil', 'Cinder Soil', 'Laterite Soil', 'Peat Soil', 'Yellow Soil']

    # Mapear el índice de predicción al nombre de la clase
    predicted_label = class_names[predicted_class]

    # Devolver el resultado
    return predicted_label