To start app:
```
minikube start
eval $(minikube docker-env)
kubectl create secret generic gcp-service-account --from-file=secrets-dont-store-in-git/gcp-service-account.json
skaffold dev
kubefwd svc
```

# Useful shortcuts (add them to ~./bashrc)
SSH to pod with label `app=<SOME_APP>`
```
export POD_NAME=$(kubectl get pods --selector=app=listings -o jsonpath='{.items[0].metadata.name}'); kubectl exec -it $POD_NAME /bin/bash
```