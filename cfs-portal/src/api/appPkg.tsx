import axios, { AxiosResponse } from "axios";

const API_URL = 'http://localhost:8080/api/v1/vnf_pkgs';

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
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        }
    );
};

export const deleteAppPkg = async (id: string) => {
    return await axios.delete(`${API_URL}/${id}`);
}