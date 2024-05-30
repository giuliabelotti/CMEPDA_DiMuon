""" Histogram of Cos(theta) distribution """

import ROOT

def AngleDistribution(file_name, Tree_name, particle):
    """ Cos(Theta) distribution in three representative bins in rapidity

        Parameters:
            file_name : string
                The name of the file ".root"
            Tree_name : string
                The name of the TTree
            particle : string
                The name of the particle

        Returns:
            Three histograms, one for each rapidity region
    """

    df = ROOT.RDataFrame(Tree_name, file_name)
    ROOT.gInterpreter.ProcessLine('#include "Vector_Library.h"')

    if particle == "Muon":
        df = df.Define("p1","Vector(GoodMuon_pt[0], GoodMuon_eta[0], GoodMuon_phi[0], GoodMuon_mass[0])")
        df = df.Define("p2","Vector(GoodMuon_pt[1], GoodMuon_eta[1], GoodMuon_phi[1], GoodMuon_mass[1])")
        df = df.Define("y", "Rapidity(p1,p2)")
        df = df.Define("pZ", "pz(p1,p2)")
        df = df.Define("P1p", "P1p(p1)")
        df = df.Define("P1m", "P1m(p1)")
        df = df.Define("P2p", "P2p(p2)")
        df = df.Define("P2m", "P2m(p2)")
        df = df.Define("SystemMass", "invMass(p1,p2)")
        df = df.Define("SystempT", "SystempT(p1,p2)")
        df = df.Define("CosThetaMu", "CosTheta(SystemMass, pZ, P1p, P2p, P1m, P2m, SystempT)")

    elif particle == "Electron":
        df = df.Define("p1","Vector(GoodElectron_pt[0], GoodElectron_eta[0], GoodElectron_phi[0], GoodElectron_mass[0])")
        df = df.Define("p2","Vector(GoodElectron_pt[1], GoodElectron_eta[1], GoodElectron_phi[1], GoodElectron_mass[1])")
        df = df.Define("y", "Rapidity(p1,p2)")
        df = df.Define("pZ", "pz(p1,p2)")
        df = df.Define("P1p", "P1p(p1)")
        df = df.Define("P1m", "P1m(p1)")
        df = df.Define("P2p", "P2p(p2)")
        df = df.Define("P2m", "P2m(p2)")
        df = df.Define("SystemMass", "invMass(p1,p2)")
        df = df.Define("SystempT", "SystempT(p1,p2)")
        df = df.Define("CosThetaEl", "CosTheta(SystemMass, pZ, P1p, P2p, P1m, P2m, SystempT)")

    df_0_y_04 = df.Filter("abs(y)>0 && abs(y)<0.4", "Range Rapidity")
    df_08_y_12 = df.Filter("abs(y)>0.8 && abs(y)<1.2", "Range Rapidity")
    df_16_y_2 = df.Filter("abs(y)>1.6 && abs(y)<2.0", "Range Rapidity")

    if particle == "Muon":
        h_0_y_04 = df_0_y_04.Histo1D(("Angle_Mu1","Angle distribution",40,-1,1),"CosThetaMu")
        h_08_y_12 = df_08_y_12.Histo1D(("Angle_Mu2","Angle distribution",40,-1,1), "CosThetaMu")
        h_16_y_2 = df_16_y_2.Histo1D(("Angle_Mu3","Angle distribution",40,-1,1),"CosThetaMu")

    elif particle == "Electron":
        h_0_y_04 = df_0_y_04.Histo1D(("Angle_El1","Angle distribution",40,-1,1),"CosThetaEl")
        h_08_y_12 = df_08_y_12.Histo1D(("Angle_El2","Angle distribution",40,-1,1),"CosThetaEl")
        h_16_y_2 = df_16_y_2.Histo1D(("Angle_El3","Angle distribution",40,-1,1),"CosThetaEl")

    return h_0_y_04, h_08_y_12, h_16_y_2

