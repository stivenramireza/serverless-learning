const dynamoDB = require('../../utils/dynamo');
const { USERS_TABLE } = require('../../utils/constants');

const handler = async (event, context) => {
    const userId = event.pathParameters.id;
    const body = JSON.parse(event.body);

    const params = {
        TableName: USERS_TABLE,
        Key: { pk: userId },
        UpdateExpression: 'set #name = :name',
        ExpressionAttributeNames:  {'#name': 'name' },
        ExpressionAttributeValues: {':name': body.name },
        ReturnValues: 'ALL_NEW'
    };

    return dynamoDB.update(params).promise().then(res => {
        return {
            "statusCode": 200,
            "body": JSON.stringify(res.Attributes)
        }
    })
}

module.exports = {
    handler
}
