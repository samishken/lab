output "instance_ip_address" {
  description = "The public IP address of the instance"
  value       = values(aws_instance.my_server)[*].public_ip
}

# output "s3_bucket_name" {
#   description = "The name of the S3 bucket"
#   value       = aws_s3_bucket.my_bucket[*].bucket
# }

output "s3_bucket_names" {
  description = "List of S3 bucket names"
  value       = [for b in aws_s3_bucket.my_bucket : b.bucket]
}