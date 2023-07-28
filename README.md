# Domain_Generalization_Image_Classification

![poster](<img width="526" alt="image" src="https://github.com/python-programmer1512/Domain_Generalization_Image_Classification/assets/68761453/b50afefd-bfe5-4a73-843e-dedfef21434e">)


## 설명서
* 모든 링크는 / 를 사용하며, 마지막에 / 를 붙이는 것을 원칙으로 한다
* 만약 \ 일경우 바꿔야 함


* 코드와 result 파일 들어있는 초기 파일 경로를
* 마지막 START 의 inital_path 에 넣어줘야함

* 왠만한 설정은 START에서 가능 함(데이터 증진의 확률 제외)

* batch_size 는 초기 상태를 16으로 잡는다. 하지만 변경가능(16정도가 colab, vsc 둘다 돌아감)
* gpu 메모리 초과가 뜰경우 batch_size 를 줄여야됨

* 손실함수는 CrossEntropyLoss 만 있음
* optimizer 는 Adam 과 SGD 가 있음
* scheduler 는 StepLR 만 있음
* Domain_Generalization 은 0 또는 1로 MixStyle 의 사용 여부다 (0 : 사용안함, 1 : 사용함)
* Data_augmentation 는 여러 데이터 증진 기법을 적용한 것이며, 순서대로 image_rotation : 이미지 회전, ColorJitter : 색체,명도 변화, RandomHorizontalFlip : 좌우반전 , * RandomVerticalFlip : 상하반전, RandomGrayscale : 색상을 grayscale 로 변경(회색정도라고 보면될듯) 이다.

* save_file_name 은 원하는 이름 상관 없으며 마지막 test 각도만 놔두면 된다.

* 모든 설정 Hyperparameter 라는 파일에 들어가있으며 txt 파일로 이루어져있다.(데이터 증진 확률 제외)
* result 폴더에 save_file_name_0, 30 , 60 이라는 폴더로 들어가며 각 파일에 각 epoch 당 학습한 모델과 Hyperparmeter.txt, train_result.txt, test_result.txt 파일이 들어있다.

