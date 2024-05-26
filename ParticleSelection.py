
import ROOT
import logging
import ImportFile


def MuCandidates(dataframe, name_dataset):
    """ Selection of good Mu for the analysis
    
        Parameters:
            dataframe : RDataFrame
                One of the RDataFrame created in the macro ImportFile
            name_dataset : string
                Name of the dataset. 
                Possible value: Data or MC 
                
        Returns:
            None   
    """
    df_mu = dataframe.Filter("nMuon >= 2", "Events with at least two muons")
    df_mu = df_mu.Define("Trigger", "Muon_pt>15 && Muon_highPtId==2")
    df_mu = df_mu.Define("NonZero_Trigger", "Nonzero(Trigger)")
    df_mu = df_mu.Filter("NonZero_Trigger.size()>=2")
    
    df_mu = df_mu.Define("Sel_pt", "Muon_pt>25")
    df_mu = df_mu.Define("NonZero_Sel_pt", "Nonzero(Sel_pt)")
    df_mu = df_mu.Filter("NonZero_Sel_pt.size()>=1")
    
    df_mu = df_mu.Define("Sel_eta", "abs(Muon_eta)<2.4 && Trigger")
    df_mu = df_mu.Define("NonZero_Sel_eta", "Nonzero(Sel_eta)")
    df_mu = df_mu.Filter("NonZero_Sel_eta.size()>=2")
    
    df_mu = df_mu.Define("Sel_dxy", "Muon_dxy<0.2 && Sel_eta")
    df_mu = df_mu.Define("NonZero_Sel_dxy", "Nonzero(Sel_dxy)")
    df_mu = df_mu.Filter("NonZero_Sel_dxy.size()>=2")
    
    df_mu = df_mu.Define("Sel_isolation", "Muon_pfRelIso03_all < 0.1*Muon_pt && ((Muon_puppiIsoId==2) || (Muon_puppiIsoId==3)) && Sel_dxy")
    df_mu = df_mu.Define("NonZero_Sel_isolation", "Nonzero(Sel_isolation)")
    df_mu = df_mu.Filter("NonZero_Sel_isolation.size()==2")
    
    df_mu = df_mu.Filter("Muon_charge[NonZero_Sel_isolation[0]] != Muon_charge[NonZero_Sel_isolation[1]]", "Muons with opposite charge")
    
    df_mu = df_mu.Filter("Muon_pt[NonZero_Sel_isolation[0]] > 25 || Muon_pt[NonZero_Sel_isolation[1]] > 25", "Pt") 
        
    df_mu = df_mu.Define("GoodMuon_pt", "ROOT::VecOps::RVec<double>({Muon_pt[NonZero_Sel_isolation[0]], Muon_pt[NonZero_Sel_isolation[1]]})")
    
    df_mu = df_mu.Define("GoodMuon_eta", "ROOT::VecOps::RVec<double>({Muon_eta[NonZero_Sel_isolation[0]], Muon_eta[NonZero_Sel_isolation[1]]})")
    
    df_mu = df_mu.Define("GoodMuon_phi", "ROOT::VecOps::RVec<double>({Muon_phi[NonZero_Sel_isolation[0]], Muon_phi[NonZero_Sel_isolation[1]]})")
     
    df_mu = df_mu.Define("GoodMuon_mass", "ROOT::VecOps::RVec<double>({Muon_mass[NonZero_Sel_isolation[0]], Muon_mass[NonZero_Sel_isolation[1]]})")
      
    logging.info('Good Muons have been selected')   
   
    outCols = ROOT.vector("std::string")()
    outCols.push_back("nMuon")
    outCols.push_back("GoodMuon_pt")
    outCols.push_back("GoodMuon_eta")
    outCols.push_back("GoodMuon_phi")
    outCols.push_back("GoodMuon_mass")
    
    if(name_dataset == "Data"):
        df_mu = df_mu.Snapshot("TreeMu", "data/GoodMu.root", outCols)
        logging.info('Created a file GoodMu.root with Muons selected')
        
    if(name_dataset == "MC"):
        df_mu = df_mu.Snapshot("TreeMuMC", "data/GoodMuMC.root", outCols)
        logging.info('Created a file GoodMuMC.root with Muons selected from MC')      
 

def ElectronCandidates(dataframe, name_dataset):
    """ Selection of good Electron for the analysis
    
        Parameters:
            dataframe : RDataFrame
                One of the RDataFrame created in the macro ImportFile
            name_dataset : string
                Name of the dataset. 
                Possible value: Data or MC 
                
        Returns:
            None
    """ 
    
    df_el = dataframe.Filter("nElectron >= 2", "Events with at least two Electrons")
    df_el = df_el.Define("Trigger", "Electron_pt>20 && (Electron_cutBased == 3 || Electron_cutBased == 4) ")
    df_el = df_el.Define("NonZero_Trigger", "Nonzero(Trigger)")
    df_el = df_el.Filter("NonZero_Trigger.size()>=2")
    
    df_el = df_el.Define("Sel_pt", "Electron_pt>30")
    df_el = df_el.Define("NonZero_Sel_pt", "Nonzero(Sel_pt)")
    df_el = df_el.Filter("NonZero_Sel_pt.size()>=1")
    
    df_el = df_el.Define("Sel_eta", "abs(Electron_eta)<2.4 && (!(1.44 < abs(Electron_eta)) || !(abs(Electron_eta) < 1.57)) && Trigger")
    df_el = df_el.Define("NonZero_Sel_eta", "Nonzero(Sel_eta)")
    df_el = df_el.Filter("NonZero_Sel_eta.size()>=2")
    
    df_el = df_el.Define("Sel_dxy", "Electron_dxy<0.2 && Sel_eta")
    df_el = df_el.Define("NonZero_Sel_dxy", "Nonzero(Sel_dxy)")
    df_el = df_el.Filter("NonZero_Sel_dxy.size()>=2")
         
    df_el = df_el.Define("Sel_isolation", "Electron_pfRelIso03_all < 0.15*Electron_pt && Sel_dxy")
    df_el = df_el.Define("NonZero_Sel_isolation", "Nonzero(Sel_isolation)")
    df_el = df_el.Filter("NonZero_Sel_isolation.size()==2")
    
    df_el = df_el.Filter("Electron_charge[NonZero_Sel_isolation[0]] != Electron_charge[NonZero_Sel_isolation[1]]", "Electrons with opposite charge")
    
    df_el = df_el.Filter("Electron_pt[NonZero_Sel_isolation[0]] > 30 || Electron_pt[NonZero_Sel_isolation[1]] > 30", "Pt") 
   
    df_el = df_el.Define("GoodElectron_pt", "ROOT::VecOps::RVec<double>({Electron_pt[NonZero_Sel_isolation[0]], Electron_pt[NonZero_Sel_isolation[1]]})")
    
    df_el = df_el.Define("GoodElectron_eta", "ROOT::VecOps::RVec<double>({Electron_eta[NonZero_Sel_isolation[0]], Electron_eta[NonZero_Sel_isolation[1]]})")
    
    df_el = df_el.Define("GoodElectron_phi", "ROOT::VecOps::RVec<double>({Electron_phi[NonZero_Sel_isolation[0]], Electron_phi[NonZero_Sel_isolation[1]]})")
     
    df_el = df_el.Define("GoodElectron_mass", "ROOT::VecOps::RVec<double>({Electron_mass[NonZero_Sel_isolation[0]], Electron_mass[NonZero_Sel_isolation[1]]})")
    
    logging.info('Good Electrons have been selected')  
    
    outCols = ROOT.vector("std::string")()
    outCols.push_back("nElectron")
    outCols.push_back("GoodElectron_pt")
    outCols.push_back("GoodElectron_eta")
    outCols.push_back("GoodElectron_phi")
    outCols.push_back("GoodElectron_mass")
    
        
    if(name_dataset == "Data"):
        df_el = df_el.Snapshot("TreeEl", "data/GoodElectron.root", outCols)
        logging.info('Created a file GoodElectron.root with the Electrons selected')
        
    if(name_dataset == "MC"):
         df_el = df_el.Snapshot("TreeElMC", "data/GoodElectronMC.root", outCols)
         logging.info('Created a file GoodElectronMC.root with the Electrons selected from MC')
         
    
