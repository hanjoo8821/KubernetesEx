# Kubeflow visualization - ROC curve

## 구성
* src/roc.py : 소스 파일
* Dockerfile : 도커 이미지 manifest
* build_image.sh : 도커 이미지 빌드 및 푸시 명령
* roc-pipeline.py : kfp dsl 파일

## 실행
* ./$ chmod +x build_image.sh
* ./$ python roc-pipeline.py
* kfp 등록 및 run