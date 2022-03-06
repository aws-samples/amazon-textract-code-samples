import boto3
import time


def start_job(s3_bucket_name, object_name):
    response = None
    client = boto3.client('textract')
    response = client.start_document_text_detection(
        DocumentLocation={
            'S3Object': {
                'Bucket': s3_bucket_name,
                'Name': object_name
            }})

    return response["JobId"]


def is_job_complete(job_id):
    time.sleep(5)
    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=job_id)
    status = response["JobStatus"]
    print("Job status: {}".format(status))

    while(status == "IN_PROGRESS"):
        time.sleep(5)
        response = client.get_document_text_detection(JobId=job_id)
        status = response["JobStatus"]
        print("Job status: {}".format(status))

    return status


def get_job_results(job_id):
    pages = []
    time.sleep(5)
    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=job_id)
    pages.append(response)
    print("Resultset page received: {}".format(len(pages)))
    next_token = None
    if 'NextToken' in response:
        next_token = response['NextToken']

    while next_token:
        time.sleep(5)
        response = client.\
            get_document_text_detection(JobId=job_id, NextToken=next_token)
        pages.append(response)
        print("Resultset page received: {}".format(len(pages)))
        next_token = None
        if('NextToken' in response):
            next_token = response['NextToken']

    return pages


if __name__ == "__main__":
    # Document
    s3BucketName = "ki-textract-demo-docs"
    documentName = "Amazon-Textract-Pdf.pdf"

    jobId = start_job(s3BucketName, documentName)
    print("Started job with id: {}".format(jobId))
    if(is_job_complete(jobId)):
        response = get_job_results(jobId)

    # print(response)

    # Print detected text
    for result_page in response:
        for item in result_page["Blocks"]:
            if item["BlockType"] == "LINE":
                print('\033[94m' + item["Text"] + '\033[0m')
