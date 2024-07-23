import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/home/ali/test_ws/src/my_package/sample_maps/corner_area.png'
# image_path = '/home/ali/test_ws/src/my_package/CADs/corner_area_cad.png'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny Edge Detection
edges = cv2.Canny(blurred, 200, 300)

# Display the result
plt.figure(figsize=(10, 10))
plt.title('Edge Detection Result')
plt.imshow(edges, cmap='gray')
plt.show()

# Save the result
cv2.imwrite('/home/ali/test_ws/src/my_package/sample_maps/corner_area_processed_map.png', edges)