import os
import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--query', required=True,
                help = 'path to input image')
ap.add_argument('-c', '--config', default='yolov3.cfg',
                help = 'path to yolo config file')
ap.add_argument('-w', '--weights', default='yolov3.weights',
                help = 'path to yolo pre-trained weights')
ap.add_argument('-cl', '--classes', default='yolov3.txt',
                help = 'path to text file containing class names')
args = ap.parse_args()


def get_output_layers(net):
    
    layer_names = net.getLayerNames()
    
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


def draw_prediction(b, img, class_id, confidence, x, y, x_plus_w, y_plus_h):

    label = str(classes[class_id])

    color = COLORS[class_id]
	
    file_path = '/Users/Fahad/Desktop/IntelliScraper/Images/'+args.query+'/IntelliScraped/'
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    cv2.imwrite(file_path + image_names[b], img)
    
image_names = os.listdir('/Users/Fahad/Desktop/IntelliScraper/Images/'+args.query)

for b, im in enumerate(image_names):
	print(im)
	image = cv2.imread('/Users/Fahad/Desktop/IntelliScraper/Images/'+args.query+'/'+im)
	Width = image.shape[1]
	Height = image.shape[0]
	scale = 0.00392

	classes = None

	with open(args.classes, 'r') as f:
		classes = [line.strip() for line in f.readlines()]

	COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

	net = cv2.dnn.readNet(args.weights, args.config)

	blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

	net.setInput(blob)

	outs = net.forward(get_output_layers(net))

	class_ids = []
	confidences = []
	boxes = []
	conf_threshold = 0.5
	nms_threshold = 0.4


	for out in outs:
		for detection in out:
			scores = detection[5:]
			class_id = np.argmax(scores)
			confidence = scores[class_id]
			if confidence > 0.5:
				center_x = int(detection[0] * Width)
				center_y = int(detection[1] * Height)
				w = int(detection[2] * Width)
				h = int(detection[3] * Height)
				x = center_x - w / 2
				y = center_y - h / 2
				class_ids.append(class_id)
				confidences.append(float(confidence))
				boxes.append([x, y, w, h])


	indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

	for i in indices:
		i = i[0]
		box = boxes[i]
		x = box[0]
		y = box[1]
		w = box[2]
		h = box[3]
		draw_prediction(b, image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))
