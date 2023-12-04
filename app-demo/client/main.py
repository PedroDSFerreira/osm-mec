import argparse
import socket
import threading

import cv2

DEFAULT_PORT = 10050
DEFAULT_HOST = "127.0.0.1"


def receive_faces_data(client_socket, exit_event):
    while not exit_event.is_set():
        try:
            # Receive the number of faces from the server
            faces_data = client_socket.recv(4096)
            num_faces = int(faces_data.decode())
            print(f"Number of Faces: {num_faces}")
        except Exception as e:
            print(f"Error receiving faces data: {e}")
            break


def main_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    cap = cv2.VideoCapture(0)

    # Event to signal the faces thread to exit
    exit_event = threading.Event()

    # Start a separate thread to receive face count data
    faces_thread = threading.Thread(
        target=receive_faces_data, args=(client_socket, exit_event)
    )
    faces_thread.start()

    try:
        while True:
            _, frame = cap.read()

            # Encode the image array to send it over the network
            _, img_encoded = cv2.imencode(
                ".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80]
            )
            data = img_encoded.tobytes() + b"<<END>>"

            # Send the image data
            client_socket.sendall(data)

            # Display the video stream
            cv2.imshow("Client Stream", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                data = b"<<END>>"
                client_socket.sendall(data)
                break

    except KeyboardInterrupt:
        pass
    finally:
        # Signal the faces thread to exit
        exit_event.set()

        # Wait for the faces thread to complete
        faces_thread.join()

        cap.release()
        cv2.destroyAllWindows()
        client_socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Client for Face Detection App")
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

    main_client(args.h, args.p)
