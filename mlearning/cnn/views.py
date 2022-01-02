
from django.core.files import storage
from django.shortcuts import render
from tensorflow import keras
from keras.models import load_model
import numpy as np
from PIL import Image
from .forms import ImageForm
from .models import ImageModel
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage

CLASSES = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

width = 32
heigth = 32
model = load_model('./models/ds883.hdf5')
fs = FileSystemStorage(location='/media/images')


def home(request):    
    form = ImageForm()

    return render(request, 'index.html', {'form': form})

def result(request):
    if request.method == 'POST':
        name = ImageForm(request.POST, request.FILES)
        if name.is_valid():
            
            name.save()
            name_obj=name.instance
            print(name_obj.image.name)
            ur = name_obj.image.url
            print(ur)
            image = Image.open(name_obj.image)
            image = image.resize((32,32))
            x = np.asarray(image.convert('RGB'))
            x = x.astype("float32") / 255
    
            result = model.predict(x.reshape(1,width,heigth,3))
            result = CLASSES[result.argmax()]
            print(result)
            context = {'form':name, 'img_obj': ur, 'result': result}
            image.close()
            #image.delete()
            name_file = ImageModel.objects.get(image = name_obj.image.name)
            #print(name_file)
            name_file.delete()

            
            return render (request, 'index.html', context)
        else:
            form = ImageForm()
            return render(request, 'index.html', {'form': form})
        
