# -*- coding: utf-8 -*-  

import pywatprop
import numpy as np
import os

def steamtab(is_makepdf=True, is_cleanup=True, is_show = True):
    """
    Returns a steam table based upon the watprop class which provides two benefits:
    1) a lookup table as a quick reference.
    2) verification against other sources.

    NOTE: Only setup to work with altSI units at this time
    """
    w=pywatprop.watprop(unittype='altSI')

    V= open ('steamtab.tex','w')
    V.write("\documentclass[7pt,a4paper]{article}"
    "\n\n\usepackage[latin1]{inputenc}"
    "\n\n\usepackage[T1]{fontenc}"
    "\n\n\usepackage{amsmath,amsfonts,amssymb}"
    "\n\usepackage{datetime}"
    "\n\usepackage{lscape}"
    "\n\usepackage{gensymb}"
    "\n\n\\begin {document}"
    "\n\\title{Steam and water properties}"
    "\n\maketitle"
    "\n\\begin{center}"
    "\n\\ Calculated with pywatprop %s(freesteam v2.0) using the IAPWS-IF97 Industrial Formulation at " 
    "\n\\currenttime"
    "\n\end{center}"
    "\n\listoftables"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n &  &  \multicolumn{2}{c}{Specific volume} &  \multicolumn{2}{c}{Internal Energy} &  \multicolumn{2}{c}{Specific enthalpy} \\\ "
    "\n &  & \multicolumn{2}{c}{$m^3/kg$} & \multicolumn{2}{c}{$kJ/kg$} &  \multicolumn{2}{c}{$kJ/kg$} \\\ "
    "\n $Temp$  &  $pressure$ & $water$ & $steam$ & $water$  & $steam$ & $water$ & $steam$ \\\ "
    "\n $T °C$ &  $P$ $bar$ &   $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    "\\"
    "\\"%pywatprop.__version__)
    T = np.arange(50,101,2)
    rhow= w.Tx(T,0).rho
    uw= w.Tx(T,0).u
    pw= w.Tx(T,0).p
    hw= w.Tx(T,0).h

    rho21= ['%.2f'% elem for elem in rhow]
    u21= ['%.2f'% elem for elem in uw]
    p21= ['%.3f'% elem for elem in pw]
    h21= ['%.2f'% elem for elem in hw]


    rhos= w.Tx(T,1).rho
    us= w.Tx(T,1).u
    ps= w.Tx(T,1).p
    hs= w.Tx(T,1).h

    rho22= ['%.3f'% elem for elem in rhos]
    u22= ['%.1f'% elem for elem in us]
    p22= ['%.2f'% elem for elem in ps]
    h22= ['%.1f'% elem for elem in hs]


    for i in range(len(T)) :
        V.write("\n"+str(T[i]) + " & " +str(p21[i])   + "&"   +str(rho21[i]) + \
            " & " + str(rho22[i])+" & "  +str(u21[i])+" & "+ str(u22[i])+ " & "+ \
            str(h21[i]) +" & "+ str(h22[i])+"\\\ ")

    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam (from $50°C$ to $100°C$)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n &  &  \multicolumn{2}{c}{Specific volume} &  \multicolumn{2}{c}{Internal Energy} &  \multicolumn{2}{c}{Specific enthalpy} \\\ "
    "\n &  & \multicolumn{2}{c}{$m^3/kg$} & \multicolumn{2}{c}{$kJ/kg$} &  \multicolumn{2}{c}{$kJ/kg$} \\\ "
    "\n $Temp$  &  $pressure$ & $water$ & $steam$ & & & & \\\ "
    "\n $T °C$ &  $P$ $bar$ &   $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    "\\"
    "\\")
    T = np.arange(100,401,10)
    rhow= w.Tx(T,0).rho
    uw= w.Tx(T,0).u
    pw= w.Tx(T,0).p
    hw= w.Tx(T,0).h

    rho21= ['%.2f'% elem for elem in rhow]
    u21= ['%.2f'% elem for elem in uw]
    p21= ['%.3f'% elem for elem in pw]
    h21= ['%.2f'% elem for elem in hw]


    rhos= w.Tx(T,1).rho
    us= w.Tx(T,1).u
    ps= w.Tx(T,1).p
    hs= w.Tx(T,1).h

    rho22= ['%.3f'% elem for elem in rhos]
    u22= ['%.1f'% elem for elem in us]
    p22= ['%.2f'% elem for elem in ps]
    h22= ['%.1f'% elem for elem in hs]


    for i in range(len(T)) :
        V.write("\n"+str(T[i]) + " & " +str(p21[i])   + "&"   +str(rho21[i]) + \
            " & " + str(rho22[i])+" & "  +str(u21[i])+" & "+ str(u22[i])+ " & "+ \
            str(h21[i]) +" & "+ str(h22[i])+"\\\ ")

    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam (from $100°C$ to $400°C$)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n $P$  &  $T$ & $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    "\n $[bar]$ &  $[°C]$ &   $[kg/m^3]$ & $[kg/m^3]$ & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] \\\ "
    "\\"
    "\\")
    p1= np.arange(1,2,0.100)
    p2= np.arange(2,5,0.200)
    p3= np.arange(5,7.5,0.500)
    p=np.hstack([p1,p2,p3])

    H= w.px(p,0).h
    rhow= w.px(p,0).rho
    uw= w.px(p,0).u
    Tw= w.p_Tsat(p)
    hw= w.px(p,0).h

    rho1= ['%.1f'% elem for elem in rhow]
    u1= ['%.1f'% elem for elem in uw]
    T1= ['%.2f'% elem for elem in Tw]
    h1= ['%.1f'% elem for elem in hw]


    rhos= w.px(p,1).rho
    us= w.px(p,1).u
    Ts= w.p_Tsat(p)
    hs= w.px(p,1).h

    rho2= ['%.3f'% elem for elem in rhos]
    u2= ['%.1f'% elem for elem in us]
    T2= ['%.2f'% elem for elem in Ts]
    h2= ['%.1f'% elem for elem in hs]


    for i in range(len(p)) :
        V.write("\n"+str(p[i]) + " & " +str(T1[i])   + "&"   +str(rho1[i]) + \
            " & " + str(rho2[i])+" & "  +str(u1[i])+" & "+ str(u2[i])+ " & "+
            str(h1[i]) +" & "+ str(h2[i])+"\\\ ")


    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam ($1$ $to$ $7$ $bar$)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n $P$  &  $T$ & $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    "\n $[bar]$ &  $[°C]$ &   $[kg/m^3]$ & $[kg/m^3]$ & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] \\\ "
    "\\"
    "\\")
    p1= np.arange(7.5,13,0.5)
    p2= np.arange(13,31,1)
    p=np.hstack([p1,p2])

    H= w.px(p,0).h
    rhow= w.px(p,0).rho
    uw= w.px(p,0).u
    Tw= w.p_Tsat(p)
    hw= w.px(p,0).h

    rho1= ['%.1f'% elem for elem in rhow]
    u1= ['%.1f'% elem for elem in uw]
    T1= ['%.2f'% elem for elem in Tw]
    h1= ['%.1f'% elem for elem in hw]


    rhos= w.px(p,1).rho
    us= w.px(p,1).u
    Ts= w.p_Tsat(p)
    hs= w.px(p,1).h

    rho2= ['%.3f'% elem for elem in rhos]
    u2= ['%.1f'% elem for elem in us]
    T2= ['%.2f'% elem for elem in Ts]
    h2= ['%.1f'% elem for elem in hs]


    for i in range(len(p)) :
        V.write("\n"+str(p[i]) + " & " +str(T1[i])   + "&"   +str(rho1[i]) + \
            " & " + str(rho2[i])+" & "  +str(u1[i])+" & "+ str(u2[i])+ " & "+
            str(h1[i]) +" & "+ str(h2[i])+"\\\ ")
    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam ($7.5$ $to$ $30$ $bar$)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n $P$  &  $T$ & $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    "\n $[bar]$ &  $[°C]$ &   $[kg/m^3]$ & $[kg/m^3]$ & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] \\\ "
    "\\"
    "\\")
    p= np.arange(30.00,90.00,2)

    H= w.px(p,0).h
    rhow= w.px(p,0).rho
    uw= w.px(p,0).u
    Tw= w.p_Tsat(p)
    hw= w.px(p,0).h

    rho1= ['%.1f'% elem for elem in rhow]
    u1= ['%.1f'% elem for elem in uw]
    T1= ['%.2f'% elem for elem in Tw]
    h1= ['%.1f'% elem for elem in hw]


    rhos= w.px(p,1).rho
    us= w.px(p,1).u
    Ts= w.p_Tsat(p)
    hs= w.px(p,1).h

    rho2= ['%.3f'% elem for elem in rhos]
    u2= ['%.1f'% elem for elem in us]
    T2= ['%.2f'% elem for elem in Ts]
    h2= ['%.1f'% elem for elem in hs]


    for i in range(len(p)) :
        V.write("\n"+str(p[i]) + " & " +str(T1[i])   + "&"   +str(rho1[i]) + \
            " & " + str(rho2[i])+" & "  +str(u1[i])+" & "+ str(u2[i])+ " & "+
            str(h1[i]) +" & "+ str(h2[i])+"\\\ ")
    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam ($30$ $to$ $88$ $bar$)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n $P$  &  $T$ & $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    "\n $[bar]$ &  $[°C]$ &   $[kg/m^3]$ & $[kg/m^3]$ & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] \\\ "
    "\\"
    "\\")
    p1= np.arange(88.00,100.00,2)
    p2= np.arange(100.00,221.00,5)
    p=np.hstack([p1,p2])

    H= w.px(p,0).h
    rhow= w.px(p,0).rho
    uw= w.px(p,0).u
    Tw= w.p_Tsat(p)
    hw= w.px(p,0).h

    rho1= ['%.1f'% elem for elem in rhow]
    u1= ['%.1f'% elem for elem in uw]
    T1= ['%.2f'% elem for elem in Tw]
    h1= ['%.1f'% elem for elem in hw]


    rhos= w.px(p,1).rho
    us= w.px(p,1).u
    Ts= w.p_Tsat(p)
    hs= w.px(p,1).h

    rho2= ['%.3f'% elem for elem in rhos]
    u2= ['%.1f'% elem for elem in us]
    T2= ['%.2f'% elem for elem in Ts]
    h2= ['%.1f'% elem for elem in hs]


    for i in range(len(p)) :
        V.write("\n"+str(p[i]) + " & " +str(T1[i])   + "&"   +str(rho1[i]) + \
            " & " + str(rho2[i])+" & "  +str(u1[i])+" & "+ str(u2[i])+ " & "+
            str(h1[i]) +" & "+ str(h2[i])+"\\\ ")


    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam ($88$ $to$ $220$ $bar$)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{landscape}"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{ c c c c c c c c c c c c c c c c c }"
    "\n $p$/$[bar]$ & 0.1 & 0.5 & 1.0 & 5.0 & 10.0 & 20.0 & 40.0 & 60.0 & 80.0 & 100.0 & 150.0 & 200.0 & 250.0 & 300.0 \\\ "
    "\n $ T_{sat} $/$[°C]$ & 45.8 & 81.3 & 99.6 & 151.8 & 179.9 & 212.4 & 250.4 & 275.6 & 295.0 & 311.0 & 342.2 & 365.7 & 377.0 & 377.0 \\\ "
    "\n\\hline"
    "\n  & & & & & & & \multicolumn{2}{c}{Density / $[kg/m^3]$} & & & & & & & \\\ "
    
    "\n $T$  &  & & & & & & & & & & & & & & & \\\ "
    "\n $°C$ &  & & & & &  & & & & & & & & & \\\ "
    "\\"
    "\\")
    p = np.array([0.1,0.5,1,5,10,20,40,60,80,100,150,200,250,300])
    T1= np.arange(0,300,25)
    T2= np.arange(300,800,50)
    T=np.hstack([T1,T2])
    
    for i in range(len(T)) :
        V.write("\n"+str(T[i]) + " & " + str('%.2f'% w.pT(p[0],T[i]).rho)   + "&"   +str('%.2f'% w.pT(p[1],T[i]).rho) + \
            " & " + str('%.2f'% w.pT(p[2],T[i]).rho)+" & "  + str('%.2f'% w.pT(p[3],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[4],T[i]).rho)+ " & "+ \
            str('%.2f'% w.pT(p[5],T[i]).rho) +" & "+ str('%.2f'% w.pT(p[6],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[7],T[i]).rho)+" & "+\
            str('%.2f'% w.pT(p[8],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[9],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[10],T[i]).rho)+\
                " & "+ str('%.2f'% w.pT(p[11],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[12],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[13],T[i]).rho)+\
                    "\\\ ")
    
    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Density of water and steam}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\end{landscape}"
    "\n\pagebreak"
    "\n\n\\begin{landscape}"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{ c c c c c c c c c c c c c c c c c }"
    "\n $p$/$[bar]$ & 0.1 & 0.5 & 1.0 & 5.0 & 10.0 & 20.0 & 40.0 & 60.0 & 80.0 & 100.0 & 150.0 & 200.0 & 250.0 & 300.0 \\\ "
    "\n $ T_{sat} $/$[°C]$ & 45.8 & 81.3 & 99.6 & 151.8 & 179.9 & 212.4 & 250.4 & 275.6 & 295.0 & 311.0 & 342.2 & 365.7 & 377.0 & 377.0 \\\ "
    "\n\\hline"
    "\n  & & & & & & & \multicolumn{2}{c}{Enthalpy / $[kJ/kg]$} & & & & & & & \\\ "
    
    "\n $T$  &  & & & & & & & & & & & & & & & \\\ "
    "\n $°C$ &  & & & & & & & & & & & & & & & \\\ "
    "\\"
    "\\")

    for i in range(len(T)) :
        V.write("\n"+str(T[i]) + " & " + str('%.2f'% w.pT(p[0],T[i]).h)   + "&"   +str('%.2f'% w.pT(p[1],T[i]).h) + \
            " & " + str('%.2f'% w.pT(p[2],T[i]).h)+" & "  + str('%.2f'% w.pT(p[3],T[i]).h)+" & "+ str('%.2f'% w.pT(p[4],T[i]).h)+ " & "+ \
            str('%.2f'% w.pT(p[5],T[i]).h) +" & "+ str('%.2f'% w.pT(p[6],T[i]).h)+" & "+ str('%.2f'% w.pT(p[7],T[i]).h)+" & "+\
            str('%.2f'% w.pT(p[8],T[i]).h)+" & "+ str('%.2f'% w.pT(p[9],T[i]).h)+" & "+ str('%.2f'% w.pT(p[10],T[i]).h)+\
                " & "+ str('%.2f'% w.pT(p[11],T[i]).h)+" & "+ str('%.2f'% w.pT(p[12],T[i]).h)+" & "+ str('%.2f'% w.pT(p[13],T[i]).h)+\
                    "\\\ ")
    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Enthalpy of water and steam}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\end{landscape}"
    "\n\pagebreak"
    "\n\n\\begin{landscape}"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{ c c c c c c c c c c c c c c c c c }"
    "\n $p$/$[bar]$ & 0.1 & 0.5 & 1.0 & 5.0 & 10.0 & 20.0 & 40.0 & 60.0 & 80.0 & 100.0 & 150.0 & 200.0 & 250.0 & 300.0 \\\ "
    "\n $ T_{sat} $/$[°C]$ & 45.8 & 81.3 & 99.6 & 151.8 & 179.9 & 212.4 & 250.4 & 275.6 & 295.0 & 311.0 & 342.2 & 365.7 & 377.0 & 377.0 \\\ "
    "\n\\hline"
    "\n  & & & & & & & \multicolumn{2}{c}{Internal Energy / $[kJ/kg]$} & & & & & & & \\\ "
    
    "\n $T$  &  & & & & & & & & & & & & & & & \\\ "
    "\n $°C$ &  & & & & & & & & & & & & & & & \\\ "
    "\\"
    "\\")
    for i in range(len(T)) :
        V.write("\n"+str(T[i]) + " & " + str('%.2f'% w.pT(p[0],T[i]).u)   + "&"   +str('%.2f'% w.pT(p[1],T[i]).u) + \
            " & " + str('%.2f'% w.pT(p[2],T[i]).u)+" & "  + str('%.2f'% w.pT(p[3],T[i]).u)+" & "+ str('%.2f'% w.pT(p[4],T[i]).u)+ " & "+ \
            str('%.2f'% w.pT(p[5],T[i]).u) +" & "+ str('%.2f'% w.pT(p[6],T[i]).u)+" & "+ str('%.2f'% w.pT(p[7],T[i]).u)+" & "+\
            str('%.2f'% w.pT(p[8],T[i]).u)+" & "+ str('%.2f'% w.pT(p[9],T[i]).u)+" & "+ str('%.2f'% w.pT(p[10],T[i]).u)+\
                " & "+ str('%.2f'% w.pT(p[11],T[i]).u)+" & "+ str('%.2f'% w.pT(p[12],T[i]).u)+" & "+ str('%.2f'% w.pT(p[13],T[i]).u)+\
                    "\\\ ")
    

    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Internal energy of water and steam}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\end{landscape}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c }"
    "\n\\hline"
    "\n $T$ & $cp$ & $rho$ & $mu$ & $k$  \\\ "
    "\n $[°C]$ &  $[J/kg$ x $K]$ & $[kg/m^3]$ & $[Pa$ x $s]$ & $[W/m$ x $K]$ \\\ "
    "\\"
    "\\")
    T1= np.arange(0.00,100.00,5)
    T2= np.arange(100.00,160.00,10)
    T3= np.arange(160.00,370.00,20)
    T=np.hstack([T1,T2,T3])

    cpX= w.Tx(T,0).cp
    rhoX= w.Tx(T,0).rho
    muX= w.Tx(T,0).mu
    kX= w.Tx(T,0).k


    Xcp= ['%.3f'% elem for elem in cpX]
    Xrho= ['%.1f'% elem for elem in rhoX]
    Xmu= ['%.3e'% elem for elem in muX]
    Xk= ['%.3f'% elem for elem in kX]


    for i in range(len(T)) :
        V.write("\n"+str(T[i]) + " & " +str(Xcp[i])   + "&"   +str(Xrho[i]) + \
            " & " + str(Xmu[i])+" & "  +str(Xk[i])+"\\\ ")


    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Transport properties Saturated of Water (Saturated liquid)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\n\n\end{document}")

    V.close()

    if is_makepdf == True:
        os.system("pdflatex steamtab.tex")
        os.system("pdflatex steamtab.tex")# run again for table of contents
    if is_cleanup == True:
        os.remove("steamtab.tex")
        os.remove("steamtab.log")
        os.remove("steamtab.aux")
    if is_show == True:
        os.system("evince steamtab.pdf")
