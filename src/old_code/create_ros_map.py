from PIL import Image, ImageDraw

# Define dimensions
feet_to_inches = 12
width_feet = 10
height_feet = 20
width_inches = width_feet * feet_to_inches
height_inches = height_feet * feet_to_inches

# Create a new image with white background for 10x20 feet
image = Image.new('RGB', (width_inches, height_inches), 'white')
draw = ImageDraw.Draw(image)

# Define parameters for grid
grid_color = 'black'
grid_thickness = 1

# Define margins (white space around the grid)
margin = 20  # in pixels

# Draw horizontal grid lines
for y in range(0, height_inches, feet_to_inches):
    draw.line((0, y, width_inches, y), fill=grid_color, width=grid_thickness)

# Draw vertical grid lines
for x in range(0, width_inches, feet_to_inches):
    draw.line((x, 0, x, height_inches), fill=grid_color, width=grid_thickness)

# Save the image
image.save('ros_map_10x20_feet_with_grid.png')

# Display the image
image.show()

# from PIL import Image, ImageDraw

# # Define dimensions
# feet_to_inches = 12
# width_feet = 10
# height_feet = 20
# width_inches = width_feet * feet_to_inches
# height_inches = height_feet * feet_to_inches

# # Create a new image with white background for 10x20 feet
# image = Image.new('RGB', (width_inches, height_inches), 'white')

# # Save the image
# image.save('ros_map_10x20_feet_no_grid.png')
# image.show()
