import os
from PIL import Image, ExifTags

def compress_image(input_path, output_path, quality=60):
    with Image.open(input_path) as img:
        # Preserve EXIF orientation
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = img._getexif()
            if exif is not None:
                orientation = exif.get(orientation)
                if orientation == 3:
                    img = img.rotate(180, expand=True)
                elif orientation == 6:
                    img = img.rotate(270, expand=True)
                elif orientation == 8:
                    img = img.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
            # cases: image don't have getexif
            pass

        img.save(output_path, "JPEG", quality=quality)

def compress_images_in_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            compress_image(input_path, output_path)

if __name__ == "__main__":
    root_folder = os.getcwd()
    compress_folder = os.path.join(root_folder, "compressed")
    compress_images_in_folder(root_folder, compress_folder)