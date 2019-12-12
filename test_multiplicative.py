#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from Secretmsg.Complexencryption import Multiplicativecipher
class Testmultiplicativecipher(unittest.TestCase): 
    def setUp(self):
        self.p3=Multiplicativecipher.Multiplicativecipher()
        self.p4=Multiplicativecipher.Multiplicativecipher()  
    def tearDown(self):
        print('Tear Down fn')

    def test_mulencrypt(self):         
        self.assertEqual(self.p3.mulencrypt("hello",3),'vmhhq') 
        self.assertEqual(self.p4.mulencrypt("help",3),'vmht') 
        self.assertEqual(self.p4.mulencrypt("I am Awesome",3),'Y#ak#Aomcqkm')
        self.assertEqual(self.p3.mulencrypt("I am Awesome",5),'O%ai%Agumsiu')
        self.assertNotEqual(self.p3.mulencrypt("I am Awesome",3),'L#dp#Dzhvrph')
    
    def test_trandecrypt(self):
        self.assertEqual(self.p3.muldecrypt("vmhhq",3),'hello') 
        self.assertEqual(self.p4.muldecrypt("Y#ak#Aomcqkm",3),'I am Awesome')
        self.assertEqual(self.p3.muldecrypt('O%ai%Agumsiu',5),'I am Awesome')
        self.assertNotEqual(self.p3.muldecrypt('L#dp#Dzhvrph',3),'I am Awesome')
    @classmethod
    def setUpClass(cls):
        print("setUpClass is run only once")
        
    @classmethod
    def tearDownClass(cls):
        print("Tear Down class")
    
        

unittest.main(argv=[''], verbosity=2, exit=False)

