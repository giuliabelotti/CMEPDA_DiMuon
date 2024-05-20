
import ROOT
import MassDistribution

def PlottingMass(histo, histoMC, canvas_name, particle):
    """ Function to plot the mass distribution
    
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
    upper_pad.SetLogy(1)
    histoMC.GetYaxis().SetTitle("Events/GeV")
    
    histoMC.Scale(histo.GetEntries()/histoMC.GetEntries()) 
    
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
    
    
def PlottingAngle(histo, histoMC, canvas_name, particle):
    """ Function to plot the angle distribution
    
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
    #histoMC.SetMinimum(0)
    #histoMC.SetMaximum(1e6)    
    histoMC.GetYaxis().SetTitle("Events/0.05")
    
    histoMC.Scale(histo.GetEntries()/histoMC.GetEntries()) 
    
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
    ratio.SetMaximum(1.8)
    
    if(particle == 'Muon'):
        ratio.GetXaxis().SetTitle("cos#theta")
        ratio.GetXaxis().SetTitleSize(0.13)
    if(particle == 'Electron'):
        ratio.GetXaxis().SetTitle("cos#theta")
        ratio.GetXaxis().SetTitleSize(0.13)    
       
    ratio.Draw("PESAME")
    ROOT.SetOwnership(ratio, 0)
    c.Draw() 
    
    CMSStyle(upper_pad, lower_pad, histo, histoMC, canvas_name, particle, legend, ratio)
       
    return c
    #c.SaveAs("Prova.pdf")    
    
def CMSStyle(upper_pad, lower_pad, histo, histoMC, canvas_name, particle, legend, ratio):
    """ Plotting Utilities

        Parameters:
            upper_pad : TPad 
                TPad for the distrubution
            lower_pad : TPad
                TPad for the ratio plot    
            histo : TH1D
                Data's histogram
            histoMC : TH1D
                MC's histogram     
            canvas_name : string
                The name of the Canvas
            particle : string
                The name of the particle
            legend : TLegend
                Histogram's legend
            ratio : TH1D
                Ratio histogram      
                
    """
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetTextFont(42)
    lower_pad.SetBottomMargin(0.3)
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
    
    if((canvas_name == 'MuMassDistribution1') or (canvas_name == 'MuMassDistribution2') or (canvas_name == 'MuMassDistribution3')):
        histoMC.SetMinimum(10)
        histoMC.SetMaximum(1e6)
        
    if((canvas_name == 'ElMassDistribution1') or (canvas_name == 'ElMassDistribution2') or (canvas_name == 'ElMassDistribution3')):
        histoMC.SetMinimum(10)
        histoMC.SetMaximum(1e6)
        
    
    if((canvas_name == 'MuAngleDistribution1') or (canvas_name == 'MuAngleDistribution2')):
        histoMC.SetMinimum(10)
        histoMC.SetMaximum(4e4)    
    if(canvas_name == 'MuAngleDistribution3'):
        histoMC.SetMinimum(10)
        histoMC.SetMaximum(1e4)
        
    if((canvas_name == 'ElAngleDistribution1') or (canvas_name == 'ElAngleDistribution2')):
        histoMC.SetMinimum(10)
        histoMC.SetMaximum(4e4)    
    if(canvas_name == 'ElAngleDistribution3'):
        histoMC.SetMinimum(10)
        histoMC.SetMaximum(4e4)    
        
   
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
        if((canvas_name == 'MuMassDistribution1') or (canvas_name == 'MuAngleDistribution1')):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "0.0 < |y_{#mu#mu}| < 0.4") 
        if((canvas_name == 'MuMassDistribution2') or (canvas_name == 'MuAngleDistribution2')):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "0.8 < |y_{#mu#mu}| < 1.2")
        if((canvas_name == 'MuMassDistribution3') or (canvas_name =='MuAngleDistribution3')):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "1.6 < |y_{#mu#mu}| < 2.0") 
            
            
    if(particle == 'Electron'):
        text.SetTextSize(0.030)
        text.DrawLatex(0.72, 0.940, "19.6 fb^{-1} (8 TeV)")
        if((canvas_name == 'ElMassDistribution1') or (canvas_name == 'ElAngleDistribution1')):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "0.0 < |y_{ee}| < 0.4") 
        if((canvas_name == 'ElMassDistribution2') or (canvas_name == 'ElAngleDistribution2')):
            text.SetTextSize(0.03)
            text.DrawLatex(0.15,0.80, "0.8 < |y_{ee}| < 1.2")
        if((canvas_name == 'ElMassDistribution3') or (canvas_name == 'ElAngleDistribution3')):
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    

