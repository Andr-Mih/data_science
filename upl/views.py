from django.shortcuts import render
from .forms import UploadDocumentForm
from base64 import b64encode
from keras.models import load_model
from keras_preprocessing import image
import numpy as np
from PIL import Image
import io
# Create your views here.

def predictor(id, img):
    img_height = 32
    img_width = 32
    labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog',
                'frog', 'horse', 'ship', 'truck']
    if id == '1':
        model = load_model('./models/SimpleNN.h5')
    elif id =='2':
        model = load_model('./models/ds883.hdf5')
    img1 = img.resize((img_height, img_width), Image.ANTIALIAS)
    x = image.img_to_array(img1)
    x = x/255
    x = np.reshape(x, (1, img_height, img_width, 3))
    prediction = model.predict(x)
    pred_label = labels[np.argmax(prediction)]
    return pred_label

def upload_doc(request):
    form = UploadDocumentForm()
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image'].read()
            encoded = b64encode(img)
            decoded = encoded.decode('ascii')
            mime = "image/jpg;"
            input_image = "data:%sbase64,%s" % (mime, decoded)
            tf_decode = Image.open(io.BytesIO(img))
            nn = form.cleaned_data['nn_id']
            prediction = predictor(nn, tf_decode)
            return render(request, 'result.html', locals())
            
    return render(request, 'upload_doc.html', locals())