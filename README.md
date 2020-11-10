![GitHub Logo](9gag.png)

# Image-Extraction

Image and video extraction from 9 gag.

## Pre-requisites:
1. Git for windows: https://gitforwindows.org/
2. Python 3.7.4: https://www.python.org/downloads/release/python-374/
3. Pip for python package management: 
  ```
  curl https://bootstrap.pypa.io/get-pip.py > get_pip.py
  set path=%PATH%;C:\Users\Admin\AppData\Local\Programs\Python\Python37\Scripts
  ```
## Setup:
### Install virtualenv
```
py -m pip install --user virtualenv
```
### Create virtualenv
```
py -m venv env
.\env\Scripts\activate
```
### Install dependencies in the virtualenv
```
pip install -r requirements.txt
```

## Run the image extraction module
```
python folder_name/9_gag_scraper.py
```
This will store the images and videos in location (path_to_save_files) as .webp extension.

## Usage:
Update this variable path_to_save_files (Absoulte Path).
Output will be saved in same folder.
