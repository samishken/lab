provider "vault" {
  address = "http://3.93.200.239:8200"
  skip_child_token = true

  auth_login {
    path = "auth/approle/login"

    parameters = {
      role_id = "7b82b041-7760-82a7-132c-424dc6e83e02"
      secret_id = "3f061c4f-0cb2-86cd-518b-44662f4f2581"
    }
  }
}

# run the below to get role-id and secret-id informations
# vault read auth/approle/role/terraform/role-id
# vault write -f auth/approle/role/terraform/secret-id
data "vault_kv_secret_v2" "example" {
  mount = "kv" // change it according to your mount
  name  = "test-secret" // change it according to your secret
}

resource "aws_instance" "vault_instance" {
  ami           = "ami-04b4f1a9cf54c11d0"
  instance_type = "t2.micro"

  tags = {
    Name = "vault-test"
    Secret = data.vault_kv_secret_v2.example.data["username"]
  }
}
