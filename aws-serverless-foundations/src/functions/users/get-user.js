const dynamoDB = require('../../utils/dynamo');
const { USERS_TABLE } = require('../../utils/constants');

const handler = async (event, context) => {
    const userId = event.pathParameters.id;

    const params = {
       ExpressionAttributeValues: {':pk': userId},
       KeyConditionExpression: 'pk = :pk',
       TableName: USERS_TABLE
    };

    const result = await dynamoDB.query(params).promise();
    const users = result.Items;

    if (!users.length) {
        return {
            "statusCode": 404,
            "body": JSON.stringify({ message: 'User not found'})
        }
    }

    return {
        "statusCode": 200,
        "body": JSON.stringify(users[0])
    }
}

module.exports = {
    handler
}
