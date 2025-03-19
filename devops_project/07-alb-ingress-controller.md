# How to setup alb add on

##  Setup OIDC Connector
- OIDC: iam oidc provider
- ALB controller pod is deployed in eks cluster. ALB controller is a pod running within eks cluster.  It creates elastic loadbalancer which is out of eks cluster. pods inside kubernetes cluster have service account.
#### How can a pod with Service Account within eks cluster can create a resource out of kubernetes cluster?
- - It is only possible if the service account is binded to the IAM role.
- - `IAM OIDC provider` is used to bind the pod from inside the cluster to a resource outside of the cluster.
- - For pod inside the cluster, service account
- - Step 1) For ELB, Create IAM role and assign policy with required permissions to the IAM role.
- - Step 2) Bind the two using IAM OIDC provider

#### Install IAM OIDC provider
#### commands to configure (create) IAM OIDC provider 

```
export cluster_name=demo-cluster
```

```
oidc_id=$(aws eks describe-cluster --name $cluster_name --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5) 
```
```
echo $oidc_id
```
## Check if there is an IAM OIDC provider configured already

- aws iam list-open-id-connect-providers | grep $oidc_id | cut -d "/" -f4\n 

If not, run the below command
- Add IAM Oidc provider to your cluster.
```
eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve
```

## Download IAM policy
- Get `iam_policy.json` file needed to create IAM policy. Update version when necessary.
```
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.12.0/docs/install/iam_policy.json
```

- Create IAM Policy using `iam_policy.json`

```
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json
```

Create IAM Role

```
eksctl create iamserviceaccount \
  --cluster=demo-otel-microservices \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name AmazonEKSLoadBalancerControllerRole \
  --attach-policy-arn=arn:aws:iam::225989363866:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve
```

## Deploy ALB controller

Add helm repo

```
helm repo add eks https://aws.github.io/eks-charts
```

Update the repo

```
helm repo update eks
```

Install

```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
-n kube-system \
--set clusterName=<your-cluster-name> \
--set serviceAccount.create=false \
--set serviceAccount.name=aws-load-balancer-controller \ 
--set region=<region> \
--set vpcId=<your-vpc-id>
```

Verify that the deployments are running.

```
kubectl get deployment -n kube-system aws-load-balancer-controller
```

You might face the issue, unable to see the loadbalancer address while giving k get ing -n robot-shop at the end. To avoid this your **AWSLoadBalancerControllerIAMPolicy** should have the required permissions for elasticloadbalancing:DescribeListenerAttributes.

## Run the following command to retrieve the policy details and look for **elasticloadbalancing:DescribeListenerAttributes** in the policy document.
```
aws iam get-policy-version \
    --policy-arn arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
    --version-id $(aws iam get-policy --policy-arn arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy --query 'Policy.DefaultVersionId' --output text)
```

If the required permission is missing, update the policy to include it
## Download the current policy
```
aws iam get-policy-version \
    --policy-arn arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
    --version-id $(aws iam get-policy --policy-arn arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy --query 'Policy.DefaultVersionId' --output text) \
    --query 'PolicyVersion.Document' --output json > policy.json
```
## Edit policy.json to add the missing permissions
```
{
  "Effect": "Allow",
  "Action": "elasticloadbalancing:DescribeListenerAttributes",
  "Resource": "*"
}
```
## Create a new policy version
```
aws iam create-policy-version \
    --policy-arn arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://policy.json \
    --set-as-default
```
