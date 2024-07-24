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

def detect_and_draw_lines(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Detect edges using Canny with lower thresholds
    edges = cv2.Canny(blurred, 30, 100, apertureSize=3)

    # Use Hough Line Transform with adjusted parameters
    lines = cv2.HoughLinesP(edges, 5, np.pi / 180, threshold=50, minLineLength=30, maxLineGap=20)

  # Create a white image to draw lines on
    line_image = np.ones_like(image) * 255

    # Draw lines on the blank image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return line_image

def template_matching(template_path, image_path):
    # Read template and image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Print dimensions
    print(f"Template dimensions (height, width): {template.shape}")
    print(f"Image dimensions (height, width): {image.shape}")

    # Perform template matching
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # Get the best match position
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Draw a rectangle around the matched region
    top_left = max_loc
    h, w = template.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    matched_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(matched_image, top_left, bottom_right, (0, 255, 0), 2)

    # Display the matched image
    plt.figure(figsize=(10, 10))
    plt.title(f"Template Matching with {template_path}")
    plt.imshow(matched_image)
    plt.axis('off')
    plt.show()

    return max_val

def process_and_display_images(template_path,cad_path):
    # Load the original image
    original_image = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Preprocess the image
    processed_image = preprocess_image(original_image)

    # Remove outliers
    final_image = remove_outliers(processed_image)

    # Detect and draw lines on the final image
    color_final_image = cv2.cvtColor(final_image, cv2.COLOR_GRAY2BGR)
    line_image = detect_and_draw_lines(color_final_image)

    # Display all images in a 1x3 matplotlib window
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(original_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Pre-Processing Image')
    plt.imshow(final_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('Line Detection Image')
    plt.imshow(cv2.cvtColor(line_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.show()

     # Save the line image
    cv2.imwrite('meeting_room_preprocessed.png', line_image)

# Path to your image
template_path = 'meeting_room.png'  #ROS Image
CAD_path = 'meeting_room_cad.png'  #CAD Image

# Process and display images
process_and_display_images(template_path,CAD_path)


