import os
import img2pdf # pip install img2pdf
import sys

current_path = str(os.path.abspath(os.getcwd())) + '\\'
path = '.'

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = current_path + str(sys.argv[1])
    else:
        print('If there is not parameter, the script will try to get the files form the current working directory')

list_of_images = [i for i in os.listdir(path) if i.endswith(".jpg")]

with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(list_of_images))

print('File created!')