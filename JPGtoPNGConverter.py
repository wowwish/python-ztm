import sys
import os
from PIL import Image

source = sys.argv[1]
destination = sys.argv[2]

if not os.path.exists(destination):
    os.makedirs(destination)

files = os.listdir(source)
for file in files:
    name = os.path.splitext(file)[0] # Get the name of the file without the extension. The extension will be in
    # The second element of the tuple returned by splittext().
    img = Image.open(f'{source}/{file}')
    img.save(f'{destination}/{name}.png', 'png')
