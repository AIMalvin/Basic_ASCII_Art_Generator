# ASCII Art Generator

This script converts images into ASCII art using the Python Imaging Library (PIL).

## Description

The ASCII Art Generator script takes an image file as input and converts it into ASCII art. It resizes the image, converts it to grayscale, and then maps each pixel to a corresponding ASCII character based on its intensity.

## Requirements

- Python 3
- Pillow (`pip install Pillow`)

## Usage

1. Place an image file in the same directory as the script.
2. Run the script using Python.
3. The ASCII art will be outputted to both the console and a text file named `ascii_image.txt`.

## Functions

- `resize_image(image, new_width=50)`: Resizes the image maintaining the aspect ratio.
- `grayify(image)`: Converts the image to grayscale.
- `pixels_to_ascii(image)`: Maps pixels to ASCII characters.
- `image_to_ascii(file_path, new_width=50)`: Main function to convert an image to ASCII art.
- `main(new_width=100)`: Entry point of the script.

