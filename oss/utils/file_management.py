def read_stream(s):
    file = b""
    while True:
        chunk = s.read(8192)
        if not chunk:
            break
        file += chunk
    return file
