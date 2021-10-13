"""Library of units converters"""

# define useful constants
NLB = 4.44822 # Newtons per pound-foot
IPM = 1550    # square inches per square meter
PKP = .001    # kilopascals per pascal

def psi2kpa(psi):
  '''
  Given a numeric value representing pounds per square inch (psi)
  returns the equivalent value in kilopascals (kPa)
  '''
  return psi * NLB * IPM * PKP
