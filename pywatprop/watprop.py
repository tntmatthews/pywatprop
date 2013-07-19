# -*- coding: utf-8 -*-  
import numpy as np
import freesteam
__all__= ['watprop'] 

class propack:
    """ Used as internal strucutre to store properties"""
    def __repr__(self):
        attrs = vars(self)
        retstr = ', '.join("%s: %s" % item for item in attrs.items())
        return retstr

class ActiveProps:
    """ Used internally to keep up with properties to calc/show """
    def __init__(self):
        self.b_h = True
        self.b_rho = True
        self.b_cp = True
        self.b_x = True
        self.b_u = True
        self.b_T = True
        self.b_p = True
        self.b_k = True
        self.b_mu = True
        self.b_s = True


    def __repr__(self):
        retstr = "Properties currently calculated:\n"
        retstr += "enthalpy (b_h): %s\n"% self.b_h
        retstr += "density (b_rho): %s\n"% self.b_rho
        retstr += "specific heat (b_cp): %s\n"% self.b_cp
        retstr += "quality (b_x): %s\n"% self.b_x
        retstr += "specific energy (b_u): %s\n"% self.b_u
        retstr += "pressure (b_p): %s\n"% self.b_p
        retstr += "Dynamic viscosity (b_mu): %s\n"% self.b_mu        
        retstr += "Thermal conductivity (b_k): %s\n"% self.b_k
        retstr += "entropy (b_s): %s\n"% self.b_s

        return retstr

class UnitType:
    """
    defines the unit type and corresponding units
    """
    def __init__(self):
        self.type = "altSI"
        print "ok"

    def __repr__(self):
        if self.type == 'altSI':
            retstr = "Property Units for altSI:"
            retstr += "pressure: bar\n"
            retstr += "temperature: C\n"
            retstr += "enthalpy: kJ/kg\n"
            retstr += "specific energy: kJ/kg\n"
            retstr += "density: kg/m3\n"
            retstr += "specific heat: kJ/kg-C\n"
            retstr += "Thermal conductivity: W/m.C\n"
            retstr += "Dynamic viscosity: bar.s\n"
            retstr += "entropy: J/K\n"
        elif self.type == 'SI':
            retstr = "Property Units for SI:\n"
            retstr += "pressure: Pa\n"
            retstr += "temperature: K\n"
            retstr += "enthalpy: J/kg\n"
            retstr += "specific energy: J/kg\n"
            retstr += "density: kg/m3\n"
            retstr += "specific heat: J/kg-K\n"
            retstr += "Thermal conductivity: W/m.k\n"
            retstr += "Dynamic viscosity: Pa.s\n"
            retstr += "entropy: J/K\n"
        else:
            retstr = "Unit Type Not Recognized\n"
            retstr += "All calculations will be performed for SI units"

        return retstr


class watprop(object):
    """
    *This class contains the water properties functions.
    Watprop class include functions which provide steam properties (pressure , temperature, enthalpy, density, etc.). 
    Once initiated the resulting object is used to make calls to obtain
    desired properties*
    """
    def __init__ (self, unittype ="altSI" , b_h= True ,b_rho=True ,b_cp=True, \
        b_x=True ,b_u=True,b_T=True,b_p=True,b_k=True,b_mu=True,b_s=True):
        """
        :param b__: b_h, b_rho, b_cp, b_x, b_u, b_T, b_p, b_k, b_mu, b_s
        :type  b__: =True Or =False (default =True)
        
        :param unittype: =altSI Or =SI (default =altSI)
        :type  unittype: units system 

        choose the properties you want from :

        +-----------------------------+
        | h  | enthalpy               |
        +-----------------------------+
        | cp | Isobaric heat capacity |
        +-----------------------------+
        |rho | Density                |
        +-----------------------------+
        | mu | Dynamic viscosity      |
        +-----------------------------+
        | k  | Thermal conductivity   |
        +-----------------------------+
        | p  | pressure               |
        +-----------------------------+
        | T  | Temperature            |
        +-----------------------------+
        | s  | Entropy                |
        +-----------------------------+


        and do:
        watprop( unittype = *"SI" or "altSI"*,b_*selectedproperties*)
        for example if you want only enthalpy and Density in SI units , first import watprop module, 
        then specify which properties you want, example::
                    
            import Pywatprop
            w=watprop.watprop(unittype="SI",b_h=True,b_rho=True,b_cp=False,b_x=False,
                b_u=False,b_T=False,b_p=False,b_k=False,b_mu=False,b_s=False)
        
        *The default output is: Alternate SI units, and all properties the specified function is able to give.**

        """

        self.active_props = ActiveProps()

        self.active_props.b_h = b_h
        self.active_props.b_rho = b_rho
        self.active_props.b_u = b_u
        self.active_props.b_x = b_x
        self.active_props.b_cp = b_cp
        self.active_props.b_T = b_T
        self.active_props.b_p = b_p
        self.active_props.b_mu = b_mu
        self.active_props.b_k = b_k
        self.active_props.b_s = b_s
        
        self.units=UnitType()
        self.units.type = unittype

        def _pT_h(p,T):
            """ given pressure and Temperature, returns enthalpy """
            fs_T=np.float(T)
            fs_p=np.float(p)
            if self.units.type == "altSI":
                fs_T=T+273.15
                fs_p=p*1e5        
            fs_val = freesteam.steam_pT(fs_p, fs_T).h
            val=fs_val
            if self.units.type == "altSI":
                val=fs_val/1000.
            return val
        
        def _pT_rho(p,T):
            """ given pressure and Temperature, return density """
            fs_T=np.float(T)
            fs_p=np.float(p)
            if self.units.type == "altSI": 
                fs_T=T+273.15
                fs_p=p*1e5        
            fs_val = freesteam.steam_pT(fs_p, fs_T).rho
            val=fs_val
            return val

        def _pT_u(p,T):
            """ given pressure and Temperature, return specific energy """
            fs_T=np.float(T)
            fs_p=np.float(p)
            if self.units.type == "altSI": 
                fs_T=T+273.15
                fs_p=p*1e5         
            fs_val = freesteam.steam_pT(fs_p, fs_T).u
            val=fs_val
            if self.units.type=="altSI":
                val=fs_val/1000
            return val
        
        def _pT_x(p,T):
            """ given pressure and Temperature, return quality """
            if (np.isnan(p) or np.isnan(T)) :
                return np.nan
            fs_T=np.float(T)
            fs_p=np.float(p)
            if self.units.type == "altSI": 
                fs_T=T+273.15
                fs_p=p*1e5         
            fs_val = freesteam.steam_pT(fs_p, fs_T).x
            val=fs_val
            return val

        def _pT_s(p,T):
            """ given pressure and Temperature, return entropy """
            if (np.isnan(p) or np.isnan(T)) :
                return np.nan
            fs_T=np.float(T)
            fs_p=np.float(p)
            if self.units.type == "altSI": 
                fs_T=T+273.15
                fs_p=p*1e5         
            fs_val = freesteam.steam_pT(fs_p, fs_T).s
            val=fs_val
            return val
        
        def _px_h(p,x=0):
            """ given pressure and quality, return enthalpy """
            fs_p=np.float(p)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_p = p*1E5    
            fs_val = freesteam.Tsat_p(fs_p)
            val=freesteam.steam_Tx(fs_val,fs_x).h
            if self.units.type=="altSI":
                val=val/1000
            return val

        def _px_u(p,x=0):
            """ given pressure and enthalpy, return specific energy """
            fs_p=np.float(p)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_p = p*1E5        
            fs_val = freesteam.Tsat_p(fs_p)
            val=freesteam.steam_Tx(fs_val,fs_x).u
            if self.units.type=="altSI":
                val=val/1000
            return val

        def _px_s(p,x=0):
            """ given pressure and enthalpy, return specific entropy """
            fs_p=np.float(p)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_p = p*1E5        
            fs_val = freesteam.Tsat_p(fs_p)
            val=freesteam.steam_Tx(fs_val,fs_x).s
            return val

        def _px_rho(p,x=0):
            """ given pressure and quality, return density """
            fs_p=np.float(p)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_p = p*1E5       
            fs_val = freesteam.Tsat_p(fs_p)
            val=freesteam.steam_Tx(fs_val,fs_x).rho
            return val
        
        def _Tx_h(T,x):
            """ given Temperature and quality, return enthalpy """
            fs_T=np.float(T)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_T = T+273.15
            val=freesteam.steam_Tx(fs_T,fs_x).h
            if self.units.type=="altSI":
                val=val/1000
            return val

        def _Tx_u(T,x):
            """ given Temperature and quality, return specific energy """
            fs_T=np.float(T)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_T = T+273.15       
            val=freesteam.steam_Tx(fs_T,fs_x).u
            if self.units.type=="altSI":
                val=val/1000
            return val

        def _Tx_rho(T,x):
            """ given Temperature and quality, return density """
            fs_T=np.float(T)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_T = T+273.15           
            val=freesteam.steam_Tx(fs_T,fs_x).rho
            return val

        def _Tx_s(T,x):
            """ given Temperature and quality, return entropy """
            fs_T=np.float(T)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_T = T+273.15           
            val=freesteam.steam_Tx(fs_T,fs_x).s
            return val

        def _Tx_cp(T,x):
            """ given Temperature and quality, return Isobaric heat capacity"""
            fs_T=np.float(T)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_T = T+273.15           
            val=freesteam.steam_Tx(fs_T,fs_x).cp
            if self.units.type=="altSI":
                val=val/1000
            return val
        def _Tx_mu(T,x):
            """ given Temperature and quality, return Dynamic viscosity """
            fs_T=np.float(T)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_T = T+273.15           
            val=freesteam.steam_Tx(fs_T,fs_x).mu
            return val
        def _Tx_k(T,x):
            """ given Temperature and quality, return Thermal conductivity """
            fs_T=np.float(T)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_T = T+273.15           
            val=freesteam.steam_Tx(fs_T,fs_x).k
            return val

        def _Tx_p(T,x):
            """
            given Temperature, return saturation pressure
            seems like a duplicate to _psat_T !!!
            """           
            fs_T=np.float(T)
            fs_x=np.float(x)
            if self.units.type == "altSI": 
                fs_T = T+273.15        
            val=freesteam.steam_Tx(fs_T,fs_x).p
            if self.units.type=="altSI":
                val=val/1E5
            return val


        def _psat_T(T):
            """ given Temperature, return saturation pressure """
            fs_T=np.float(T)
            if self.units.type == "altSI": 
                fs_T=T+273.15        
            fs_val = freesteam.psat_T(fs_T)
            val=fs_val
            if self.units.type=="altSI":
                val=fs_val/1E5
            return val
       

        def _Tsat_p(p):
            """ given pressure, return saturation Temperature """
            fs_p=np.float(p)
            if self.units.type == "altSI": 
                fs_p = p*1E5       
            fs_val = freesteam.Tsat_p(fs_p)
            val=fs_val
            if self.units.type=="altSI":
                val=fs_val-273.15
            return val

        # Vectorization of each of the internal functions above
        self._pT_h=_pT_h
        self._vpT_h=np.vectorize(_pT_h)

        self._pT_rho=_pT_rho
        self._vpT_rho=np.vectorize(_pT_rho)

        self._pT_u=_pT_u
        self._vpT_u=np.vectorize(_pT_u)

        self._pT_x=_pT_x
        self._vpT_x=np.vectorize(_pT_x)

        self._pT_s=_pT_s
        self._vpT_s=np.vectorize(_pT_s)

        self._px_h=_px_h
        self._vpx_h=np.vectorize(_px_h)

        self._px_u=_px_u
        self._vpx_u=np.vectorize(_px_u)

        self._px_s=_px_s
        self._vpx_s=np.vectorize(_px_s)

        self._px_rho=_px_rho
        self._vpx_rho=np.vectorize(_px_rho)

        self._Tx_h=_Tx_h
        self._vTx_h=np.vectorize(_Tx_h)

        self._Tx_u=_Tx_u
        self._vTx_u=np.vectorize(_Tx_u)

        self._Tx_rho=_Tx_rho
        self._vTx_rho=np.vectorize(_Tx_rho)

        self._Tx_mu=_Tx_mu
        self._vTx_mu=np.vectorize(_Tx_mu)

        self._Tx_k=_Tx_k
        self._vTx_k=np.vectorize(_Tx_k)

        self._Tx_s=_Tx_s
        self._vTx_s=np.vectorize(_Tx_s)

        self._Tx_cp=_Tx_cp
        self._vTx_cp=np.vectorize(_Tx_cp)

        self._Tx_p=_Tx_p
        self._vTx_p=np.vectorize(_Tx_p)

        self._psat_T=_psat_T
        self._vpsat_T=np.vectorize(_psat_T)

        self._Tsat_p=_Tsat_p
        self._vTsat_p=np.vectorize(_Tsat_p)


    def px(self,press,qual=0):
        """
        *pressure and temperature give output a steam state*

        :param pressure: Pressure
        :type  pressure: Single values or arrays

        :param Quality: quality
        :type  Quality: Single values or arrays

        :return: With .h for Enthalpy 
                      .u for Internal energy 
                      .x for Quality 
                      .rho for Density 
                      .T for Saturation Temperature
                      .s for Entropy
        :rtype:  Water properties for the condition defined by the input

        :todo: T=[single or array or values],x=[single or array or values] 
                given pressure ,return enthalpy,internal energy, quality, density, or saturation temperature

        
        example for enthalpy from an array of 2 values:
        ::
                    
            import pywatprop
            w=pywatprop.watprop(unittype="SI")
            state=w.px([10,20],[0,0])
            print state.h
                 
        """
        if np.size(qual)<>1 and np.size(qual)<>np.size(press) :
            raise BaseException( "Inconsistent lenght for Temp and qual parameters")
        if np.size(qual)==1 and np.size(press)>1:
            qual=np.ones(np.size(press))*qual 
            
        pxprop = propack()

        if self.active_props.b_h == True :
            try:
                xhtemp = self._px_h(press,qual)
            except:
                xhtemp = self._vpx_h(press,qual)
            pxprop.h=xhtemp
        
        if self.active_props.b_u == True :
            try:
                xutemp = self._px_u(press,qual)
            except:
                xutemp = self._vpx_u(press,qual)
            pxprop.u=xutemp


        if self.active_props.b_s == True :
            try:
                xstemp = self._px_s(press,qual)
            except:
                xstemp = self._vpx_s(press,qual)
            pxprop.s=xstemp
        
        if self.active_props.b_rho == True :
            try:
                xrhotemp = self._px_rho(press,qual)
            except:
                xrhotemp = self._vpx_rho(press,qual)
            pxprop.rho=xrhotemp

        if self.active_props.b_T == True :
            try:
                xTtemp = self._Tsat_p(press)
            except:
                xTtemp = self._vTsat_p(press)
            pxprop.T = xTtemp

        return pxprop


    def Tx(self,Temp,qual=0):
        """
        *pressure and temperature give output a steam state*

        :param Temperature: a single floating point number or an array of Temperature
        :type  Temperature: Single values or arrays
        
        :param Quality: Quality (default=0)
        :type  Quality: Single values or arrays

        :return: Enthalpy, Internal energy, Quality, Density, Saturation pressure, Thermal conductivity, Dynamic viscosity, Entropy
        :rtype: Single values or arrays

        example for enthalpy from an array of 2 values::
                    
            import pywatprop
            w=pywatprop.watprop(unittype="SI")
            state=w.Tx([300,400],[0,0])
            print state.h

        """
        if np.size(qual)<>1 and np.size(qual)<>np.size(Temp) :
            raise BaseException( "Inconsistent lenght for Temp and qual parameters")
        if np.size(qual)==1 and np.size(Temp)>1:
            qual=np.ones(np.size(Temp))*qual 

        Txprop = propack()

        if self.active_props.b_h== True :
            try:
                xhtemp = self._Tx_h(Temp,qual)
            except:
                xhtemp = self._vTx_h(Temp,qual)
            Txprop.h=xhtemp
        if self.active_props.b_u== True :
            try:
                xutemp = self._Tx_u(Temp,qual)
            except:
                xutemp = self._vTx_u(Temp,qual)
            Txprop.u=xutemp
        if self.active_props.b_rho== True :
            try:
                xrhotemp = self._Tx_rho(Temp,qual)
            except:
                xrhotemp = self._vTx_rho(Temp,qual)
            Txprop.rho=xrhotemp
        if self.active_props.b_k== True :
            try:
                xktemp = self._Tx_k(Temp,qual)
            except:
                xktemp = self._vTx_k(Temp,qual)
            Txprop.k=xktemp
        if self.active_props.b_s== True :
            try:
                xstemp = self._Tx_s(Temp,qual)
            except:
                xstemp = self._vTx_s(Temp,qual)
            Txprop.s=xstemp
        if self.active_props.b_mu== True :
            try:
                xmutemp = self._Tx_mu(Temp,qual)
            except:
                xmutemp = self._vTx_mu(Temp,qual)
            Txprop.mu=xmutemp
        if self.active_props.b_cp== True :
            try:
                xcptemp = self._Tx_cp(Temp,qual)
            except:
                xcptemp = self._vTx_cp(Temp,qual)
            Txprop.cp=xcptemp
        if self.active_props.b_p == True :
            try:
                xptemp = self._Tx_p(Temp,qual)
            except:
                xptemp = self._vTx_p(Temp,qual)
            Txprop.p=xptemp

        return Txprop


    def pT(self,press,temp) :
        """
        *pressure and temperature give output a steam state*

        :param p,T: Pressure and Temperature
        :type  p,T: Single values or arrays

        :return: .h for Enthalpy
                .u for internal energy
                .x for quality
                .rho for density
                .s for Entropy

        :rtype: Water properties defined for the stated defined by the input
        
        Example::
                    
            import pywatprop
            w=pywatprop.watprop(unittype="SI")
            state=w.pT([10,20],[300,400])
            print state.h
                
        """
        props = propack()
        
        if self.active_props.b_h== True :
            try:
                htemp = self._pT_h(press,temp)
            except:
                htemp = self._vpT_h(press,temp)
            props.h=htemp

        if self.active_props.b_rho== True :
            try:
                rhotemp = self._pT_rho(press,temp)
            except:
                rhotemp = self._vpT_rho(press,temp)
            props.rho=rhotemp

        if self.active_props.b_u== True :
            try:
                utemp = self._pT_u(press,temp)
            except:
                utemp = self._vpT_u(press,temp) 
            props.u=utemp

        if self.active_props.b_s== True :
            try:
                stemp = self._pT_s(press,temp)
            except:
                stemp = self._vpT_s(press,temp) 
            props.s=stemp
        

        if self.active_props.b_x== True :
            try:
                xtemp = self._pT_x(press,temp)
            except:
                xtemp = self._vpT_x(press,temp) 
            props.x=xtemp
        return props
    
    def T_psat(self,temp) :
        """
        *Saturation temperature gives output pressure*

        :param Temperature: A single floating point number or an array of pressure
        :type  Temperature: Single values or arrays

        :return: Saturation pressure
        :rtype: Single values or arrays

        example for an array of 2 Temperatures in altSI units:
        ::
                    
            import pywatprop
            w=pywatprop.watprop()
            P=w.T_psat([100,200])
            print P
        
     
        """

        try:
            ptemp = self._psat_T(temp)
        except:
            ptemp = self._vpsat_T(temp)
        return ptemp


    def p_Tsat(self,press) :
        """
        *Saturation pressure gives output temperature*

        :param pressure: A single floating point number or an array of pressure
        :type  pressure: Single values or arrays

        :return: Saturation Temperature
        :rtype: Single values or arrays

        example for an array of 2 Pressures in SI units:
        ::
                    
            import pywatprop
            w=pywatprop.watprop(unittype="SI")
            T=w.p_Tsat([100,200])
            print T
        
        
        """
        try:
            Ttemp = self._Tsat_p(press)
        except:
            Ttemp = self._vTsat_p(press)
        return Ttemp

 