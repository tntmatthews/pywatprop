from watprop import watprop
import nose
import numpy as np

W = watprop()

def test_phT() :
	W.phT(100.,200.)
	W.phT([34,np.nan],[100,200])
	W.phT("bad", np.nan) # error
	W.phT("","") # error

def test_pTh() :
	W.pTh(100.,200.)
	W.pTh([34,np.nan],[100,200])
	W.pTh("bad", np.nan) # error
	W.pTh("","") # error

def test_pTrho() :
	W.pTrho(100.,200.)
	W.pTrho([34,np.nan],[100,200])
	W.pTrho("bad", np.nan) # error
	W.pTrho("","") # error

def test_pTh() :
	W.pTh(100.,200.)
	W.pTh([34,np.nan],[100,200])
	W.pTh("bad", np.nan) # error
	W.pTh("","") # error

def test_psat_T() :
	W.psat_T(30)
	W.psat_T(100.,200.) # error
	W.psat_T([34,np.nan],[100,200]) # error
	W.psat_T("bad", np.nan) # error
	W.psat_T("","") # error
	
def test_Tsat_p() :
	W.Tsat_p(500)
	W.Tsat_p(100.,200.) # error
	W.Tsat_p([34,np.nan],[100,200]) # error
	W.Tsat_p("bad", np.nan) # error
	W.Tsat_p("","") # error



print __name__
if __name__ == '__main__':
    import nose
    nose.runmodule()
