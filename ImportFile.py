
import ROOT

def CreateDF():
    """ Create dataframe from NanoAOD files
    
        Returns:
            The RDataFrames        
    """
    df_data_mu = ROOT.RDataFrame("Events", "root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/Run2012B_DoubleMuParked.root")
    #df_data_mu = ROOT.RDataFrame("Events", "http://opendata.cern.ch/eos/opendata/cms/derived-data/NanoAODRun1/01-Jul-22/Run2011B_DoubleMu_merged.root")
        
        
    df_data_el = ROOT.RDataFrame("Events", "root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/Run2012B_DoubleElectron.root")
    #df_data_el = ROOT.RDataFrame("Events", "http://opendata.cern.ch/eos/opendata/cms/derived-data/NanoAODRun1/01-Jul-22/Run2011B_DoubleElectron_merged.root")
    
    df_MC = ROOT.RDataFrame("Events", "root://eospublic.cern.ch//eos/opendata/cms/derived-data/NanoAODRun1/01-Jul-22/MonteCarlo11_Summer11LegDR_DYJetsToLL_M-50_7TeV-madgraph-pythia6-tauola_merged.root")
    
    #print("Created the RDataFrame for data")
    return df_data_mu, df_data_el, df_MC
