from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


def get_image_caption(image_path):
    image = Image.open(image_path).convert("RGB")

    model_name = "Salesforce/blip-image-captioning-larger"
    device = "cpu"

    processor = BlipProcessor.from_pretrained(model_name).to(device)
    model = BlipForConditionalGeneration.from_pretrained(model_name).to(device)
