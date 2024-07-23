import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load images
img1 = cv2.imread('image1.png', 0)
img2 = cv2.imread('image2.png', 0)

# Initialize ORB detector
orb = cv2.ORB_create()

# Find keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Use BFMatcher to find matches
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort matches based on distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw matches
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display matches
plt.imshow(img_matches)
plt.show()

# Extract location of good matches
points1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
points2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# Find homography
H, mask = cv2.findHomography(points1, points2, cv2.RANSAC, 5.0)

# Use homography to warp image
height, width = img2.shape
img1_reg = cv2.warpPerspective(img1, H, (width, height))

# Display result
plt.imshow(img1_reg, cmap='gray')
plt.title('Registered Image')
plt.show()
