terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0" # it will automatically chooses the latest 6 something version
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  owner = "samishken"
}
