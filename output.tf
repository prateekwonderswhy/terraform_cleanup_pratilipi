# output "instance_ids" {
  
#   value       = data.aws_instances.batch-infra.ids

# }

output "asg_names" {
  
  value = data.aws_autoscaling_groups.asgs.names


}

