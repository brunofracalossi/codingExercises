from unittest import TestCase
from impl.walmartLabsHashmap import hashmap


class testHashmap(TestCase):

    def test_insert(self):
    	test = hashmap()
    	self.assertEquals({1: ['word']}, test.insert(1, 'word'))

    def test_insert_multiple(self):
    	test = hashmap()
    	test.insert(500, 'tv')
    	self.assertEquals({500: ['tv', 'test']}, test.insert(500, 'test'))
    	test.insert(1, 'car')
    	self.assertEquals({1: ['car'], 500: ['tv', 'test', 'test']}, test.insert(500, 'test'))

    def test_find_and_replace(self):
    	test = hashmap()
    	self.assertEquals({1: ['word']}, test.insert(1, 'word'))
    	self.assertEquals({1: ['new']}, test.findAndReplace('word', 'new'))

    def test_find_and_replace_multiple(self):
    	test = hashmap()
    	self.assertEquals({1: ['word']}, test.insert(1, 'word'))
    	self.assertEquals({1: ['word', 'test']}, test.insert(1, 'test'))
    	self.assertEquals({1: ['word', 'test'], 50: ['car']}, test.insert(50, 'car'))
    	self.assertEquals({1: ['word', 'test'], 50: ['car', 'test']}, test.insert(50, 'test'))
    	self.assertEquals({1: ['word', 'test'], 50: ['car', 'test', 'test']}, test.insert(50, 'test'))
    	
    	self.assertEquals({1: ['word', 'replaced'], 50: ['car', 'replaced', 'replaced']}, test.findAndReplace('test', 'replaced'))

    def test_empty_hashmap(self):
    	test = hashmap()
    	test.insert(500, 'tv')
    	self.assertEquals({500: ['tv', 'test']}, test.insert(500, 'test'))
    	test.insert(1, 'car')
    	self.assertEquals({1: ['car'], 500: ['tv', 'test', 'test']}, test.insert(500, 'test'))
    	test.empty_hashmap()
    	self.assertEquals({}, test.get_hashmap())
