# Client-Server Face Detection Application

This is a simple client-server application for face detection using YOLOv3. The server receives video frames from clients, processes them using YOLOv3 for face detection, and returns the count of detected faces back to the clients.

## Requirements

- Python 3

## Installation

- Clone the repo and install the required Python packages.

  ```bash
  git clone https://github.com/PedroDSFerreira/osm-mec.git
  cd osm-mec/app-demo
  pip install -r requirements.txt
  ```

## Usage

### Server

1. Open a terminal and navigate to the server directory.

   ```bash
   cd app-demo/server
   ```

2. Download the YOLOv3 model files and place them in the `yolo` directory.

   ```bash
   wget https://pjreddie.com/media/files/yolov3.weights -P yolo
   ```

3. Run the server script.

   ```bash
   python server.py --h <host_ip> --p <port>
   ```

The server will start listening for incoming connections on the specified port.

### Client

1. Open a terminal and navigate to the client directory.

   ```bash
   cd app-demo/client
   ```

2. Run the client script.

   ```bash
   python client.py --h <host_ip> --p <port>
   ```

The client will establish a connection with the server and start sending video frames. The server will process each frame and return the count of detected faces to the client.

## Configuration

- The YOLO model configuration file (`yolov3.cfg`), weights file (`yolov3.weights`), and class names file (`coco.names`) should be placed in the `yolo` directory.
- In the 'server/face_detection.py' file, you can customize the face detection parameters:
  - confidence_thresh: Adjust the confidence threshold for face detection. Faces with confidence below this threshold will not be counted.
  - NMS_thresh: Set the Non-Maximum Suppression (NMS) threshold to control the overlap of bounding boxes.
    Feel free to experiment with these parameters to optimize face detection based on your specific use case.

## Dependencies

- YOLOv3 model files: [YOLOv3 Official Website](https://pjreddie.com/darknet/yolo/)
- COCO class names file: [COCO Official Website](https://cocodataset.org/#home)

## License

This project is licensed under the [MIT License](LICENSE).
