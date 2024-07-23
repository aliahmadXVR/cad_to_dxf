import cv2
import numpy as np

# Create a blank main image
main_image = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.rectangle(main_image, (150, 150), (250, 250), (255, 255, 255), -1)

# Create a template image (a smaller section of the main image)
template_image = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.rectangle(template_image, (0, 0), (100, 100), (255, 255, 255), -1)

# Save the images
cv2.imwrite('main_image.png', main_image)
cv2.imwrite('template_image.png', template_image)

# Display the images
cv2.imshow('Main Image', main_image)
cv2.imshow('Template Image', template_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
