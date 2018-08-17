from django.db import models
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):   
    def get_available_name(self, filename):
        if self.exists(filename):
            os.remove(os.path.join(settings.MEDIA_ROOT, filename))
        return filename

def issue_document_image_path(document, filename):
    # "return the canonical file name for an image on this plane instance"
    extension = os.path.splitext(filename)[1]
    filename = "new"
    return os.path.join('documents', filename+extension) 

class Document(models.Model):
    docfile = models.ImageField(upload_to=issue_document_image_path, storage=OverwriteStorage(), null=True, blank=True)
    directory_string_var = 'image'

