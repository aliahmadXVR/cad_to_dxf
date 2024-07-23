import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to preprocess the image
def preprocess_image(image_path, lower_thresh, upper_thresh):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edges = cv2.Canny(blurred, lower_thresh, upper_thresh)
    return edges

# Paths to the images
map_image_path = '/home/ali/test_ws/src/my_package/sample_maps/corner_area.png'
cad_image_path = '/home/ali/test_ws/src/my_package/CADs/corner_area_cad.png'

# Preprocess the images
preprocessed_map = preprocess_image(map_image_path, 50, 150)
preprocessed_cad = preprocess_image(cad_image_path, 50, 150)

# Display the preprocessed images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Preprocessed Map Image')
plt.imshow(preprocessed_map, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Preprocessed CAD Image')
plt.imshow(preprocessed_cad, cmap='gray')
plt.show()

# Use ORB for feature detection and description
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(preprocessed_map, None)
kp2, des2 = orb.detectAndCompute(preprocessed_cad, None)

# Use BFMatcher with default parameters
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw the matches
img_matches = cv2.drawMatches(preprocessed_map, kp1, preprocessed_cad, kp2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the matches
plt.figure(figsize=(20, 10))
plt.title('Feature Matches between Map and CAD Image (ORB)')
plt.imshow(img_matches)
plt.show()

# Homography
if len(matches) > 4:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1, 1, 2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1, 1, 2)

    # Find the homography matrix
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    
    # Use the homography matrix to transform the map image to the CAD image's perspective
    h, w = preprocessed_map.shape
    map_transformed = cv2.warpPerspective(preprocessed_map, M, (w, h))

    # Display the transformed map image
    plt.figure(figsize=(10, 10))
    plt.title('Transformed Map Image (ORB)')
    plt.imshow(map_transformed, cmap='gray')
    plt.show()
else:
    print("Not enough matches are found - %d/%d" % (len(matches), 4))
