import cv2
import matplotlib.pyplot as plt

# Load the map image
map_image = cv2.imread('/home/ali/test_ws/src/my_package/sample_maps/corner_area.png', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur
blurred_map = cv2.GaussianBlur(map_image, (5, 5), 0)

# Apply Median Filter
median_map = cv2.medianBlur(map_image, 5)

# Apply Dilation and Erosion
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated_map = cv2.dilate(map_image, kernel, iterations=1)
eroded_map = cv2.erode(dilated_map, kernel, iterations=1)

# Create a 1x3 plot to display the images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot the original map
axes[0].imshow(map_image, cmap='gray')
axes[0].set_title('Original Map')
axes[0].axis('off')

# Plot the Gaussian Blurred map
axes[1].imshow(blurred_map, cmap='gray')
axes[1].set_title('Gaussian Blurred Map')
axes[1].axis('off')

# Plot the Median Filtered map
axes[2].imshow(median_map, cmap='gray')
axes[2].set_title('Median Filtered Map')
axes[2].axis('off')

# Display the plot
plt.show()