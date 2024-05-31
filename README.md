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
positional arguments:
  Particle              Choose one particle: Muon or Electron

optional arguments:
  -h, --help            show this help message and exit
  -Sel, --Selection     Selection the good particles
  -M, --Mass            Mass distribution
  -A, --Angle           Angle distribution
  -Asym, --Asymmetry    Forward-Backward Asymmetry
  -Muon_Sel [MUON_SEL], --Muon_Sel [MUON_SEL]
                        Selection global cuts for Muons.
                        Default string: Muon_pt>15, |Muon_eta|<2.4, Muon_dxy<0.2, Muon_pfRelIso03_all<0.1, Muon_mediumId>0
  -Electron_Sel [ELECTRON_SEL], --Electron_Sel [ELECTRON_SEL]
                        Selection global cuts for Electrons.
                        Default string: Electron_pt>20, |Electron_eta|<2.4, Electron_pfRelIso03_all<0.15, Electron_cutBased>=3
```
## Analysis
The data are imported from CMS Open Data portal and have to be selected. 

For example, the selection of Muons is done with the command:
```bash
python3 main.py "Muon" --Selection
```
If no specified, the selection is done with the default value of --Muon_Sel, as descripted in the help. 
The outputs are two files ".root" (one for data, and one for MC) in a folder named "data", which contain the "good" particles.

Afterwards, we can choose one of the three analysis. For example, if we would like to see the dimuon mass distribution, we have to type:
```bash
python3 main.py "Muon" --Mass
```
All the plots are saved in a folder called "Plot" .

## Test




