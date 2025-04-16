Project: Automate Security scanning and Deployment for IaC

Usecase: Create CI/CD pipeline for Terraform  infrastructure with built-in securtiy scanning and code validation

Technology Used:
1. Aws S3
2. Terraform
3. Gitlab CI/CD
4. TF Sec


Project Description:

1. Create s3 bucket and configure Terraform to use bucket for storing Terraform State.
2. Create new gitlab CI pipeline for Terraform Infrastructure That:

        a. Initialize Terraform and build a Plan Artifact
        b. Validate Terraform Configuration and Syntax
        c. Run TFSec Security scan on Terraform code and produce scan result artifact.
        d. Deploy the terraform code to AWs/Azure.



