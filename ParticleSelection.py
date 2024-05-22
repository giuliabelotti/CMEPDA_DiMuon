
import ROOT
import ImportFile

df_data_mu, df_data_el, df_MC = ImportFile.CreateDF()

def MuCandidates():
    """ Selection of good Mu for the analysis
    """
    df_mu = df_data_mu.Filter("nMuon == 2", "Events with exactly two muons")
    df_mu = df_mu.Filter("Muon_pt[0] > 25 || Muon_pt[1] > 25", "Trigger")
    df_mu = df_mu.Filter("Muon_charge[0] != Muon_charge[1]", "Muons with opposite charge")
    df_mu = df_mu.Filter("(Muon_pt[0] > 25 && Muon_pt[1] > 15) || (Muon_pt[1] > 25 && Muon_pt[0] > 15) ", "pT Cuts")
    df_mu = df_mu.Filter("abs(Muon_eta[0]) < 2.4 && abs(Muon_eta[1]) < 2.4","Eta cuts")
    df_mu = df_mu.Filter("Muon_dxy[0] < 0.2 && Muon_dxy[1] < 0.2", "Distance to the primary vertex")
    df_mu = df_mu.Filter("Muon_pfRelIso03_all[0] < 0.1*Muon_pt[0] && Muon_pfRelIso03_all[1] < 0.1*Muon_pt[1] ","Require good isolation")

    print("Good Muons have been selected")
    
    outCols = ROOT.vector("std::string")()
    outCols.push_back("nMuon")
    outCols.push_back("Muon_pt")
    outCols.push_back("Muon_eta")
    outCols.push_back("Muon_phi")
    outCols.push_back("Muon_mass")
   
    df_mu = df_mu.Snapshot("TreeMu", "data/GoodMu.root", outCols)
    print("Created a file GoodMu.root with the Muons selected")

   #Filter of MC events
    
    df_MC_mu = df_MC.Filter("nMuon == 2", "Events with exactly two muons")
    df_MC_mu = df_MC_mu.Filter("Muon_charge[0] != Muon_charge[1]", "Muons with opposite charge")
    df_MC_mu = df_MC_mu.Filter("(Muon_pt[0] > 25 && Muon_pt[1] > 15) || (Muon_pt[1] > 25 && Muon_pt[0] > 15)", "pT Cuts")
    df_MC_mu = df_MC_mu.Filter("abs(Muon_eta[0]) < 2.4 && abs(Muon_eta[1]) < 2.4","Eta cuts")
    df_MC_mu = df_MC_mu.Filter("Muon_dxy[0] < 0.2 && Muon_dxy[1] < 0.2", "Distance to the primary vertex")
    df_Mc_mu = df_MC_mu.Filter("Muon_pfRelIso03_all[0] < 0.1*Muon_pt[0] && Muon_pfRelIso03_all[1] < 0.1*Muon_pt[1] ","Require good isolation")

    print("Good Muons have been selected from MC dataset")
    
    outColsMC = ROOT.vector("std::string")()
    outColsMC.push_back("nMuon")
    outColsMC.push_back("Muon_pt")
    outColsMC.push_back("Muon_eta")
    outColsMC.push_back("Muon_phi")
    outColsMC.push_back("Muon_mass")
    
    df_MC_mu = df_MC_mu.Snapshot("TreeMuMC", "data/GoodMuMC.root", outColsMC)
    
    print("Created a file GoodMuMC.root with the Muons selected from MC")


def ElectronCandidates():
    """ Selection of good Electron for the analysis
    """
   
    df_e = df_data_el.Filter("Electron_pt[0] > 30 || Electron_pt[1] > 30", "Trigger")
   
    df_e = df_e.Filter("(Electron_pt[0] > 30 && Electron_pt[1] > 20) || (Electron_pt[1] > 30 && Electron_pt[0] > 20)  ", "pT Cuts")
    df_e = df_e.Filter("Electron_pfRelIso03_all[0] < 0.15*Electron_pt[0] && Electron_pfRelIso03_all[1] < 0.15*Electron_pt[1] ","Require good isolation")
    df_e = df_e.Filter("abs(Electron_eta[0]) < 2.4 && abs(Electron_eta[1]) < 2.4","Eta cuts")
    
    df_e = df_e.Filter("nElectron == 2", "Events with exactly two electrons")
    df_e = df_e.Filter("Electron_charge[0] != Electron_charge[1]", "Electrons with opposite charge")
    
    print("Good Electrons have been selected")
    
    outCols = ROOT.vector("std::string")()
    outCols.push_back("nElectron")
    outCols.push_back("Electron_pt")
    outCols.push_back("Electron_eta")
    outCols.push_back("Electron_phi")
    outCols.push_back("Electron_mass")
    
    df_e = df_e.Snapshot("TreeEl", "data/GoodElectron.root", outCols)
    print("Created a file GoodElectron.root with the Electrons selected")
    
    #Filter of MC events
    
    df_MC_e = df_MC.Filter("nElectron == 2", "Events with exactly two electrons")
    df_MC_e = df_MC_e.Filter("Electron_pt[0] > 30 || Electron_pt[1] > 30", "Trigger")
    df_MC_e = df_MC_e.Filter("Electron_charge[0] != Electron_charge[1]", "Electrons with opposite charge")
    df_MC_e = df_MC_e.Filter("(Electron_pt[0] > 30 && Electron_pt[1] > 20) || (Electron_pt[1] > 30 && Electron_pt[0] > 20)  ", "pT Cuts")
    df_MC_e = df_MC_e.Filter("abs(Electron_eta[0]) < 2.4 && abs(Electron_eta[1]) < 2.4","Eta cuts")
    df_MC_e = df_MC_e.Filter("Electron_pfRelIso03_all[0] < 0.15*Electron_pt[0] && Electron_pfRelIso03_all[1] < 0.15*Electron_pt[1] ","Require good isolation")
    
    print("Good Electrons have been selected from MC dataset")
    
    outColsMC = ROOT.vector("std::string")()
    outColsMC.push_back("nElectron")
    outColsMC.push_back("Electron_pt")
    outColsMC.push_back("Electron_eta")
    outColsMC.push_back("Electron_phi")
    outColsMC.push_back("Electron_mass")
    
    df_MC_e = df_MC_e.Snapshot("TreeElMC", "data/GoodElectronMC.root", outColsMC)
    
    print("Created a file GoodElectronMC.root with the Electrons selected from MC")
    
    
    
    
    
