# -*- coding: utf-8 -*-
from unittest import TestCase
from tnltk import SentenceSplitter 

class TestSentenceSplitter(TestCase):
    
    """
    TestSentenceSplitter is a class that test the SentenceSplitter class by providing test cases

    Methods:
    setUp(self) : Initializes the SentenceSplitter object
    test_split_sentences(self) : test the split_sentences method of SentenceSplitter class by providing a test text and its expected output.
    """
    
    def setUp(self):
        # Initializes the SentenceSplitter object
        self.splitter = SentenceSplitter()

    def test_split_sentences(self):
        text = "Dr Ahmet Öztürk, Türkiye genelinde birçok hastanede çalışmıştır. Bu hastaneler arasında Ankara Üniversitesi Tıp Fakültesi ve İstanbul Üniversitesi Tıp Fakültesi de vardır. Dr Öztürk, özellikle kalp ve damar cerrahisi alanında uzmanlaşmıştır ve uluslararası çok sayıda makale yazmıştır. Ayrıca Dr Öztürk, Türk Kardiyoloji Derneği üyesidir ve derneğin yönetim kurulu üyesi olarak görev yapmaktadır."
        
        expected_output = ['Dr Ahmet Öztürk, Türkiye genelinde birçok hastanede çalışmıştır.',
        'Bu hastaneler arasında Ankara Üniversitesi Tıp Fakültesi ve İstanbul Üniversitesi Tıp Fakültesi de vardır.',
        'Dr Öztürk, özellikle kalp ve damar cerrahisi alanında uzmanlaşmıştır ve uluslararası çok sayıda makale yazmıştır.',
        'Ayrıca Dr Öztürk, Türk Kardiyoloji Derneği üyesidir ve derneğin yönetim kurulu üyesi olarak görev yapmaktadır.']
        
        self.assertEqual(self.splitter.split_sentences(text), expected_output)