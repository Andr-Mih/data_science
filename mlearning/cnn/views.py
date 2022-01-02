
from django.core.files import storage
from django.shortcuts import render
from tensorflow import keras
from keras.models import load_model
import numpy as np
from PIL import Image
from .forms import NameForm
from django.core.files.storage import FileSystemStorage

CLASSES = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

width = 32
heigth = 32
model = load_model('./models/ds883.hdf5')
#fs = FileSystemStorage(location='/media/photos')

def home(request):    
    form = NameForm()

    return render(request, 'index.html', {'form': form})

def result(request):
    if request.method == 'POST':
        name = NameForm(request.POST, request.FILES)
        if name.is_valid():
            #name.save(storage=fs)
            #name_obj=name.instance
            #context = {'form':name, 'img_obj': name_obj}

            fileobj = request.FILES['filePath']
            fs = FileSystemStorage()
            filePathName = fs.save(fileobj.name, fileobj)
            filePathName = fs.url(filePathName)
            #name_obj=filePathName.instance

            #testimg = '.'+filePathName
            context = {'img_obj': filePathName}
            return render (request, 'index.html', context)
        else:
            form = NameForm()
        return render(request, 'index.html', {'form': form})
        
    #image = Image.open(name)
    #image = image.resize((32,32))
    #x = np.asarray(image.convert('RGB'))
    #x = x.astype("float32") / 255
    
    #result = model.predict(x.reshape(1,width,heigth,3))
    #result = CLASSES[result.argmax()]
    #return render(request, 'result.html', {'result':result})
