#!/usr/bin/env python
# encoding: utf-8

name = "BoronAllendorf"
shortDesc = u"Boron"
longDesc = u"""
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 

Experimental for Boron Nitride CVD reactions.
"""
entry(
    index = 1,
    label = "Cl3BNH3 <=> BCl3 + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 's^-1'), n=0, Ea=(7.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "Cl3BNH3 <=> Cl2BNH2 + HCl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.0e+13, 's^-1'), n=0, Ea=(38.0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "BCl3 + NH3 <=> Cl2BNH2 + HCl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.21e+11, 's^-1'), n=0, Ea=(8.35, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "Cl2BNH2 <=> ClBNH + HCl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.89e+14, 's^-1'), n=0, Ea=(79.0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "Cl2BNH2 + NH3 <=> ClB(NH2)2 + HCl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.88e+11, 's^-1'), n=0, Ea=(18.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "ClB(NH2)2 + NH3 <=> B(NH2)3 + HCl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.66e+12, 's^-1'), n=2, Ea=(19.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "BCl3 <=> BCl2 + Cl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.86e+15, 's^-1'), n=0, Ea=(113.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "BCl2 <=> BCl + Cl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.25e+15, 's^-1'), n=0, Ea=(76.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "BCl3 + H <=> BCl2 + HCl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.00e+14, 's^-1'), n=0, Ea=(12, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "BCl + HCl <=> BCl2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.23e+13, 's^-1'), n=0, Ea=(24.2, 'kcal/mol'), T0=(1, 'K')),
)


