* [학습 결과 전체](https://github.com/python-programmer1512/Domain_Generalization_Image_Classification/blob/main/result/README.md)

* [학습 결과 상위 10개](https://github.com/python-programmer1512/Domain_Generalization_Image_Classification/blob/main/result/result_non_sort.md)

# resnet18 로 학습


* **epoch = 10**
* **batch_size = 16**

|**MixStyle**|**rotation**|**color jitter**|**RandomHorizontalFlip**|**RandomVerticalFlip**|**RandomGrayscale**|**평균 acc**|
|:------:|:---:|:---:|:---:|:---:|:---:|:---:|
|❌|❌|❌|⭕|⭕|⭕|**0.9306**|
|❌|❌|❌|⭕|❌|⭕|0.9161|
|❌|❌|❌|❌|⭕|⭕|0.9152|
|⭕|⭕|❌|⭕|❌|⭕|0.9087|
|❌|⭕|❌|⭕|⭕|❌|0.9071|
|⭕|❌|❌|⭕|⭕|❌|0.9057|
|⭕|⭕|❌|⭕|❌|❌|0.9022|
|❌|⭕|❌|⭕|❌|⭕|0.9013|
|⭕|⭕|❌|⭕|⭕|❌|0.8975|
|⭕|❌|❌|⭕|❌|⭕|0.8973|


* **epoch = 15**
* **batch_size = 16**

|**MixStyle**|**rotation**|**color jitter**|**RandomHorizontalFlip**|**RandomVerticalFlip**|**RandomGrayscale**|**평균 acc**|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|❌|❌|❌|⭕|⭕|❌|**0.9237**|
|❌|❌|❌|❌|⭕|⭕|0.9156|
|❌|⭕|❌|❌|❌|⭕|0.9137|
|❌|❌|❌|⭕|❌|⭕|0.9089|
|❌|⭕|❌|❌|⭕|❌|0.8841|
|❌|❌|⭕|❌|❌|⭕|0.8580|
|❌|❌|⭕|⭕|❌|❌|0.8399|
|❌|❌|⭕|❌|⭕|❌|0.8309|
|⭕|❌|❌|❌|❌|❌|0.7497|
|❌|❌|❌|❌|❌|❌|0.7323|



* **epoch = 20**
* **batch_size = 16**

|**MixStyle**|**rotation**|**color jitter**|**RandomHorizontalFlip**|**RandomVerticalFlip**|**RandomGrayscale**|**평균 acc**|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|❌|❌|❌|⭕|⭕|⭕|**0.9479**|
|❌|⭕|❌|❌|❌|⭕|0.9092|
|⭕|⭕|❌|⭕|❌|⭕|0.9081|
|❌|⭕|❌|❌|⭕|❌|0.9063|
|❌|⭕|❌|❌|⭕|⭕|0.9039|
|⭕|⭕|❌|⭕|⭕|❌|0.9010|
|❌|❌|⭕|⭕|❌|⭕|0.8750|
|❌|❌|⭕|⭕|⭕|❌|0.8735|
|❌|❌|⭕|❌|⭕|⭕|0.8673|
|⭕|⭕|⭕|❌|⭕|❌|0.8345|

