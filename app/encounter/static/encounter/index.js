const getMonsterList = (URL) => {
    $.ajax({
        url: URL,
        success: (result) => returnMonsterList(result)
    });
}

const returnMonsterList = (data) => {
    console.log(data);
}