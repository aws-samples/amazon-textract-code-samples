## Amazon Textract Code Samples

This repository contains example code snippets showing how Amazon Textract and other AWS services can be used to get insights from documents.

## Usage

python3 01-detect-text-local.py

For examples that use S3 bucket, upload sample images to an S3 bucket and update variable "s3BucketName" in the example before running it.

## Python Samples

| Argument                                                    | Description                                                |
| ----------------------------------------------------------- | ---------------------------------------------------------- |
| [01-detect-text-local.py](./python/01-detect-text-local.py) | Example showing processing a document on local machine.    |
| [02-detect-text-s3.py](./python/02-detect-text-s3.py)       | Example showing processing a document in Amazon S3 bucket. |
| [03-reading-order.py](./python/03-reading-order.py)         | Example showing printing document in reading order.        |
| [04-nlp-comprehend.py](./python/04-nlp-comprehend.py)       | Example showing detecting entities and sentiment.          |
| [05-nlp-medical.py](./python/05-nlp-medical.py)             | Example showing detecting medical entities.                |
| [06-translate.py](./python/06-translate.py)                 | Example showing translation of documents.                  |
| [07-search.py](./python/07-search.py)                       | Example showing document indexing in Elasticsearch.        |
| [08-forms.py](./python/08-forms.py)                         | Example showing form (key/value) processing.               |
| [09-forms-redaction.py](./python/09-forms-redaction.py)     | Example showing redacting information in document.         |
| [10-tables.py](./python/10-tables.py)                       | Example showing table processing.                          |
| [11-tables-expense.py](./python/11-tables-expense.py)       | Example showing validation of table data.                  |
| [12-pdf-text.py](./python/12-pdf-text.py)                   | Example showing PDF document processing.                   |

## .NET Usage

Go to `src-csharp` folder for .NET [Readme](src-csharp/readme.md)

```
Usage: dotnet run [--switch]
To run this console app, use the following valid switches one at a time:
                     --detect-text-local
                     --detect-text-s3
                     --pdf-text
                     --forms
                     --forms-redaction
                     --tables
                     --tables-expense
                     --reading-order
                     --nlp-comprehend
                     --nlp-medical
                     --translate
                     --search
      e.g. dotnet run --detect-text-s3
```

## .NET Samples

| Argument            | Description                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| --detect-text-local | Detect text from files read from your local machine                                                  |
| --detect-text-s3    | Detect text from files read from your Amazon S3 bucket                                               |
| --pdf-text          | Detect text from a pdf document                                                                      |
| --forms             | Extract forms from a document                                                                        |
| --forms-redaction   | Reads and then redacts specified regions in the document                                             |
| --tables            | Detect tables                                                                                        |
| --tables-expense    | Detects and computes on a table                                                                      |
| --reading-order     | Detects and keeps the reading order from a two-column document                                       |
| --nlp-comprehend    | Detects text and then apply Amazon Comprehend sentiment, entities, syntax, and key phrases detection |
| --nlp-medical       | Detects text and then apply Amazon Comprehend entities and PHI detection                             |
| --translate         | Translate to a different language                                                                    |
| --search            | Index detected text using Elastic Search                                                             |

## Other Resources

- [Large scale document processing with Amazon Textract - Reference Architecture](https://github.com/aws-samples/amazon-textract-serverless-large-scale-document-processing)
- [Batch processing tool](https://github.com/aws-samples/amazon-textract-textractor)
- [JSON response parser](https://github.com/aws-samples/amazon-textract-response-parser)

## License Summary

This sample code is made available under the MIT-0 license. See the LICENSE file.
