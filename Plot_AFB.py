
import ROOT
import numpy as np
import A_FB

def Plot(A_FB_1Range, A_FB_2Range, A_FB_3Range, A_FB_4Range, A_FB_5Range, A_FB_6Range, canvas_name, particle):

    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetTextFont(42)
    c = ROOT.TCanvas(canvas_name, "", 800, 700)
        
    pad1 = ROOT.TPad("pad1", "pad1", 0.03, 0., 0.18, 0.9)
    pad2 = ROOT.TPad("pad2", "pad2", 0.19, 0., 0.34, 0.9)
    pad3 = ROOT.TPad("pad3", "pad3", 0.35, 0., 0.50, 0.9)
    pad4 = ROOT.TPad("pad4", "pad4", 0.52, 0., 0.67, 0.9)
    pad5 = ROOT.TPad("pad5", "pad5", 0.69, 0., 0.84, 0.9)
    pad6 = ROOT.TPad("pad6", "pad6", 0.86, 0., 1.00, 0.9)
    
    pad1.SetTopMargin(0.1)
    pad1.SetLeftMargin(0.20)
    pad1.SetBottomMargin(0.1)
    pad1.SetBorderMode(0)
    pad2.SetTopMargin(0.1)
    pad2.SetLeftMargin(0.17)
    pad2.SetBottomMargin(0.1)
    pad2.SetBorderMode(0)
    pad3.SetTopMargin(0.1)
    pad3.SetLeftMargin(0.17)
    pad3.SetBottomMargin(0.1)
    pad3.SetBorderMode(0)
    pad4.SetTopMargin(0.1)
    pad4.SetLeftMargin(0.17)
    pad4.SetBottomMargin(0.1)
    pad4.SetBorderMode(0)
    pad5.SetTopMargin(0.1)
    pad5.SetLeftMargin(0.17)
    pad5.SetBottomMargin(0.1)
    pad5.SetBorderMode(0)
    pad6.SetTopMargin(0.1)
    pad6.SetLeftMargin(0.17)
    pad6.SetBottomMargin(0.1)
    pad6.SetBorderMode(0)
    pad1.Draw()
    pad2.Draw()
    pad3.Draw()
    pad4.Draw()
    pad5.Draw()
    pad6.Draw()

    n = 12
    x = np.array([62.5, 67.5, 72.5, 77.5, 82.5, 87.5, 92.5, 97.5, 102.5, 107.5, 112.5, 117.5])
    x =  ROOT.std.vector("double")(x)
    
    histo1 = ROOT.TH1D("histo", "histo", 12, 60,120)
    
    for i in range(12):
        histo1.SetBinContent(i,A_FB_1Range[i])
    
    
    pad1.cd()
    histo1.Draw("E")
       
  
    
    pad1.Draw() 
       
    return c

        
