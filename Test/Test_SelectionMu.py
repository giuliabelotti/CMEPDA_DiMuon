
import unittest
import ROOT

from ParticleSelection import MuCandidates

class TestSelection(unittest.TestCase):
    
    def test_MuCandidates(self):
       
        f = ROOT.TFile.Open("data/GoodMu.root")
        tree = f.TreeMu
             
        for entry in tree:
           
            self.assertTrue(((entry.GoodMuon_pt[0] > 15) and (entry.GoodMuon_pt[1] > 25)) or ((entry.GoodMuon_pt[1] > 15) and (entry.GoodMuon_pt[0] > 25)) , "pT Cuts")
            
            self.assertTrue(abs(entry.GoodMuon_eta[0]) < 2.4 and abs(entry.GoodMuon_eta[1]) < 2.4, "Eta Cuts")
                             

if __name__ == '__main__':
    unittest.main()

