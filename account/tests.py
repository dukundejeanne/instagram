from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image,User
import datetime as dt

class ImageTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):

        

        self.image=Image(name='leaves',description='beautiful',user="dukunde",likes="1",post="image")
        self.image.save_image()

 
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0) 
   

    def test_delete_method(self):
        '''
        test of delete image
        '''
       
        Image.objects.all().delete()

    def test_update(self):
        '''
        test of filter image by location
        '''
        self.image.save_image()
        img=self.image.get_image_by_id(self.image.id)
        image=Image.objects.get(id=self.image.d)
        self.assertTrue(img,image)
    

    def test_filter_by_location(self):
        '''
        test of filter image by location
        '''
        self.image.save_image()
        img=self.image.filter_by_location(self.image.location_id)
        image=Image.objects.filter(location=self.image.location_id)
        self.assertTrue(img,image)
        
    def test_filter_by_name(self):
        '''
        test image by category
        '''
        self.image.save_image()
        images=Image.search_by_category('this')
        self.assertFalse(len(images)>0)



