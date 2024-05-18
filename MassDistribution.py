
import ROOT
import ParticleSelection

def MassDistribution(file_name, Tree_name, particle):
    """ Mass distribution in three representative bins in rapidity
    
        Parameters:
            file_name : string
                The name of the file '.root'
            Tree_name : string
                The name of the TTree 
            particle : string
                The name of the particle 
                
        Returns:
            Three histograms, one for each rapidity region    
    """
    df = ROOT.RDataFrame(Tree_name, file_name)
    
    cpp_code_invMass = '''   
        float invMass(float pt1, float eta1, float phi1, float pt2, float eta2, float phi2, float mass){
            TLorentzVector p1, p2;
            p1.SetPtEtaPhiM(pt1, eta1, phi1, mass);
            p2.SetPtEtaPhiM(pt2, eta2, phi2, mass);
            return (p1+p2).M();
        } 
    '''

    cpp_code_rapidity = '''   
        float Rapidity(float pt1, float eta1, float phi1, float pt2, float eta2, float phi2, float mass){
            TLorentzVector p1, p2;
            p1.SetPtEtaPhiM(pt1, eta1, phi1, mass);
            p2.SetPtEtaPhiM(pt2, eta2, phi2, mass);
            return (p1+p2).Rapidity();
        } 
    '''

    ROOT.gInterpreter.ProcessLine(cpp_code_invMass)
    ROOT.gInterpreter.ProcessLine(cpp_code_rapidity)
    
    if(particle == 'Muon'):   
        df = df.Define("DiMuon_Mass", "invMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[0])")
        df = df.Define("y", "Rapidity(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[0])")
        
    elif(particle == 'Electron'):
        df = df.Define("DiElectron_Mass", "invMass(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[0])")
        df = df.Define("y", "Rapidity(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[0])")       

    
    df_0_y_04 = df.Filter("abs(y)>0 && abs(y)<0.4", "Range Rapidity")
    df_08_y_12 = df.Filter("abs(y)>0.8 && abs(y)<1.2", "Range Rapidity")
    df_16_y_2 = df.Filter("abs(y)>1.6 && abs(y)<2.0", "Range Rapidity") 

    
    if(particle == 'Muon'): 
        h_0_y_04 = df_0_y_04.Histo1D(("DiMuon_Mass1","Invariant Mass",60,60,120),"DiMuon_Mass")
        h_08_y_12 = df_08_y_12.Histo1D(("DiMuon_Mass2","Invariant Mass",60,60,120),"DiMuon_Mass")
        h_16_y_2 = df_16_y_2.Histo1D(("DiMuon_Mass3","Invariant Mass",60,60,120),"DiMuon_Mass")
    
    elif(particle == 'Electron'):
        h_0_y_04 = df_0_y_04.Histo1D(("DiElectron_Mass","Invariant Mass",60,60,120),"DiElectron_Mass")
        h_08_y_12 = df_08_y_12.Histo1D(("DiElectron_Mass","Invariant Mass",60,60,120),"DiElectron_Mass")
        h_16_y_2 = df_16_y_2.Histo1D(("DiELectron_Mass","Invariant Mass",60,60,120),"DiElectron_Mass")
    
    
    return h_0_y_04, h_08_y_12, h_16_y_2















