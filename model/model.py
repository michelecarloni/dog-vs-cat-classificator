from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

class Model:
    def __init__(self):
        self.input_shape = (128, 128)
        self.categories = ['Cat', 'Dog']
        self.model = load_model('ai_models\cat_dog_squared_10.keras')
        
    def returnCategoryAndProbability(self, file_path):
        
        img = Image.open(file_path)
        new_image = self.make_square(img) 
        img_resized = new_image.resize(self.input_shape, Image.Resampling.LANCZOS)
        img_result = np.array(img_resized)
        img_result = np.expand_dims(img_result, axis=0)
        img_result = img_result / 255.0
        
        probability = self.model.predict(img_result, verbose=1)

        if probability < 0.5:
            category = self.categories[0]
        else:
            category = self.categories[1]

        print(f'result: {probability}')
        print(f'category: {category}')
        
        return category, probability   
    
    def make_square(self, image):
        width, height = image.size

        # If the image is already square, return the original image
        if width == height:
            return image

        # Determine the size of the new square image (it should be the max of width and height)
        new_size = max(width, height)

        # Create a new black image with a square size
        new_image = Image.new("RGB", (new_size, new_size), color=(0, 0, 0))  # Black background

        # Calculate the position to paste the original image (centered)
        paste_position = ((new_size - width) // 2, (new_size - height) // 2)

        # Paste the original image onto the new black square
        new_image.paste(image, paste_position)

        return new_image