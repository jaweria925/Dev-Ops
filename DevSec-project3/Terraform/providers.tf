terraform {
  backend "s3" {
    bucket = "terraform-s3-bucket01"
    key = "infra/state.tfstate"
    region = "us-east-1"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.3"
    }
  }
}
