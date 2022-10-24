import os
from rembg import remove
from PIL import Image

dir_containing_file ='C:\\git\\Python-code-examples\\'
os.chdir(dir_containing_file)


input_path = "img.jpg"
output_path = "image1.png"
input1 = Image.open(input_path)
#print(input)
output = remove(input1)
output.save(output_path)



#clcoding.com