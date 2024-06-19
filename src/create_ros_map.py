from PIL import Image, ImageDraw

# Define dimensions
feet_to_inches = 12
width_feet = 10
height_feet = 20
width_inches = width_feet * feet_to_inches
height_inches = height_feet * feet_to_inches

# Create a new image with white background for 10x20 feet
image = Image.new('RGB', (width_inches, height_inches), 'white')

# Save the image
image.save('ros_map_10x20_feet_no_grid.png')
image.show()
