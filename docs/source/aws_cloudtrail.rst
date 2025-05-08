AWS CloudTrail Logs
==================

For tracking actions taken within your AWS environment.

1. Source
---------

**Name:** AWS CloudTrail

**Description:**  
AWS CloudTrail logs all API calls made within your AWS environment, including those made via the AWS Management Console, AWS SDKs, command-line tools, and other AWS services.

**Log Location:**

* Default location: Logs are stored in an Amazon S3 bucket specified during setup.
* Custom locations can be configured via CloudTrail settings.

2. Purpose
----------

**Primary Purpose:**  
CloudTrail logs provide a detailed record of all API activity within your AWS account, helping you monitor resource changes, track user actions, and investigate security incidents.

**Security Relevance:**  
CloudTrail logs are critical for detecting unauthorized access, suspicious API calls, and potential security breaches. They also help in identifying misconfigurations and ensuring compliance with regulatory standards.

3. Log Format
-------------

**Example Log Entry (JSON Format):**

::

   {
      "eventVersion": "1.05",
      "userIdentity": {
         "type": "IAMUser",
         "principalId": "AIDAEXAMPLEID",
         "arn": "arn:aws:iam::123456789012:user/ExampleUser",
         "accountId": "123456789012",
         "accessKeyId": "ASIAEXAMPLEKEY",
         "userName": "ExampleUser"
      },
      "eventTime": "2023-10-10T13:55:36Z",
      "eventSource": "ec2.amazonaws.com",
      "eventName": "RunInstances",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.168.1.10",
      "userAgent": "aws-sdk-java/1.11.15 Linux/4.4.0-116-generic",
      "requestParameters": {
         "instances": {
            "instanceType": "t2.micro",
            "amiId": "ami-12345678"
         }
      },
      "responseElements": {
         "reservationId": "r-0123456789abcdef0"
      },
      "errorCode": null,
      "errorMessage": null,
      "readOnly": false,
      "resources": [
         {
            "arn": "arn:aws:ec2:us-west-2:123456789012:instance/i-1234567890abcdef0",
            "accountId": "123456789012",
            "type": "AWS::EC2::Instance"
         }
      ]
   }

**Field Breakdown:**

.. list-table:: 
   :header-rows: 1
   :widths: 20 80

   * - Field
     - Description
   * - ``eventVersion``
     - The version of the log event format.
   * - ``userIdentity``
     - Information about the user who made the API call (e.g., IAM user, role).
   * - ``eventTime``
     - The timestamp when the API call was made.
   * - ``eventSource``
     - The AWS service that received the API call (e.g., ec2.amazonaws.com).
   * - ``eventName``
     - The name of the API action performed (e.g., RunInstances).
   * - ``awsRegion``
     - The AWS region where the API call was made.
   * - ``sourceIPAddress``
     - The IP address of the client making the API call.
   * - ``userAgent``
     - The user agent string indicating the tool or application used (e.g., AWS CLI, console).
   * - ``requestParameters``
     - The parameters provided in the API request (e.g., instance type, bucket name).
   * - ``responseElements``
     - The response returned by the API (if any).
   * - ``errorCode``
     - The error code if the API call failed (e.g., AccessDenied).
   * - ``errorMessage``
     - The error message if the API call failed.
   * - ``readOnly``
     - Indicates whether the API call was read-only (true) or modified resources (false).
   * - ``resources``
     - Details about the AWS resources affected by the API call (e.g., ARN, resource type).

