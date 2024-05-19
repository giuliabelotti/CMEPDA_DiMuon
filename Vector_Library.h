
#ifndef VECTOR_LIBRARY_H
#define VECTOR_LIBRARY_H


#include <Math/Vector4D.h>
using namespace ROOT::Math;

PtEtaPhiMVector Vector(float pt1, float eta1, float phi1, float mass){
    PtEtaPhiMVector V1 = PtEtaPhiMVector(pt1, eta1, phi1, mass);
    return V1;
}

PtEtaPhiMVector SystemFourVector(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    return (p1+p2);
}


float invMass(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    return (p1+p2).M();
} 
    

float Rapidity(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    return (p1+p2).Rapidity();
} 

float pz(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    return (p1+p2).Pz();
} 


float P1p(PtEtaPhiMVector p1){
    return (p1.E() + p1.Pz())/sqrt(2);
} 


float P2p(PtEtaPhiMVector p2){
    return (p2.E() + p2.Pz())/sqrt(2);
} 
    

float P1m(PtEtaPhiMVector p1){
    return (p1.E() - p1.Pz())/sqrt(2);
} 
    

float P2m(PtEtaPhiMVector p2){
    return (p2.E() - p2.Pz())/sqrt(2);
} 
   
    
float SystempT(PtEtaPhiMVector p1, PtEtaPhiMVector p2){
    return (p1+p2).Pt();
} 


float CosTheta(float invMass, float pz, float P1p, float P2p, float P1m, float P2m, float SystempT ){
    return (2*(P1p*P2m - P1m*P2p)*pz)/(sqrt(pow(invMass,2)*(pow(invMass,2) + pow(SystempT,2)))*abs(pz));
}             




#endif













