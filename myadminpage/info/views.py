from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse
from .models import *

# Main
def main(request):
    infos = TrakingInfo.objects.all()  # 객체로 가져옴
    data = {'infos' : infos} # 딕셔너리 타입으로 만들어서 템플릿 파일에 data를 전달함

    return render(request, 'info_list.html', data)  # 템플릿 파일에서 받아서 반복문으로 처리함

def createInfo(request):
    # [1] 넘어오는 폼 입력값 값 저장 -> request 객체로 넘어옴
    invoiceNo = request.POST['invoiceNo']
    productName = request.POST['productName']
    receiverName = request.POST['receiverName']
    receiverPhone = request.POST['receiverPhone']
    city = request.POST['city']
    street = request.POST['street']
    details = request.POST['details']
    zipcode = request.POST['zipcode']
  
    # return HttpResponse(f'넘어온 값들 {m_id}, {m_name}, {m_email} {m_password}')
    # [2] DB 입력 -> 안될 시 models.py를 확인해서 수정해야함
    article = TrakingInfo(invoiceNo=invoiceNo, productName=productName, receiverName=receiverName,
                          receiverPhone=receiverPhone, city=city, street=street, details=details, zipcode=zipcode)
    article.save()
    # [3] 리다이렉트
    return HttpResponsePermanentRedirect(reverse('main'))
   

def editForm(request, idx):
    # return HttPResponse ('수정페이지=' + idx)
    info = TrakingInfo.objects.get(id = idx)
    return render(request, 'info_list.html', {"user1":info}) # 템플릿에서 받을때 'user'로 받는다는 의미


def updateInfo(request):
    idx = request.POST['idx'] # 히든으로 들어옴
    invoiceNo = request.POST['invoiceNo']
    productName = request.POST['productName']
    receiverName = request.POST['receiverName']
    receiverPhone = request.POST['receiverPhone']
    city = request.POST['city']
    street = request.POST['street']
    details = request.POST['details']
    zipcode = request.POST['zipcode']

    db_info = TrakingInfo.objects.get(id=idx)
    db_info.invoiceNo=invoiceNo
    db_info.productName=productName
    db_info.receiverName=receiverName
    db_info.receiverPhone=receiverPhone
    db_info.city=city
    db_info.street=street
    db_info.details=details
    db_info.zipcode=zipcode

    db_info.save()
    return HttpResponsePermanentRedirect(reverse('main'))


def deleteInfo(request, idx):
    db_info = TrakingInfo.objects.get(pk=idx)
    db_info.delete()
    return HttpResponsePermanentRedirect(reverse('main'))