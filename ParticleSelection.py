""" Particles selection """

import os
import logging
import ROOT

def MuCandidates(dataframe, name_dataset, Muon_Sel, nevents=None):
    """ Selection of good Mu for the analysis

        Parameters:
            dataframe : RDataFrame
                One of the RDataFrame created in the macro ImportFile
            name_dataset : string
                Name of the dataset
                Possible value: Data, MC or TEST
            Muon_Sel : string
                Selection global cuts for Muons
            nevents : int
                Number of event that have to be selected
                Default value = None

        Returns:
            None
    """

    if nevents>0:
        dataframe = dataframe.Range(nevents)

    df_mu = dataframe.Filter("nMuon >= 2", "Events with at least two muons")
    df_mu = df_mu.Define("GoodMuon_pt", f"Muon_pt[{Muon_Sel}]")
    df_mu = df_mu.Define("GoodMuon_eta", f"Muon_eta[{Muon_Sel}]")
    df_mu = df_mu.Define("GoodMuon_phi", f"Muon_phi[{Muon_Sel}]")
    df_mu = df_mu.Define("GoodMuon_mass", f"Muon_mass[{Muon_Sel}]")

    df_mu = df_mu.Filter("GoodMuon_pt.size() == 2")
    df_mu = df_mu.Filter("GoodMuon_pt[0] > 25")
    df_mu = df_mu.Filter("Muon_charge[0] != Muon_charge[1]")

    logging.info('Good Muons have been selected')

    outCols = ROOT.vector("std::string")()
    outCols.push_back("nMuon")
    outCols.push_back("GoodMuon_pt")
    outCols.push_back("GoodMuon_eta")
    outCols.push_back("GoodMuon_phi")
    outCols.push_back("GoodMuon_mass")

    if name_dataset == "Data":
        if not os.path.exists("data"):
            os.makedirs("data")
        df_mu = df_mu.Snapshot("TreeMu", "data/GoodMu.root", outCols)
        logging.info('Created a file GoodMu.root with Muons selected')

    if name_dataset == "MC":
        df_mu = df_mu.Snapshot("TreeMuMC", "data/GoodMuMC.root", outCols)
        logging.info('Created a file GoodMuMC.root with Muons selected from MC')

    if name_dataset == "TEST":
        df_mu = df_mu.Snapshot("TreeMuTest", "Test/GoodMuTest.root", outCols)
        logging.info('Created a file GoodMuTest.root with Muons selected only for Test')


def ElectronCandidates(dataframe, name_dataset, Electron_Sel, nevents=None):
    """ Selection of good Electron for the analysis

        Parameters:
            dataframe : RDataFrame
                One of the RDataFrame created in the macro ImportFile
            name_dataset : string
                Name of the dataset
                Possible value: Data or MC
            Electron_Sel : string
                Selection global cuts for Electrons
            nevents : int
                Number of event that have to be selected
                Default value = None

        Returns:
            None
    """

    if nevents>0:
        dataframe = dataframe.Range(nevents)

    df_el = dataframe.Filter("nElectron >= 2", "Events with at least two electrons")
    df_el = df_el.Define("GoodElectron_pt", f"Electron_pt[{Electron_Sel}]")
    df_el = df_el.Define("GoodElectron_eta", f"Electron_eta[{Electron_Sel}]")
    df_el = df_el.Define("GoodElectron_phi", f"Electron_phi[{Electron_Sel}]")
    df_el = df_el.Define("GoodElectron_mass", f"Electron_mass[{Electron_Sel}]")

    df_el = df_el.Filter("GoodElectron_pt.size() == 2")
    df_el = df_el.Filter("GoodElectron_pt[0] > 30")
    df_el = df_el.Filter("Electron_charge[0] != Electron_charge[1]")

    logging.info('Good Electrons have been selected')

    outCols = ROOT.vector("std::string")()
    outCols.push_back("nElectron")
    outCols.push_back("GoodElectron_pt")
    outCols.push_back("GoodElectron_eta")
    outCols.push_back("GoodElectron_phi")
    outCols.push_back("GoodElectron_mass")

    if name_dataset == "Data":
        if not os.path.exists("data"):
            os.makedirs("data")
        df_el = df_el.Snapshot("TreeEl", "data/GoodElectron.root", outCols)
        logging.info('Created a file GoodElectron.root with the Electrons selected')

    if name_dataset == "MC":
        df_el = df_el.Snapshot("TreeElMC", "data/GoodElectronMC.root", outCols)
        logging.info('Created a file GoodElectronMC.root with the Electrons selected from MC')

    if name_dataset == "TEST":
        df_el = df_el.Snapshot("TreeElTest", "Test/GoodElTest.root", outCols)
        logging.info('Created a file GoodElTest.root with Electron selected only for Test')

