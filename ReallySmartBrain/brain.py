# REFER https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Classification/README.md
from imageai.Prediction import ImagePrediction # Import the Model
import os

execution_path = os.getcwd() # Get the current working directory of this script

prediction = ImagePrediction() # Instantiate the model

# Download the MobileNetV2 model and put it in the current directory 
# from https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/mobilenet_v2.h5
prediction.setModelTypeAsMobileNetV2() # Set the Model to use out of the four available
prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2.h5")) # Add name of the model file to current path
prediction.loadModel() # Load the Model

# Can also try out ResNet50: https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_imagenet_tf.2.0.h5
# prediction.setModelTypeAsResNet50() # Set the Model to use out of the four available
# prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5")) # Add name of the model file to current path
# prediction.loadModel()

# Get 5 predictions from the model for our image file
predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "giraffe.jpg"), result_count=5)
# Print the prediction and its probability (confidence) for each of the five runs we had for our image file
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)

