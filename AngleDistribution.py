
import ROOT
import ParticleSelection

def AngleDistribution(file_name, Tree_name, particle):
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
    
    cpp_code_rapidity = '''   
        float Rapidity(float pt1, float eta1, float phi1, float pt2, float eta2, float phi2, float mass){
            TLorentzVector p1, p2;
            p1.SetPtEtaPhiM(pt1, eta1, phi1, mass);
            p2.SetPtEtaPhiM(pt2, eta2, phi2, mass);
            return (p1+p2).Rapidity();
        } 
    '''
    
    cpp_code_pz = '''   
        float pz(float pt1, float eta1, float phi1, float pt2, float eta2, float phi2, float mass){

            TLorentzVector p1, p2;
            p1.SetPtEtaPhiM(pt1, eta1, phi1, mass);
            p2.SetPtEtaPhiM(pt2, eta2, phi2, mass);
            return (p1+p2).Pz();
        } 
    '''
    
    cpp_code_P1p = '''   
        float P1p(float pt1, float eta1, float phi1, float mass){
            TLorentzVector p1;
            p1.SetPtEtaPhiM(pt1, eta1, phi1, mass);
            return (p1.E() + p1.Pz())/sqrt(2);
        } 
    '''
    
    cpp_code_P2p = '''   
        float P2p(float pt2, float eta2, float phi2, float mass){
            TLorentzVector p2;
            p2.SetPtEtaPhiM(pt2, eta2, phi2, mass);
            return (p2.E() + p2.Pz())/sqrt(2);
        } 
        
    '''
    
    cpp_code_P1m = '''   
        float P1m(float pt1, float eta1, float phi1, float mass){
            TLorentzVector p1;
            p1.SetPtEtaPhiM(pt1, eta1, phi1, mass);
            return (p1.E() - p1.Pz())/sqrt(2);
        } 
        
    '''
    
    cpp_code_P2m = '''   
        float P2m(float pt2, float eta2, float phi2, float mass){
            TLorentzVector p2;
            p2.SetPtEtaPhiM(pt2, eta2, phi2, mass);
            return (p2.E() - p2.Pz())/sqrt(2);
        } 
        
    ''' 
    
    cpp_code_mass = '''   
        float SystemMass(float pt1, float eta1, float phi1, float pt2, float eta2, float phi2, float mass){
            TLorentzVector p1, p2;
            p1.SetPtEtaPhiM(pt1, eta1, phi1, mass);
            p2.SetPtEtaPhiM(pt2, eta2, phi2, mass);
            return (p1+p2).M();
        } 
        
    ''' 
    
    cpp_code_pT = '''   
        float SystempT(float pt1, float eta1, float phi1, float pt2, float eta2, float phi2, float mass){
            TLorentzVector p1, p2;
            p1.SetPtEtaPhiM(pt1, eta1, phi1, mass);
            p2.SetPtEtaPhiM(pt2, eta2, phi2, mass);
            return (p1+p2).Pt();
        }             
    ''' 
            
    ROOT.gInterpreter.ProcessLine(cpp_code_rapidity)
    ROOT.gInterpreter.ProcessLine(cpp_code_pz)
    ROOT.gInterpreter.ProcessLine(cpp_code_P1p)
    ROOT.gInterpreter.ProcessLine(cpp_code_P1m)
    ROOT.gInterpreter.ProcessLine(cpp_code_P2p)
    ROOT.gInterpreter.ProcessLine(cpp_code_P2m)
    ROOT.gInterpreter.ProcessLine(cpp_code_mass)
    ROOT.gInterpreter.ProcessLine(cpp_code_pT)
    
    
    if(particle == 'Muon'):
        df = df.Define("y", "Rapidity(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[0])")   
        df = df.Define("pZ", "pz(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[0])")
        df = df.Define("P1p", "P1p(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0])")
        df = df.Define("P1m", "P1m(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0])")
        df = df.Define("P2p", "P2p(Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1])")
        df = df.Define("P2m", "P2m(Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1])")
        df = df.Define("SystemMass", "SystemMass(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[0])")
        df = df.Define("SystempT", "SystempT(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[0])")
        df = df.Define("CosThetaMu", "(2*(P1p*P2m - P1m*P2p)*pZ)/(sqrt(pow(SystemMass,2)*(pow(SystemMass,2) + pow(SystempT,2)))*abs(pZ))")
        
    
    elif(particle == 'Electron'):
        df = df.Define("y", "Rapidity(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[0])")    
        df = df.Define("pZ", "pz(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[0])")
        df = df.Define("P1p", "P1p(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_mass[0])")
        df = df.Define("P1m", "P1m(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_mass[0])")
        df = df.Define("P2p", "P2p(Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[1])")
        df = df.Define("P2m", "P2m(Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[1])")
        df = df.Define("SystemMass", "SystemMass(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[0])")
        df = df.Define("SystempT", "SystempT(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[0])")
        df = df.Define("CosThetaEl", "(2*(P1p*P2m - P1m*P2p)*pZ)/(sqrt(pow(SystemMass,2)*(pow(SystemMass,2) + pow(SystempT,2)))*abs(pZ))")
        
    df_0_y_04 = df.Filter("abs(y)>0 && abs(y)<0.4", "Range Rapidity")
    df_08_y_12 = df.Filter("abs(y)>0.8 && abs(y)<1.2", "Range Rapidity")
    df_16_y_2 = df.Filter("abs(y)>1.6 && abs(y)<2.0", "Range Rapidity") 
    
    if(particle == 'Muon'): 
        h_0_y_04 = df_0_y_04.Histo1D(("Angle_Mu1","Angle distribution",40,-1,1),"CosThetaMu")
        h_08_y_12 = df_08_y_12.Histo1D(("Angle_Mu2","Angle distribution",40,-1,1), "CosThetaMu")
        h_16_y_2 = df_16_y_2.Histo1D(("Angle_Mu3","Angle distribution",40,-1,1),"CosThetaMu")
   
    
    elif(particle == 'Electron'):
        h_0_y_04 = df_0_y_04.Histo1D(("Angle_El1","Angle distribution",40,-1,1),"CosThetaEl")
        h_08_y_12 = df_08_y_12.Histo1D(("Angle_El2","Angle distribution",40,-1,1),"CosThetaEl")
        h_16_y_2 = df_16_y_2.Histo1D(("Angle_El3","Angle distribution",40,-1,1),"CosThetaEl")
        
    return h_0_y_04, h_08_y_12, h_16_y_2
    
    
    
    
    
    
    
    


