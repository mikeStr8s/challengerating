const loadPage = (endpoints) => {
    getApiEndpoint(endpoints['monster_list'], getMonsterList);
}

/**
 * Provides HTTP GET functionality for api endpoints.
 * @param {string} URL - The url of the api endpoint desired
 * @param {Object} handler - The function handler for the returned api data
 */
const getApiEndpoint = (URL, handler) => {
    $.ajax({
        url: URL,
        success: (result) => handler(result)
    });
}

const getMonsterList = (data) => {
    console.log(data);
}

const returnMonsterList = (data) => {
    console.log(data);
}