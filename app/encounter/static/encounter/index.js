/**
 * Provides HTTP GET functionality for api endpoints.
 * @param {string} URL - The url of the api endpoint desired
 * @param {Object} handler - The function handler for the returned api data
 */
const getMonsterList = (URL, handler) => {
    $.ajax({
        url: URL,
        success: (result) => handler(result)
    });
}

const returnMonsterList = (data) => {
    console.log(data);
}