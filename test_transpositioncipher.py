
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
from Secretmsg.Complexencryption import Transpositioncipher
class Testtranspositioncipher(unittest.TestCase):
    def setUp(self):
        self.p1=Transpositioncipher.Transpositioncipher()
        self.p2=Transpositioncipher.Transpositioncipher()
    def tearDown(self):
        print('Tear Down')

    def test_tranencrypt(self):
        self.assertEqual(self.p1.tranencrypt(3,"hello"),'hleol')
        self.assertEqual(self.p2.tranencrypt(3,"help"),'hpel')
        self.assertEqual(self.p2.tranencrypt(3,"I am Awesome"),'Imwo  emaAse')
        self.assertEqual(self.p1.tranencrypt(2,"I am Awesome"),'Ia wsm mAeoe')
        self.assertNotEqual(self.p1.tranencrypt(3,"I am Awesome"),'L#dp#Dzhvrph')
        self.assertIsNone(self.p1.tranencrypt(3,3))

    def test_trandecrypt(self):
        self.assertEqual(self.p1.trandecrypt(3,"hleol"),'hello')
        self.assertEqual(self.p2.trandecrypt(3,"hpel"),'help')
        self.assertEqual(self.p2.trandecrypt(3,"Imwo  emaAse"),'I am Awesome')
        self.assertEqual(self.p1.trandecrypt(2,'Ia wsm mAeoe'),'I am Awesome')
        self.assertNotEqual(self.p1.trandecrypt(3,'L#dp#Dzhvrph'),'I am Awesome')
        self.assertIsNone(self.p1.trandecrypt(4,3))
    @classmethod
    def setUpClass(cls):
        print("setUpClass is run only once")

    @classmethod
    def tearDownClass(cls):
        print("Tear Down class")


unittest.main(argv=[''], verbosity=2, exit=False)
