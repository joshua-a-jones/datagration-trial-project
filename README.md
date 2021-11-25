# periodic-monthly-volume-plotting
A simple program that uses Arps decline curves and displays a graph of 40-year projections of monthly gas volumes, in Mcf, vs. time for the following three cases:

#### Exponential:
* Qi= 5,000 Mcfd
* Di (nominal)= 2.0/year

#### Hyperbolic:
* Qi= 15,000 Mcfd
* Di (nominal)= 1.4/year
* B exponent= 1.5
* Dmin (nominal)= 0.06/year

#### Harmonic:
* Qi= 10,000 Mcfd
* Di (nominal)= 1.2/year
* Dmin (nominal)= 0.10/year

See here for information on calculations and parameters: https://www.extractiveshub.org/servefile/getFile/id/4377

# Running the program
To run the program, simply clone this repo and then run the `plotting.py` script (must have python installed, as well as the matplotlib library)
