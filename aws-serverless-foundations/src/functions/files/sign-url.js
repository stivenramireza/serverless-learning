const s3 = require('../../utils/s3');

const handler = async (event, context) => {
    const fileName = event.queryStringParameters.filename;

    const signedUrl = await s3.getSignedUrlPromise('putObject', {
        Key: `upload/${fileName}`,
        Bucket: process.env.BUCKET,
        Expires: 300
    });

    return {
        statusCode: 200,
        body: JSON.stringify({ signedUrl })
    };
}

module.exports = {
    handler
}
