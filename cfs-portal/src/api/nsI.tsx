import axios from "axios";

export const getNsI = async () => {
    await axios.get(
        'http://localhost:3000/api/nsI' // TODO: replace with actual API
    ).then(res => {
        console.log(res.data);
    }).catch(err => {
        console.log(err);
    });
};