from PIL import Image

def reduce_image_size(input_path, output_path, scale_factor):
    # Open the image file
    with Image.open(input_path) as img:
        # Calculate the new size
        new_size = tuple(int(dim / scale_factor) for dim in img.size)
        
        # Resize the image
        resized_img = img.resize(new_size, Image.ANTIALIAS)
        
        # Save the resized image
        resized_img.save(output_path, format='PNG')

# Usage
reduce_image_size('B:\002.일별업무\1122\img\1-0kang.png', 'B:\002.일별업무\1122\img\resize\1-0kang.png', 2)  # Reduces size by half