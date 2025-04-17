resource "github_repository" "mtc_repo" {
  name        = "mtc-repo-test"
  description = "Code for MTC-test"
  visibility  = "private"
  auto_init   = true
}

# # add readme file to the Github repo
resource "github_repository_file" "readme" {
  repository          = github_repository.mtc_repo.name    # this ensures...depends on github_repository.mtc_repo creation
  branch              = "main"
  file                = "README.md"
  content             = "# This repository is for infra developers"
  overwrite_on_create = true
}


# # to create rand number and attache to github repo name
# resource "random_id" "random" {
#   byte_length = 2
#   count       = 2
# }

# # Create Github repo
# resource "github_repository" "mtc_repo" {
#   count       = 2
#   name        = "mtc-repo-${random_id.random[count.index].dec}"
#   description = "Code for MTC"
#   visibility  = "private"
#   auto_init   = true
# }


# # add readme to the Github repo
# resource "github_repository_file" "readme" {
#   count               = 2
#   repository          = github_repository.mtc_repo[count.index].name
#   branch              = "main"
#   file                = "README.md"
#   content             = "# This repository is for infra developers"
#   overwrite_on_create = true
# }

# # # add index.html file into github repo
# resource "github_repository_file" "index_html" {
#   count               = 2
#   repository          = github_repository.mtc_repo[count.index].name
#   branch              = "main"
#   file                = "index.html"
#   content             = "Hellow Terraform!"
#   overwrite_on_create = true
# }

# # add index.html file into github repo
# resource "github_repository_file" "notes_folder" {
#   count               = 2
#   repository          = github_repository.mtc_repo[count.index].name
#   branch              = "main"
#   file                = "notes/test.txt"
#   content             = "Test creation of folder!"
#   overwrite_on_create = true
# }

# # Output
# output "repo-names" {
#   value = github_repository.mtc_repo[*].name
#   description = "Repository Names"
# }