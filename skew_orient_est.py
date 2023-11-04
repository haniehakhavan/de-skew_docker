import cv2
import numpy as np
import onnxruntime

# Load the ONNX model
skew_model = onnxruntime.InferenceSession("./models/regression0.onnx")
orientation_model = onnxruntime.InferenceSession("./models/classification0.onnx")

def preprocess_image(image):
    image = image.astype(np.float32) / 127.5 - 1  # Apply the same normalization as during training
    image = image.reshape(1, 224, 224, 1)  # Add batch dimension
    return image


def skew_estimate(image):
    # Preprocess the image
    image = preprocess_image(image)

    # Perform inference using the ONNX model
    input_name = skew_model.get_inputs()[0].name
    output_name = skew_model.get_outputs()[0].name
    result = skew_model.run([output_name], {input_name: image})

    # Extract the regression result
    regression_result = result[0]
    skew = regression_result[0][0] * 45

    return skew

def orientation_estimate(image):
    class_labels = ["down", "left", "right", "up"]
    # Preprocess the image
    image = preprocess_image(image)
    # Perform inference using the ONNX model
    input_name = orientation_model.get_inputs()[0].name
    output_name = orientation_model.get_outputs()[0].name
    result = orientation_model.run([output_name], {input_name: image})

    # Extract the classification result
    classification_result = result[0][0]
    predicted_orientation = np.argmax(classification_result)
    predicted_class = class_labels[predicted_orientation]
    return predicted_class
