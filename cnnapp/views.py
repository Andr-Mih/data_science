from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

img_height = 32
img_width = 32
labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog',
            'frog', 'horse', 'ship', 'truck']

model = load_model('./models/SimpleNN.h5')


def index(request):
    context = {'a':1}
    return render(request, 'index.html', context)

def predictImage(request):
    fileobj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileobj.name, fileobj)
    filePathName = fs.url(filePathName)

    testimg = '.'+filePathName
    img = image.load_img(testimg, target_size = (img_height, img_width))
    x = image.img_to_array(img)
    x = x/255
    x = x.reshape(1, img_height, img_width, 3)
    prediction = model.predict(x)
    pred_label = labels[np.argmax(prediction)]

    context = {'filePathName':filePathName, 'pred_label': pred_label}
    return render(request, 'index.html', context)