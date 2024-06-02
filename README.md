# Forward-backward asymmetry of Drell-Yan events at 13 TeV 

The goal of this analysis is reproduce the forward-backward asymmetry of Drell-Yan events in pp collisions using CMS Open Data at 13 TeV, according to the results presented by CMS Collaboration in the article [arXiv:1806.00863v2 [hep-ex]](https://arxiv.org/abs/1806.00863v2).
Three analysis are provided:
  * Mass distribution
  * Angle distribution
  * Forward-backward asymmetry
    
for two di-leptons channels, muons and electrons, depending on the Z decay.

## How to run
The analysis and the unittests are written in PyRoot.

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
The data are imported from [CMS Open Data Portal](https://opendata.cern.ch/) and have to be selected. 

The selection is done adding the optional argument --Selection after the name of the particle chosed. If no specified, the selection is done with the default value of --Muon_Sel and --Electron_Sel, as descripted in the help.

For example, if we wanted to filter muons with the default parameters, we would have to write in the terminal
```bash
python3 main.py "Muon" --Selection
```
If we wanted to change some parameters, we would have to write them in a string, after --Selection.

The selection's outputs are two files ".root" (one for data, and one for the MC) saved in a folder named "data", which contain the "good" particles.

Afterwards, we can choose one of the three possible analysis, typing the corresponding option after the name of the particle. Each analysis can be performed independently from the others.
Both mass and angle distribution analysis are presented in three differents bins in rapidity, so in output we have three plots. 
The forward-backward asymmetry is instead presented in six bins in rapidity but the output is a comparative plot. 
In the folder "Plot" we can find two subfolders called "Muon" and "Electron", where are saved all the plots relative to that channel. 

## Test
Four unittests are been written for this analysis to test the selection of the particles, the mass and angle distributions, the forward-backward asymmetry and the library Vector_Library.h. 
All the unittests can be run in the main folder typing:
```bash
python3 -m unittest Test/name_of_the_test.py
```
If the test passes, there will be written: OK

## Documentation
The documentation is done with Doxigen and can be found here.


