from PIL import Image

# Path to the input PGM file
# pgm_file_path = '/home/ali/test_ws/src/my_package/sample_maps/corner_area.pgm'
pgm_file_path = '/home/ali/test_ws/src/my_package/sample_maps/meeting_room.pgm'

# Open the PGM file
with Image.open(pgm_file_path) as img:
    # Ensure the image is in the correct mode (P mode for palette-based images)
    img = img.convert("L")  # "L" mode for grayscale images
    
    # Path to the output PNG file
    # png_file_path = '/home/ali/test_ws/src/my_package/sample_maps/corner_area.png'
    png_file_path = '/home/ali/test_ws/src/my_package/sample_maps/meeting_room.png'
   
    # Save the image as a PNG file
    img.save(png_file_path)

print(f"Converted {pgm_file_path} to {png_file_path}")
