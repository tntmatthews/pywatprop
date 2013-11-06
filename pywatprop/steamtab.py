# -*- coding: utf-8 -*-  

import pywatprop
import numpy as np
import os

def steamtab(units='altSI', is_makepdf=True, is_cleanup=True, is_show = True):
    """
    Returns a steam table based upon the watprop class which provides two benefits:
    1) a lookup table as a quick reference.
    2) verification against other sources.

    NOTE: Only setup to work with altSI and US units at this time
    """
    allowedtypes = ['US','altSI']
    if units not in allowedtypes:
        print "table printout limited to the following unit types: %s" % \
            allowedtypes
        return

    w=pywatprop.watprop(unittype=units)

    V= open ('steamtab.tex','w')

    T = np.arange(50,101,2)
    unitdescline = ''
    if units == "US":
        unitdescline = \
            "\n &  & \multicolumn{2}{c}{$ft^3/lbm$} & \multicolumn{2}{c}{$Btu/(lbm hr)$} &  \multicolumn{2}{c}{$Btu/(lbm hr)$} \\\ " + \
            "\n $Temp$  &  $Pressure$ & $water$ & $steam$ & $water$  & $steam$ & $water$ & $steam$ \\\ " + \
            "\n $°F$ &  $psia$ &   $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
        T = np.arange(50,211,5)
        T = np.append(T, [212.])
    elif units == "altSI":
        unitdescline = \
            "\n &  & \multicolumn{2}{c}{$m^3/kg$} & \multicolumn{2}{c}{$kJ/kg$} &  \multicolumn{2}{c}{$kJ/kg$} \\\ " + \
            "\n $Temp$  &  $Pressure$ & $water$ & $steam$ & $water$  & $steam$ & $water$ & $steam$ \\\ " + \
            "\n $°C$ &  $bar$ &   $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "

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
    +"\n\\ Calculated with pywatprop %s(freesteam v2.0) using the IAPWS-IF97 Industrial Formulation at "%pywatprop.__version__ + 
    "\n\\currenttime"
    "\n\end{center}"
    "\n\listoftables"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n &  &  \multicolumn{2}{c}{Specific volume} &  \multicolumn{2}{c}{Internal Energy} &  \multicolumn{2}{c}{Specific enthalpy} \\\ "
    + unitdescline +
    "\\"
    "\\")
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

    T = np.arange(100,401,10)
    unitdescline = ''
    if units == 'US':
        unitdescline = \
            "\n &  & \multicolumn{2}{c}{$ft^3/lbm$} & \multicolumn{2}{c}{$Btu/(hr F)$} &  \multicolumn{2}{c}{$Btu/(hr F)$} \\\ " + \
            "\n $Temp$  &  $Pressure$ & $water$ & $steam$ & $water$ & $steam$ & $water$ & $steam$ \\\ " + \
            "\n $[°F]$ &  $[psia]$ &   $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
        T = np.arange(220,801,20)
    elif units == 'altSI':
        unitdescline = \
            "\n &  & \multicolumn{2}{c}{$m^3/kg$} & \multicolumn{2}{c}{$kJ/kg$} &  \multicolumn{2}{c}{$kJ/kg$} \\\ " + \
            "\n $Temp$  &  $Pressure$ & $water$ & $steam$ & & & & \\\ " + \
            "\n $[°C]$ &  $[bar]$ &   $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "

    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam (Lower Temperatures)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n &  &  \multicolumn{2}{c}{Specific volume} &  \multicolumn{2}{c}{Internal Energy} &  \multicolumn{2}{c}{Specific enthalpy} \\\ "
    + unitdescline +
    "\\"
    "\\")
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

    p1= np.arange(1,2,0.100)
    p2= np.arange(2,5,0.200)
    p3= np.arange(5,7.5,0.500)
    p=np.hstack([p1,p2,p3])

    unitdescline = ''
    if units == 'US':
        unitdescline = \
            "\n $[psia]$ &  $[°F]$ &   $[lbm/ft^3]$ & $[lbm/ft^3]$ & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] \\\ "
        p1= np.arange(10,50,2)
        p2= np.arange(50,70,5)
        p3= np.arange(70,151,10)
        p=np.hstack([p1,p2,p3])
    elif units == 'altSI':
        unitdescline = \
            "\n $[bar]$ &  $[°C]$ &   $[kg/m^3]$ & $[kg/m^3]$ & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] \\\ "

    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam (Higher Temperatures)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n $Press$  &  $Temp$ & $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    + unitdescline +
    "\\"
    "\\")

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

    p1= np.arange(7.5,13,0.5)
    p2= np.arange(13,31,1)
    p=np.hstack([p1,p2])
    unitdescline = ''
    if units == 'US':
        unitdescline = \
            "\n $[psia]$ &  $[°F]$ &   $[lbm/ft^3]$ & $[lbm/ft^3]$ & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] \\\ " 

        p= np.arange(150,451,10)

    elif units == 'altSI':
        unitdescline = \
            "\n $[bar]$ &  $[°C]$ &   $[kg/m^3]$ & $[kg/m^3]$ & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] \\\ "

    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam (Low Pressures)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n $Press$  &  $Temp$ & $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    + unitdescline +
    "\\"
    "\\")

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

    p= np.arange(30.00,90.00,2)
    unitdescline = ''
    if units == 'US':
        unitdescline = \
            "\n $[psia]$ &  $[°F]$ &   $[lbm/ft^3]$ & $[lbm/ft^3]$ & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] \\\ "
        p= np.arange(450.0, 1301.0, 25)

    elif units == 'altSI':
        unitdescline = \
            "\n $[bar]$ &  $[°C]$ &   $[kg/m^3]$ & $[kg/m^3]$ & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] \\\ "

    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam (Mid-Pressures)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n $P$  &  $T$ & $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    + unitdescline +
    "\\"
    "\\")

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

    p1= np.arange(88.00,100.00,2)
    p2= np.arange(100.00,221.00,5)
    p=np.hstack([p1,p2])
    unitdescline = ''
    if units == 'US':
        unitdescline = \
            "\n $[psia]$ &  $[°F]$ &   $[lbm/ft^3]$ & $[lbm/ft^3]$ & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] & [$Btu/(lbm hr)$] \\\ "
        p1= np.arange(1300.00,1500,25)
        p2= np.arange(1500.00,3201.00,50)
        p=np.hstack([p1,p2])
    elif units == 'altSI':
        unitdescline = \
            "\n $[bar]$ &  $[°C]$ &   $[kg/m^3]$ & $[kg/m^3]$ & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] & [$kJ/kg$] \\\ "

    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam (Mid2-Pressures)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{c c c c c c c c }"
    "\n\\hline"
    "\n $Press$  &  $Temp$ & $\\rho_f$ & $\\rho_g$ & $u_f$ & $u_g$ & $h_f$ & $h_g$ \\\ "
    + unitdescline +
    "\\"
    "\\")

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

    unitdescline = ''
    p = np.array([0.1,0.5,1,5,10,20,40,60,80,100,150,200,250,300])
    T1= np.arange(0,300,25)
    T2= np.arange(300,800,50)
    T=np.hstack([T1,T2])
    if units == 'US':
        unitdescline = \
            "\n $p$/$[psia]$ & 1.0 & 10.0 & 14.7 & 25.0 & 100.0 & 250.0 & 500.0 & 750.0 & 1000.0 & 1500.0 & 2000.0 & 2250.0 & 2500.0 & 3000.0 \\\ " + \
            "\n $ T_{sat} $/$[°F]$ & 101.7 & 193.1 & 212.7 & 240.0 & 327.8 & 401.0 & 467.1 & 510.9 & 544.7 & 596.3 & 635.9 & 652.8 & 668.2 & 695.4 \\\ " + \
            "\n\\hline" + \
            "\n  & & & & & & & \multicolumn{2}{c}{Density / $[kg/m^3]$} & & & & & & & \\\ " + \
            "\n $T$  &  & & & & & & & & & & & & & & & \\\ " + \
            "\n $°F$ &  & & & & &  & & & & & & & & & \\\ "
        p = np.array([1,10,14.7,25,100,250,500,750,1000,1500,2000,2250,2500,3000])
        T1= np.arange(0,700,50)
        T2= np.arange(700,1400,100)
        T=np.hstack([T1,T2])
    elif units == 'altSI':
        unitdescline = \
            "\n $p$/$[bar]$ & 0.1 & 0.5 & 1.0 & 5.0 & 10.0 & 20.0 & 40.0 & 60.0 & 80.0 & 100.0 & 150.0 & 200.0 & 250.0 & 300.0 \\\ " + \
            "\n $ T_{sat} $/$[°C]$ & 45.8 & 81.3 & 99.6 & 151.8 & 179.9 & 212.4 & 250.4 & 275.6 & 295.0 & 311.0 & 342.2 & 365.7 & 377.0 & 377.0 \\\ " + \
            "\n\\hline" + \
            "\n  & & & & & & & \multicolumn{2}{c}{Density / $[kg/m^3]$} & & & & & & & \\\ " + \
            "\n $T$  &  & & & & & & & & & & & & & & & \\\ " + \
            "\n $°C$ &  & & & & &  & & & & & & & & & \\\ "
        # p, T1, T2 defined above

    V.write("\n\hline"
    "\n\end{tabular}"
    "\n\end{center}"
    "\n\caption{Saturated Water and Steam (High Pressures)}"
    "\n\label{table:inputparams}"
    "\n\end{table}"
    "\n\pagebreak"
    "\n\n\\begin{landscape}"
    "\n\n\\begin{table}[h]"
    "\n\n\\begin{center}"
    "\n\\begin{tabular}{ c c c c c c c c c c c c c c c c c }"
    + unitdescline +
    "\\"
    "\\")
    
    for i in range(len(T)) :
        V.write("\n"+str(T[i]) + " & " + str('%.2f'% w.pT(p[0],T[i]).rho)   + "&"   +str('%.2f'% w.pT(p[1],T[i]).rho) + \
            " & " + str('%.2f'% w.pT(p[2],T[i]).rho)+" & "  + str('%.2f'% w.pT(p[3],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[4],T[i]).rho)+ " & "+ \
            str('%.2f'% w.pT(p[5],T[i]).rho) +" & "+ str('%.2f'% w.pT(p[6],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[7],T[i]).rho)+" & "+\
            str('%.2f'% w.pT(p[8],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[9],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[10],T[i]).rho)+\
                " & "+ str('%.2f'% w.pT(p[11],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[12],T[i]).rho)+" & "+ str('%.2f'% w.pT(p[13],T[i]).rho)+\
                    "\\\ ")

    if units == 'US':
        unitdescline = \
            "\n $p$/$[psia]$ & 1.0 & 10.0 & 14.7 & 25.0 & 100.0 & 250.0 & 500.0 & 750.0 & 1000.0 & 1500.0 & 2000.0 & 2250.0 & 2500.0 & 3000.0 \\\ " + \
            "\n $ T_{sat} $/$[°F]$ & 101.7 & 193.1 & 212.7 & 240.0 & 327.8 & 401.0 & 467.1 & 510.9 & 544.7 & 596.3 & 635.9 & 652.8 & 668.2 & 695.4 \\\ " + \
            "\n\\hline" + \
            "\n  & & & & & & & \multicolumn{2}{c}{Enthalpy / $[Btu(lbm hr)]$} & & & & & & & \\\ " + \
            "\n $T$  &  & & & & & & & & & & & & & & & \\\ " + \
            "\n $°F$ &  & & & & & & & & & & & & & & & \\\ "
    elif units == 'altSI':
        unitdescline = \
            "\n $p$/$[bar]$ & 0.1 & 0.5 & 1.0 & 5.0 & 10.0 & 20.0 & 40.0 & 60.0 & 80.0 & 100.0 & 150.0 & 200.0 & 250.0 & 300.0 \\\ " + \
            "\n $ T_{sat} $/$[°C]$ & 45.8 & 81.3 & 99.6 & 151.8 & 179.9 & 212.4 & 250.4 & 275.6 & 295.0 & 311.0 & 342.2 & 365.7 & 377.0 & 377.0 \\\ " + \
            "\n\\hline" + \
            "\n  & & & & & & & \multicolumn{2}{c}{Enthalpy / $[kJ/kg]$} & & & & & & & \\\ " + \
            "\n $T$  &  & & & & & & & & & & & & & & & \\\ " + \
            "\n $°C$ &  & & & & & & & & & & & & & & & \\\ "
    
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
    + unitdescline +
    "\\"
    "\\")

    for i in range(len(T)) :
        V.write("\n"+str(T[i]) + " & " + str('%.2f'% w.pT(p[0],T[i]).h)   + "&"   +str('%.2f'% w.pT(p[1],T[i]).h) + \
            " & " + str('%.2f'% w.pT(p[2],T[i]).h)+" & "  + str('%.2f'% w.pT(p[3],T[i]).h)+" & "+ str('%.2f'% w.pT(p[4],T[i]).h)+ " & "+ \
            str('%.2f'% w.pT(p[5],T[i]).h) +" & "+ str('%.2f'% w.pT(p[6],T[i]).h)+" & "+ str('%.2f'% w.pT(p[7],T[i]).h)+" & "+\
            str('%.2f'% w.pT(p[8],T[i]).h)+" & "+ str('%.2f'% w.pT(p[9],T[i]).h)+" & "+ str('%.2f'% w.pT(p[10],T[i]).h)+\
                " & "+ str('%.2f'% w.pT(p[11],T[i]).h)+" & "+ str('%.2f'% w.pT(p[12],T[i]).h)+" & "+ str('%.2f'% w.pT(p[13],T[i]).h)+\
                    "\\\ ")

    if units == 'US':
        unitdescline = \
            "\n $p$/$[psia]$ & 1.0 & 10.0 & 14.7 & 25.0 & 100.0 & 250.0 & 500.0 & 750.0 & 1000.0 & 1500.0 & 2000.0 & 2250.0 & 2500.0 & 3000.0 \\\ " + \
            "\n $ T_{sat} $/$[°F]$ & 101.7 & 193.1 & 212.7 & 240.0 & 327.8 & 401.0 & 467.1 & 510.9 & 544.7 & 596.3 & 635.9 & 652.8 & 668.2 & 695.4 \\\ " + \
            "\n\\hline" + \
            "\n  & & & & & & & \multicolumn{2}{c}{Int Energy / $[Btu(lbm hr)]$} & & & & & & & \\\ " + \
            "\n $T$  &  & & & & & & & & & & & & & & & \\\ " + \
            "\n $°F$ &  & & & & & & & & & & & & & & & \\\ "
    elif units == 'altSI':
        unitdescline = \
            "\n $p$/$[bar]$ & 0.1 & 0.5 & 1.0 & 5.0 & 10.0 & 20.0 & 40.0 & 60.0 & 80.0 & 100.0 & 150.0 & 200.0 & 250.0 & 300.0 \\\ " + \
            "\n $ T_{sat} $/$[°C]$ & 45.8 & 81.3 & 99.6 & 151.8 & 179.9 & 212.4 & 250.4 & 275.6 & 295.0 & 311.0 & 342.2 & 365.7 & 377.0 & 377.0 \\\ " + \
            "\n\\hline" + \
            "\n  & & & & & & & \multicolumn{2}{c}{Int Energy / $[kJ/kg]$} & & & & & & & \\\ " + \
            "\n $T$  &  & & & & & & & & & & & & & & & \\\ " + \
            "\n $°C$ &  & & & & & & & & & & & & & & & \\\ "


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
    + unitdescline +
    "\\"
    "\\")
    for i in range(len(T)) :
        V.write("\n"+str(T[i]) + " & " + str('%.2f'% w.pT(p[0],T[i]).u)   + "&"   +str('%.2f'% w.pT(p[1],T[i]).u) + \
            " & " + str('%.2f'% w.pT(p[2],T[i]).u)+" & "  + str('%.2f'% w.pT(p[3],T[i]).u)+" & "+ str('%.2f'% w.pT(p[4],T[i]).u)+ " & "+ \
            str('%.2f'% w.pT(p[5],T[i]).u) +" & "+ str('%.2f'% w.pT(p[6],T[i]).u)+" & "+ str('%.2f'% w.pT(p[7],T[i]).u)+" & "+\
            str('%.2f'% w.pT(p[8],T[i]).u)+" & "+ str('%.2f'% w.pT(p[9],T[i]).u)+" & "+ str('%.2f'% w.pT(p[10],T[i]).u)+\
                " & "+ str('%.2f'% w.pT(p[11],T[i]).u)+" & "+ str('%.2f'% w.pT(p[12],T[i]).u)+" & "+ str('%.2f'% w.pT(p[13],T[i]).u)+\
                    "\\\ ")

    T1= np.arange(0.00,100.00,5)
    T2= np.arange(100.00,160.00,10)
    T3= np.arange(160.00,370.00,20)
    T=np.hstack([T1,T2,T3])
    if units == 'US':
        unitdescline = \
            "\n $[°F]$ &  $[Btu/(lbm F)]$ & $[lbm/ft^3]$ & $[lb/(ft^2 s)]$ & $[Btu/(hr ft F)]$ \\\ "
        T1= np.arange(0.00,200.00,10)
        T2= np.arange(200.00,300.00,20)
        T3= np.arange(300.00,700.00,50)
        T=np.hstack([T1,T2,T3])
    elif units == 'altSI':
        unitdescline = \
            "\n $[°C]$ &  $[J/kg$ x $K]$ & $[kg/m^3]$ & $[Pa$ x $s]$ & $[W/m$ x $K]$ \\\ "

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
    + unitdescline +
    "\\"
    "\\")

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
    "\n\caption{Transport properties of Water (Saturated liquid)}"
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