To start app:
```
minikube start
eval $(minikube docker-env)
kubectl create secret generic gcp-service-account --from-file=secrets-dont-store-in-git/gcp-service-account.json
skaffold dev
sudo kubefwd svc
```

# Recommended environment setup 

Add this to ~./bashrc
```
alias python=python3.7
source <(kubectl completion bash)
alias fw='sudo kubefwd svc'
alias sl='minikube service list'
export PYTHONDONTWRITEBYTECODE=1
export PIPENV_VENV_IN_PROJECT="enabled"
export SKAFFOLD_NO_PRUNE=true
export SKAFFOLD_CACHE_ARTIFACTS=true
```