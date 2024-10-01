import cv2
import torch
from torchvision import transforms
from PIL import Image
import streamlit as st
from PIL import Image




# handles the resizing of the uploaded image to the correct size for the model.
def preprocess_image(image):
    # Convert PIL image to OpenCV format (numpy array)
    open_cv_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Resize image to 256x256 (or whatever size the model requires)
    resized_image = cv2.resize(open_cv_image, (256, 256))

    return resized_image



# Load pre-trained CycleGAN model
model = torch.hub.load('junyanz/pytorch-CycleGAN-and-pix2pix', 'cyclegan_horse2zebra', pretrained=True)
model.eval()

# applies the pre-trained style transfer model (CycleGAN to the preprocessed image)
def apply_style_transfer(image):
    # Define image transformations needed for the model
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # Apply the transformation and add batch dimension
    image_tensor = transform(image).unsqueeze(0)

    # Apply the style transfer model
    with torch.no_grad():
        stylized_image = model(image_tensor)

    # Convert the output tensor back to an image format
    stylized_image = stylized_image.squeeze().detach().cpu()
    stylized_image = (stylized_image * 0.5) + 0.5  # De-normalize the image
    return transforms.ToPILImage()(stylized_image)





# web interface, allow the user to upload an image, and display the stylized avatar.
st.title("AI Avatar Generator")

# Upload image file
uploaded_file = st.file_uploader("Upload a selfie (jpg/png)", type=["jpg", "png"])

if uploaded_file is not None:
    # Open the image using PIL
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image (resize)
    processed_image = preprocess_image(image)

    # Apply style transfer (convert to avatar)
    if st.button("Generate Avatar"):
        avatar_image = apply_style_transfer(Image.fromarray(processed_image))
        st.image(avatar_image, caption="Stylized Avatar", use_column_width=True)
