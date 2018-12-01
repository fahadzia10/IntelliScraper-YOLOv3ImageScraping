# IntelliScraper-YOLOv3ImageScraping

## What is IntelliScraper
This is an intelligent image scraper for the web that uses a simple python web scraper to generate images which are then refined based on output from a YOLO v3 Deep Learning model that extracts only the required images of objects and stores them in a separate sub-folder.

## How To Run
1. Download weights of model from the following link and paste in IntelliScraper folder:
https://pjreddie.com/media/files/yolov3.weights

2. Run the following command in a Python 2.7 environment for searching for some image on google (can change search website in the code) for e.g. apple:
	python script.py --search apple

Or add optional parameters like the number of images to download:
	python script.py --search apple  --num_images 20

3. Run the following command in a Python 3.5 environment to refine the acquired dataset intelligently:
	python yolo_opencv.py --apple

4. The "yolo_opencv" will create a subfolder "Intelliscraped" inside the fodler with the images with refined images automatically.
