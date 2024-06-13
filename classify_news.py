# classify_news.py
import sys
import torch
from transformers import RobertaTokenizer, RobertaModel
from preprocessing import clean_text, preprocess_image, extract_image_features

# Load text model
text_model = RobertaModel.from_pretrained("roberta-base")
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")

def classify_text(text):
    """Classify text using the text model."""
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = text_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def multimodal_classification(text, image_path):
    """Classify news using both text and image features."""
    clean_text_data = clean_text(text)
    text_features = classify_text(clean_text_data)

    image_tensor = preprocess_image(image_path)
    image_features = extract_image_features(image_tensor)

    # Concatenate features
    combined_features = torch.cat((text_features, image_features), dim=1)

    # Example: Dummy classifier, replace with your actual classification logic
    classification_result = combined_features.mean().item() > 0.5  # Dummy condition
    return classification_result

# Main function to run the classification
if __name__ == "__main__":
    headline = sys.argv[1]
    image_path = sys.argv[2]
    
    result = multimodal_classification(headline, image_path)
    print(f"Classification Result: {'Positive' if result else 'Negative'}")
