const { DynamoDB } = require('aws-sdk');

let dynamoDBClientParams = {};

if (process.env.IS_OFFLINE) {
    dynamoDBClientParams = {
        region: 'localhost',
        endpoint: 'http://localhost:8000',
        accessKeyId: 'DEFAULT_ACCESS_KEY',  // needed if you don't have aws credentials at all in env
        secretAccessKey: 'DEFAULT_SECRET' // needed if you don't have aws credentials at all in env
    };
}

const dynamoDB = new DynamoDB.DocumentClient(dynamoDBClientParams);

module.exports = dynamoDB;
