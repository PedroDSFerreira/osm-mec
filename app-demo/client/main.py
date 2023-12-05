import argparse
import json
import queue
import socket
import threading

import cv2

DEFAULT_PORT = 10050
DEFAULT_HOST = "127.0.0.1"


def receive_objs_data(client_socket, frame_queue, exit_event):
    while not exit_event.is_set():
        try:
            # Receive the data from the server
            data = client_socket.recv(4096)
            data = json.loads(data.decode())

            num_objs = data["count"]

            # Enqueue the frame with objects for display
            frame_queue.put((data["positions"], num_objs))

        except Exception as e:
            print(f"Error receiving data: {e}")
            break

    # Signal the main thread to stop displaying
    frame_queue.put(None)


def draw_boxes(frame, objs_positions):
    for box in objs_positions:
        # Draw rectangle around the object
        frame = cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

    return frame


def main_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    cap = cv2.VideoCapture(0)

    # Queue to pass frames from the receiving thread to the main thread
    frame_queue = queue.Queue()

    # Event to signal the recv_data_thread to exit
    exit_event = threading.Event()

    # Start a separate thread to receive data
    recv_data_thread = threading.Thread(
        target=receive_objs_data, args=(client_socket, frame_queue, exit_event)
    )
    recv_data_thread.start()

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

            # Try to get the next frame with boxes from the queue
            try:
                objs_data = frame_queue.get_nowait()
                if objs_data is None:
                    # receiving thread has stopped
                    break

                objs_positions, num_objs = objs_data

                # Draw boxes on the video stream
                frame_with_boxes = draw_boxes(frame, objs_positions)

                # Display the number of objects
                cv2.putText(
                    frame_with_boxes,
                    f"Objects Detected: {num_objs}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )
                # Display the video stream with objects
                cv2.imshow("Client Stream", frame_with_boxes)

            except queue.Empty:
                pass

            # Check for the "q" key press
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                data = b"<<END>>"
                client_socket.sendall(data)
                break  # Exit the loop when "q" is pressed

    except KeyboardInterrupt:
        pass
    finally:
        # Signal the thread to exit
        exit_event.set()
        recv_data_thread.join()

        cap.release()
        cv2.destroyAllWindows()
        client_socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Client for Object Detection App")
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
