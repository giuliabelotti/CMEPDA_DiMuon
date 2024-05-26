
import unittest
import ROOT

from ParticleSelection import ElectronCandidates

class TestSelection(unittest.TestCase):
    
    def test_ElectronCandidates(self):
       
        f = ROOT.TFile.Open("data/GoodElectron.root")
        tree = f.TreeEl
             
        for entry in tree:
           
            self.assertTrue(((entry.GoodElectron_pt[0] > 20) and (entry.GoodElectron_pt[1] > 30)) or ((entry.GoodElectron_pt[1] > 20) and (entry.GoodElectron_pt[0] > 30)) , "pT Cuts")
            
            self.assertTrue(abs(entry.GoodElectron_eta[0]) < 2.4 and abs(entry.GoodElectron_eta[1]) < 2.4, "Eta Cuts")
                             

if __name__ == '__main__':
    unittest.main()

