from haystack import indexes
from app.models import Image, Gallery

class ImageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    filename = indexes.CharField(model_attr='filename')
    exifIdx = indexes.CharField(model_attr='exif')
    misrIdx = indexes.CharField(model_attr='misr')
    wunderIdx = indexes.CharField(model_attr='wunder')
    resultsIdx = indexes.CharField(model_attr='results')

    def get_model(self):
        return Image

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class GalleryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    imageIdIdx = indexes.IntegerField(model_attr='imageId')
    usernameIdx = indexes.CharField(model_attr='username')

    def get_model(self):
        return Gallery

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
