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

        self.user1 = User(username='dukunde')
        self.user1.save()
        
        
        self.image=Image(name='leaves',description='beautiful',user=self.user1,likes="1",post="image")
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

   
    
    def test_filter_by_name(self):
        '''
        test of filter image by location
        '''
        self.image.save_image()
        img=self.image.filter_by_name(self.image.name)
        image=Image.objects.filter(name=self.image.name)
        self.assertTrue(img,image)
   
class ProfileTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):

        self.user1 = User(username='dukunde')
        self.user1.save()
        
        
        self.image=Image(name='leaves',description='beautiful',user=self.user1,likes="1",post="image")
        self.image.save_image()

 
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))