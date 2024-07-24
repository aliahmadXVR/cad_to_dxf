import cv2
import numpy as np
import matplotlib.pyplot as plt

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

# Paths to the images
template_path = 'meeting_room_preprocessed.png'     #ROS Image
image_path = 'meeting_room_cad_h.png'                  #CAD Image

# Perform template matching
match_score = template_matching(template_path, image_path)
print(f"Template matching score: {match_score}")
