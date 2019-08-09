```
minikube start
kubectl create secret generic gcp-service-account --from-file=secrets-dont-store-in-git/gcp-service-account.json
skaffold dev
kubefwd svc
```