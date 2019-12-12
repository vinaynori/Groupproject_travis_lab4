#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from Secretmsg.Simpleencryption import Reversecipher
class TestReversecipher(unittest.TestCase): 
    def setUp(self):
        self.p1=Reversecipher.Reversecipher()
        self.p2=Reversecipher.Reversecipher()  
    def tearDown(self):
        print('Tear Down fn') 
    

    def test_set_encrypt(self):         
        self.assertEqual(self.p1.revencrypt("hi"),'ih') 
        self.assertEqual(self.p2.revencrypt("hello"),'olleh') 
        self.assertEqual(self.p2.revencrypt("I am Awesome"),'emosewA ma I')
        self.assertEqual(self.p1.revencrypt("python"),'nohtyp')
        self.assertNotEqual(self.p1.revencrypt("Soft!!wa"),'aw!tfoS')
        
    
    def test_set_decrypt(self):
        self.assertEqual(self.p1.revdecrypt("ih"),'hi') 
        self.assertEqual(self.p2.revdecrypt("olleh"),'hello') 
        self.assertEqual(self.p2.revdecrypt("emosewA ma I"),'I am Awesome')
        self.assertEqual(self.p1.revdecrypt('nohtyp'),'python')
        self.assertNotEqual(self.p1.revdecrypt('L#dp#Dzhvrph'),'I am Awesome')
        
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass is run only once")
        
    @classmethod
    def tearDownClass(cls):
        print("Tear Down class")
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




