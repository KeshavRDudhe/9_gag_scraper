![GitHub Logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJcAAACXCAMAAAAvQTlLAAAAY1BMVEUAAAD///+4uLh6enr4+Pj8/Pzb29vLy8stLS1ra2vh4eElJSVycnJaWlpfX1+np6efn5/n5+cODg4dHR2KiooVFRVVVVXw8PCRkZHBwcE0NDTR0dFmZmZPT0+AgIA+Pj5HR0d/XdPMAAADpElEQVR4nO2b6ZaqMAyAKVBAUVlkFFxw3v8pB9cLtE3qTBfPPfn+CsdPG0OS1iAgCIIgCIIgCIIgCIIgLHMKT74VJOQhZzzMfGvM+CpjdiUuv3yrjFlV7Em18i3zYpOyMelnhFkWxmxKHB58SwV1y5kIbz2H2WkpsbqF2cKj1S5VWF05rn1pCYE1DzMvViVsdTNzn81OCWp1JXEbZutOy+pKunFmVRf4Eo4Ws3CzmHUvy1ggvQOzsypjQSx3lq2+oYwFcTzb1Cr2v9RibF9Ys2qRPJrCr/PWitX5CH8hyS7YIUnNwqPpjGSs5b0cXCFmneEfQIkEVpk/LsxL+MLYYJhtIyRwpg9o5HHOo60hL+QrSOZ18wZZTFNfWQi9ibTPWFTQLabqH8irlHeMeevTi3e58qatOsxseyEljLIYsu2FtLDK0tF+fHUX5U2Z+i4XcV/IW9gDlFtceLGqkdzRO8kTBfQmw6NxHv4bpHQ05ZU3SD3fjZNYhvYk5vrKLdJp8Fd6zUq8+jfZ726QAnrZ3y7rdap/s3041skm62Ct1+yang8gnT9PNRs443OLL6S00sTCPAWcLHn0Gn4Av2/VrHoFNZbNBOafxNZc7BC+M6GI+8iR17CY+nOm4cHuzmuo4PXGJ8drv+jSC28p2esh4NbrtlMF8ZquOvZCstm/TQ/nXkG9UC1mMhpEuPcaaGVm0yLWi1dwEcIsnjW7fryGRnEaZt337HVfXpN5xFLcffTn9cpme9ms0qfX8NBk49zwMV5BcA4Vs3DPXkrI6z0+1WvhxmvVvXcM4TLfkLDidTsB0Krnl3MyceJkwavu7k2H9jGElWTiZNwrG02cEp39Yfkk37TXdCiicQyhk3d0Zr0W4mcvoR2VrXKUadLr0MmKeWELBvwY5r0OylFmKt9SXIOVvyktaIwbh7VwfQ3PfUx5NUjb30zDbNvAl5vbT94hW8iTiTQ2jRbG138Be7Pjsy3DPoLp44fY4jz2h7ETMoptwb+ABDPjTYYEIg/1H6vvsMHCDHnZ3gnSSG8QLkO6j2SMXGM7Q0ph/YQyctpFBk/F3Gse7BiCQOXqADB8DGFuFTmyCqTFsYrS7ZlkvVk5f7NFMcECyWYDicMlHAHvYlvOWBA5tPNtP2NBZoo9R576/qeHtI5f+jzl/iSah1nV+1a6k03DzGtgTbm8ujgOHNnxweMgZvI5/9J50uzZ3lvGgsjazwksgiAIgiAIgiAIgiCI/5YftsIoTf2nsl8AAAAASUVORK5CYII=)

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
