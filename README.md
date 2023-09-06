# Welcome_app
### Technology Details
You will be using the following technologies and platforms to set up a DevOps environment.

1.Azure
Azure will be used to host the application, cloud infrastructure, and any other services we may need to ensure the Uber app is deployed properly. <br />
2.GitHub
To store the application and infrastructure/automation code <br />
3.Python
Python will be used for the welcome-app (it is written in Python) and some automation efforts that aren't in Terraform. <br />
4.Terraform
Create an Azure ACR repository with Terraform <br />
Create an AKS cluster
5.Docker
Create a Docker image 
Store the Docker image in Azure ACR <br />
6.Kubernetes
To run the Docker image that's created for the containerized Uber app. Kubernetes, in this case, AKS, will be used to orchestrate the container. <br />
7.CI/CD
Use GitHub Action to create an AKS cluster

## Prerequisites
1.Create Storage Account for Terraform State file - When deploying Terraform there is a requirement that it must store a state file; this file is used by Terraform to map Azure Resources to your configuration that you want to deploy, keeps track of meta data and can also assist with improving performance for larger Azure Resource deployments.
2.Create Azure AD Group for AKS Admins - The Azure AD Group will be used for AKS cluster access
In this scenario, the Terraform State file will be stored in remote state location of an Azure Storage Account.

3.Terraform - The purpose of the Terraform section is to create all of the Azure cloud services you'll need from an environment/infrastructure perspective to run the Welcome-app application

- Create ACR
- Create VNET
- Create Log Analytics
- Create AKS Cluster with relevant IAM roles
  4.Docker - The purpose of the Docker section is to create a Docker image from the app that the organization is running on-prem (the uber app), containerize it, and store the container inside of a container repository. For the container repo, you'll use Azure ECR.
 - Create The Docker Image
  - Log Into Azure ACR Repository
5. Kubernetes - The purpose of the Kubernetes section is to connect to AKS locally and to write the Kubernetes manifest to deploy the Welcome-app.
    Connect To ACR From The Terminal
    Create A Kubernetes Manifest
6. Deploy Welcome App into Kubernetes
7. CI/CD
  -Use GitHub Action to create an AKS cluster

### Create Docker image build and deployment to the AKS cluster
Here we create an the image build and pushing image to the acr registry anddeploy to the aks  using GitHub Actions. The code can be found here

Secrets
Prior to running the pipeline, you'll need to set up authentication from GitHub to Azure. To do that, you'll setup an Azure Service Principal.

You'll need both the clientID of the service principal and secret that was created.

Please Note: The Service Principal needs IAM permission to the subscription/resource group to where the Azure resources are deployed. In this example, I gave contributor access to the subscription. See examples on how to assign an Azure Role here

You'll be adding 4 secrets into the GitHub repository. These four secrets will allow you to connect to Azure from GitHub Actions.

In the code repository, go to Settings --> Secrets
Add in four secrets:
${{ secrets.AZURE_CREDENTIALS }}
${{ secrets.REGISTRY_LOGIN_SERVER}}
${{ secrets.REGISTRY_PASSWORD}}
${{ secrets.REGISTRY_USERNAME}}

Save the secrets.
Pipeline
Now that the secrets are created, it's time to create the pipeline.

Under the GitHub repository, click on the Actions tab
You will see a workflow already called CI
Select CI workflow and then select Run workflow from main branch
The pipeline does a few things:

On line 4, you'll see workflow_dispatch, which means the pipeline won't automatically run unless you kick it off. You can of course change this to have the pipeline automatically run if you, for example, push code to the dev or main branch.
The code is checked-out
- Authentication occurs to Azure
- Acr Login
- Build and push image to ACR
kubectl create secret docker-registry acrsecret --docker-server=testacrforevaluvation.azurecr.io --docker-username=testacrforevaluvation --docker-password=aiTXr/xB19HQpkWp9oNlZ5464hR+ivAe5LW7qzT+59+ACRBtm92L <br />
Secret is created to pull the image from the acr
- Deploys application
![image](https://github.com/dhanyapvarghese/Welcome_app/assets/43697021/41b98400-d551-43d6-a152-9af818781413)




