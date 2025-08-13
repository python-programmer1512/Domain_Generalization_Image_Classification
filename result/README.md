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
|❌|⭕|❌|⭕|⭕|⭕|**0.9398**|
|❌|❌|❌|⭕|⭕|⭕|0.9362|
|❌|❌|❌|⭕|⭕|❌|0.9237|
|❌|⭕|❌|⭕|⭕|❌|0.9232|
|⭕|❌|❌|❌|⭕|⭕|0.9180|
|❌|❌|❌|❌|⭕|⭕|0.9156|
|❌|⭕|❌|❌|⭕|⭕|0.9147|
|❌|⭕|❌|❌|❌|⭕|0.9137|
|❌|❌|❌|⭕|❌|⭕|0.9089|
|⭕|❌|❌|⭕|⭕|⭕|0.9071|



* **epoch = 20**
* **batch_size = 16**

|**MixStyle**|**rotation**|**color jitter**|**RandomHorizontalFlip**|**RandomVerticalFlip**|**RandomGrayscale**|**평균 acc**|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|❌|❌|❌|⭕|⭕|⭕|**0.9479**|
|⭕|❌|❌|⭕|⭕|⭕|0.9409|
|❌|❌|❌|⭕|❌|⭕|0.9341|
|❌|❌|❌|❌|⭕|⭕|0.9274|
|❌|⭕|❌|⭕|⭕|⭕|0.9191|
|❌|⭕|❌|⭕|❌|⭕|0.9176|
|❌|❌|❌|⭕|⭕|❌|0.9173|
|⭕|⭕|❌|⭕|⭕|⭕|0.9121|
|❌|⭕|❌|❌|❌|⭕|0.9092|
|⭕|⭕|❌|⭕|❌|⭕|0.9081|

