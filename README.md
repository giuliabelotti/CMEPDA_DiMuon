# Forward-backward asymmetry of Drell-Yan events at 13 TeV 

The goal of this analysis is reproduce the forward-backward asymmetry of Drell-Yan events in pp collisions using CMS Open Data at 13 TeV, according to the results presented by CMS Collaboration in the article [arXiv:1806.00863v2 [hep-ex]](https://arxiv.org/abs/1806.00863).
Three analysis are provided:
  * Mass distribution
  * Angle distribution
  * Forward-backward asymmetry
    
for two di-leptons channels, muons and electrons, depending on the Z decay.

## How to run
With the command 
```bash
python3 main.py --help
``` 
we have the options for running the anaysis
```bash  
optional arguments:
  -h, --help            show this help message and exit
  --SelectionMu         Selection of good Muons
  --SelectionEl         Selection of good Electrons
  --DiMuonMass          Muon mass distribution
  --DiElectronMass      Electron mass distribution
  --MuonAngle           Muon angle distribution
  --ElectronAngle       Electron angle distribution
  --MuonA_FB            Muon Forward-Backward Asymmetry
  --ElectronA_FB        Electron Forward-Backward Asymmetry
  --Muon_Sel [MUON_SEL]
                        Selection global cuts for Muons
  --Electron_Sel [ELECTRON_SEL]
                        Selection global cuts for Electrons
```

