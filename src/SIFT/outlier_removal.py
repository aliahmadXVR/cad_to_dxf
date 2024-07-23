import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image):
    # Threshold the image to get binary image (black and white)
    _, binary_image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY_INV)

    # Convert background to white and keep black pixels
    processed_image = cv2.bitwise_not(binary_image)
    return processed_image

def remove_outliers(processed_image):
    # Apply morphological operations to remove small blobs
    kernel = np.ones((3, 3), np.uint8)
    opened_image = cv2.morphologyEx(processed_image, cv2.MORPH_OPEN, kernel)

    # Find contours and filter by area
    contours, _ = cv2.findContours(opened_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_contour_area = 500  # Adjust this value to remove smaller areas
    mask = np.zeros_like(opened_image)

    for contour in contours:
        if cv2.contourArea(contour) >= min_contour_area:
            cv2.drawContours(mask, [contour], -1, (255), thickness=cv2.FILLED)

    # Apply mask to remove small blobs
    final_image = cv2.bitwise_and(processed_image, mask)
    return final_image

def process_and_display_images(input_path):
    # Load the original image
    original_image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Preprocess the image
    processed_image = preprocess_image(original_image)

    # Remove outliers
    final_image = remove_outliers(processed_image)

    # Display all images in a 1x3 matplotlib window
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(original_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Smoothed Image')
    plt.imshow(final_image, cmap='gray')
    plt.axis('off')

    plt.show()

# Path to your image
input_image_path = 'meeting_room.png'

# Process and display images
process_and_display_images(input_image_path)
