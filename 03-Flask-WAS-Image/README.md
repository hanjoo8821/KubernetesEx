# Flask 파일
app.js

# Docker Image Manifest
Dockerfile

# Docker Image 만들기
## 1. Dockerfile 디렉토리로 이동
## 2. Docker Image 빌드
* $ docker build -t hanjoo8821/was-flask:ex .
## 3. Docker Hub repository 만들기
* Repository 이름: was-flask
## 4. Docker Hub push
* $ docker push hanjoo8821/was-flask:ex