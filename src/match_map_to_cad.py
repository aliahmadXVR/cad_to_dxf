import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges


def extract_contours(edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def match_shapes(contours1, contours2):
    for contour1 in contours1:
        for contour2 in contours2:
            match = cv2.matchShapes(contour1, contour2, cv2.CONTOURS_MATCH_I1, 0.0)
            if match < 0.1:  # Adjust the threshold based on your requirement
                return True
    return False


dxf_image = preprocess_image('image_from_dxf.png')
map_image = preprocess_image('ros_map_10x10_feet_no_grid.png')

dxf_contours = extract_contours(dxf_image)
map_contours = extract_contours(map_image)

if match_shapes(dxf_contours, map_contours):
    print("The shapes match.")
else:
    print("The shapes do not match.")
