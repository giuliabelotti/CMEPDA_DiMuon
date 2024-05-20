
#ifndef VECTOR_LIBRARY_H
#define VECTOR_LIBRARY_H


#include <Math/Vector4D.h>
using namespace ROOT::Math;

PtEtaPhiMVector Vector(float pt1, float eta1, float phi1, float mass){
    /*!
        Parameters:
            pt1 : float
                Particle's pT
            eta1 : float
                Particle's eta
            phi1 : float
                Particle's phi
            mass : float
                Particle's mass        
                
        Returns:
            A LorentzVector     
    */
    
    PtEtaPhiMVector V1 = PtEtaPhiMVector(pt1, eta1, phi1, mass);
    return V1;
}

PtEtaPhiMVector SystemFourVector(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    /*!
        Parameters:
            p1 : LorentzVector
            p2 : LorentzVector      
                
        Returns:
            The sum of two LorentzVectors     
    */
    return (p1+p2);
}


float invMass(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    /*!
        Parameters:
            p1 : LorentzVector
            p2 : LorentzVector      
                
        Returns:
            The mass of the di-LorentzVector system
    */
    return (p1+p2).M();
} 
    

float Rapidity(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    /*!
        Parameters:
            p1 : LorentzVector
            p2 : LorentzVector      
                
        Returns:
            The rapidity of the di-LorentzVector system
    */
    return (p1+p2).Rapidity();
} 

float pz(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    /*!
        Parameters:
            p1 : LorentzVector
            p2 : LorentzVector      
                
        Returns:
            The longitudinal momentum of the di-LorentzVector system
    */
    return (p1+p2).Pz();
} 


float P1p(PtEtaPhiMVector p1){
     /*!
        Parameters:
            p1 : LorentzVector 
                
        Returns:
            P1p, in terms of the energy and longitudinal momentum 
    */
    return (p1.E() + p1.Pz())/sqrt(2);
} 


float P2p(PtEtaPhiMVector p2){
    /*!
        Parameters:
            p2 : LorentzVector 
                
        Returns:
            P2p, in terms of the energy and longitudinal momentum 
    */
    return (p2.E() + p2.Pz())/sqrt(2);
} 
    

float P1m(PtEtaPhiMVector p1){
    /*!
        Parameters:
            p1 : LorentzVector 
                
        Returns:
            P1m, in terms of the energy and longitudinal momentum 
    */
    return (p1.E() - p1.Pz())/sqrt(2);
} 
    

float P2m(PtEtaPhiMVector p2){
    /*!
        Parameters:
            p2 : LorentzVector 
                
        Returns:
            P2m, in terms of the energy and longitudinal momentum 
    */
    return (p2.E() - p2.Pz())/sqrt(2);
} 
   
    
float SystempT(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    /*!
        Parameters:
            p1 : LorentzVector
            p2 : LorentzVector      
                
        Returns:
            The transverse momentum of the di-LorentzVector system
    */
    return (p1+p2).Pt();
} 


float CosTheta(float invMass, float pz, float P1p, float P2p, float P1m, float P2m, float SystempT){
    /*!
        Parameters:
            invMass : float
                The mass of the di-LorentzVector system       
            pz : float 
                 The longitudinal momentum of the di-LorentzVector system     
            P1p : float
            P2p : float
            P1m : float
            P2m : float
            SystempT : float 
                 The transverse momentum of the di-LorentzVector system 
                             
        Returns:
            The Cos(Theta)
    */
    return (2*(P1p*P2m - P1m*P2p)*pz)/(sqrt(pow(invMass,2)*(pow(invMass,2) + pow(SystempT,2)))*abs(pz));
}             




#endif













