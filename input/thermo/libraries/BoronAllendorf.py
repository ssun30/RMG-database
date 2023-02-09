#!/usr/bin/env python
# encoding: utf-8

name = "BoronAllendorf"
shortDesc = u"Boron"
longDesc = u"""
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 

Experimental for Boron Nitride CVD reactions.
"""
entry(
    index = 0,
    label = "BH3",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.32535003e+01, 0.17414763e-02, 0.94006960e-05, -0.98644881e-08, 0.30205618e-11, 0.10137202e+05, 0.32586092e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.14650198e+01, 0.10215915e-01, -0.53335935e-05, 0.13346981e-08, -0.13029262e-12, 0.10430268e+05, 0.11560353e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BH3-Allendorf""",
    longDesc = 
u"""
BH3 from 
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 1,
    label = "BH2",
    molecule = 
"""
1 B u1 p0 c0 {2,S} {3,S} 
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.37263717e+01, 0.11128168e-02, 0.17957147e-05, -0.10825122e-08, 0.43055770e-13, 0.36846964e+05, 0.17299717e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.25107703e+01, 0.50119927e-02, -0.24525447e-05, 0.57888467e-09, -0.53656168e-13, 0.37133057e+05, 0.78223818e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BH2-Allendorf""",
    longDesc = 
u"""
BH2 from 
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 2,
    label = "BH",
    molecule = 
"""
1 B u2 p0 c0 {2,S} 
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.37967940e+01, -0.21493190e-02, 0.48271230e-05, -0.32633751e-08, 0.73754692e-12, 0.50456201e+05, -0.53188944e+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.26605388e+01, 0.21187148e-02, -0.10617224e-05, 0.25523516e-09, -0.23996510e-13, 0.50694044e+05, 0.50109881e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BH-Allendorf""",
    longDesc = 
u"""
BH from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 3,
    label = "BCl3",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 Cl u0 p3 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.30803194e+01, 0.24319377e-01, -0.37301543e-04, 0.27382117e-07, -0.78218403e-11, -0.50379630e+05, 0.11589219e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.82753631e+01, 0.25203824e-02, -0.15105616e-05, 0.41696296e-09, -0.43717163e-13, -0.51419840e+05, -0.13349514e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BCl3-Allendorf""",
    longDesc = 
u"""
BCl3 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 4,
    label = "BCl2",
    molecule = 
"""
1 B u1 p0 c0 {2,S} {3,S} 
2 Cl u0 p3 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.28747005e+01, 0.14082895e-01, -0.21042366e-04, 0.15116765e-07, -0.42462241e-11, -0.51143865e+04, 0.12824085e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.59044924e+01, 0.16118626e-02, -0.97185633e-06, 0.26967602e-09, -0.28404116e-13, -0.57306237e+04, -0.17746236e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BCl2-Allendorf""",
    longDesc = 
u"""
BCl2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 5,
    label = "BCl",
    molecule = 
"""
1 B u2 p0 c0 {2,S} 
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.26499292e+01, 0.63301060e-02, -0.94302405e-05, 0.67394087e-08, -0.18821550e-11, 0.20996015e+05, 0.90569461e+01], Tmin=(298,'K'), Tmax=(1300,'K')),
            NASAPolynomial(coeffs=[0.40189145e+01, 0.71156845e-03, -0.43061708e-06, 0.11983297e-09, -0.12650592e-13, 0.20717417e+05, 0.24582053e+01], Tmin=(1300,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BCl-Allendorf""",
    longDesc = 
u"""
BCl from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 6,
    label = "BHCl2",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.329574,0.0332696,-3.88267e-05,2.20593e-08,-4.94837e-12,-113504,21.2017], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[9.80832,0.00328269,-1.34045e-06,2.43738e-10,-1.62862e-14,-116025,-27.0002], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-946.655,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = u"""BHCl2-Allendorf""",
    longDesc = 
u"""
BHCl2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 7,
    label = "BH2Cl",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.15680049e+01, 0.15354933e-01, -0.15741459e-04, 0.95308826e-08, -0.25380343e-11, -0.11241591e+05, 0.15338649e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.34456712e+01, 0.80121746e-02, -0.42576400e-05, 0.10808557e-08, -0.10673403e-12, -0.11649571e+05, 0.61778901e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BH2Cl-Allendorf""",
    longDesc = 
u"""
BH2Cl from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 8,
    label = "BHCl",
    molecule = 
"""
1 B u1 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.25206723e+01, 0.10250390e-01, -0.13488863e-04, 0.96905711e-08, -0.28210939e-11, 0.15110857e+05, 0.11982520e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.40140440e+01, 0.35951909e-02, -0.18835927e-05, 0.47214009e-09, -0.46106141e-13, 0.14826272e+05, 0.48983014e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BHCl-Allendorf""",
    longDesc = 
u"""
BHCl from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 9,
    label = "H3BNH3",
    molecule = 
"""
1 B u0 p0 c-1 {2,S} {3,S} {4,S} {5,S}
2 N u0 p0 c+1 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.19486989e+01, 0.20093319e-01, -0.50634675e-05, -0.33493641e-08, 0.17462886e-11, -0.11417782e+05, 0.12764981e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.22071150e+01, 0.21525925e-01, -0.10696339e-04, 0.25848974e-08, -0.24612315e-12, -0.11599960e+05, 0.10883752e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H3BNH3-Allendorf""",
    longDesc = 
u"""
H3BNH3 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 10,
    label = "H2BNH2",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.41936332e+00, 0.23120948e-01, -0.18491259e-04, 0.84716927e-08, -0.16998117e-11, -0.12695021e+05, 0.19007699e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.30438396e+01, 0.14103071e-01, -0.67818204e-05, 0.16085416e-08, -0.15269824e-12, -0.13307340e+05, 0.59425555e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H2BNH2-Allendorf""",
    longDesc = 
u"""
H2BNH2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 11,
    label = "H2BNH",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.24812213e+01, 0.15474766e-01, -0.14128864e-04, 0.79911700e-08, -0.20319425e-11, 0.21132870e+05, 0.12750733e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.39564653e+01, 0.95166114e-02, -0.47139857e-05, 0.11349029e-08, -0.10764237e-12, 0.20827617e+05, 0.56151721e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H2BNH-Allendorf""",
    longDesc = 
u"""
H2BNH from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 12,
    label = "HBNH2",
    molecule = 
"""
1 B u1 p0 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.12969619e+01, 0.18873270e-01, -0.18102730e-04, 0.10181584e-07, -0.24043388e-11, 0.14586513e+05, 0.16144349e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.34942392e+01, 0.98631960e-02, -0.43446503e-05, 0.90653661e-09, -0.74574453e-13, 0.14161055e+05, 0.56063699e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""HBNH2-Allendorf""",
    longDesc = 
u"""
HBNH2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 13,
    label = "B(NH2)2",
    molecule = 
"""
1 B u1 p0 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.23853503e+01, 0.28621000e-01, -0.30284743e-04, 0.18423211e-07, -0.46834331e-11, -0.11458350e+03, 0.11584189e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.62477507e+01, 0.12884149e-01, -0.58229691e-05, 0.12606148e-08, -0.10815990e-12, -0.88688858e+03, -0.70133168e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""B(NH2)2-Allendorf""",
    longDesc = 
u"""
B(NH2)2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 14,
    label = "HBNH",
    molecule = 
"""
1 B u1 p0 c0 {2,S} {3,S}
2 N u1 p1 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.23193329e+01, 0.15323100e-01, -0.21011123e-04, 0.16044587e-07, -0.48276744e-11, 0.42950620e+04, 0.39657952e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.42145555e+01, 0.55614479e-02, -0.23877281e-05, 0.50186293e-09, -0.41915774e-13, 0.40013964e+04, -0.46915153e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""HBNH-Allendorf""",
    longDesc = 
u"""
HBNH from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 15,
    label = "BNH2",
    molecule = 
"""
1 B u2 p0 c0 {2,S} 
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.30264833e+01, 0.10551614e-01, -0.10757413e-04, 0.65359666e-08, -0.16255074e-11, 0.23294943e+05, 0.67984399e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.41846862e+01, 0.53132431e-02, -0.21639674e-05, 0.43137685e-09, -0.34195004e-13, 0.23099328e+05, 0.13765407e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BNH2-Allendorf""",
    longDesc = 
u"""
BNH2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 16,
    label = "H2BN",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S} 
2 N u2 p1 c0 {1,S} 
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.16880774e+01, 0.13942306e-01, -0.12349144e-04, 0.64602304e-08, -0.15665199e-11, 0.50777755e+05, 0.14530334e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.32827991e+01, 0.83489442e-02, -0.44948262e-05, 0.11527939e-08, -0.11476111e-12, 0.50398116e+05, 0.65867961e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H2BN-Allendorf""",
    longDesc = 
u"""
H2BN from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 17,
    label = "BNH",
    molecule = 
"""
1 B u2 p0 c0 {2,S} 
2 N u1 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.29255150e+01, 0.89665322e-02, -0.12284371e-04, 0.93288082e-08, -0.27872964e-11, 0.34063491e+05, 0.63616789e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.41529691e+01, 0.29418661e-02, -0.11461845e-05, 0.21661728e-09, -0.16079884e-13, 0.33859445e+05, 0.68289197e+00], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BNH-Allendorf""",
    longDesc = 
u"""
BNH from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 18,
    label = "BN",
    molecule = 
"""
1 B u0 p0 c0 {2,T} 
2 N u0 p1 c0 {1,T} 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.37776064e+01, -0.27279471e-02, 0.82596218e-05, -0.74915752e-08, 0.23074239e-11, 0.69545746e+05, 0.26545159e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.29023763e+01, 0.21631386e-02, -0.12385196e-05, 0.33237094e-09, -0.34236397e-13, 0.69653826e+05, 0.65358093e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BN-Allendorf""",
    longDesc = 
u"""
BN from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 19,
    label = "B3N3H6",
    molecule = 
"""
1 B u0 p0 c0 {4,S} {5,S} {7,S}
2 B u0 p0 c0 {4,S} {6,S} {8,S}
3 B u0 p0 c0 {5,S} {6,S} {9,S}
4 N u0 p1 c0 {1,S} {2,S} {10,S}
5 N u0 p1 c0 {1,S} {3,S} {11,S}
6 N u0 p1 c0 {2,S} {3,S} {12,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.59944330e+01, 0.82459624e-01, -0.88959868e-04, 0.51292394e-07, -0.12333185e-10, -0.62578083e+05, 0.48139645e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.81091459e+01, 0.30955806e-01, -0.16341882e-04, 0.41535622e-08, -0.41209942e-12, -0.65735258e+05, -0.21356929e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""B3N3H6-Allendorf""",
    longDesc = 
u"""
B3N3H6 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 20,
    label = "Cl3BNH3",
    molecule = 
"""
1 B u0 p0 c-1 {2,S} {3,S} {4,S} {5,S}
2 N u0 p0 c+1 {1,S} {6,S} {7,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.33004107e+01, 0.43921800e-01, -0.61316269e-04, 0.44561820e-07, -0.12760718e-10, -0.69387983e+05, 0.10652892e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.10672418e+02, 0.11079021e-01, -0.50888600e-05, 0.11473083e-08, -0.10284438e-12, -0.70759017e+05, -0.24235022e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""Cl3BNH3-Allendorf""",
    longDesc = 
u"""
Cl3BNH3 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 21,
    label = "H3NBCl2NH2",
    molecule = 
"""
1 B u0 p0 c-1 {2,S} {3,S} {4,S} {8,S}
2 N u0 p0 c+1 {1,S} {5,S} {6,S} {7,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 N u0 p1 c0 {1,S} {9,S} {10,S}
9 H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.43319819e+01, 0.43504102e-01, -0.53588016e-04, 0.36948205e-07, -0.10279360e-10, -0.62688254e+05, 0.70622761e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.10430558e+02, 0.16185565e-01, -0.70991712e-05, 0.15318220e-08, -0.13186112e-12, -0.63799247e+05, -0.21722493e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""H3NBCl2NH2-Allendorf""",
    longDesc = 
u"""
H3NBCl2NH2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 22,
    label = "HClBNH2",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.44186831e+00, 0.32025491e-01, -0.38260171e-04, 0.24991354e-07, -0.66704942e-11, -0.32980931e+05, 0.21838898e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.54814084e+01, 0.11357911e-01, -0.54962072e-05, 0.13080063e-08, -0.12307055e-12, -0.33996650e+05, -0.24298198e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""HClBNH2-Allendorf""",
    longDesc = 
u"""
HClBNH2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 23,
    label = "Cl2BNH2",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.16111386e+01, 0.36173832e-01, -0.49919403e-04, 0.35397672e-07, -0.98978999e-11, -0.51690058e+05, 0.17464603e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.83411997e+01, 0.76665966e-02, -0.32517436e-05, 0.66381355e-09, -0.54527459e-13, -0.53007598e+05, -0.14734497e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""Cl2BNH2-Allendorf""",
    longDesc = 
u"""
Cl2BNH2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 24,
    label = "ClB(NH2)2",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {8,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.19105125e+01, 0.41847052e-01, -0.51964008e-04, 0.35646261e-07, -0.10056248e-10, -0.47998560e+05, 0.15203049e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.80587679e+01, 0.15654719e-01, -0.81648086e-05, 0.20318401e-08, -0.19694852e-12, -0.49218637e+05, -0.14234880e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ClB(NH2)2-Allendorf""",
    longDesc = 
u"""
ClB(NH2)2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 25,
    label = "HB(NH2)2",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {8,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.70745868e+00, 0.37546266e-01, -0.40400690e-04, 0.25177066e-07, -0.65373221e-11, -0.27993309e+05, 0.18272199e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.53313244e+01, 0.17685809e-01, -0.81717344e-05, 0.18050633e-08, -0.15768405e-12, -0.28862858e+05, -0.37265961e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""HB(NH2)2-Allendorf""",
    longDesc = 
u"""
HB(NH2)2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 26,
    label = "B(NH2)3",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 N u0 p1 c0 {1,S} {9,S} {10,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.36530985e+01, 0.41482257e-01, -0.46943381e-04, 0.30913755e-07, -0.83890618e-11, -0.40098577e+05, 0.78506603e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.84127036e+01, 0.19469817e-01, -0.89816447e-05, 0.19891808e-08, -0.17338987e-12, -0.40917865e+05, -0.14408349e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""B(NH2)3-Allendorf""",
    longDesc = 
u"""
B(NH2)3 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 27,
    label = "Cl2BNH",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.31037539e+01, 0.25930864e-01, -0.38729895e-04, 0.28489750e-07, -0.81415790e-11, -0.14727305e+05, 0.12838216e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.81855453e+01, 0.38988504e-02, -0.18073858e-05, 0.41360457e-09, -0.37721658e-13, -0.15702328e+05, -0.11362047e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""Cl2BNH-Allendorf""",
    longDesc = 
u"""
Cl2BNH from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 28,
    label = "ClBNH2",
    molecule = 
"""
1 B u1 p0 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 Cl u0 p3 c0 {1,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.18171184e+01, 0.24164438e-01, -0.30408483e-04, 0.20427987e-07, -0.54712704e-11, -0.54546202e+04, 0.16395343e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.59002683e+01, 0.69705810e-02, -0.28384537e-05, 0.53689880e-09, -0.39504979e-13, -0.62444325e+04, -0.31287938e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ClBNH2-Allendorf""",
    longDesc = 
u"""
ClBNH2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 29,
    label = "ClBNH",
    molecule = 
"""
1 B u1 p0 c0 {2,S} {3,S}
2 N u1 p1 c0 {1,S} {4,S} 
3 Cl u0 p3 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.25918568e+01, 0.22736363e-01, -0.36393493e-04, 0.28764736e-07, -0.87021588e-11, -0.11046941e+05, 0.91986346e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.65995152e+01, 0.36131559e-02, -0.14917860e-05, 0.30031014e-09, -0.23890943e-13, -0.11746446e+05, -0.94943598e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ClBNH-Allendorf""",
    longDesc = 
u"""
ClBNH from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 30,
    label = "Cl2BN",
    molecule = 
"""
1 B u0 p0 c0 {2,S} {3,S} {4,S} 
2 N u2 p1 c0 {1,S} 
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.29048020e+01, 0.23454774e-01, -0.34454677e-04, 0.24568659e-07, -0.68890384e-11, 0.10189709e+05, 0.13703212e+02], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.79110437e+01, 0.30520990e-02, -0.18323017e-05, 0.50696803e-09, -0.53289094e-13, 0.91589533e+04, -0.10475566e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""Cl2BN-Allendorf""",
    longDesc = 
u"""
Cl2BN from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 31,
    label = "BNCl2",
    molecule = 
"""
1 B u2 p0 c0 {2,S} 
2 N u0 p1 c0 {1,S} {3,S} {4,S} 
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.40543637e+01, 0.18339636e-01, -0.25543760e-04, 0.17534109e-07, -0.47936684e-11, 0.51367811e+05, 0.80291847e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.79558725e+01, 0.29812492e-02, -0.17900249e-05, 0.49576603e-09, -0.52181544e-13, 0.50538872e+05, -0.10945888e+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""BNCl2-Allendorf""",
    longDesc = 
u"""
BNCl2 from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)

entry(
    index = 32,
    label = "ClBN",
    molecule = 
"""
1 B u1 p0 c0 {2,S} {3,S}
2 N u2 p1 c0 {1,S} 
3 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.34053685e+01, 0.10908439e-01, -0.14706586e-04, 0.10453817e-07, -0.30356048e-11, 0.28633091e+05, 0.73054184e+01], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.54106426e+01, 0.28670155e-02, -0.16494607e-05, 0.44274233e-09, -0.45505023e-13, 0.28200903e+05, -0.24441627e+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ClBN-Allendorf""",
    longDesc = 
u"""
ClBN from
Thermochemistry of Molecules in the B-N-Cl-H System: Ab Initio Predictions Using the BAC-MP4 Method', J. Phys. Chem., vol. 101, 2670-2680 (1997). 
""",
)


