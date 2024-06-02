""" Test the library Vector_Library.h """

import unittest
import ROOT
import numpy as np

ROOT.gInterpreter.ProcessLine('#include "src/Vector_Library.h"')

class TestVectorLibrary(unittest.TestCase):
    """ Class to test the library Vector_Library.h """

    def test_Vector_Library(self):
        """ Test the library Vector_Library.h """    

        pt1 = 50.
        eta1 = 2.
        phi1 = 7.
        mass1 = 106.

        pt2 = 20.
        eta2 = 1.
        phi2 = 5.
        mass2 = 106.

        v1 = ROOT.PtEtaPhiMVector(pt1,eta1,phi1,mass1)
        v2 = ROOT.PtEtaPhiMVector(pt2,eta2,phi2,mass2)

        self.assertEqual(v1, ROOT.Vector(pt1,eta1,phi1,mass1))
        self.assertEqual(v1+v2, ROOT.SystemFourVector(v1,v2))
        self.assertAlmostEqual((v1 + v2).M(), ROOT.invMass(v1,v2), 3)
        self.assertAlmostEqual((v1 + v2).Rapidity(), ROOT.Rapidity(v1,v2), 3)
        self.assertAlmostEqual((v1 + v2).Pz(), ROOT.pz(v1,v2), 3)
        self.assertAlmostEqual((v1.E() + v1.Pz())/np.sqrt(2), ROOT.P1p(v1), 3)
        self.assertAlmostEqual((v1.E() - v1.Pz())/np.sqrt(2), ROOT.P1m(v1), 3)
        self.assertAlmostEqual((v2.E() + v2.Pz())/np.sqrt(2), ROOT.P2p(v2), 3)
        self.assertAlmostEqual((v2.E() - v2.Pz())/np.sqrt(2), ROOT.P2m(v2), 3)
        self.assertAlmostEqual((v1 + v2).Pt(), ROOT.SystempT(v1,v2), 3)

        var1 = (v1.E() + v1.Pz())/np.sqrt(2)
        var2 = (v1.E() - v1.Pz())/np.sqrt(2)
        var3 = (v2.E() + v2.Pz())/np.sqrt(2)
        var4 = (v2.E() - v2.Pz())/np.sqrt(2)
        long_momentum = (v1 + v2).Pz()
        trans_momentum = (v1 + v2).Pt()
        mass = (v1 + v2).M()
        cos = (2*(var1*var4 - var2*var3)*long_momentum)/(np.sqrt(mass**2*(mass**2+trans_momentum**2))*np.abs(long_momentum))

        self.assertAlmostEqual(cos, ROOT.CosTheta(mass,long_momentum,var1,var2,var3,var4,trans_momentum), 3)

        H = (0.5*0.1*(1-3*cos**2))

        self.assertAlmostEqual(H, ROOT.h(cos),3)
        self.assertAlmostEqual((0.5*(cos**2)/(((1+(cos**2)+(0.5*0.1*(1-3*cos**2)))**3))), ROOT.wD(cos,(0.5*0.1*(1-3*cos**2))),3)
        self.assertAlmostEqual((0.5*np.abs(cos)/(((1+(cos**2)+(0.5*0.1*(1-3*cos**2)))**2))), ROOT.wN(cos,(0.5*0.1*(1-3*cos**2))),3)

        
if __name__ == '__main__':
    unittest.main()

