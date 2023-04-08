const dynamoDB = require('../../utils/dynamo');
const { USERS_TABLE } = require('../../utils/constants');

const handler = async(event, context) => {
    const body = event.Records[0].body;
    const userId = JSON.parse(body).id;

    const params = {
        TableName: USERS_TABLE,
        Key: { pk: userId },
        UpdateExpression: "ADD likes :inc",
        ExpressionAttributeValues: {
            ':inc': 1
        },
        ReturnValues: 'ALL_NEW'
    }

    const result = await dynamoDB.update(params).promise();
    
    await sleep(4000);
    console.log(result);
}

const sleep = (ms) => {
    return new Promise(resolve => {
        setTimeout(resolve, ms);
    });
}

module.exports = {
    handler
}
