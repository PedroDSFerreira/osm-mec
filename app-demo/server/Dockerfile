# syntax=docker/dockerfile:1
FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# set the working directory
WORKDIR /code

# install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the project files
COPY . .

# download yolov3 weights
RUN wget https://pjreddie.com/media/files/yolov3.weights -P yolo

# run server
CMD ["python", "main.py", "--h", "0.0.0.0", "--p", "8080"]
