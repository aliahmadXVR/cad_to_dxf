import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, 100, 200)
    return edges

def extract_features(image):
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return keypoints, descriptors

def match_features(desc1, desc2):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc1, desc2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

def find_homography(kp1, kp2, matches):
    src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matches_mask = mask.ravel().tolist()
    return M, matches_mask

def compute_similarity_score(matches_mask):
    return np.sum(matches_mask)

def find_best_match(ros_map_path, cad_image_paths):
    ros_map_edges = preprocess_image(ros_map_path)
    kp_ros, desc_ros = extract_features(ros_map_edges)

    best_match_score = 0
    best_match_image = None

    for cad_path in cad_image_paths:
        cad_edges = preprocess_image(cad_path)
        kp_cad, desc_cad = extract_features(cad_edges)

        matches = match_features(desc_ros, desc_cad)
        _, matches_mask = find_homography(kp_ros, kp_cad, matches)

        score = compute_similarity_score(matches_mask)
        print(f"Score for {cad_path}: {score}")

        if score > best_match_score:
            best_match_score = score
            best_match_image = cad_path

    return best_match_image

ros_map_path = 'corner_area.png'
cad_image_paths = ['meeting_room_cad.png']

best_match = find_best_match(ros_map_path, cad_image_paths)
print(f"The best matching CAD image is: {best_match}")
