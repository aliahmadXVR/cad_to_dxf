import cv2
import numpy as np
import matplotlib.pyplot as plt

def visualize_matching_result(result):
    plt.figure(figsize=(6, 6))
    plt.title("Matching Result Heatmap")
    plt.imshow(result, cmap='hot')
    plt.colorbar()
    plt.show()



def template_matching(template_path, image_path):
    # Read template and image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Perform template matching
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # Call this function after computing the result
    visualize_matching_result(result)

    # Get the best match position
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Draw a rectangle around the matched region
    top_left = max_loc
    h, w = template.shape
    print(h)
    print(w)
    bottom_right = (top_left[0] + w, top_left[1] + h)
    matched_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(matched_image, top_left, bottom_right, (0, 255, 0), 2)

    # Display the matched image
    plt.figure(figsize=(6, 6))
    plt.title(f"Template Matching Result")
    plt.imshow(matched_image)
    plt.axis('on')
    plt.show()

    return max_val

# Paths to images
main_image_path = 'main_image.png'
template_image_path = 'template_image.png'

# Perform template matching
match_score = template_matching(template_image_path, main_image_path)
print(f"Template matching score: {match_score}")
