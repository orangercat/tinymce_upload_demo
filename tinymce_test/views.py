from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from django.contrib import messages
import os
from django.conf import settings



def index(request):
    print("123123")
    return render(request, 'index.html')


@csrf_exempt
def upload(request):
    try:
        file = request.FILES['image']
        print(file.name)
        # form提交的文件的名字，上面html里面的name
        img = Image.open(file)
        #print(os.path(file))
        img.thumbnail((500, 500), Image.ANTIALIAS)
        print(settings.IMAGE_ROOT)
        try:
            print(file.name)
            img.save('/Users/chaochen/Dropbox/project/env_Django_Demo/tinymce_test/static/img/' + file.name,img.format)
            print("img save pass")
        except:
            print("img.save error")
        # 图片的name和format都是动态获取的，支持png，jpeg，gif等
        path = settings.MEDIA_ROOT + file.name

        print("upload end")
        return HttpResponse(
            "<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('%s').closest('.mce-window').find('.mce-primary').click();</script>" % path)

    except Exception:
        return HttpResponse("error")


