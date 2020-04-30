import urllib.request 

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path) # will go to URL and save img to FULL_PATH

url = input('Enter img URL to download: ')
file_name = input('Enter filename to save as: ')

dl_jpg(url, 'InstagramPostingBot/images/', file_name) # will save to images folder