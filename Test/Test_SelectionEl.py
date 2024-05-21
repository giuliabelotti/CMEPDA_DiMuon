
import unittest
import ROOT

from ParticleSelection import MuCandidates

class TestSelection(unittest.TestCase):
    
    def test_ElCandidates(self):
       
        f = ROOT.TFile.Open("data/GoodElectron.root")
        tree = f.TreeEl
             
        for entry in tree:
            self.assertEqual(entry.nElectron, 2, 'Exactly two electron')
            self.assertTrue(entry.Electron_pt[0]>30 or entry.Electron_pt[1]>30, "Trigger")
            self.assertTrue((entry.Electron_pt[0] > 30 and entry.Electron_pt[1] > 20) or (entry.Electron_pt[1] > 30 and entry.Electron_pt[0] > 20), "pT Cuts")
            self.assertTrue(abs(entry.Electron_eta[0]) < 2.4 and abs(entry.Electron_eta[1]) < 2.4, "pT Cuts")
            
        

if __name__ == '__main__':
    unittest.main()

