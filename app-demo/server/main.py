import argparse
import json
import logging
import socket

import cv2
import numpy as np
from object_detection import detect_objects

DEFAULT_PORT = 10050
DEFAULT_HOST = "127.0.0.1"
DEFAULT_CONF_THRESH = 0.7
DEFAULT_NMS_THRESH = 0.3

logging.basicConfig(level=logging.INFO)


def handle_client(client_socket, client_address, opts):
    try:
        logging.info(f"{client_address}: Connection started")

        while True:
            data = b""
            while b"<<END>>" not in data:
                packet = client_socket.recv(4096)
                if not packet:
                    break
                data += packet

            # Ensure that the received data is not empty
            if len(data) > 7:
                # Extract the image data from the received stream
                image_data = data[:-7]
                image_array = cv2.imdecode(
                    np.frombuffer(image_data, dtype=np.uint8), cv2.IMREAD_COLOR
                )

                if image_array is not None:
                    # Detect objects and get their positions
                    num_objs, objs_positions = detect_objects(
                        frame=image_array,
                        object=opts[0],
                        confidence_thresh=opts[1],
                        NMS_thresh=opts[2],
                    )

                    # Serialize the objects positions
                    objs_data = {"count": num_objs, "positions": objs_positions}
                    serialized_objs_data = json.dumps(objs_data)

                    # Send the serialized objects data to the client
                    client_socket.sendall(serialized_objs_data.encode("utf-8"))

                    # Log the number of objects detected
                    logging.info(
                        f"{client_address}: {num_objs} objects detected in the image"
                    )

            else:
                break

    except Exception as e:
        logging.error(f"{client_address}: Error: {e}")

    finally:
        logging.info(f"{client_address}: Connection closed")
        client_socket.close()


def main_server(host, port, opts):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    logging.info(f"Server listening on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()

            handle_client(client_socket, client_address, opts)

    except KeyboardInterrupt:
        logging.info("Server interrupted, closing...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Server for Object Detection App")
    parser.add_argument(
        "--h",
        type=str,
        default=DEFAULT_HOST,
        help=f"Host IP address (default: {DEFAULT_HOST})",
    )
    parser.add_argument(
        "--p",
        type=int,
        default=DEFAULT_PORT,
        help=f"Port number (default: {DEFAULT_PORT})",
    )
    parser.add_argument(
        "--o",
        type=str,
        default="person",
        help="Object to detect (default: person)",
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=DEFAULT_CONF_THRESH,
        help=f"Confidence threshold (default: {DEFAULT_CONF_THRESH})",
    )
    parser.add_argument(
        "--nms",
        type=float,
        default=DEFAULT_NMS_THRESH,
        help=f"NMS threshold (default: {DEFAULT_NMS_THRESH})",
    )
    args = parser.parse_args()

    main_server(args.h, args.p, (args.o, args.conf, args.nms))
