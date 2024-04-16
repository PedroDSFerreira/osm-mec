# Project

## Project Goals

This project targets the development of a service that uses OSM's NFV capabilities to 
create and handle MEC Applications as VNF's. This service includes a UI for interaction with the system. 
The onboarding of a MEC App was also defined as a goal

## Main Components

### CFS Portal

The CFS Portal is the "user's gateway" for interacting with the system. It consists on a website built in React.js with the following pages:

- Dashboard
 - The Dashboard gives a standard status of the system
- App Catalog
 - Apps that can be instantiated on the system
- MEC Instances
 - Current MEC Apps instantiated
- VIM Accounts
 - Virtual Infrastructure Manager accounts on the system

### OSS

The Operations Support System is the component which is responsible for receiving MEC App instantion and termination requests and decides on the granting of these requests. 

### MEAO

The MEC Application Orchestrator is the key component that translates the MEC Applications in VNF's within a Network Service. 

## Interaction Between Components

### API

The API that was developped has the purpose of interacting between the OSS and the MEAO. The endpoints are well defined at **SWAGGER API SOURCE** and their workflow is described above:

1. The user triggers a request at the CFS Portal (Ex: Listing current MEC App instances)
2. The OSS detects the request, and either communicates with MEAO or OSM directly (for GETS)
    - With OSM via OSM's NBAPI
    - With MEAO via Kafka with the following workflow:
        1. The OSS saves the file descriptor in MongoDB and it returns an id 
        2. The id is sent through Kafka to the MEAO
        3. The MEAO gets the file descriptor from MongoDB using the id
        4. The MEAO performs the corresponding operation/NBAPI endpoint
3. Answer is returned

### Kafka

Kafka is used for the communication between the OSS and the MEAO, as previously described. 
The topics are the following: 

- responses

### MongoDB

MongoDB is used for storage of file descriptors, as previously described.
Two collections were defined: one for MEC Apps and other for Network Services.
Each one of those collections is composed of documents, with the attributes related to the id, collections name and file descriptor.

## Demonstration App

The Demonstration App functions as a simple client-server system dedicated to object detection.The client transmits a video stream to the server via socket, and YOLOv3 algorithm detects the objects on the frames.

This application runs inside a Containerized Network Function (CNF), which is a VNF where the virtualized hardware runs inside a container on it's machine. The Demo App runs in a Docker Container, managed by Kubernetes.
Frames are sent periodically so that it doesn't congest the network excessively (since it's for demonstration purposes only).