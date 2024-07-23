import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    # Display the original and edge-detected images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title("Edge Detection")
    plt.imshow(edges, cmap='gray')
    plt.show()
    
    return edges

def extract_contours(edges, title):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create an empty image to draw contours
    contour_image = np.zeros_like(edges)
    cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 2)
    
    # Display the contours
    plt.figure(figsize=(5, 5))
    plt.title(f"Contours - {title}")
    plt.imshow(contour_image, cmap='gray')
    plt.show()
    
    return contours

def match_shapes(contours1, contours2):
    match_found = False
    for contour1 in contours1:
        for contour2 in contours2:
            match = cv2.matchShapes(contour1, contour2, cv2.CONTOURS_MATCH_I1, 0.0)
            print(f"Match score between contours: {match}")
            if match < 0.001:  # Adjust the threshold based on your requirement
                match_found = True
                break
        if match_found:
            break
    return match_found

# Paths to your images
dxf_image_path = 'image_from_dxf.png'
map_image_path = 'map1.png'
# map_image_path = 'ros_map_10x20_feet_no_grid.png'

# Preprocess and display DXF image
print("Preprocessing DXF image...")
dxf_image = preprocess_image(dxf_image_path)

# Display DXF image and wait for user to close it
plt.show()

# Preprocess and display map image
print("Preprocessing map image...")
map_image = preprocess_image(map_image_path)

# Display map image and wait for user to close it
plt.show()

# Extract contours and display
print("Extracting contours from DXF image...")
dxf_contours = extract_contours(dxf_image, "DXF Image")

# Display contours from DXF image and wait for user to close it
plt.show()

print("Extracting contours from map image...")
map_contours = extract_contours(map_image, "Map Image")

# Display contours from map image and wait for user to close it
plt.show()

# Match shapes
print("Matching shapes...")
if match_shapes(dxf_contours, map_contours):
    print("The shapes match.")
else:
    print("The shapes do not match.")
