import argparse
import logging
import socket

import cv2
import numpy as np
from face_detection import count_faces

DEFAULT_PORT = 10050
DEFAULT_HOST = "127.0.0.1"

# Configure logging
logging.basicConfig(level=logging.INFO)


def handle_client(client_socket, client_address):
    try:
        logging.info(f"{client_address}:Connection started")

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
                    # Count the number of faces in the frame
                    num_faces = count_faces(image_array)
                    # Send the number of faces to the client
                    client_socket.sendall(str(num_faces).encode("utf-8"))
                    logging.info(f"{client_address}:Faces: {num_faces}")
            else:
                break

    except Exception as e:
        logging.error(f"{client_address}:Error: {e}")

    finally:
        logging.info(f"{client_address}:Connection closed")
        client_socket.close()


def main_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Maximum 5 queued connections
    logging.info(f"Server listening on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()

            handle_client(client_socket, client_address)

    except KeyboardInterrupt:
        logging.info("Server interrupted, closing...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Server for Face Detection App")
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
    args = parser.parse_args()

    main_server(args.h, args.p)
