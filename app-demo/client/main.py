import argparse
import pickle
import socket
import struct
import sys
import threading

import cv2


def receive_values(client_socket):
    while True:
        data = b""
        payload_size = struct.calcsize("Q")

        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)
            if not packet:
                break
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)

        value_data = data[:msg_size]
        data = data[msg_size:]
        value = pickle.loads(value_data)
        print(f"\rReceived from server:{value}", end="")
        sys.stdout.write("\033[K")


def send_video(client_socket):
    vid = cv2.VideoCapture(0)

    while vid.isOpened():
        _, frame = vid.read()
        a = pickle.dumps(frame)
        message = struct.pack("Q", len(a)) + a
        client_socket.sendall(message)
        cv2.imshow("Sending...", frame)
        key = cv2.waitKey(10)
        if key == 13:
            break

    vid.release()
    cv2.destroyAllWindows()
    client_socket.close()


def main():
    parser = argparse.ArgumentParser(description="Client for Face Detection App")
    parser.add_argument("--h", type=str, default="127.0.0.1", help="Host IP address")
    parser.add_argument("--p", type=int, default=10050, help="Port number")
    args = parser.parse_args()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((args.h, args.p))

    try:
        # Start a thread for receiving values
        value_thread = threading.Thread(target=receive_values, args=(client_socket,))
        value_thread.start()

        # Send video to the server
        send_video(client_socket)
    except Exception as e:
        print("Error:", e)
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
