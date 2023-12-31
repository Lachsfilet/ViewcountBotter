import requests
import threading

def main():
    url = input('Please input your Viewcount API URL (for help enter h): ')
    if url == 'h':
        print('if you dont know whats going on you probaly dont have a profile readme.md follow the tutorial in the readme.md')
    requests.get(url)

if __name__ == "__main__":
    main()