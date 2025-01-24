module "networking" {
  source = "../../modules/networking"
}

module "compute" {
  source = "../../modules/compute"
}

module "storage" {
  source = "../../modules/storage"
}

module "security" {
  source = "../../modules/security"
}
