# Drift detection ('terraform refresh' to update tf state file)
- create CRON job to detect terraform drift
# S: someone changed workload configuration manually
# T: create automated solution 
# A: 
- Implemented strickt aws IAM policies so that people can not log in
- Setup Audit logs; In audit implement automation to detect when someone makes changes to resources created by Terraform. 
- Verify is resouce is created by terraform using lambda functions.
- lambda function checks if there's any change managed by terraform and manual changes made by IAM user or terraform role. 
- If change made to terraform managed resource by terraform role no issue, 
- if change made to terraform managed resource it made by IAM user... this will go to audit logs and
- send out notification to team members.
# R: