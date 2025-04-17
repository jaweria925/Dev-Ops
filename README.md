Projects: Fetch secrets from AWS Secrets Manager using External Secrets Operator CRDs and map them to K8s secrets.

Technology Used: 

1. AWs Secret Manager
2. External Secret Operators
3. Kubernetes
4. Kustomize
5. Argocd
6. Gitlab CI


Description: 

1. Create ClusterSecretStore to connect to Kubernetes Cluster to AWS secret Manager, using K8 Service Account for Authentication with the Secret Manager.
2. Create ExternalSecret to map the secret from AWS Secret Manager to Kubernetes secret component.
3. Deploy the CRDS using ArgoCD.
4. Mount the fetched secret into the pod to validate the secrets ahs been fetched into Cluster.
5. Update Secret value in AWS Secret Manager to showcase the automatic Syncingof the secret value in k8 cluster.