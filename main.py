import logging
import os
import argparse
import ImportFile
import ParticleSelection
import MassDistribution
import AngleDistribution
import A_FB
import Plotting
import Plot_AFB

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--SelectionMu', help='Selection of good Muons', action = "store_true")
    parser.add_argument('--SelectionEl', help='Selection of good Electrons', action = "store_true")
    parser.add_argument('--DiMuonMass', help='Muon mass distribution', action = "store_true")
    parser.add_argument('--DiElectronMass', help='Electron mass distribution', action = "store_true")
    parser.add_argument('--MuonAngle', help='Muon angle distribution', action = "store_true")
    parser.add_argument('--ElectronAngle', help='Electron angle distribution', action = "store_true")
    parser.add_argument('--MuonA_FB', help='Muon Forward-Backward Asymmetry', action = "store_true")
    parser.add_argument('--ElectronA_FB', help='Electron Forward-Backward Asymmetry', action = "store_true")
    parser.add_argument('--Muon_Sel', help='Selection global cuts for Muons', nargs='?', default= "Muon_pt>15 && abs(Muon_eta)<2.4 && Muon_dxy<0.2 && Muon_pfRelIso03_all<0.1 && Muon_mediumId>0", type = str, action = "store")
    parser.add_argument('--Electron_Sel', help='Selection global cuts for Electrons', nargs='?', default= "Electron_pt>20 && abs(Electron_eta)<2.4 && Electron_pfRelIso03_all<0.15 && Electron_cutBased>=3", type = str, action = "store")

    args = parser.parse_args()
    logging.basicConfig(level = logging.INFO)
    
    if not os.path.exists("Plot"):
            os.makedirs("Plot")
            logging.info("Created the folder Plot")

    df_data_mu, df_data_el, df_MC = ImportFile.CreateDF()

    if args.SelectionMu is True:
        logging.info("Imported the right RDataFrame")
        ParticleSelection.MuCandidates(df_data_mu, "Data", args.Muon_Sel)
        ParticleSelection.MuCandidates(df_MC, "MC", args.Muon_Sel)

    if args.SelectionEl is True:
        logging.info("Imported the right RDataFrame")
        ParticleSelection.ElectronCandidates(df_data_el, "Data", args.Electron_Sel)
        ParticleSelection.ElectronCandidates(df_MC, "MC", args.Electron_Sel)

    if args.DiMuonMass is True:
        h_mu_0_y_04, h_mu_08_y_12, h_mu_16_y_2 = MassDistribution.MassDistribution("data/GoodMu.root", "TreeMu", "Muon")
        h_mu_0_y_04_MC, h_mu_08_y_12_MC, h_mu_16_y_2_MC = MassDistribution.MassDistribution("data/GoodMuMC.root", "TreeMuMC", "Muon")
        canvas1 = Plotting.PlottingMass(h_mu_0_y_04, h_mu_0_y_04_MC, "MuMassDistribution1", "Muon")
        canvas1.Update()
        if not os.path.exists("Plot/Muon/MassDistribution"):
            os.makedirs("Plot/Muon/MassDistribution")
            logging.info("Created the subfolder Muon and MassDistribution")
        canvas1.SaveAs("Plot/Muon/MassDistribution/MuMass_1range.png")

        canvas2 = Plotting.PlottingMass(h_mu_08_y_12, h_mu_08_y_12_MC, "MuMassDistribution2", "Muon")
        canvas2.Update()
        canvas2.SaveAs("Plot/Muon/MassDistribution/MuMass_2range.png")

        canvas3 = Plotting.PlottingMass(h_mu_16_y_2, h_mu_16_y_2_MC, "MuMassDistribution3", "Muon")
        canvas3.Update()
        canvas3.SaveAs("Plot/Muon/MassDistribution/MuMass_3range.png")

    if args.DiElectronMass is True:     
        h_e_0_y_04, h_e_08_y_12, h_e_16_y_2 = MassDistribution.MassDistribution("data/GoodElectron.root", "TreeEl", "Electron")
        h_e_0_y_04_MC, h_e_08_y_12_MC, h_e_16_y_2_MC = MassDistribution.MassDistribution("data/GoodElectronMC.root", "TreeElMC", "Electron")
        canvas4 = Plotting.PlottingMass(h_e_0_y_04, h_e_0_y_04_MC,  "ElMassDistribution1", "Electron")
        canvas4.Update()
        if not os.path.exists("Plot/Electron/MassDistribution"):
            os.makedirs("Plot/Electron/MassDistribution")
            logging.info("Created the subfolder Electron and MassDistribution")
        canvas4.SaveAs("Plot/Electron/MassDistribution/ElMass_1range.png")

        canvas5 = Plotting.PlottingMass(h_e_08_y_12, h_e_08_y_12_MC, "ElMassDistribution2", "Electron")
        canvas5.Update()
        canvas5.SaveAs("Plot/Electron/MassDistribution/ElMass_2range.png")

        canvas6 = Plotting.PlottingMass(h_e_16_y_2, h_e_16_y_2_MC, "ElMassDistribution3", "Electron")
        canvas6.Update()
        canvas6.SaveAs("Plot/Electron/MassDistribution/ElMass_3range.png")

    if args.MuonAngle is True:
        h_mu_0_y_04_a, h_mu_08_y_12_a, h_mu_16_y_2_a = AngleDistribution.AngleDistribution("data/GoodMu.root", "TreeMu", "Muon")
        h_mu_0_y_04_MC_a, h_mu_08_y_12_MC_a, h_mu_16_y_2_MC_a = AngleDistribution.AngleDistribution("data/GoodMuMC.root", "TreeMuMC", "Muon")
        canvasAngle1 = Plotting.PlottingAngle(h_mu_0_y_04_a, h_mu_0_y_04_MC_a, "MuAngleDistribution1", "Muon")
        canvasAngle1.Update()
        if not os.path.exists("Plot/Muon/AngleDistribution"):
            os.makedirs("Plot/Muon/AngleDistribution")
            logging.info("Created the subfolder Muon and AngleDistribution")
        canvasAngle1.SaveAs("Plot/Muon/AngleDistribution/MuAngle_1range.png")

        canvasAngle2 = Plotting.PlottingAngle(h_mu_08_y_12_a, h_mu_08_y_12_MC_a, "MuAngleDistribution2", "Muon")
        canvasAngle2.Update()
        canvasAngle2.SaveAs("Plot/Muon/AngleDistribution/MuAngle_2range.png")

        canvasAngle3 = Plotting.PlottingAngle(h_mu_16_y_2_a, h_mu_16_y_2_MC_a, "MuAngleDistribution3", "Muon")
        canvasAngle3.Update()
        canvasAngle3.SaveAs("Plot/Muon/AngleDistribution/MuAngle_3range.png")

    if args.ElectronAngle is True:
        h_e_0_y_04_a, h_e_08_y_12_a, h_e_16_y_2_a = AngleDistribution.AngleDistribution("data/GoodElectron.root", "TreeEl", "Electron")
        h_e_0_y_04_MC_a, h_e_08_y_12_MC_a, h_e_16_y_2_MC_a = AngleDistribution.AngleDistribution("data/GoodElectronMC.root", "TreeElMC", "Electron")
        canvasAngle4 = Plotting.PlottingAngle(h_e_0_y_04_a, h_e_0_y_04_MC_a,  "ElAngleDistribution1", "Electron")
        canvasAngle4.Update()
        if not os.path.exists("Plot/Electron/AngleDistribution"):
            os.makedirs("Plot/Electron/AngleDistribution")
            logging.info("Created the subfolder Electron and AngleDistribution")
        canvasAngle4.SaveAs("Plot/Electron/AngleDistribution/ElAngle_1range.png")

        canvasAngle5 = Plotting.PlottingAngle(h_e_08_y_12_a, h_e_08_y_12_MC_a, "ElAngleDistribution2", "Electron")
        canvasAngle5.Update()
        canvasAngle5.SaveAs("Plot/Electron/AngleDistribution/ElAngle_2range.png")
        
        canvasAngle6 = Plotting.PlottingAngle(h_e_16_y_2_a, h_e_16_y_2_MC_a, "ElAngleDistribution3", "Electron")
        canvasAngle6.Update()
        canvasAngle6.SaveAs("Plot/Electron/AngleDistribution/ElAngle_3range.png")

    if args.MuonA_FB is True:
        A_FB_Mu = A_FB.Asymmetry("data/GoodMu.root", "TreeMu", "Muon")
        c_mu = Plot_AFB.Plot(A_FB_Mu, "Asymmetry_Muon", "Muon")
        c_mu.Update()
        if not os.path.exists("Plot/Muon/Asymmetry"):
            os.makedirs("Plot/Muon/Asymmetry")
            logging.info("Created the subfolder Muon and Asymmetry")
        c_mu.SaveAs("Plot/Muon/Asymmetry/Mu_AFB.png")

    if args.ElectronA_FB is True:
        A_FB_El = A_FB.Asymmetry("data/GoodElectron.root", "TreeEl", "Electron")
        c_el = Plot_AFB.Plot(A_FB_El, "Asymmetry_El", "Electron")
        c_el.Update()
        if not os.path.exists("Plot/Electron/Asymmetry"):
            os.makedirs("Plot/Electron/Asymmetry")
            logging.info("Created the subfolder Electron and Asymmetry")
        c_el.SaveAs("Plot/Electron/Asymmetry/El_AFB.png")      

