locals {
  project_name = "terraform-exam-prep"
}

locals {
  environment = "dev" # Change to "prod", "staging", etc. as needed
}

locals {
  module_path = "${path.module}/../../modules/vpc"
}

output "resolved_path" {
  value = local.module_path
}