import axios from "axios";

export const getVims = async () => {
    return await axios.get(
        'http://localhost:8080/oss/v1/vims'
    ).catch(err => {
        return Promise.reject(err);
    });
};