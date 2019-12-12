#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from Secretmsg.Simpleencryption import Ceasercipher
class Testceasercipher(unittest.TestCase): 
    def setUp(self):
        self.p1=Ceasercipher.Ceasercipher(2)
        self.p2=Ceasercipher.Ceasercipher(3)  
    def tearDown(self):
        print('Tear Down fn') 
    

    def test_set_encrypt(self):         
        self.assertEqual(self.p1.ceaserencrypt("hi"),'jk') 
        self.assertEqual(self.p2.ceaserencrypt("hello"),'khoor') 
        self.assertEqual(self.p2.ceaserencrypt("I am Awesome"),'L#dp#Dzhvrph')
        self.assertEqual(self.p1.ceaserencrypt("I am Awesome"),'K"co"Cyguqog')
        self.assertNotEqual(self.p1.ceaserencrypt("I am Awesome"),'L#dp#Dzhvrph')
        
    
    def test_set_decrypt(self):
        self.assertEqual(self.p1.ceaserdecrypt("jk"),'hi') 
        self.assertEqual(self.p2.ceaserdecrypt("khoor"),'hello') 
        self.assertEqual(self.p2.ceaserdecrypt("L#dp#Dzhvrph"),'I am Awesome')
        self.assertEqual(self.p1.ceaserdecrypt('K"co"Cyguqog'),'I am Awesome')
        self.assertNotEqual(self.p1.ceaserdecrypt('L#dp#Dzhvrph'),'I am Awesome')
        
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass is run only once")
        
    @classmethod
    def tearDownClass(cls):
        print("Tear Down class")
unittest.main(argv=[''], verbosity=2, exit=False)

