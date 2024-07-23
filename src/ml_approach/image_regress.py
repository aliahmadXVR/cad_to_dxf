import cv2
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

def load_and_convert(image_path):
    # Load image and convert to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def resize_image(image, target_shape):
    # Resize image to match target shape
    return cv2.resize(image, (target_shape[1], target_shape[0]))

def compare_images(imageA, imageB):
    # Compute SSIM between two images
    score, diff = ssim(imageA, imageB, full=True)
    diff = (diff * 255).astype("uint8")
    return score, diff

# Load images
image1 = load_and_convert('corner_area_cad.png')
image2 = load_and_convert('meeting_room.png')

# Resize image2 to match image1 dimensions
image2 = resize_image(image2, image1.shape)

# Compare images
similarity_score, diff = compare_images(image1, image2)
print(f"SSIM similarity score: {similarity_score:.4f}")

# Plot images and differences
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Original images
ax1.imshow(image1, cmap='gray')
ax1.set_title('Image 1')
ax1.axis('off')

ax2.imshow(image2, cmap='gray')
ax2.set_title('Image 2')
ax2.axis('off')

# Differences
ax3.imshow(diff, cmap='coolwarm')
ax3.set_title('Differences')
ax3.axis('off')

plt.show()

