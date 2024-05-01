import os
import tarfile


def save_file(folder_name, file):
    """Save file stream to disk and return the path"""
    file_path = "get_path(folder_name)"

    with open(file_path, "wb") as f:
        while True:
            data = file.read(8192)
            if not data:
                break
            f.write(data)
    f.close()

    return file_path


def get_dir(folder):
    dir = os.path.join(os.getcwd(), "tmp", folder)

    if not os.path.exists(dir):
        os.makedirs(dir)

    return dir


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def create_tar_gz_file(folder_path):
    tar_gz_file_path = folder_path + ".tar.gz"
    with tarfile.open(tar_gz_file_path, "w:gz") as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))
    return tar_gz_file_path
