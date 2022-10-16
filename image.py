# Import required Classes from the pillow package (PIL)
# The 'Image' class allows us to work with image files and the 'ImageFilter' class allows us to modify and
# edit the image
from PIL import Image, ImageFilter

img = Image.open('images/pikachu.jpg')  # Creates an image object
print("img : ", img)
print("img.format : ", img.format)  # The format of the image
print("img.size : ", img.size)  # The size of the image
print("img.mode : ", img.mode)  # The coloring mode of the image
print()
print()
# All properties and attributes of an 'Image' object
print("dir(img) : ", dir(img))

# View the image in a temporary pane
# img.show()

# EACH OF THESE IMAGE OPERATIONS RETURN ANOTHER IMAGE OBJECT WHICH CAN BE FURTHER EDITED AND MODIFIED USING OTHER
# SUCH METHODS.
filtered_img = img.filter(ImageFilter.BLUR)  # Blur the image
# Save the blurred image using .save(<name>, <img_file_type>)
filtered_img.save('images/blur.png', 'png')

# Smoothen the image - this filter works better with landscape images
smoothed_img = img.filter(ImageFilter.SMOOTH)
smoothed_img.save('images/smooth.png', 'png')  # Save the smoothed image

sharp_img = img.filter(ImageFilter.SHARPEN)  # Sharpen the image
sharp_img.save('images/sharp.png', 'png')  # Save the sharper image

converted_img = img.convert('L')  # Convert image to greyscale
converted_img.save('images/grey.png', 'png')  # Save converted greyscale image

# converted_img.show() # View image in a temporary new pane

crooked = converted_img.rotate(90)  # Rotate image
crooked.save('images/rotate_90.png', 'png')  # Save rotated image

# Resize the image to 300 x 300 pixels
# The image is now squished and the original aspect ratio is lost
resize = converted_img.resize((300, 300))
resize.save('images/resize.png', 'png')  # Save resized image in PNG format


# Crop an image using box coordinates in pixels
box = (100, 100, 400, 400)  # pixed coordinates of crop box
region = filtered_img.crop(box)  # extract the cropped image
region.save('images/crop.png', 'png')  # save the cropped image


# Reduce Image Size by resizing
img = Image.open('images/astro.jpg')
print("astro image size : ", img.size) # Image is bigger than 5000 x 5000 
# .thumbnail() takes a tuple of width and height that it uses as the maximum for retaining the original aspect ratio
img.thumbnail((400, 400)) # An inplace method that resizes the image and retains the original aspect ratio
print("thumbnail dimensions : ", img.size) # You can see that the image size is not exactly 400 x 400. This is because
# .thumbnail() tries to retain the original image aspect-ratio and uses the dimension we provide as the maximum limit
# for the image size.
img.save('images/thumbnail.jpg', 'jpeg')
print("")
