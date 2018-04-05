import os
import shutil
import sys


des_path = './data'
src_path = os.path.join(os.path.expandvars("%userprofile%"),r'AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')

# os.getcwd()

def copy_files():
    file_list = os.listdir(src_path)
    for file in file_list:
        # file = file_list[0]
        file_path = src_path + "\\" + file
        # assert not os.path.isabs(file)
        # dstdir =  des_path os.path.join(des_path, os.path.dirname(file_path))
        if not os.path.exists(des_path + "\\" + file):
            shutil.copy(file_path, des_path + "\\" + file + ".png")


def del_files():
    file_list = os.listdir(des_path)
    for single_file in file_list:
        # single_file = file_list[0]
        os.remove(des_path + "\\" + single_file)



def main():
    if len(sys.argv)>1:
        operation = sys.argv[1]
    else:
        operation = ''
    # print(operation)
    if operation == "make":
        print("Coping and renaming files")
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        copy_files()
    elif operation == "clean":
        print("Cleaning the files")
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        del_files()
    else:
        print("Please provide arguments :: make || clean")


if __name__ == '__main__':
    main()
