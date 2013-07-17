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
    """ Used internally to keep up with properties for calc/show """
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

        return retstr

class UnitType:
    """
    defines the unit type and corresponding units
    """
    def __init__(self):
        self.type = "altSI"

    def __repr__(self):
        if self.type == 'altSI\n':
            retstr = "Property Units for altSI:"
            retstr += "pressure: bar\n"
            retstr += "temperature: C\n"
            retstr += "enthalpy: kJ/kg\n"
            retstr += "specific energy: kJ/kg\n"
            retstr += "density: kg/m3\n"
            retstr += "specific heat: kJ/kg-C\n"
            retstr += "Thermal conductivity: W/m.C\n"
            retstr += "Dynamic viscosity: bar.s\n"
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
        else:
            retstr = "Unit Type Not Recognized\n"
            retstr += "All calculations will be performed for SI units"

        return retstr


class watprop(object):
    """
    This class contains the water properties functions.

    watprop class include functions which provide steam properties
    (pressure , temperature, enthalpy, density, etc.)

    Once initiated the resulting object is used to make calls to obtain
    desired properties.
    """
    def __init__ (self, unittype ="altSI" , b_h= True ,b_rho=True ,b_cp=True, \
        b_x=True ,b_u=True,b_T=True,b_p=True,b_k=True,b_mu=True):

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

        self._px_h=_px_h
        self._vpx_h=np.vectorize(_px_h)

        self._px_u=_px_u
        self._vpx_u=np.vectorize(_px_u)

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
        input:  pressure and quality
                both are an floating point number or an array of numbers
                quality can be a single value even if pressure is an array
        return: water properties for the condition defined by the input
                .h for Enthalpy
                .u for internal energy
                .x for quality
                .rho for density
                .T for saturation Temperature
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
        input: Temperature and quality
                both are an floating point number or an array of numbers
                quality can be a single value even if pressure is an array
        return: water properties for the condition defined by the input
                .h for Enthalpy
                .u for internal energy
                .x for quality
                .rho for density
                .p for saturation pressure
                .K for Thermal conductivity
                .mu for Dynamic viscosity
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
        This function calculates the enthalpy, quality, density, and internal energy from the pressure and the temperature

        input: pressure and Temperature
               a single floating point value for each or an array of values
               if an array, both arrays must be same length

        Return: properties defined for the stated defined by the input
                .h for Enthalpy
                .u for internal energy
                .x for quality
                .rho for density
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
        

        if self.active_props.b_x== True :
            try:
                xtemp = self._pT_x(press,temp)
            except:
                xtemp = self._vpT_x(press,temp) 
            props.x=xtemp
        return props
    
    def T_psat(self,temp) :
        """
        This function calculates the saturated pressure from the temperature

        input: temperature
               a single floating point number or an array of numbers

        returns: saturation pressure
        """
        try:
            ptemp = self._psat_T(temp)
        except:
            ptemp = self._vpsat_T(temp)
        return ptemp


    def p_Tsat(self,press) :
        """watprop function , works with arrays or single values

        This function calculates the temperature from the saturated pressure

        input: pressure
               a single floating point number or an array of numbers

        returns: saturation Temperature
        """
        try:
            Ttemp = self._Tsat_p(press)
        except:
            Ttemp = self._vTsat_p(press)
        return Ttemp

 
