const { randomUUID } = require('crypto');

const dynamoDB = require('../../utils/dynamo');
const { USERS_TABLE } = require('../../utils/constants');

const handler = async (event, context) => {
    const userId = randomUUID();

    let userBody = JSON.parse(event.body);
    userBody.pk = userId;

    const params = {
       TableName: USERS_TABLE,
       Item: userBody
    };

    console.log(params.Item);

    return dynamoDB.put(params).promise().then(res => {
        return {
            "statusCode": 200,
            "body": JSON.stringify(params.Item)
        }
    })
}

module.exports = {
    handler
}
