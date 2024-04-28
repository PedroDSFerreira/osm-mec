# API

## [API Documentation](https://documenter.getpostman.com/view/22366745/2sA358cQVv)

## API Requests

**This section presents the Postman Workspace of the API. It consists of 2 packages:**

- OSM, which are a set of endpoints from Open Source Mano
- OSS, which are the endpoints developed to interact with the MEAO

### How to test the endpoints

1. Enter on the Workspace (id: 22366745-c79bf165-8176-42c9-a82d-e82b9c9ba285)
2. You must configure the global variable **osm-url** to the ip where OSM is installed
3. Same task for **oss-url**
4. Go to OSM/Token package
5. Open POST request-token endpoint and send it. 
It returns a token used on the other endpoints for authentication
6. You must start executing the POST endpoints because most of them return ids which are associated with variables (Ex: **vnf-pkg-id** is associated with the POST of a VNF package)
7. Select it and send it. The body of the request has the necessary fields.
