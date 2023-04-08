const { S3 } = require('aws-sdk');

const s3 = new S3({ signatureVersion: 'v4' });

module.exports = s3;
