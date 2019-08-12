# App init (once)
```
minikube start
eval $(minikube docker-env)
kubectl create secret generic gcp-service-account --from-file=secrets-dont-store-in-git/gcp-service-account.json
```

# App run (every time)
```
skaffold dev
```

To forward ports:
```
sudo kubefwd svc
```
or
```
minikube service list
```


# Recommended environment setup 

Add this to ~./bashrc
```
source <(kubectl completion bash)

alias python=python3.7
alias fw='sudo kubefwd svc'
alias sl='minikube service list'
alias ka='kubectl get all'

export PYTHONDONTWRITEBYTECODE=1
export PIPENV_VENV_IN_PROJECT="enabled"
export SKAFFOLD_NO_PRUNE=true
export SKAFFOLD_CACHE_ARTIFACTS=true
```