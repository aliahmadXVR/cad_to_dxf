import cv2
import numpy as np
import matplotlib.pyplot as plt

def resize_images(image1, image2):
    resized_image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))
    resized_image2 = cv2.resize(image2, (image2.shape[1], image2.shape[0]))
    return resized_image1, resized_image2

def display_image_dimensions(image, title):
    height, width = image.shape
    print(f"{title} Dimensions: {width}x{height}")

def template_matching(smoothed_image, image2):
    result = cv2.matchTemplate(image2, smoothed_image, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)
    
    h, w = smoothed_image.shape
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image2, top_left, bottom_right, 255, 2)
    
    return image2

def process_and_display_images(input_image_path, match_image_path):
    original_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    match_image = cv2.imread(match_image_path, cv2.IMREAD_GRAYSCALE)
    
    # Print initial dimensions
    display_image_dimensions(original_image, "Original ROS Map Image")
    display_image_dimensions(match_image, "Original CAD Image")
    
    # Display original images
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.title('Original ROS Map Image')
    plt.imshow(original_image, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.title('Original CAD Image')
    plt.imshow(match_image, cmap='gray')
    plt.axis('off')
    
    # Resize images
    resized_image, resized_match_image = resize_images(original_image, match_image)
    
    # Print resized dimensions
    display_image_dimensions(resized_image, "Resized ROS Map Image")
    display_image_dimensions(resized_match_image, "Resized CAD Image")
    
    # Display resized images
    plt.subplot(2, 2, 3)
    plt.title('Resized ROS Map Image')
    plt.imshow(resized_image, cmap='gray')
    plt.axis('off')
    
    plt.subplot(2, 2, 4)
    plt.title('Resized CAD Image')
    plt.imshow(resized_match_image, cmap='gray')
    plt.axis('off')
    
    plt.show()
    
    # Preprocess and smooth the resized image
    smoothed_image = cv2.blur(resized_image, (5, 5))
    
    # Run template matching
    matched_image = template_matching(smoothed_image, resized_match_image)
    
    # Display result of template matching
    plt.figure(figsize=(6, 6))
    plt.title('Template Matching Result')
    plt.imshow(matched_image, cmap='gray')
    plt.axis('off')
    plt.show()

# Paths to your images
input_image_path = 'corner_area.png'
cad_map_path = 'corner_area_cad.png'

# Process and display images and run template matching
process_and_display_images(input_image_path, cad_map_path)




















# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# def resize_images(image1, image2):
#     resized_image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))
#     return resized_image1, image2

# def preprocess_image(image):
#     _, binary_image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY_INV)
#     processed_image = cv2.bitwise_not(binary_image)
#     return processed_image

# def apply_moving_average(image):
#     smoothed_image = cv2.blur(image, (5, 5))
#     return smoothed_image

# def display_image_dimensions(image, title):
#     height, width = image.shape
#     print(f"{title} Dimensions: {width}x{height}")

# def sift_matching(smoothed_image, image2):
#     sift = cv2.SIFT_create()
#     keypoints1, descriptors1 = sift.detectAndCompute(smoothed_image, None)
#     keypoints2, descriptors2 = sift.detectAndCompute(image2, None)
    
#     bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
#     matches = bf.match(descriptors1, descriptors2)
#     matches = sorted(matches, key=lambda x: x.distance)
    
#     img_matches = cv2.drawMatches(smoothed_image, keypoints1, image2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
#     plt.figure(figsize=(12, 6))
#     plt.title('SIFT Matches')
#     plt.imshow(img_matches)
#     plt.axis('off')
#     plt.show()

# def template_matching(smoothed_image, image2):
#     result = cv2.matchTemplate(image2, smoothed_image, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
#     h, w = smoothed_image.shape
#     top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#     cv2.rectangle(image2, top_left, bottom_right, 255, 2)
    
#     plt.figure(figsize=(12, 6))
#     plt.title('Template Matching Result')
#     plt.imshow(image2, cmap='gray')
#     plt.axis('off')
#     plt.show()

# def process_and_display_images(input_image_path, match_image_path):
#     original_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
#     match_image = cv2.imread(match_image_path, cv2.IMREAD_GRAYSCALE)
    
#     # Print initial dimensions
#     display_image_dimensions(original_image, "Original Image")
#     display_image_dimensions(match_image, "CAD Image")
    
#     # Resize images
#     resized_image, resized_match_image = resize_images(original_image, match_image)
    
#     # Print resized dimensions
#     display_image_dimensions(resized_image, "Resized Image")
#     display_image_dimensions(resized_match_image, "Resized CAD Image")
    
#     # Preprocess and smooth the resized image
#     processed_image = preprocess_image(resized_image)
#     smoothed_image = apply_moving_average(processed_image)
    
#     plt.figure(figsize=(12, 6))
#     plt.subplot(1, 2, 1)
#     plt.title('Resized Image')
#     plt.imshow(resized_image, cmap='gray')
#     plt.axis('off')
    
#     plt.subplot(1, 2, 2)
#     plt.title('Smoothed Image')
#     plt.imshow(smoothed_image, cmap='gray')
#     plt.axis('off')
    
#     plt.show()

#     # Run template matching
#     template_matching(smoothed_image, resized_match_image)

# # Paths to your images
# # input_image_path = 'image1.png'
# # cad_map_path = 'image2.png'

# input_image_path = 'corner_area.png'
# cad_map_path = 'corner_area_cad.png'

# # Process and display images and run template matching
# process_and_display_images(input_image_path, cad_map_path)
