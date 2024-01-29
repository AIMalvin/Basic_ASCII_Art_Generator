from PIL import Image

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=50):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image, scaling_factor=35):
    pixels = image.getdata()
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // scaling_factor]
    return ascii_str

def image_to_ascii(file_path, new_width=100, scaling_factor=35):
    try:
        image = Image.open(file_path)
    except Exception as e:
        print(e)
        return
    
    image = resize_image(image, new_width)
    image = grayify(image)
    
    ascii_str = pixels_to_ascii(image, scaling_factor)
    img_width = image.width
    
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)
    return ascii_img

def main(new_width=100, scaling_factor=35):
    path = "dog.png"
    ascii_art = image_to_ascii(path, new_width=new_width, scaling_factor=scaling_factor)
    print(ascii_art)

if __name__ == '__main__':
    main()
