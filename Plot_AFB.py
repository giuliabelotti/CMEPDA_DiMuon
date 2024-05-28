
import ROOT
import numpy as np
import A_FB

def Plot(A_FB, canvas_name, particle):
    """ Function to plot Forward-backward asymmetry 

        Parameters:
            A_FB : TH2D 
                Histogram for the forward-backward asymmetry 
            canvas_name : string
                The name of the Canvas
            particle : string
                The name of the particle
                
        Returns:
            The Canvas    
    """


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
    pad1.SetLeftMargin(0.17)
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

    text = ROOT.TLatex()
    text.SetNDC()
    text.SetTextAlign(13);
    text.SetTextFont(42)
    text.SetTextSize(0.05)
            
    pad1.cd()
    A_FB1_range = A_FB.ProjectionX("Range1", 1,1, "ED")
    AFB_Style(A_FB1_range, canvas_name, particle)
    if(particle == 'Muon'):
        text.DrawLatex(0.19,0.87, "0.0 < |y_{#mu#mu}| < 0.4")  
    elif(particle == 'Electron'):
        text.DrawLatex(0.19,0.87, "0.0 < |y_{ee}| < 0.4")    

    pad2.cd()
    A_FB2_range = A_FB.ProjectionX("Range2", 2,2, "ED")
    AFB_Style(A_FB2_range, canvas_name, particle)
    if(particle == 'Muon'):
        text.DrawLatex(0.19,0.87, "0.4 < |y_{#mu#mu}| < 0.8")    
    elif(particle == 'Electron'):
        text.DrawLatex(0.19,0.87, "0.4 < |y_{ee}| < 0.8")    

    pad3.cd()
    A_FB3_range = A_FB.ProjectionX("Range3",3 ,3, "ED")
    AFB_Style(A_FB3_range, canvas_name, particle)
    if(particle == 'Muon'):
        text.DrawLatex(0.19,0.87, "0.8 < |y_{#mu#mu}| < 1.2")
    elif(particle == 'Electron'):
        text.DrawLatex(0.19,0.87, "0.8 < |y_{ee}| < 1.2")    
        
    
    pad4.cd()
    A_FB4_range = A_FB.ProjectionX("Range4", 4,4, "ED")
    AFB_Style(A_FB4_range, canvas_name, particle)
    if(particle == 'Muon'):
        text.DrawLatex(0.19,0.87, "1.2 < |y_{#mu#mu}| < 1.6")
    elif(particle == 'Electron'):
        text.DrawLatex(0.19,0.87, "1.2 < |y_{ee}| < 1.6")    
          
    pad5.cd()
    A_FB5_range = A_FB.ProjectionX("Range5", 5,5, "ED")
    AFB_Style(A_FB5_range, canvas_name, particle)
    if(particle == 'Muon'):
        text.DrawLatex(0.19,0.87, "1.6 < |y_{#mu#mu}| < 2.0")
    elif(particle == 'Electron'):
        text.DrawLatex(0.19,0.87, "1.6 < |y_{ee}| < 2.0")    
        
    
    pad6.cd()
    A_FB6_range = A_FB.ProjectionX("Range6", 6,6, "ED")
    AFB_Style(A_FB6_range, canvas_name, particle)
    if(particle == 'Muon'):
        text.DrawLatex(0.19,0.87, "2.0 < |y_{#mu#mu}| < 2.4")
    elif(particle == 'Electron'):
        text.DrawLatex(0.19,0.87, "2.0 < |y_{ee}| < 2.4")
         
    c.Draw()
    #c.SaveAs("A_fb.pdf")
    return c

def AFB_Style(histo, canvas_name, particle):
    """ Plotting utilities for the forward-backward asymmetry
    
        Parameters:
            histo : TH2D 
                Histogram for the forward-backward asymmetry 
            canvas_name : string
                The name of the Canvas
            particle : string
                The name of the particle
                
        Returns:
            The modified histogram 

    """
    
    text = ROOT.TLatex()
    text.SetNDC()
    text.SetTextAlign(13);
    text.SetTextFont(62)
    text.SetTextSize(0.05)
    text.DrawLatex(0.19, 0.89, "CMS")
    text.SetTextFont(42)
    text.DrawLatex(0.19+0.12, 0.89, "Open Data")

    histo.SetMaximum(1.4)
    histo.SetMinimum(-1.4)
    histo.SetTitle("")
    
    if(particle == 'Muon'):
        text.SetTextSize(0.05)
        text.DrawLatex(0.55, 0.92, "41.6 fb^{-1} (13 TeV)")
        histo.GetXaxis().SetTitle("m_{#mu#mu} [GeV]")
        
    elif(particle == 'Electron'):
        text.SetTextSize(0.05)
        text.DrawLatex(0.55, 0.92, "41.6 fb^{-1} (13 TeV)")
        histo.GetXaxis().SetTitle("m_{ee} [GeV]")     
        
    histo.GetXaxis().SetLabelSize(0.07)
    histo.GetXaxis().SetTitleSize(0.08)
    histo.GetXaxis().SetTitleOffset(0.5)
    histo.GetXaxis().SetLabelOffset(-0.03)
    histo.GetXaxis().ChangeLabel(1,-1,0.)
    histo.GetXaxis().ChangeLabel(3,-1,0.)
    histo.GetXaxis().ChangeLabel(5,-1,0.)
    histo.GetXaxis().ChangeLabel(7,-1,0.)
           
    histo.GetYaxis().SetTitle("A_{FB}")  
    histo.GetYaxis().SetLabelSize(0.07)
    histo.GetYaxis().SetTitleSize(0.08)
    histo.GetYaxis().CenterTitle()
    histo.GetYaxis().SetTitleOffset(1)
      
    return histo
    


