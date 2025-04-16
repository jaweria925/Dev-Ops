data "aws_vpc" "main" {
  depends_on = [module.vpc]
  filter {
    name   = "tag:Name"
    values = ["main"]
  }
}

data "aws_security_group" "main" {
  depends_on = [aws_security_group.main]
  vpc_id     = data.aws_vpc.main.id

  filter {
    name   = "tag:Name"
    values = ["main"]
  }
}

data "aws_security_group" "app-server" {
  depends_on = [aws_security_group.app-server]
  vpc_id     = data.aws_vpc.main.id

  filter {
    name   = "tag:Name"
    values = ["app-server"]
  }
}

data "aws_iam_instance_profile" "app-server-role" {
  depends_on = [aws_iam_instance_profile.app-server-role]
  name       = "app-server-role"
}

data "aws_iam_instance_profile" "gitlab-runner-role" {
  depends_on = [aws_iam_instance_profile.gitlab-runner-role]
  name       = "gitlab-runner-role"
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ami-084568db4383264d4"]
  }

}