import axios, { AxiosResponse } from "axios";

export const getAppPkg = async () => {
    return await axios.get(
        'http://localhost:8080/api/v1/vnf_pkgs'
    ).then(res => {
        return res.data;
    }).catch(err => {
        return Promise.reject(err);
    });
};

export const newAppPkg = async (formData: FormData): Promise<AxiosResponse> => {
    try {
        const response = await axios.post(
            'http://localhost:8080/api/v1/vnf_pkgs',
            formData,
            {
                headers: {
                    // 'Content-Type': 'multipart/form-data',
                    // 'Authorization': `Bearer ${localStorage.getItem('token')}`
                    'Content-Type': 'application/zip',
                    'Authorization': 'eVNkTu8RLQDWYA8GfnjzsGMlFsN3kY00'
                }
            }
        );
        return response;
    } catch (error) {
        return Promise.reject(error);
    }
};