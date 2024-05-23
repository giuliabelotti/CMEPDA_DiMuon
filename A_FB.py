
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
            An histogram 2D, that represents the asymmetry forward-backward    
    """
       
    df = ROOT.RDataFrame(Tree_name, file_name)
    ROOT.gInterpreter.ProcessLine('#include "Vector_Library.h"')

    if(particle == 'Muon'):
        df = df.Define("p1","Vector(Muon_pt[0], Muon_eta[0], Muon_phi[0], Muon_mass[0])")
        df = df.Define("p2","Vector(Muon_pt[1], Muon_eta[1], Muon_phi[1], Muon_mass[1])")
        df = df.Define("y", "abs(Rapidity(p1,p2))")
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
        
    if(particle == 'Electron'):
        df = df.Define("p1","Vector(Electron_pt[0], Electron_eta[0], Electron_phi[0], Electron_mass[0])")
        df = df.Define("p2","Vector(Electron_pt[1], Electron_eta[1], Electron_phi[1], Electron_mass[1])")
        df = df.Define("y", "abs(Rapidity(p1,p2))")
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
        
        
    df_cp = df.Filter("CosThetaMu>0", "Forward events: cosTheta>0")
    df_cn = df.Filter("CosThetaMu<0", "Backward events: cosTheta<0")
    
    D_F = df_cp.Histo2D(("D_F","D_F",12,60,120,6,0,2.4),"SystemMass", "y", "wD").GetValue()
    D_B = df_cn.Histo2D(("D_B","D_B",12,60,120,6,0,2.4),"SystemMass", "y", "wD").GetValue()
    N_F = df_cp.Histo2D(("N_F","N_F",12,60,120,6,0,2.4),"SystemMass", "y", "wN").GetValue()
    N_B = df_cn.Histo2D(("N_B","N_B",12,60,120,6,0,2.4),"SystemMass", "y", "wN").GetValue()
    A_FB_num = N_F
    A_FB_num.Add(N_B, -1.)
    A_FB_den = D_F
    A_FB_den.Add(D_B, 1.)
    A_FB = A_FB_num
    A_FB.Divide(A_FB_den)
    A_FB.Scale(3/8)
    
    
    return A_FB
       
       
       
       





