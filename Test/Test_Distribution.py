import unittest
import ROOT

from MassDistribution import MassDistribution
from AngleDistribution import AngleDistribution

from Plotting import PlottingMass
from Plotting import PlottingAngle

class TestDistribution(unittest.TestCase):
    
    def test_MassDistribution(self):
    
        h_mu_0_y_04, h_mu_08_y_12, h_mu_16_y_2 = MassDistribution('data/GoodMu.root', 'TreeMu', 'Muon') 
        h_mu_0_y_04_MC, h_mu_08_y_12_MC, h_mu_16_y_2_MC = MassDistribution('data/GoodMuMC.root', 'TreeMuMC', 'Muon')       
        self.assertIs(type(h_mu_0_y_04.GetValue()), ROOT.TH1D)               
        self.assertIs(type(h_mu_0_y_04_MC.GetValue()), ROOT.TH1D)
        
        canvas_mu = PlottingMass(h_mu_0_y_04, h_mu_0_y_04_MC, "MuMassDistribution1", "Muon")   
        self.assertTrue(h_mu_0_y_04_MC.GetMinimum() == 10)
        self.assertTrue(h_mu_0_y_04_MC.GetMaximum() == 1e6)
        self.assertTrue(h_mu_0_y_04_MC.GetYaxis().GetTitle() == "Events/GeV")
        self.assertTrue(h_mu_0_y_04_MC.GetXaxis().GetLabelSize() == 0)
        self.assertTrue(h_mu_0_y_04_MC.GetFillColor() == ROOT.kOrange-2) 
        self.assertTrue(h_mu_0_y_04.GetMarkerStyle() == 20)
        self.assertTrue(h_mu_0_y_04.GetMarkerSize() == 1.0)
        self.assertTrue(h_mu_0_y_04.GetMarkerColor() == ROOT.kBlack)
        self.assertTrue(h_mu_0_y_04.GetLineColor() == ROOT.kBlack)

        h_e_0_y_04, h_e_08_y_12, h_e_16_y_2 = MassDistribution('data/GoodElectron.root', 'TreeEl', 'Electron')
        h_e_0_y_04_MC, h_e_08_y_12_MC, h_e_16_y_2_MC = MassDistribution('data/GoodElectronMC.root', 'TreeElMC', 'Electron')
        self.assertIs(type(h_e_0_y_04.GetValue()), ROOT.TH1D)               
        self.assertIs(type(h_e_0_y_04_MC.GetValue()), ROOT.TH1D)
        
        canvas_e = PlottingMass(h_e_0_y_04, h_e_0_y_04_MC,  "ElMassDistribution1", "Electron")
        self.assertTrue(h_e_0_y_04_MC.GetMinimum() == 10)
        self.assertTrue(h_e_0_y_04_MC.GetMaximum() == 1e6)
        self.assertTrue(h_e_0_y_04_MC.GetYaxis().GetTitle() == "Events/GeV")
        self.assertTrue(h_e_0_y_04_MC.GetXaxis().GetLabelSize() == 0)
        self.assertTrue(h_e_0_y_04_MC.GetFillColor() == ROOT.kOrange-2)
        self.assertTrue(h_e_0_y_04.GetMarkerStyle() == 20)
        self.assertTrue(h_e_0_y_04.GetMarkerSize() == 1.0)
        self.assertTrue(h_e_0_y_04.GetMarkerColor() == ROOT.kBlack)
        self.assertTrue(h_e_0_y_04.GetLineColor() == ROOT.kBlack)


    def test_AngleDistribution(self):
    
        h_mu_0_y_04_a, h_mu_08_y_12_a, h_mu_16_y_2_a = AngleDistribution('data/GoodMu.root', 'TreeMu', 'Muon')
        h_mu_0_y_04_MC_a, h_mu_08_y_12_MC_a, h_mu_16_y_2_MC_a = AngleDistribution('data/GoodMuMC.root', 'TreeMuMC', 'Muon')
        self.assertIs(type(h_mu_0_y_04_a.GetValue()), ROOT.TH1D)               
        self.assertIs(type(h_mu_0_y_04_MC_a.GetValue()), ROOT.TH1D)
        
        canvasAngle_mu = PlottingAngle(h_mu_0_y_04_a, h_mu_0_y_04_MC_a, "MuAngleDistribution1", "Muon")
        self.assertTrue(h_mu_0_y_04_MC_a.GetMinimum() == 10)
        self.assertTrue(h_mu_0_y_04_MC_a.GetMaximum() == 6e4)
        self.assertTrue(h_mu_0_y_04_MC_a.GetYaxis().GetTitle() == "Events/0.05")
        self.assertTrue(h_mu_0_y_04_MC_a.GetXaxis().GetLabelSize() == 0)
        self.assertTrue(h_mu_0_y_04_MC_a.GetFillColor() == ROOT.kOrange-2) 
        self.assertTrue(h_mu_0_y_04_a.GetMarkerStyle() == 20)
        self.assertTrue(h_mu_0_y_04_a.GetMarkerSize() == 1.0)
        self.assertTrue(h_mu_0_y_04_a.GetMarkerColor() == ROOT.kBlack)
        self.assertTrue(h_mu_0_y_04_a.GetLineColor() == ROOT.kBlack)
        
        h_e_0_y_04_a, h_e_08_y_12_a, h_e_16_y_2_a = AngleDistribution('data/GoodElectron.root', 'TreeEl', 'Electron')
        h_e_0_y_04_MC_a, h_e_08_y_12_MC_a, h_e_16_y_2_MC_a = AngleDistribution('data/GoodElectronMC.root', 'TreeElMC', 'Electron')        
        self.assertIs(type(h_e_0_y_04_a.GetValue()), ROOT.TH1D)               
        self.assertIs(type(h_e_0_y_04_MC_a.GetValue()), ROOT.TH1D)
                
        canvasAngle_el = PlottingAngle(h_e_0_y_04_a, h_e_0_y_04_MC_a,  "ElAngleDistribution1", "Electron")        
        self.assertTrue(h_e_0_y_04_MC_a.GetMinimum() == 10)
        self.assertTrue(h_e_0_y_04_MC_a.GetMaximum() == 6e4)
        self.assertTrue(h_e_0_y_04_MC_a.GetYaxis().GetTitle() == "Events/0.05")
        self.assertTrue(h_e_0_y_04_MC_a.GetXaxis().GetLabelSize() == 0)
        self.assertTrue(h_e_0_y_04_MC_a.GetFillColor() == ROOT.kOrange-2) 
        self.assertTrue(h_e_0_y_04_a.GetMarkerStyle() == 20)
        self.assertTrue(h_e_0_y_04_a.GetMarkerSize() == 1.0)
        self.assertTrue(h_e_0_y_04_a.GetMarkerColor() == ROOT.kBlack)
        self.assertTrue(h_e_0_y_04_a.GetLineColor() == ROOT.kBlack)
                         

if __name__ == '__main__':
    unittest.main()

