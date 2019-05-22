## Amazon Textract Code Samples

This repository contains example code snippets showing how Amazon Textract and other AWS services can be used to get insights from documents.

## Usage

python3 01-detect-text-local.py

For examples that use S3 bucket, upload sample images to an S3 bucket and update variable "s3BucketName" in the example before running it.

## Python Samples

| Argument  | Description |
  | ------------- | ------------- |
  | [01-detect-text-local.py](./python/01-detect-text-local.py)  | Example showing processing a document on local machine. |
  | [02-detect-text-s3.py](./python/02-detect-text-s3.py)  | Example showing processing a document in Amazon S3 bucket. |
  | [03-reading-order.py](./python/03-reading-order.py)  | Example showing printing document in reading order.  |
  | [04-nlp-comprehend.py](./python/04-nlp-comprehend.py) | Example showing detecting entities and sentiment. |
  | [05-nlp-medical.py](./python/05-nlp-medical.py)  | Example showing detecting medical entities. |
  | [06-translate.py](./python/06-translate.py)  | Example showing translation of documents. |
  | [07-search.py](./python/07-search.py)  | Example showing document indexing in Elasticsearch. |
  | [08-forms.py](./python/08-forms.py)  | Example showing form (key/value) processing. |
  | [09-forms-redaction.py](./python/09-forms-redaction.py)  | Example showing redacting information in document. |
  | [10-tables.py](./python/10-tables.py)  | Example showing table processing. |
  | [11-tables-expense.py](./python/11-tables-expense.py)  | Example showing validation of table data. |
  | [12-pdf-text.py](./python/12-pdf-text.py)  | Example showing PDF document processing. |

## License Summary

This sample code is made available under the MIT-0 license. See the LICENSE file.
