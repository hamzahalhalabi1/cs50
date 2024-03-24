import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    check_arg()
    shirt = Image.open("shirt.png")
    try:
        input_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')
    size = shirt.size
    muppet = ImageOps.fit(input_image, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])


def check_arg():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    before = sys.argv[1]
    after = sys.argv[2]
    check_extension(before, after)


def check_extension(before, after):
    before_split = splitext(before)
    after_split = splitext(after)
    before_extension = before_split[1]
    after_extension = after_split[1]
    if before_extension and after_extension in ['.jpg', '.jpeg', '.png']:
        if before_extension == after_extension:
            return True
        else:
            sys.exit('Input and output have different extensions')
    else:
        sys.exit('Invalid output')


if __name__ == "__main__":
    main()


## with ChatGPT
# import sys
# from PIL import Image, ImageOps
#
#
# def overlay_shirt(input_path, output_path):
#     try:
#         # Open the input image
#         input_image = Image.open(input_path)
#
#         # Open the shirt image
#         shirt = Image.open("shirt.png")
#
#         # Resize and crop the input image to the same size as the shirt
#         input_image = ImageOps.fit(input_image, shirt.size, method=0, bleed=0.0, centering=(0.5, 0.5))
#
#         # Overlay the shirt on the input image
#         input_image.paste(shirt, (0, 0), shirt)
#
#         # Save the result to the output path
#         input_image.save(output_path)
#
#     except FileNotFoundError:
#         print("Input image does not exist")
#         sys.exit(1)
#
#
# if __name__ == "__main__":
#     # Check the number of command-line arguments
#     if len(sys.argv) != 3:
#         print("Too few or too many command-line arguments")
#         sys.exit(1)
#
#     # Check if the file extensions are valid
#     input_filename, output_filename = sys.argv[1], sys.argv[2]
#     if not (input_filename.lower().endswith(('.jpg', '.jpeg', '.png')) and
#             output_filename.lower().endswith(('.jpg', '.jpeg', '.png'))):
#         print("Invalid file extensions")
#         sys.exit(1)
#
#     # Check if the input file exists
#     try:
#         with open(input_filename):
#             pass
#     except FileNotFoundError:
#         print("Input file does not exist")
#         sys.exit(1)
#
#     # Check if the input and output file extensions match
#     if input_filename.lower().endswith(('.jpg', '.jpeg', '.png')) != output_filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#         print("Input and output have different extensions")
#         sys.exit(1)
#
#     # Run the overlay_shirt function
#     overlay_shirt(input_filename, output_filename)
