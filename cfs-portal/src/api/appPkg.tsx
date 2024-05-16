import axios from "axios";

const API_URL = 'http://localhost:8080/oss/v1/app_pkgs';

export const getAppPkg = async () => {
    return await axios.get(API_URL);
};

export const newAppPkg = async (formData: FormData) => {
    return await axios.post(
        API_URL,
        formData,
        {
            headers: {
                'Content-Type': 'multipart/form-data',
            }
        }
    );
};

export const deleteAppPkg = async (id: string) => {
    return await axios.delete(`${API_URL}/${id}`);
}

export const instantiateAppPkg = async (id: string, formData: FormData) => {
    return await axios.post(
        `${API_URL}/${id}/instantiate`,
        formData,
        {
            headers: {
                'Content-Type': 'multipart/form-data',
            }
        }
    );
}

export const updateAppPkg = async (id: string, formData: FormData) => {
    return await axios.patch(
        `${API_URL}/${id}`,
        formData,
        {
            headers: {
                'Content-Type': 'multipart/form-data',
            }
        }
    );
}