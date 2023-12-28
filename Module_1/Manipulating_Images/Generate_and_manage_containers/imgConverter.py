# Iterate through each file in the folder
    # For each file:
    #     Rotate the image 90° clockwise
    #     Resize the image from 192x192 to 128x128
    #     Save the image to a new folder in .jpeg format


# The images received are in the wrong format:

#     .tiff format
#     Image resolution 192x192 pixel (too large)
#     Rotated 90° anti-clockwise

# The images required for the launch should be in this format:

#     .jpeg format
#     Image resolution 128x128 pixel
#     Should be straight

#!/usr/bin/env python3

from PIL import Image
import os

img_folder = "images"
output_folder = "/opt/icons/"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if os.path.exists(img_folder):
    for i in os.listdir(img_folder):
        img_path = os.path.join(img_folder, i)
        if os.path.isfile(img_path):
            img = Image.open(img_path)
            if img.mode == 'LA':
                img = img.convert('RGB')

            output_filename = f"{i.split('.')[0]}.jpeg"
            output_path = os.path.join(output_folder, output_filename)
            img.rotate(-90).resize((128,128)).save(output_path, format="JPEG")
            print(f"Processed {i} finished sucsesfully")
else:
    print(f"Folder path '{img_folder}' does not exist.")









# #!/usr/bin/env python3

# from PIL import Image
# import os

# img_folder = "images"
# output_folder = "/opt/icons/"

# if not os.path.exists(output_folder):
#     ok.makedirs(output_folder)

# if os.path.exists(img_folder):
#     for i in os.listdir(img_folder):
#         img_path = os.path.join(img_folder, i)
#         if i.lower().endswith((".tiff")):
#             img = Image.open(img_path)
#             output_filename = f"corrected_{i[:-5]}.jpg"
#             output_path = os.path.join(output_folder, output_filename)
#             img.rotate(-90).resize((128,128)).save(output_filename, format="JPEG")
#             print(f"Processed {i} finished sucsesfully")
#         else:
#             print(f"{i} is not a valid file.")
# else:
#     print(f"Folder path '{img_folder}' does not exist.")


#====================================================================================================================================================================

# #!/usr/bin/env python3

# from PIL import Image
# import os

# img_folder = "images"
# output_folder = "/opt/icons/"

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# if os.path.exists(img_folder):
#     for i in os.listdir(img_folder):
#         img_path = os.path.join(img_folder, i)
#         if i.lower().endswith((".tiff")):
#             img = Image.open(img_path)
#             output_path = os.path.join(output_folder, img)
#             img.rotate(-90).resize((128,128)).save(img, format="JPEG")
#             print(f"Processed {i} finished sucsesfully")
#         else:
#             print(f"{i} is not a valid file.")
# else:
#     print(f"Folder path '{img_folder}' does not exist.")




#====================================================================================================================================================================


# ORIGINAL

# #!/usr/bin/env python3

# from PIL import Image
# import os

# img_folder = "images"
# output_folder = "/opt/icons/"

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# if os.path.exists(img_folder):
#     for i in os.listdir(img_folder):
#         img_path = os.path.join(img_folder, i)
#         img = Image.open(img_path)
#         output_path = os.path.join(output_folder, img)
#         img.rotate(-90).resize((128,128)).save(img, format="JPEG")
#         print(f"Processed {i} finished sucsesfully")
# else:
#     print(f"Folder path '{img_folder}' does not exist.")