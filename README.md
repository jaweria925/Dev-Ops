Project: Deploy Istio Service Mesh and Expose a Secure Istio Gateway

Technology Used:
1. Istio
2. AWS EkS
3. Gitlab CI
4. Kubernetes
5. Terraform
6. Istio Gateway
7. AWs Secret Manager
8. ArgoCD


Description: 

1. Create Resources using Terraform
2. Execute pipleine to Deploy istio to EKS cluster
3. Configure Traffic Routing in clustervia Istio
4. Create a Virtaul Service for Frontend Application to route traffic to App via gateway
5. Generate SelfSigned Certificate  for Istio Gateway TLS and store in Aws Seceret Manager.
6. Configure Istio Gateway Only to access on HTTPS connections.
