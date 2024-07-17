import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/home/ali/test_ws/src/my_package/sample_maps/corner_area.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the range of pixel values to be kept
lower_bound = 230
upper_bound = 255

# Create a binary mask where pixels in the specified range are set to 1 and everything else is set to 0
mask = cv2.inRange(image, lower_bound, upper_bound)

# Create a new image with the same shape as the original image, filled with white pixels
result = np.full_like(image, 255)

# Copy the pixels in the specified range from the original image to the result image
result[mask == 255] = image[mask == 255]

# Display the result
plt.figure(figsize=(10, 10))
plt.title('Image with Pixels in Range 200-255 Kept')
plt.imshow(result, cmap='gray')
plt.show()

# Save the result
cv2.imwrite('/home/ali/test_ws/src/my_package/sample_maps/corner_area_processed.png', result)











