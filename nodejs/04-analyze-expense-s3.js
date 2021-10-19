/*Example showing analyzing expense with document on AWS S3 bucket.*/ 

const aws = require('aws-sdk');
/*Initializing Textract from AWS SDK JS*/
const textract = new aws.Textract({ apiVersion: "2018-06-27" });
const s3BucketName = "ki-textract-demo-docs"
const documentName = "receipt.jfif"

exports.handler = async (event, context) => {
    let textractParams = {
        Document: {
            S3Object: {
                Bucket: s3BucketName,
                Name: documentName,
            }
        },
    };
    try {
        let response = await textract.analyzeExpense(params).promise();
        console.log(JSON.stringify(response),null,2)
    } catch (e) {
        console.log("Error: ", e)
    }
}