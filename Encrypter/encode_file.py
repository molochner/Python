import random
import os
import tkinter as tk
from tkinter import filedialog

# the \n will cause everything to be shifted in the file after its written
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;?@[ ]^_`{|}~' #\n' #not sure yet

def SelectFile():
    # Select which file to encode or decode
    root = tk.Tk()
    root.withdraw()

    global filepath
    global folderpath
    global filename
    global filetype

    filepath = filedialog.askopenfilename()
    folderpath = os.path.dirname(filepath)
    folderpath += "/"

    name_type = os.path.splitext(os.path.basename(filepath))
    filename = name_type[0]
    filetype = name_type[1]

    # print("Filepath: " + filepath)
    # print("Folderpath: " + folderpath)
    # print("Filename: " + filename)
    # print("Filetype: " + filetype)

def SelectKeyFile():
    # Select key
    print("Please select the decryption key file")
    root = tk.Tk()
    root.withdraw()

    global filepathKEY
    global folderpathKEY
    global filenameKEY
    global filetypeKEY

    filepathKEY = filedialog.askopenfilename()
    folderpathKEY = os.path.dirname(filepathKEY)
    folderpathKEY += "/"

    name_type = os.path.splitext(os.path.basename(filepathKEY))
    filenameKEY = name_type[0]
    filetypeKEY = name_type[1]

def rand_chars(rand):
    # each num in rand finds its spot in chars
    # turns it into the list of corralating chars
    rand_to_chars = ''
    for i in range(0, len(rand)):
        rand_to_chars += chars[rand[i]]
    write_decode_key_file(rand_to_chars)
    return rand_to_chars

def write_decode_key_file(content):
    # creates decode file
    global decryption_key_filename
    decryption_key_filename = filename + "_decryption_key" + filetype
    myfile = open(folderpath + decryption_key_filename, "w")
    myfile.write(repr(str(content)))
    myfile.write("\n")
    myfile.write(repr(str(chars)))
    myfile.close()

def Encoder(rand_to_chars):
    # encodes a file
    with open(filepath, "r") as myfile:
        text_file_contents = myfile.read()  # file as string

    global encoded_filename
    encoded_filename = filename + "_encoded" + filetype
    file_encoded = open(folderpath + encoded_filename, "w")
    encoded_str = ''

    for char in range(0, len(text_file_contents)):  # loops through text_file_contents
        for i in range(0, len(chars)):  # loops through chars list
            if str(text_file_contents[char]) == str(chars[i]):  # same spot in chars
                if str(chars[i]) != "\n":
                    encoded_str += rand_to_chars[i]  # then same spot in rand
                else:
                    encoded_str += "\n"

    file_encoded.write(str(encoded_str))

    myfile.close()
    file_encoded.close()

def Decoder():
    # decodes a file with a key
    with open(filepath, "r") as myfile:
        encoded_text = myfile.read()  # file as string
    with open(filepathKEY, "r") as mykeyfile:
        key_text = mykeyfile.read()  # file as string

    global decoded_filename
    decoded_filename = filename + "_decoded" + filetype
    file_decoded = open(folderpath + decoded_filename, "w")
    decoded_str = ''

    for char in range(0, len(encoded_text)):  # loops through encoded text file
        for i in range(0, int(len(key_text) / 2)):  # loops through key text list
            if str(encoded_text[char]) == str(key_text[i]):  # same spot in key
                decoded_str += chars[i-1]

    file_decoded.write(str(decoded_str))

    myfile.close()
    mykeyfile.close()
    file_decoded.close()

def MakeNewNumsStr():
    # creates random string of nums
    rand = random.sample(range(len(chars)), len(chars))
    return rand

def Menu():
    os.system('cls')
    print('~~~~~~~~~~~~~~~~Encoder/Decoder~~~~~~~~~~~~~~~~~')
    print('Would you like to Encode(1) or Decode(2) a file?')
    selection = (input("Select option 1 or 2 by typing the number: "))

    try:
        selection = int(selection)
        if selection == 1:
            os.system('cls')
            print("You've choosen to Encode a file.")
            print("Please select a file to encode")
            SelectFile()
            rand = MakeNewNumsStr()
            rand_to_chars = rand_chars(rand)
            Encoder(rand_to_chars)
            os.system('cls')
            print("File named " + str(filename + filetype) + 
                " has been encoded into a new file named " + str(encoded_filename))
            print("The decryption key is stored in a file named " + decryption_key_filename)
        
        elif selection == 2:
            os.system('cls')
            print("You've choosen to Decode a file.")
            print("Please select a file to Decode")
            SelectFile()
            SelectKeyFile()
            Decoder()
            os.system('cls')
            print("File named " + str(filename + filetype) + 
                " has been decoded into a new file named " + str(decoded_filename))
        
        else:
            print('Incorrect selection. Good-Bye')
            return 0
    except:
        print('An error has occured. Good-Bye')
        return 0

Menu()