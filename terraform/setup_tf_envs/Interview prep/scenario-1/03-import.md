### Interview Questions
- Scenario 1.  Import cloudformation to terraform <br>

- Problems: Lots of resources to import. 
- --- how terraform know which resources to import?

#### Steps: <br>
##### 1st step: create Main.tf file to create "import block"
        ``` 
        provider "aws" {
            region = "us-east-1"
        }

        import {
            id = "i-abcd1234"
            to = aws_instance.example
        }
        ```
##### 2nd step (pull the resource we want to import to our local): 
- run `terraform plan -generate-config-out=generated_resouces.tf`
- This will generate a "generated_resouces.tf" file. copy the resource information and paste to main.tf file
- Inside the file we should see something like the below.  Resource name is from import block created in main.tf file.
```
        resource "aws_instance" "example" {
            name             = "test"
            instance_type    = "t2.micro"
        }
```

##### 3rd step (generate the statefile)
- run `terraform import aws_instance.example i-03468b51ccd2bf9e1`  
- The above will generate statefile

##### 4th step (terraform plan to validate)
- run `terraform plan` this should say no change.