# Create and Onboard MEC App

## Requirements
- OSM
- K3s
- Helm

## 
### Create and Containerize App
**replace
1. Create the application
2. **[Containerize the app](https://docs.docker.com/get-started/02_our_app/)**
3. Push the container image to a repository, such as the **[Docker Hub](https://docs.docker.com/get-started/04_sharing_app/)** or **[Github Packages](https://docs.github.com/en/actions/publishing-packages/publishing-docker-images)**
4. **[Create kubernetes cluster](https://docs.k3s.io/quick-start)**
5. **[Add cluster to OSM as a OSM Network Service](https://osm.etsi.org/docs/user-guide/latest/15-k8s-installation.html#installation-method-1-osm-kubernetes-cluster-from-an-osm-network-service)**
6. Create Helm Chart:
```bash
helm create <chart-name>
```

![Example Image](./images/create_helm.png)
And then package it:

```bash
helm package <path-to-chart>
```

![Example Image](./images/package_helm.png)

7. Create MEC App Descriptor
8. Create an archive with app descriptor and helm chart
9. Onboard app using CFS Portal












