from django.db import models

# Create your models here.
class TrakingInfo(models.Model):
    invoiceNo = models.CharField(max_length=30)
    productName = models.CharField(max_length=30)
    receiverName = models.CharField(max_length=50)
    receiverPhone = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    details = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)  # 객체가 저장이 될떄 자동으로 입력이 되게함


    # 이름을 출력하고자 할때 선언 -> shell 모드에서 출력할시 리스트의 내용이 지정한 값으로 나옴
    def __str__(self) -> str:
        return self.mem_name
