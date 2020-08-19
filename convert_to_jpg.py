from PIL import Image
import os
import sys


def get_image_files(input):
    # If input is a single file
    if os.path.isfile(input):
        return input
    # Input is a directory
    else:
        # Converting .HEIC or .PNG files from iPhone
        valid_extensions = [".heic", ".png"]
        # Return all files that are .HEIC or .PNG
        return [os.path.join(input, f) for f in os.listdir(input) if os.path.splitext(f)[1].lower() in valid_extensions]


def convert_to_jpg(image_file):
    # Open file with Pillow
    im = Image.open(image_file)
    # Get file extension
    file_ext = os.path.splitext(image_file)[1]
    # Convert to JPG
    im.convert('RGB').save(image_file.replace(file_ext, ".JPG"), quality=100, subsampling=0)
    print(f'successfully converted {image_file} to jpg')
    # Delete original file
    os.remove(image_file)


if __name__ == '__main__':
    # Ask user for image(s) to convert to JPG
    image_files = get_image_files(sys.argv[1])
    print(image_files)
    # Convert image(s) to JPG
    for image_file in image_files:
        convert_to_jpg(image_file)
