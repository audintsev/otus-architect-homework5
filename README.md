# Homework for the lesson #5 (Kubernetes basics) of the [Otus "Software Architect" course](https://otus.ru/lessons/arhitektor-po/)

## How to run it

This will run the pre-build application image [published on Docker hub](https://hub.docker.com/r/udintsev/otus-architect-homework5)
as Kubernetes deployment using 4 replicas:
```shell script
git clone https://github.com/audintsev/otus-architect-homework5.git
cd otus-architect-homework5
kubectl apply -f .
```

The application itself listens port 8000 and is exposed as ClusterIP service on port 8000.
An Ingress resource configures virtual host `arch.homework` and forwards path `/otusapp/audintsev/*`
to the application, removing the prefix `/otusapp/audintsev/`.

## Invoking the service

Invoking the service via Ingress depends on how your Ingress is installed.
If you're using `minikube` chances are, your Ingress controller listens standard http(s)
ports (80 and 443). Mine was installed using [plain yaml manifests](https://github.com/kubernetes/ingress-nginx/blob/master/docs/deploy/index.md#bare-metal)
and is exposed as a NodePort service on non-standard ports.

Retrieve the port, which Ingress listens for HTTP traffic:

```
export INGRESS_HTTP_PORT=$(kubectl get service ingress-nginx-controller -n ingress-nginx -o jsonpath='{.spec.ports[?(@.name=="http")].nodePort}')
echo Ingres HTTP port is $INGRESS_HTTP_PORT
```

Invoke the service
```
curl -H "Host: arch.homework" localhost:$INGRESS_HTTP_PORT/otusapp/audintsev
curl -H "Host: arch.homework" localhost:$INGRESS_HTTP_PORT/otusapp/audintsev/health
curl -H "Host: arch.homework" localhost:$INGRESS_HTTP_PORT/otusapp/audintsev/version
```

## Building the image

In order to build the image:

```shell script
cd application
docker build -t udintsev/otus-architect-homework5:0.1 . 
``` 
