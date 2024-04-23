# Getting Started

## Preparation:

1. **Download Repository:**
    ```bash
    git clone https://github.com/PedroDSFerreira/osm-mec.git
    ```

2. **Change .env-sample file:**
    - **Rename it to .env**
    - **Change OSM_HOSTNAME variable to the ip of the machine where OSM is installed**
3. **Launch Containers:**
    - **Create Image:**
        ```bash
        cd /path-to-repository/osm-mec
        docker-compose build
        ```
    - **Run the Whole Set of Containers:**
        ```bash
        docker-compose up
        ```

4. **Access CFS Portal:**
    - **Open a web browser of your choice.**
   
    - **Enter the following address in the browser's address bar:**
   
        ```
        http://localhost:3000
        ```

![Example Image](./images/dashboard.png)


## CFS Portal Functionalities

## [API Documentation](https://documenter.getpostman.com/view/22366745/2sA358cQVv)

## API Requests

**This section presents the Postman Workspace of the API. It consists of 2 packages:**

- OSM, which are a set of endpoints from Open Source Mano
- OSS, which are the endpoints developed to interact with the MEAO

### How to test the endpoints

1. Enter on the Workspace (id: 22366745-c79bf165-8176-42c9-a82d-e82b9c9ba285)
2. Go to OSM/Token package
3. Open POST request-token endpoint and send it. 
It returns a token used on the other endpoints for authentication
4. Select a package of your choice until you find the desired endpoint
5. Select it and send it. The body of the request has the necessary fields.

