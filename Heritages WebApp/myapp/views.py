from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myapp.models import Document
from myapp.forms import DocumentForm

#imports for image recognition
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import numpy as np
from keras import backend as K
K.set_image_dim_ordering('th')

def recogniser():
    #Loading already trained model
    model = load_model('C:/Users/Anima/Desktop/myproject/myproject/database/trained_model.hdf5')
    
    imagePath = "C:/Users/Anima/Desktop/myproject/myproject/media/documents/new.jpg"
    
    #pre processing image before feeding to trained ML_model
    img = image.load_img(imagePath, target_size=(224, 224))
    test_image = image.img_to_array(img)
    test_image = preprocess_input(test_image)
    test_image=np.moveaxis(test_image,0,-1)
    test_image = np.expand_dims(test_image, axis=0)
    
    # Predicting the test image
    classProba = model.predict(test_image)
    K.clear_session()
    recognisedClassNo = np.argmax(classProba)
    return recognisedClassNo

def index(request):

	 
    templeClass = {0:"bhandarkhal_tank", 1:"bhimsen_temple", 2:"char_narayan_temple", 3:"chyasing_dewal",
              4: "degutale_temple", 5:"garuda_pillar", 6:"keshav_narayan_temple", 7:"kopeshvara_temple", 
              8:"krishna_mandir",9:"mani_chaitya", 10:"mani_dhara", 11:"maniganesh_temple",
              12:"museuem", 13:"narasimha_temple", 14:"north_taleju_temple",
              15:"south_taleju_temple", 16:"taleju_bell", 17:"tushahiti", 
              18:"yantaju_shrine", 19:"yoganarendra_pillar"}
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            # Redirect to the document list after POST
            classNo = recogniser()
            return HttpResponseRedirect(reverse(templeClass[classNo]))
			         
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/index.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
    


def list(request):
    return render_to_response('myapp/index.html')


def bhandarkhal_tank(request):
    return render_to_response('myapp/bhandarkhal_tank.html')

def bhimsen_temple(request):
    return render_to_response('myapp/bhimsen_temple.html')

def char_narayan_temple(request):
    return render_to_response('myapp/char_narayan_temple.html')

def chyasing_dewal(request):
    return render_to_response('myapp/chyasing_dewal.html')

def degu_taleju_temple(request):
    return render_to_response('myapp/degu_taleju_temple.html')

def garuda_pillar(request):
    return render_to_response('myapp/garuda_pillar.html')

def keshav_narayan_temple(request):
    return render_to_response('myapp/keshav_narayan_temple.html')

def kopeshvara_temple(request):
    return render_to_response('myapp/kopeshvara_temple.html')

def krishna_mandir(request):
    return render_to_response('myapp/krishna_mandir.html')

def mani_chaitya(request):
    return render_to_response('myapp/mani_chaitya.html')

def mani_dhara(request):
    return render_to_response('myapp/mani_dhara.html')

def maniganesh_temple(request):
    return render_to_response('myapp/maniganesh_temple.html')

def museuem(request):
    return render_to_response('myapp/museuem.html')

def narasimha_temple(request):
    return render_to_response('myapp/narasimha_temple.html')

def north_taleju_temple(request):
    return render_to_response('myapp/north_taleju_temple.html')

def south_taleju_temple(request):
    return render_to_response('myapp/south_taleju_temple.html')

def taleju_bell(request):
    return render_to_response('myapp/taleju_bell.html')

def tushahiti(request):
    return render_to_response('myapp/tushahiti.html')
        
def yantaju_shrine(request):
    return render_to_response('myapp/yantaju_shrine.html')
        
def yoganarendra_pillar(request):
    return render_to_response('myapp/yoganarendra_pillar.html')








