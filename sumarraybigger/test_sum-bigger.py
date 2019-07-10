import unittest

class SumBigger(unittest.TestCase):
    
    def test_lenReturn(self):
        alice = [1,2,3]
        bob = [2,3,1]

        result = sumBigger(alice, bob)
        
        self.assertEqual(len(result), 2)

    def test_correctValue(self):
        alice = [1,2,3]
        bob = [2,3,1]

        result = sumBigger(alice, bob)
        
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 2)

def sumBigger(alice, bob):
    result = []
    result.append(0)
    result.append(0)
    for item in alice:
        index = alice.index(item)
        tAlice = alice[index]
        tBob = bob[index]
        if tAlice > tBob:
            result[0] = result[0] + 1
        if tBob > tAlice:
            result[1] = result[1] + 1
    return result
