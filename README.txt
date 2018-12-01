1. Download weights of model from the following link and paste in IntelliScraper folder:
https://pjreddie.com/media/files/yolov3.weights

2. Run the following command for searching for some image on google for e.g. apple:
	python script.py --search apple

Or add optional parameters like the number of images to download:
	python script.py --search apple  --num_images 20

3. Run the following command to refine the acquired dataset intelligently:
	python yolo_opencv.py --apple

4. The "yolo_opencv" will create a subfolder "Intelliscraped" inside the fodler with the images with refined images automatically.
