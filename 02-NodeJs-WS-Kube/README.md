# Kubernetes Cluster 구성
1. POD: ws-nodejs:ex 이미지로 인스턴스화한 컨테이너 (app: hello-node로 라벨링)
2. ReplicationController: POD 2개 복제
3. Service: hello-node로 라벨링된 POD를 LoadBalancer 타입으로 연결

# Web Service 배포
## 1. Manifest(ws-node.yaml) 파일이 있는 디렉토리로 이동
## 2. namespace 만들기
* $ kubectl create namespace ws-node
## 3. Kubernetes Cluster 형성
* $ kubectl apply -f ws-node.yaml -n ws-node
## 4. Cluster 구성 확인
* $ kubectl get pod -n ws-node
* $ kubectl get replicationcontroller -n ws-node
* $ kubectl get svc -n ws-node
## 5. 서비스 배포 (minikube)
* $ minikube service ws-svc -n ws-node