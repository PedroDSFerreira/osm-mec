import axios from 'axios';

export const getNsPkg = async () => {
    await axios.get(
        'http://localhost:8080/api/v1/nsds'
    ).then(res => {
        console.log(res.data);
    }).catch(err => {
        console.log(err);
    });
};

