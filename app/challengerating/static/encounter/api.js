const loadPage = (endpoints) => {
    getApiEndpoint(endpoints['monster_list'], getMonsterList);
}

/**
 * Provides HTTP GET functionality for api endpoints.
 * @param {string} URL - The url of the api endpoint desired
 * @param {Object} handler - The function handler for the returned api data
 */
const getApiEndpoint = (URL, handler) => {
    let data;
    $.ajax({
        url: URL,
        success: (result) => data = handler(result)
    });
    return data;
}

/**
 * Handler and cleanser for the list of monster data to be returned wholesale to the calling function for consumption.
 * @param {Array} data - List of initial monster objects, {name: <string:monster_name>, url: "/api_v1/monsters/<int:id>"}, to be used for traversal.
 */
const getMonsterList = (data) => {
    return data;
}

const returnMonsterList = (data) => {
    console.log(data);
}