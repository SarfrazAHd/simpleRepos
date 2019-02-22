
# 1. Launch one Ubuntu instance and execute below steps to install kops.


# 2. kops binary download

    >> curl -LO https://github.com/kubernetes/kops/releases/download/$(curl https://api.github.com/repos/kubernetes/kops/releases/latest      grep tag_name | cut -d '"' -f 4)/kops-linux-amd64

    >> chmod +x kops-linux-amd64
    >> sudo mv kops-linux-amd64 /usr/local/bin/kops



# 3. aws cli setup to enable ubuntu to interact with aws.

    >>  apt-get update
    >>  apt-get install -y python-pip 
    >>  pip install awscli

    >> aws --version



# 4.

Create IAM user & make a note of access key & secruity key
Create S3 bucket and enable versioning

  >>  aws configure

    
Give access & security access key details here..



# 5. kubectl installation
    
    >>  curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

    >>  echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

    >>   sudo apt-get update
    >>  sudo apt -y install kubectl



# 6. Environment variables setup -- Remember cluster name should ends with k8s.local
updated these two vars in .bashrc & .profile in ~ dir.

    >> export KOPS_CLUSTER_NAME=sarfraz.k8s.local
    >> export KOPS_STATE_STORE=s3://"Bucket_name"

set in Variabel for everytime

    >>  vi  ~ /.bashrc


# 7. Create cluster -- This will actually prepare the configuration files.

    >> kops create cluster \
    --node-count=1 \
    --node-size=t2.micro \
    --master-size=t2.micro \
    --zones=us-east-1a \
    --name=${KOPS_CLUSTER_NAME} 


(optional)if you wanted to review & edit the cluster configuration:
    
    >> kops edit cluster --name ${KOPS_CLUSTER_NAME}



RUN if you're okay withe the configuration run the command with --yes as like below:

    >> kops update cluster --name ${KOPS_CLUSTER_NAME} --yes



# Output 
    Cluster is starting.  It should be ready in a few minutes.

    Suggestions:
    * validate cluster: kops validate cluster
    * list nodes: kubectl get nodes --show-labels
    * ssh to the master: ssh -i ~/.ssh/id_rsa admin@api.advith.k8s.local
    * the admin user is specific to Debian. If not using Debian please use the appropriate user based on your OS.
    * read about installing addons at: https://github.com/kubernetes/kops/blob/master/docs/addons.md.




    >> kops validate cluster


Edit master's security group:
- Make sure 443 port is allowed from ANYWHERE in aws security group.


# 8. deploying dashboard feature

    >>  kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml



# Dashboard access URL

    >>  https://"DNS URL  of master Instance"/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#!/overview


# 9. To get admin user's password::

    >>  kops get secrets kube --type secret -oplaintext 

Or

    >>   grep password: ~/.kube/config 


# 10 . Launch kubernetes url:

http://master dns/ui 
    admin
    passwrod


# 11. Token Generation for admin

    >>  kops get secrets admin --type secret -oplaintext

    >>  kubectl cluster-info

    >>  kubectl get nodes -- To get the nodes status


# 12. Deploy hello-minicube to validate

    >> kubectl run hello-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080


# 13.

    >> kubectl expose deployment hello-minikube --type=NodePort

    >>  kubectl get service

https://master-dns:nodeport/


