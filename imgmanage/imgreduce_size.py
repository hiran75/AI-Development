from PIL import Image


##이미지 사이즈를 줄이기 
def reduce_image_size(input_path, output_path, scale_factor):
    # Open the image file
    with Image.open(input_path) as img:
        # Calculate the new size
        new_size = tuple(int(dim / scale_factor) for dim in img.size)

        # Resize the image using LANCZOS resampling
        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)

        # Save the resized image
        resized_img.save(output_path, format='PNG')

##이미지 늘리기, 줄이기
def increase_vertical_size(input_path, output_path, scale_factor):
    # Open the image file
    with Image.open(input_path) as img:
        # Calculate the new size
        new_width = img.width
        new_height = int(img.height * scale_factor)

        # Resize the image, keeping the width the same and increasing the height
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Save the resized image
        resized_img.save(output_path, format='PNG')

ddd

# Usage
filename="1-5kang.png"
orgfilename='D:/deeplearning/sjcu_working/imgmanage/img/' + filename
resizefilename="D:/deeplearning/sjcu_working/imgmanage/img/resize/" + filename
increasefilename ="D:/deeplearning/sjcu_working/imgmanage/img/increase/" + filename


increase_vertical_size(orgfilename, increasefilename, 1.2)  # Increases height by 50%

reduce_image_size(increasefilename, resizefilename, 1.5)  # Reduces size by half