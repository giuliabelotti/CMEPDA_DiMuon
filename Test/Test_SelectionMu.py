
import unittest
import ROOT

from ParticleSelection import MuCandidates

class TestSelection(unittest.TestCase):
    
    def test_MuCandidates(self):
       
        f = ROOT.TFile.Open("data/GoodMu.root")
        tree = f.TreeMu
             
        for entry in tree:
            self.assertEqual(entry.nMuon, 2, 'Exactly two muon')
            self.assertTrue(entry.Muon_pt[0]>25 or entry.Muon_pt[1]>25, "Trigger")
            self.assertTrue((entry.Muon_pt[0] > 25 and entry.Muon_pt[1] > 15) or (entry.Muon_pt[1] > 25 and entry.Muon_pt[0] > 15), "pT Cuts")
            self.assertTrue(abs(entry.Muon_eta[0]) < 2.4 and abs(entry.Muon_eta[1]) < 2.4, "pT Cuts")
            
        

if __name__ == '__main__':
    unittest.main()

