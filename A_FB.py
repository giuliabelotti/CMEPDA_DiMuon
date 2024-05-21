
import ROOT
import numpy as np


def Asymmetry(file_name, Tree_name, particle):
    """ Forward-backward asymmetry in six representative bins in rapidity
    
        Parameters:
            file_name : string
                The name of the file '.root'
            Tree_name : string
                The name of the TTree 
            particle : string
                The name of the particle 
                
        Returns:
            Six histograms, one for each rapidity region    
    """
       
    df = ROOT.RDataFrame(Tree_name, file_name)
    ROOT.gInterpreter.ProcessLine('#include "Vector_Library.h"')

    if(particle == 'Muon'):
        df = df.Define("p1","Vector(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0])")
        df = df.Define("p2","Vector(Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1])")
        df = df.Define("y", "Rapidity(p1,p2)")   
        df = df.Define("pZ", "pz(p1,p2)")
        df = df.Define("P1p", "P1p(p1)")
        df = df.Define("P1m", "P1m(p1)")
        df = df.Define("P2p", "P2p(p2)")
        df = df.Define("P2m", "P2m(p2)")
        df = df.Define("SystemMass", "invMass(p1,p2)")
        df = df.Define("SystempT", "SystempT(p1,p2)")
        df = df.Define("CosThetaMu", "CosTheta(SystemMass, pZ, P1p, P2p, P1m, P2m, SystempT)")
        df = df.Define("h", "h(CosThetaMu)")
        df = df.Define("wD", "wD(CosThetaMu,h)")
        df = df.Define("wN", "wN(CosThetaMu,h)")
                
        df_0_y_04 = df.Filter("abs(y)>0 && abs(y)<0.4", "Range Rapidity")
        df_04_y_08 = df.Filter("abs(y)>0.4 && abs(y)<0.8", "Range Rapidity")
        df_08_y_12 = df.Filter("abs(y)>0.8 && abs(y)<1.2", "Range Rapidity") 
        df_12_y_16 = df.Filter("abs(y)>1.2 && abs(y)<1.6", "Range Rapidity")
        df_16_y_20 = df.Filter("abs(y)>1.6 && abs(y)<2.0", "Range Rapidity")
        df_20_y_24 = df.Filter("abs(y)>2.0 && abs(y)<2.4", "Range Rapidity")
        
        A_FB_1Range = ROOT.std.vector('double')()
        A_FB_2Range = ROOT.std.vector('double')()
        A_FB_3Range = ROOT.std.vector('double')()
        A_FB_4Range = ROOT.std.vector('double')()
        A_FB_5Range = ROOT.std.vector('double')()
        A_FB_6Range = ROOT.std.vector('double')()
        
        for bin_index in range(12):
            A_FB_1Range.push_back(Calculate_AFB(df_0_y_04, bin_index))
        '''
            A_FB_2Range.push_back(Calculate_AFB(df_04_y_08, bin_index))
            A_FB_3Range.push_back(Calculate_AFB(df_08_y_12, bin_index))
            A_FB_4Range.push_back(Calculate_AFB(df_12_y_16, bin_index))
            A_FB_5Range.push_back(Calculate_AFB(df_16_y_20, bin_index))
            A_FB_6Range.push_back(Calculate_AFB(df_20_y_24, bin_index))
        '''
    return A_FB_1Range, A_FB_2Range, A_FB_3Range, A_FB_4Range, A_FB_5Range, A_FB_6Range 
            
        

def Calculate_AFB(dataframe, bin_index):
    dataframe = dataframe.Filter(f"SystemMass>60+5*{bin_index} && SystemMass<65+5*{bin_index}", "Range mass")
    df_cp = dataframe.Filter("CosThetaMu>0", "Forward events: cosTheta>0")
    df_cn = dataframe.Filter("CosThetaMu<0", "Backward events: cosTheta<0")
    D_F = df_cp.Sum("wD").GetValue()
    D_B = df_cn.Sum("wD").GetValue()
    N_F = df_cp.Sum("wN").GetValue()
    N_B = df_cn.Sum("wN").GetValue()
    print(bin_index)   
    A_FB = (3/8)*(N_F - N_B)/(D_F + D_B) 
    return A_FB
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








