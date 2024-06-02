""" Test the forward-backward asymmetry """

import unittest
import ROOT

from src.A_FB import Asymmetry

class TestAsymmetry(unittest.TestCase):
    """ Class to test the forward-backward asymmetry """

    def test_A_FB(self):
        """ Test the forward-backward asymmetry """

        A_FB_Mu = Asymmetry('data/GoodMu.root', 'TreeMu', 'Muon')
        self.assertIs(type(A_FB_Mu), ROOT.TH2D)

        A_FB_El = Asymmetry('data/GoodElectron.root', 'TreeEl', 'Electron')
        self.assertIs(type(A_FB_El), ROOT.TH2D)

if __name__ == '__main__':
    unittest.main()
