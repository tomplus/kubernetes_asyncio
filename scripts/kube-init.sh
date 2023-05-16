#!/bin/bash

# Copyright 2017 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -x

function clean_exit(){
    local error_code="$?"
    local spawned=$(jobs -p)
    if [ -n "$spawned" ]; then
        sudo kill $(jobs -p)
    fi
    return $error_code
}

trap "clean_exit" EXIT

# Switch off SE-Linux
setenforce 0

# define HOME dir
#HOME=/home/runner

# Install conntrack (required by minikube)
sudo apt-get update
sudo apt-get install -y conntrack

# Install docker if needed
path_to_executable=$(which docker)
if [ -x "$path_to_executable" ] ; then
    echo "Found Docker installation"
else
    curl -sSL https://get.docker.io | sudo bash
fi
docker --version

# Get the latest stable version of kubernetes
K8S_VERSION=$(curl -sSL https://dl.k8s.io/release/stable.txt)
echo "K8S_VERSION : ${K8S_VERSION}"

echo "Starting docker service"
sudo systemctl enable docker.service
sudo systemctl start docker.service --ignore-dependencies
echo "Checking docker service"
sudo docker ps

echo "Download Kubernetes CLI"
wget -O kubectl "http://storage.googleapis.com/kubernetes-release/release/${K8S_VERSION}/bin/linux/amd64/kubectl"
sudo chmod +x kubectl
sudo mv kubectl /usr/local/bin/

echo "Download  CRI tools"
CRI_VERSION="v1.27.0"
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/$CRI_VERSION/crictl-$CRI_VERSION-linux-amd64.tar.gz
sudo tar zxvf crictl-$CRI_VERSION-linux-amd64.tar.gz -C /usr/local/bin
rm -f crictl-$CRI_VERSION-linux-amd64.tar.gz

echo "Download CRI Dockerd"
CRI_DOCKERD_VERSION="0.3.2"
RELEASE_CODENAME=$(lsb_release --short --codename)
wget https://github.com/Mirantis/cri-dockerd/releases/download/v$CRI_DOCKERD_VERSION/cri-dockerd_$CRI_DOCKERD_VERSION.3-0.ubuntu-${RELEASE_CODENAME}_amd64.deb
sudo dpkg -i cri-dockerd_$CRI_DOCKERD_VERSION.3-0.ubuntu-${RELEASE_CODENAME}_amd64.deb
rm -f cri-dockerd_$CRI_DOCKERD_VERSION.3-0.ubuntu-${RELEASE_CODENAME}_amd64.deb

echo "Download localkube from minikube project"
wget -O minikube "https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"
sudo chmod +x minikube
sudo mv minikube /usr/local/bin/

# L68-100: Set up minikube within Travis CI
# See https://github.com/kubernetes/minikube/blob/master/README.md#linux-continuous-integration-without-vm-support
echo "Set up minikube"
export MINIKUBE_WANTUPDATENOTIFICATION=false
export MINIKUBE_WANTREPORTERRORPROMPT=false
export CHANGE_MINIKUBE_NONE_USER=true
mkdir -p $HOME/.kube
mkdir -p $HOME/.minikube
export MINIKUBE_HOME=$HOME
export MINIKUBE_DRIVER=${MINIKUBE_DRIVER:-none}
# Used bootstrapper to be kubeadm for the most recent k8s version
# since localkube is depreciated and only supported up to version 1.10.0
echo "Starting minikube"
#sudo --preserve-env=MINIKUBE_HOME --preserve-env=HOME minikube start --vm-driver=$MINIKUBE_DRIVER --bootstrapper=kubeadm --kubernetes-version=$K8S_VERSION --logtostderr -v8 --wait=all
minikube start --bootstrapper=kubeadm --logtostderr -v8 --wait=all

# Update ownership for configs/certs
#sudo chown -R $USER /home/runner/.minikube /home/runner/.kube

echo "Dump kube config"
kubectl config view

# check if kubectl can access the api server that Minikube has created
kubectl get po &> /dev/null
if [ $? -eq 1 ]; then
  minikube logs
  echo "minikube did not start"
  exit 1
fi

echo "Dump Kubernetes Objects..."
kubectl get componentstatuses
kubectl get configmaps
kubectl get daemonsets
kubectl get deployments
kubectl get events
kubectl get endpoints
kubectl get horizontalpodautoscalers
kubectl get ingress
kubectl get jobs
kubectl get limitranges
kubectl get nodes
kubectl get namespaces
kubectl get pods
kubectl get persistentvolumes
kubectl get persistentvolumeclaims
kubectl get quota
kubectl get resourcequotas
kubectl get replicasets
kubectl get replicationcontrollers
kubectl get secrets
kubectl get serviceaccounts
kubectl get services

echo "Running tests..."
set -x -e
# Yield execution to venv command
$*
