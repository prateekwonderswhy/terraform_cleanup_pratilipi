data "aws_instances" "batch-infra" {

    instance_tags = {
      "Name" = "batch-infra"
    }

    filter {
    name   = "instance-type"
    values = ["t2.micro"]
  }   

}

data "aws_autoscaling_groups" "asgs" {
  
}
