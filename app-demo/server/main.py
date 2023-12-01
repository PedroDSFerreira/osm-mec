import argparse
import concurrent.futures
import pickle
import socket
import struct

from face_detection import count_faces


def receive_video(client_socket, _):
    data = b""
    payload_size = struct.calcsize("Q")

    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)
            if not packet:
                break
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            packet = client_socket.recv(4 * 1024)
            if not packet:
                break
            data += packet

        frame_data = data[:msg_size]
        data = data[msg_size:]

        try:
            frame = pickle.loads(frame_data)

            face_count = count_faces(frame)

            # Send face count to the client
            face_count_pickled = pickle.dumps(face_count)
            message = struct.pack("Q", len(face_count_pickled)) + face_count_pickled
            client_socket.sendall(message)

        except Exception as e:
            print("Error decoding frame:", e)
            break

    client_socket.close()


def handle_client(client_socket, addr):
    try:
        # Receive video from the client
        receive_video(client_socket, addr)
    except Exception as e:
        print("Error:", e)


def main():
    # Add a command-line argument for the port
    parser = argparse.ArgumentParser(description="Server for Face Detection App")
    parser.add_argument("--p", type=int, default=10050, help="Port number")
    args = parser.parse_args()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("HOST IP:", host_ip)

    # Use the port from the command-line argument
    socket_address = (host_ip, args.p)
    print(f"Socket created. Listening on port {args.p}")

    server_socket.bind(socket_address)
    print("Socket bind complete")

    server_socket.listen(5)
    print("Socket now listening")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            client_socket, addr = server_socket.accept()
            print("Connection from:", addr)
            executor.submit(handle_client, client_socket, addr)


if __name__ == "__main__":
    main()
