# Kubernetes Cluster 구성
1. POD: was-flask:ex 이미지로 인스턴스화한 컨테이너 (app: photoview로 라벨링)
2. Deployment: Replica Set 형성
3. Replicas: POD 2개 복제
4. Service: photoview로 라벨링된 POD를 LoadBalancer 타입으로 연결

# Web Service 배포
## 1. Manifest(was-flask.yaml) 파일이 있는 디렉토리로 이동
## 2. namespace 만들기
* $ kubectl create namespace was-flask
## 3. Kubernetes Cluster 형성
* $ kubectl apply -f was-flask.yaml -n was-flask
## 4. Cluster 구성 확인
* $ kubectl get pod -n was-flask
* $ kubectl get deployment -n was-flask
* $ kubectl get replicasets -n was-flask
* $ kubectl get svc -n ws-was-flask
## 5. 서비스 배포 (minikube)
* $ minikube service ws-svc -n was-flask