# preprocessing.py
import re
import os
from PIL import Image
import torch
from torchvision import transforms
from transformers import CLIPProcessor, CLIPModel

# Text preprocessing
def clean_text(text):
    """Clean and preprocess text."""
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\W', ' ', text)  # Remove non-alphanumeric characters
    return text.strip()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def preprocess_image(image_path):
    """Preprocess the image and return the tensor."""
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    return image

def extract_image_features(image_tensor):
    """Extract features using the CLIP model."""
    with torch.no_grad():
        features = model.get_image_features(image_tensor)
    return features

# Example usage
if __name__ == "__main__":
    text_example = "Example News Headline: This is an example!"
    clean_text_example = clean_text(text_example)
    print(f"Cleaned Text: {clean_text_example}")

    image_path_example = "path/to/your/image.jpg"
    if os.path.exists(image_path_example):
        image_tensor = preprocess_image(image_path_example)
        image_features = extract_image_features(image_tensor)
        print(f"Extracted Image Features: {image_features}")
    else:
        print("Image path does not exist.")
