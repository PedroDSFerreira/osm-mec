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

export const terminateAppI = async (id: string) => {
    return await axios.delete(
        `http://localhost:8080/oss/v1/appis/${id}`
    ).catch(err => {
        return Promise.reject(err);
    });
}