# Working with multiple providers



## Deploy resource in multiple region.
- To deploy resources in multiple region make use of alias in provider configuration.

provider aws {
    region = us-east-1
}

provier aws {
    region = ap-southeast-1
    alias = singapore
}

resource "aws_eip" "eip" {
    vpc = true
}

resource "aws_eip" "eip2" {
    vpc = true
    provider = aws.singapore
}

## Using muliple AWS accounts
- To make use of multiple AWS account to deploy resource make use of profile parameter in provider configuration. 
- Resource can use provider parameter using alias

## Terraform with AWS STS
- To make use of asume role in AWS to create resource. Use asume_role parameter in provider configuration.

provider aws {
    region = us-east-1
    asume_role = {
        role_arn = ARN_VALUE_FOR_ROLE_TO_ASUME
        session_name = SESSION_NAME
    }
}






## Sensetive parameter
- With organization managing their entire infrastructure in terraform, it is likely that you will see some sensitive information embedded in the code.
- When working with a field that contains information likely to be considered sensitive, it is best to set the Sensitive property on its schema to true.
- Setting the sensitive to "true" will prevent the field's value from showing up in the CLI output and in Terraform Cloud. It will not encrypt or obsecure the value in the state.


## HashiCorp Vault
- Allows organizations to securely store secrets like token, passwords, certificates, along with access management for protecting secrets.
- One of the common challenge nowadays in an organization is "Secrets Management".
- Secrets can include, database passwords, AWS access/screts keys, API token, encryption keys and others.
- Once Vault is intergrated with multiple backends, your life will become much easier and you can focus more on the right work.
- Major aspect releated to Access Management cab be taken over by Vault.

## Vault Provider
- The Vault provider allows Terraform to read from, write to, and configure HashiCorp Vault. 
- Interacting with Vault from Terraform causes any secrets that you read and write to be persisted in both Terraform's state file.

provider "vault" {
    address = "http://127.0.0.1:8200"
}

data "vault_generic_secret" "demo" {
    path = "secrets/db-creds"
}





## Depdendency Lock File
- Provider Plugins and Terraform are managed independently and have different release cycle.
- If there is a requirement to use newer or downgrade a provider, can override that behaviour by adding the -uprade option when you run terraform init. in which case Terraform will disregard the existing selections.
- When installing a particular provider for the first time. Terraform will pre-populate the hashes values with any checksums that are covered by the provider developer's cyrptographic signature, which usually covers all the available packages for that provider version across all supported platform.
- At present, the dependency lock file tracks only provider dependencies. 
- Terraform does not remember version selections for remote modules, and so Terraform will always select the newest available module version that meets the specified version constraints.
