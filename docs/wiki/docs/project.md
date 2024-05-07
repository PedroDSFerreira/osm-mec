# Project


## Project Goals

- Create a CFS Portal enabling the instantiation, termination and monitoring of MEC Apps.

- Develop an MEC Application Orchestrator capable of deploying MEC Apps as VNFs through OSM platform.

- Create a video processing application to showcase the project's functionalities.


## Main Components

![Project Diagram](./images/Drawing6.png)


### CFS Portal

The CFS Portal is the UI for interacting with the system. 

- Dashboard: Overview of the system

- App Catalog: View and create MEC Apps

- MEC Instances: View and update instantiated MEC Apps

- VIM Accounts: View and create VIM Accounts


### OSS

The Operations Support System is responsible to redirect the user requests to MEAO.


### MEAO

The MEC Application Orchestrator is responsible for:

- Instantiating, updating, and terminating MEC Apps.

- Deploying MEC Apps as VNFs.

- Monotoring MEC Apps.

## Interaction Between Components

### API

The API enables communication between the CFS Portal and OSS, as well as allowing users to make requests directly to the API instead of using the CFS Portal.

### Kafka

Kafka enables communication between OSS and MEAO.

The Kafka topics available are: 
- new_app_pkg <a id="new_app_pkg"></a>
- instantiate_app_pkg <a id="instantiate_app_pkg"></a>
- update_app_pkg <a id="update_app_pkg"></a>
- terminate_app_pkg <a id="terminate_app_pkg"></a>
- delete_app_pkg <a id="delete_app_pkg"></a>
- responses <a id="responses"></a>


### MongoDB

Mongo Database is used to storage of file descriptors. 

MongoDB has two collections:
- App Packages


Each collection has documents. Document fields are: <a id="document-fields"></a>
- app_id
- name
- provider
- version
- mec-version
- info-name
- description
- appd
- ns_pkg_id
- vnf_pkg_id


## Requests Process Flow

### App Package

#### POST
1. OSS receives a POST request from the CFS Portal
2. OSS validates the app descriptor
3. OSS sends the app package and some [fields](#document-fields), belonging to the app descriptor, to the Database
4. Database returns an _id that identifies the document
5. OSS sends the _id through Kafka, on the topic [new_app_pkg](#new_app_pkg), to MEAO
6. MEAO retrieves the app package previously stored in the Database, using the _id
7. MEAO obtains the helm chart and the app descriptor from the app package
8. MEAO validates the app descriptor
9. MEAO translates the app descriptor into a VNF descriptor and a NS descriptor
10. MEAO compresses the vnfd + artifcats + nsd
11. MEAO sends the vnfd to OSM, and receives a [vnf_package_id](#document-fields)
12. MEAO sends the nsd to OSM, and receives a [nsd_package_id](#document-fields)
13. MEAO stores [vnf_package_id](#document-fields) and the [nsd_package_id](#document-fields) in the Database
14. MEAO deletes vnfd and nsd from local storage
15. MEAO returns a response to OSS
16. OSS returns a response 


#### GET (List) 
1. OSS receives a GET request from CFS Portal
2. OSS extracts [document fields](#document-fields) from the database and list them, for every App package

### App Package/{app_pkg_id}

#### GET (Individual Package)
1. OSS receives a GET request from CFS Portal
2. OSS extracts the [document fields](#document-fields) using the app_pkg_id, from the database, and list them, for the requested App package


#### PUT
1. OSS receives a PUT request from the CFS Portal
2. OSS unpacks archive
3. OSS validates the app descriptor
3. OSS parses the app descriptor
4. OSS checks if the app_pkg_id is valid and exists in the Database  
5. OSS sends the app descriptor and the app_pkg_id through Kafka, on the topic [update_app_pkg](#update_app_pkg)
6. MEAO validates the app descriptor
7. MEAO retrieves the [vnf_package_id](#document-fields) and the [nsd_package_id](#document-fields) from the Database
8. MEAO converts the descriptor to an nsd and a vnfd
9. MEAO compresses and saves the vnfd and nsd in the local storage
9. MEAO sends a request to update the vnfd and nsd using OSM
10. MEAO receives the response from OSM, and deletes the files from local storage
11. MEAO returns a response to OSS
12. OSS receives the response from MEAO
13. OSS updates the Database with the new descriptor 
14. OSS returns a response


#### DELETE
1. OSS receives a DELETE request from the CFS Portal
2. OSS checks if the app_pkg_id is valid and exists in the Database
3. OSS sends the app_pkg_id through Kafka, on the topic [delete_app_pkg](#delete_app_pkg)
4. MEAO receives the app_pkg_id through Kafka, on the topic [delete_app_pkg](#delete_app_pkg)
5. MEAO uses the app_pkg_id to retrive the [vnf_package_id](#document-fields) and the [ns_package_id](#document-fields) from the Database
6. MEAO sends a request to delete the NS using OSM
7. MEAO updates the [ns_package_id](#document-fields) from the Database, setting it to None
8. MEAO sends a request to delete the VNF using OSM
9. MEAO updates the [vnf_package_id](#document-fields) from the Database, setting it to None
10. MEAO returns a response to OSS
11. OSS receives the response from MEAO
12. OSS updates the Database
13. OSS return the response

### App Package/{app_pkg_id}/instantiate

#### Instantiate
1. OSS receives a POST request from the CFS Portal
2. OSS checks if app_pkg_id exists in the DB
3. OSS sends the app_pkg_id through Kafka, on the topic instantiate_app_pkg
4. MEAO requests the app pkg from the DB
5. DB returns the app pkg
6. MEAO gets ns_pkg_id from the app pkg
7. MEAO sends request to OSM to create the NS instance with ns_pkg_id
8. OSM returns response
9. MEAO returns response
10. OSS returns response

#### Terminate

1. DELETE request
2. OSS checks if appi_id is valid
3. OSS sends appi_id through Kafka, on topic terminate_app_pkg
4. MEAO validates appi_id
5. MEAO requests OSM to delete the NS instance with the appi_id
6. OSM returns response
7. MEAO returns response
8. OSS returns response




## [Demonstration App](https://github.com/PedroDSFerreira/video-object-detection)

![Example Image](./images/demo_app.png)

### Purpose:
This application is used to showcase the onboarding of MEC App.

### Overview:
**Object detection client-server application:**
Server receives a video stream from the client. Using YOLOv3, the server processes the video stream and returns the number of detected objects and their position for each frame.

### Infrastructure:
The application operates within a Containerized Network Function (CNF), which is a form of Virtualized Network Function (VNF). In this setup, the virtualized hardware runs inside a container on its machine.

**Deployment:**
The Demo App is containerized using Docker and is managed by Kubernetes, a container orchestration platform. This setup ensures scalability, reliability, and efficient resource utilization.

### More Information:
For detailed documentation and access to the codebase, visit the [GitHub repository](https://github.com/PedroDSFerreira/video-object-detection).