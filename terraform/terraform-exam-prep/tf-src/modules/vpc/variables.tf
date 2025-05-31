variable "cidr" {
  type        = string
  description = "CIDR block for the VPC"
}




variable "azs" { type = list(string) }
variable "private_subnets" { type = list(string) }
variable "public_subnets" { type = list(string) }
variable "tags" { type = map(string) }

