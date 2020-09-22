# Simple Machine Learning - MNIST (Artifact: json metrics)

## 순서

1. 머신러닝 프로그램 with Tensorflow
* ml-mnist.py

2. Dockerfile

3. 도커 컨테이너 이미지 빌드
* $ docker build -t hanjoo8821/mnist:artifact .

4. 도커 허브에 push
* $ docker push hanjoo8821/mnist:artifact

5. 파이프라인 코드
* pipeline-mnist.py

6. Argo Workflow Manifest
* $ python pipeline-mnist.py
* $ tar -xvf pipeline-mnist.py.tar.gz

8. Argo Workflow
* $ argo submit pipeline.yaml -n argo