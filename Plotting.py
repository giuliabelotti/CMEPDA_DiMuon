
import ROOT
import MassDistribution

def PlottingMass(histo, histoMC, canvas_name, particle):
    """ Plotting Utilities
    
        Parameters:
            histo : TH1D
                Data's histogram
            histoMC : TH1D
                MC's histogram     
            canvas_name : string
                The name of the Canvas
            particle : string
                The name of the particle
                
        Returns:
            A Canvas    
    """
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetTextFont(42)
    c = ROOT.TCanvas(canvas_name, "", 800, 700)
    
    upper_pad = ROOT.TPad("upper_pad", "", 0, 0.18, 1, 1)
    lower_pad = ROOT.TPad("lower_pad", "", 0, 0, 1, 0.25)
    upper_pad.Draw()
    lower_pad.Draw()
    
    upper_pad.cd()     
    histoMC.SetMinimum(10)
    histoMC.SetMaximum(1e6)    
    histoMC.GetYaxis().SetTitle("Events/GeV")
    histoMC.Draw("HIST")
    histo.Draw("E SAME")
    
    legend = ROOT.TLegend(0.7, 0.75, 0.85, 0.88)
    if(particle == 'Muon'):
        legend.AddEntry(histo.GetValue(), "Data", "lep")
        legend.AddEntry(histoMC.GetValue(), "Z#rightarrow#mu#mu", "f")
         
    if(particle == 'Electron'):
        legend.AddEntry(histo.GetValue(), "Data", "lep")
        legend.AddEntry(histoMC.GetValue(), "Z#rightarrow ee", "f") 
    
    legend.Draw() 
    ROOT.SetOwnership(legend, 0)       
    
    lower_pad.cd()
    ratio = histo.Clone()
    ratio.Sumw2()
    ratio.Divide(histoMC.Clone())
    ratio.SetMinimum(0.3)
    ratio.SetMaximum(1.5)
    
    if(particle == 'Muon'):
        ratio.GetXaxis().SetTitle("m_{#mu#mu} [GeV]")
        ratio.GetXaxis().SetTitleSize(0.13)
    if(particle == 'Electron'):
        ratio.GetXaxis().SetTitle("m_{ee} [GeV]")
        ratio.GetXaxis().SetTitleSize(0.13)    
       
    ratio.Draw("PESAME")
    ROOT.SetOwnership(ratio, 0)
    c.Draw() 
    
    CMSStyle(upper_pad, lower_pad, histo, histoMC, canvas_name, particle, legend, ratio)
       
    return c
    #c.SaveAs("Prova.pdf")
    
def CMSStyle(upper_pad, lower_pad, histo, histoMC, canvas_name, particle, legend, ratio):

    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetTextFont(42)
    lower_pad.SetBottomMargin(0.3)
    upper_pad.SetLogy(1)
    upper_pad.cd()    
     
    histo.SetTitle("")
    histoMC.GetXaxis().SetLabelSize(0)
    histoMC.SetTitle("")
    
    histoMC.SetFillColor(ROOT.kOrange-2)
    
    histoMC.GetYaxis().SetTitleSize(0.04)
    histo.SetMarkerStyle(20)
    histo.SetMarkerSize(1.0)
    histo.SetMarkerColor(ROOT.kBlack)
    histo.SetLineColor(ROOT.kBlack)
   
    legend.SetTextFont(42)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.03)
    legend.SetTextAlign(32)     
    ROOT.SetOwnership(legend, 0)
    
    text = ROOT.TLatex()
    text.SetNDC()
    text.SetTextAlign(13);
    text.SetTextFont(62)
    text.SetTextSize(0.04)
    text.DrawLatex(0.15, 0.85, "CMS")
    text.SetTextFont(42)
    text.DrawLatex(0.15+0.08, 0.85, "Open Data")
    
    if(particle == 'Muon'):
        text.SetTextSize(0.030)
        text.DrawLatex(0.73, 0.940, "18.8 fb^{-1} (8 TeV)")
        if(canvas_name == 'MuMassDistribution1'):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "0.0 < |y_{#mu#mu}| < 0.4") 
        if(canvas_name == 'MuMassDistribution2'):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "0.8 < |y_{#mu#mu}| < 1.2")
        if(canvas_name == 'MuMassDistribution3'):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "1.6 < |y_{#mu#mu}| < 2.0") 
            
            
    if(particle == 'Electron'):
        text.SetTextSize(0.030)
        text.DrawLatex(0.72, 0.940, "19.6 fb^{-1} (8 TeV)")
        if(canvas_name == 'ElMassDistribution1'):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "0.0 < |y_{ee}| < 0.4") 
        if(canvas_name == 'ElMassDistribution2'):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "0.8 < |y_{ee}| < 1.2")
        if(canvas_name == 'ElMassDistribution3'):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "1.6 < |y_{ee}| < 2.0")    
    
    
    lower_pad.cd()
    lower_pad.SetGridy()
    lower_pad.SetTicks()
    
    ratio.SetTitle("")
    ratio.SetMarkerStyle(20)
    ratio.SetMarkerSize(1.0)
    ratio.GetXaxis().SetLabelSize(0.13)  
    ratio.GetYaxis().SetLabelSize(0.11)
    ratio.GetYaxis().SetTitleSize(0.13)
    ratio.GetYaxis().SetTitle("Data/MC")
    ratio.GetYaxis().CenterTitle()
    ratio.GetYaxis().SetTitleOffset(0.3)
    ratio.GetYaxis().SetNdivisions(505) 
    
    ratio.Draw("PESAME")
    ROOT.SetOwnership(ratio, 0)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    

