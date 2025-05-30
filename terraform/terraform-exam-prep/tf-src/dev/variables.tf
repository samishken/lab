variable "instance_type" {
  description = "The size of the instance"
  type    = string
  default = "t3.micro"
  sensitive = false # Set to true if the variable contains sensitive data
  validation {
    condition     = can(regex("^(t[2-3]\\.(micro|small|medium|large|xlarge))$", var.instance_type))
    error_message = "The instance_type must be in the format t2.micro, t2.small, t3.micro, etc. type"
  }
}
