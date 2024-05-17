
import argparse
import ROOT
import ParticleSelection
import MassDistribution
import Plotting

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--SelectionMu', help='Selection of good Muons', action = "store_true")
    parser.add_argument('--SelectionEl', help='Selection of good Electrons', action = "store_true")
    parser.add_argument('--DiMuonMass', help='Muon mass distribution', action = "store_true")
    parser.add_argument('--DiElectronMass', help='Electron mass distribution', action = "store_true")
    args = parser.parse_args()
    
    if(args.SelectionMu == True):
        ParticleSelection.MuCandidates()
        
    if(args.SelectionEl == True):
        ParticleSelection.ElectronCandidates()    
    
    if(args.DiMuonMass == True):   
        h_mu_0_y_04, h_mu_08_y_12, h_mu_16_y_2 = MassDistribution.MassDistribution('data/GoodMu.root', 'TreeMu', 'Muon')
        h_mu_0_y_04_MC, h_mu_08_y_12_MC, h_mu_16_y_2_MC = MassDistribution.MassDistribution('data/GoodMuMC.root', 'TreeMuMC', 'Muon')
        canvas1 = Plotting.CMSStyle(h_mu_0_y_04, h_mu_0_y_04_MC, "MuMassDistribution1", "Muon")
        canvas2 = Plotting.CMSStyle(h_mu_08_y_12, h_mu_08_y_12_MC, "MuMassDistribution2", "Muon")
        canvas3 = Plotting.CMSStyle(h_mu_16_y_2, h_mu_16_y_2_MC, "MuMassDistribution3", "Muon")
        
    if(args.DiElectronMass == True):     
        h_e_0_y_04, h_e_08_y_12, h_e_16_y_2 = MassDistribution.MassDistribution('data/GoodElectron.root', 'TreeEl', 'Electron')
        h_e_0_y_04_MC, h_e_08_y_12_MC, h_e_16_y_2_MC = MassDistribution.MassDistribution('data/GoodElectronMC.root', 'TreeElMC', 'Electron')
        canvas4 = Plotting.CMSStyle(h_e_0_y_04, h_e_0_y_04_MC,  "ElMassDistribution1", "Electron")
        canvas5 = Plotting.CMSStyle(h_e_08_y_12, h_e_08_y_12_MC, "ElMassDistribution2", "Electron")
        canvas6 = Plotting.CMSStyle(h_e_16_y_2, h_e_16_y_2_MC, "ElMassDistribution3", "Electron")
            
        
    
    
    
  
    
