import torch
from torchvision import transforms
from PIL import Image
import sys
sys.path.append('pytorch-CycleGAN-and-pix2pix')  # Add the repository to the path

# Import the generator model architecture (you may need to adjust based on repository structure)
from models.networks import ResnetGenerator

# Function to load the pre-trained model based on the selected style
def load_model(style):
    if style == 'vangogh':
        model_path = 'pytorch-CycleGAN-and-pix2pix/checkpoints/style_vangogh_pretrained/latest_net_G.pth'
    elif style == 'monet':
        model_path = 'pytorch-CycleGAN-and-pix2pix/checkpoints/style_monet_pretrained/latest_net_G.pth'
    elif style == 'ukiyoe':
        model_path = 'pytorch-CycleGAN-and-pix2pix/checkpoints/style_ukiyoe_pretrained/latest_net_G.pth'
    elif style == 'zebra':
        model_path = 'pytorch-CycleGAN-and-pix2pix/checkpoints/horse2zebra_pretrained/latest_net_G.pth'
    else:
        raise ValueError("Unknown style!")

    # Instantiate the model architecture (CycleGAN uses ResnetGenerator)
    model = ResnetGenerator(input_nc=3, output_nc=3, ngf=64, norm_layer=torch.nn.InstanceNorm2d, use_dropout=False, n_blocks=9)

    # Load the pre-trained model weights for the selected style
    model.load_state_dict(torch.load(model_path), strict=False)

    # Set the model to evaluation mode
    model.eval()

    return model

def preprocess_image(image):
    preprocess = transforms.Compose([
        transforms.Resize((256, 256)),            # Resize the image to 256x256 pixels
        transforms.ToTensor(),                    # Convert the image to a PyTorch tensor
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normalize to [-1, 1]
    ])
    return preprocess(image).unsqueeze(0)         # Add batch dimension and return
# Function to apply the style transfer


def apply_style_transfer(image_tensor, model):
    # Apply the CycleGAN model to the image tensor
    with torch.no_grad():
        stylized_image_tensor = model(image_tensor)
    return stylized_image_tensor

def denormalize(tensor):
    tensor = tensor * 0.5 + 0.5  # Reverse the normalization: scale values back to [0, 1]
    return tensor.clamp(0, 1)  # Ensure all values are between 0 and 1
