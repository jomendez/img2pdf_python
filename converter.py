import os
import img2pdf # pip install img2pdf
import sys

current_path = os.path.abspath(os.getcwd())
path = '.'

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = os.path.join(current_path, sys.argv[1])
    else:
        print('If there is not parameter, the script will try to get the files form the current working directory')


# list_of_images = [i for i in os.listdir(path) if i.endswith(".jpg")]
list_of_images = []
for file_path in os.listdir(path):
        if file_path.endswith(".jpg"):
            list_of_images.append(os.path.join(path, file_path))
        else:
            pass


with open("output.pdf", "wb+") as f:
    f.write(img2pdf.convert(list_of_images))

print('File created!')