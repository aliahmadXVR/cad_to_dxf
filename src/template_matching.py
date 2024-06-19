import cv2
import numpy as np
import matplotlib.pyplot as plt

def template_matching(template_path, image_path):
    # Read template and image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Perform template matching
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Draw a rectangle around the matched region
    top_left = max_loc
    h, w = template.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    matched_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(matched_image, top_left, bottom_right, (0, 255, 0), 2)

    # Display the matched image
    plt.figure(figsize=(10, 10))
    plt.title("Template Matching")
    plt.imshow(matched_image)
    plt.show()

    return max_val

# Paths to your images
dxf_image_path = 'image_from_dxf.png'
map_image_path = 'map1.png'

# Perform template matching
match_score = template_matching(dxf_image_path, map_image_path)
print(f"Template matching score: {match_score}")

