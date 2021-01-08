## About the project

This is my final project for [Harvard CS50x 2020](https://cs50.harvard.edu/x/2020/) course.
My project is a simple image viewer made with python 3 and it's GUI library Tkinter.
It opens images from current directory, resizes it to fit a window with doing some math and shows it on a screen.
GUI also has navigation buttons to navigate through images in current directory.



## Description
  Image viewer runs on tkinter GUI library. When program is executed, it opens 800x600 window, then scans for images in current directory, saves filenames in a list called images. Then it opens first photo by name found in a created list and determines it's dimensions with PIL library. If photo does not fit program window (800x560 area of window is for showing an image) it does some math to resize it without it's messing current ratio. 
  GUI also has buttons (back "<<" and forward ">>") to navigate through images.




## How to use

How to run Image Viewer

```
$ python3 image_viewer.py
```

## Requirements

- python 3
- Tkinter library
- PIL library

This is CS50 :)
