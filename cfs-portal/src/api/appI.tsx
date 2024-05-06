import axios from "axios";

export const getAppI = async () => {
    return await axios.get(
        'http://localhost:8080/oss/v1/appis'
    ).then(res => {
        return res.data;
    }).catch(err => {
        return Promise.reject(err);
    });
};