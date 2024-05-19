import axios from "axios";

const api = axios.create({
    baseURL: 'http://localhost:8080/oss/v1'
});

// App Package
export const getAppPkg = async () => {
    return await api.get('/app_pkgs');
}

export const newAppPkg = async (formData: FormData) => {
    return await api.post(
        '/app_pkgs',
        formData,
        {
            headers: {
                'Content-Type': 'multipart/form-data',
            }
        }
    );
}

export const deleteAppPkg = async (id: string) => {
    return await api.delete(`/app_pkgs/${id}`);
}

export const instantiateAppPkg = async (id: string, formData: FormData) => {
    return await api.post(
        `/app_pkgs/${id}/instantiate`,
        formData,
        { headers: { 'Content-Type': 'multipart/form-data' } }
    );
}

export const updateAppPkg = async (id: string, formData: FormData) => {
    return await api.patch(
        `/app_pkgs/${id}`,
        formData,
        { headers: { 'Content-Type': 'multipart/form-data' } }
    );
}

// App Instance
export const getAppI = async () => {
    return await api.get('/appis');
}

export const terminateAppI = async (id: string) => {
    return await api.delete(`/appis/${id}`);
}

// VIM
export const getVims = async () => {
    return await api.get('/vims');
}

export default api;