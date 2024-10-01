
# AI Cartoon Avatar Generator Based on Your Selfies 🎨

## Overview
The **AI Avatar Generator** is a personal project that transforms user selfies into stylized avatars using deep learning techniques. By utilizing state-of-the-art neural networks, this model processes images to generate various artistic styles, such as 2D cartoons, anime, or other creative avatars. This application provides users with an engaging experience by allowing them to generate customized and shareable avatars, optimized for social platforms like TikTok, Instagram, and more.

## Features
- **Style Transfer**: Apply artistic styles (e.g., 2D cartoons, 3D avatars, Van Gogh, Monet, Ukiyo-e) using pre-trained models **CycleGAN** / **StyleGAN**.
- **Dynamic Image Processing**: The back-end efficiently processes and stylizes images in real time using PyTorch and pre-trained CycleGAN models.
- **Real-Time Cropping**: Crop and adjust images dynamically with **Cropper.js** before applying artistic styles.
- **Download & Share**: After stylization, users can download the transformed image and share it directly on social media.
- **High-Quality Output**: Image resolution is maintained, and additional padding ensures no content is lost during resizing or cropping.

## 🛠️ Tech Stack

### Frontend:
- **HTML5, CSS3, Bootstrap**: For responsive and accessible design.
- **JavaScript (AJAX, Cropper.js)**: Provides a smooth and interactive user experience for cropping and uploading images.

### Backend:
- **Flask (Python)**: Lightweight and scalable backend framework.
- **PyTorch**: For deep learning inference and style transfer, utilizing pre-trained models like **CycleGAN**.
- **OpenCV**: Used for image preprocessing and handling.

### Other Tools:
- **Pillow**: For image manipulation and processing.
- **RESTful API**: Architected to handle requests for image transformations.

## How It Works
1. **Upload a Selfie**: Users upload their selfies through the web interface.
2. **Select a Style**: Choose from various pre-trained artistic models (e.g., Van Gogh, anime, etc.).
3. **Crop & Adjust**: Use the integrated cropping tool to focus on specific areas of the photo.
4. **Generate Avatar**: The backend applies the selected style in real-time, using deep learning models.
5. **Download & Share**: Once processed, users can download their newly styled avatars or share them directly on social media platforms.

## Potential Applications
- **Social Media**: Avatars and stylized content are widely popular on platforms like TikTok, Instagram, and Snapchat.
- **Gaming & Virtual Worlds**: Custom avatars are essential in virtual environments and gaming.
- **Content Creation**: A valuable tool for influencers, artists, or creators looking to stylize their imagery.

## 📧 Contact

Interested in collaborating or learning more about this project? Feel free to reach out!

- **Email**: [ronney@cs.washington.edu](mailto:ronney@cs.washington.edu)
- **LinkedIn**: [Ronney Do](https://www.linkedin.com/in/ronneydo/)
- **GitHub**: [github.com/ronney221](https://github.com/ronney221)

---

## 👏 Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/ronney221/Cartoonify/issues) or submit a pull request.

---

## Project Screenshots

![upload](https://github.com/user-attachments/assets/e5641c04-ee8d-44bd-aa3d-68709414fb03)
![style](https://github.com/user-attachments/assets/a7682a31-5cdb-4b14-ab31-21099bcbe02d)
![crop](https://github.com/user-attachments/assets/573a9c3e-6516-4abc-9c6a-45b04371dc17)
![upload](https://github.com/user-attachments/assets/69784e04-fcc6-46fc-a64c-be7da659f922)
![results](https://github.com/user-attachments/assets/bfb5c4bb-36a4-46d3-8245-f4cdf950c74c)


