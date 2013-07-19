from watprop import watprop
import nose
import numpy as np

W = watprop()


def test_pT() :
	W.pT(100.,200.).h
	W.pT([34,np.nan],[100,200]).h
	W.pT(33, np.nan).h 
	W.pT(1.0,0.0).h 
	W.pT(100.,200.).u
	W.pT([34,np.nan],[100,200]).u
	W.pT(33, np.nan).u 
	W.pT(0,0).u 
	W.pT(100.,200.).x
	W.pT([34,np.nan],[100,200]).x
	W.pT(00.0, np.nan).x 
	W.pT(1,4).x
	W.pT(100.,200.).rho
	W.pT([34,np.nan],[100,200]).rho
	W.pT(00.0, np.nan).rho
	W.pT(1,4).rho 
	W.pT(100.,200.).s
	W.pT([34,np.nan],[100,200]).s
	W.pT(00.0, np.nan).s
	W.pT(1,4).s

def test_px() :
	W.px(100.).h
	W.px([34,np.nan],[100,200]).h
	W.px(0, np.nan).h 
	W.px(1,2).h 
	W.px(100.).rho
	W.px([34,np.nan],[100,200]).rho
	W.px(0, np.nan).rho 
	W.px(1,2).rho 
	W.px(100.).u
	W.px([34,np.nan],[100,200]).u
	W.px(0, np.nan).u
	W.px(1,2).u
	W.px(100.).s
	W.px([34,np.nan],[100,200]).s
	W.px(0, np.nan).s
	W.px(1,2).s

def test_Tx() :
	W.Tx(100.,200.).h
	W.Tx([np.nan],[1200]).h
	W.Tx(33/4, np.nan).h
	W.Tx(1).h
	W.Tx(100.,200.).u
	W.Tx([np.nan],[1200]).u
	W.Tx(33/4, np.nan).u
	W.Tx(1).u
	W.Tx(100.,200.).rho
	W.Tx([np.nan],[1200]).rho
	W.Tx(33/4, np.nan).rho
	W.Tx(1).rho
	W.Tx(100.,200.).mu
	W.Tx([np.nan],[1200]).mu
	W.Tx(33/4, np.nan).mu
	W.Tx(1).mu
	W.Tx(100.,200.).k
	W.Tx([np.nan],[1200]).k
	W.Tx(33/4, np.nan).k
	W.Tx(1).k
	W.Tx(100.,200.).cp
	W.Tx([np.nan],[1200]).cp
	W.Tx(33/4, np.nan).cp
	W.Tx(1).cp
	W.Tx(100.,200.).s
	W.Tx([np.nan],[1200]).s
	W.Tx(33/4, np.nan).s
	W.Tx(1).s


def test_p_Tsat() :
	W.p_Tsat(100.)
	W.p_Tsat([np.nan])
	W.p_Tsat(1.8975/80)
	W.p_Tsat(1)

	
def test_T_psat() :
	W.T_psat(30)
	W.T_psat(100.)
	W.T_psat(np.nan)
	W.T_psat(0/8*5)
	W.T_psat(0)


print __name__
if __name__ == '__main__':
    import nose
    nose.runmodule()
