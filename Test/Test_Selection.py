import unittest
import ROOT
from src import ImportFile
from src.ParticleSelection import MuCandidates
from src.ParticleSelection import ElectronCandidates

class TestSelection(unittest.TestCase):
    """
        Class to test the particle selection
        
    """
    
    def test_MuCandidates(self):
        
        df_data_mu, df_data_el, df_MC = ImportFile.CreateDF()
          
        MuCandidates(df_data_mu, "TEST", "Muon_pt>15 && abs(Muon_eta)<2.4 && Muon_dxy<0.2 && Muon_pfRelIso03_all<0.1 && Muon_mediumId>0", 1000)
       
        f = ROOT.TFile.Open("Test/GoodMuTest.root")
        tree = f.TreeMuTest       
             
        for entry in tree:
           
            self.assertTrue(((entry.GoodMuon_pt[0] > 25) and (entry.GoodMuon_pt[1] > 15)) , "pT Cuts")
            
            self.assertTrue(abs(entry.GoodMuon_eta[0]) < 2.4 and abs(entry.GoodMuon_eta[1]) < 2.4, "Eta Cuts")
            
    def test_ElectronCandidates(self):
        
        df_data_mu, df_data_el, df_MC = ImportFile.CreateDF()
        
        ElectronCandidates(df_data_el, "TEST", "Electron_pt>20 && abs(Electron_eta)<2.4 && Electron_pfRelIso03_all<0.15 && Electron_cutBased>=3", 1000)
       
        f = ROOT.TFile.Open("Test/GoodElTest.root")
        tree = f.TreeElTest
             
        for entry in tree:
           
            self.assertTrue(((entry.GoodElectron_pt[0] > 30) and (entry.GoodElectron_pt[1] > 20)) , "pT Cuts")
            
            self.assertTrue(abs(entry.GoodElectron_eta[0]) < 2.4 and abs(entry.GoodElectron_eta[1]) < 2.4, "Eta Cuts")        
                             

if __name__ == '__main__':
    unittest.main()

