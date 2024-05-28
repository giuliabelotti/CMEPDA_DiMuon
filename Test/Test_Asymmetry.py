import unittest
import ROOT

from A_FB import Asymmetry

class TestAsymmetry(unittest.TestCase):
    
    def test_A_FB(self):
    
        A_FB_Mu = Asymmetry('data/GoodMu.root', 'TreeMu', 'Muon')        
        self.assertIs(type(A_FB_Mu), ROOT.TH2D)               
        

if __name__ == '__main__':
    unittest.main()

