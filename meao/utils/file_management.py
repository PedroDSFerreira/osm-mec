import os
import uuid


def save_file(folder_name, file):
    """Save file stream to disk and return the path"""
    file_path = get_path(folder_name)

    with open(file_path, "wb") as f:
        while True:
            data = file.file.read(8192)
            if not data:
                break
            f.write(data)
    f.close()

    return file_path


def get_path(folder_name):
    dir = os.path.join(os.getcwd(), "assets", folder_name)

    if not os.path.exists(dir):
        os.makedirs(dir)

    return os.path.join(dir, str(uuid.uuid4()))


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
