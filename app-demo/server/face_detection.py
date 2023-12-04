import cv2
import numpy as np

# define the minimum confidence (to filter weak detections),
# Non-Maximum Suppression (NMS) threshold
confidence_thresh = 0.7
NMS_thresh = 0.3

# load the class labels the model was trained on
classes_path = "yolo/coco.names"
with open(classes_path, "r") as f:
    classes = f.read().strip().split("\n")

# load the configuration and weights from disk
yolo_config = "yolo/yolov3.cfg"
yolo_weights = "yolo/yolov3.weights"

# load the pre-trained YOLOv3 network
net = cv2.dnn.readNetFromDarknet(yolo_config, yolo_weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Get the name of all the layers in the network
layer_names = net.getLayerNames()
# Get the names of the output layers
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]


def count_faces(frame):
    # get the frame dimensions
    h, w = frame.shape[:2]

    # create a blob from the frame
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), swapRB=True, crop=False)
    # pass the blog through the network and get the output predictions
    net.setInput(blob)
    outputs = net.forward(output_layers)

    # create empty lists for storing the bounding boxes, confidences, and class IDs
    boxes = []
    confidences = []

    # loop over the output predictions
    for output in outputs:
        # loop over the detections
        for detection in output:
            # get the class ID and confidence of the detected object
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # check if the detected object is a person face (class_id 0 corresponds to "person" in COCO dataset)
            if confidence > confidence_thresh and classes[class_id] == "person":
                # perform element-wise multiplication to get
                # the coordinates of the bounding box
                box = [int(a * b) for a, b in zip(detection[0:4], [w, h, w, h])]
                boxes.append(box)
                confidences.append(float(confidence))

    # apply non-maximum suppression to remove weak bounding boxes that overlap with others.
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_thresh, NMS_thresh)

    if indices is not None and len(indices) > 0:
        indices = indices.flatten()

    # return the total number of faces detected
    return len(indices)
