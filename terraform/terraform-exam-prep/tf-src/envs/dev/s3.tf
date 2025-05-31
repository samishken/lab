resource "random_id" "bucket_suffix" {
  count       = 3
  byte_length = 4
}

resource "aws_s3_bucket" "my_bucket" {
  count      = 3
  bucket     = "${local.environment}-${local.project_name}-${random_id.bucket_suffix[count.index].hex}"
  depends_on = [aws_instance.my_server]

  tags = {
    Terraform   = "true"
    Environment = "${local.environment}"
    Project     = "${local.project_name}"
  }
}