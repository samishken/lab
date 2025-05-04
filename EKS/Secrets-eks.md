# Secrets
- Secrets should be rotated & audited on regularly.

### Config Maps


### Secrets
- secrets built in eks (kubernetes) are base64 encoded data.
- Not really secured
- so we use the below external tools
- These tools help with regularly rotate & audited secrets

### AWS Secrets manager
- 

### HashiCoprp Vault
- 

---
## How do we fetch from these external tools?
- container storage interface (CSI) driver... is used to fetch secrets from Hashicorp Vault and Secrets manager.

- 
