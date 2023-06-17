from transformers import BlipProcessor, BlipForConditionalGeneration, DetrImageProcessor, DetrForObjectDetection
from PIL import Image



def get_image_caption(image_path):
    image = Image.open(image_path).convert("RGB")

    model_name = "Salesforce/blip-image-captioning-larger"
    device = "cpu"

    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name).to(device)

    inputs = processor(image, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_new_tokens=20)

    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption


def detect_objects(image_path):
    pass


if __name__ == "__main__":
    image_path = "/Users/venugopalmiriyala/Desktop/1672363037692.jpeg"
    caption = get_image_caption(image_path)
    print(caption)
