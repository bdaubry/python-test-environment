import math
mrc = input('What is the monthly recurring charge (MRC)?')
mrc = float(mrc)
nrc = input('What is the non-recurring charge (NRC)?')
nrc = float(nrc)
circuit_type = input('What type of circuit is needed (Ethernet or T1)?')

def circuit_type_input():
    if circuit_type == "Ethernet":
        speed = input('What is the desired circuit speed in Mbps?')
    elif circuit_type == "T1":
        speed = 1.554
    return float(speed)

speed = circuit_type_input()

term = input('What is the desired term length, in years?')

def term_modifier():
    if term == "1":
        mod = 10.0
    elif term == "2":
        mod = 20.0
    elif term == "3":
        mod = 24.0
    return mod

mod = term_modifier()
price = 0
def mrc_markup():
    if circuit_type == "T1":
        price = ((mrc + (nrc / mod)) + 25.0) / 0.65
    elif circuit_type == "Ethernet" and speed * 3.0 >= 200.0:
        price = ((mrc + (nrc / mod)) + 200.0) / 0.65
    elif circuit_type == "Ethernet" and speed * 3.0 < 200.0:
        price = (((mrc + (nrc / mod))) + (speed * 3.0)) / 0.65
    else:
        print ("error")
    return price

def nrc_markup():
    if circuit_type == "T1":
        if nrc * 1.25 + 325.0 > 399.0:
            nrr = nrc * 1.25 + 325.0
        else:
            nrr = 399.0
    elif circuit_type == "Ethernet":
        if nrc * 1.25 + 325.0 > 399.0:
            nrr = nrc * 1.25 + 325.0
        else:
            nrr = 500.0
    else:
        print ("error")
    return nrr

def roundup(x):
    return int(math.ceil(x / 25.0)) * 25

mrr = mrc_markup()
mumrr = roundup(mrr)
nrr = nrc_markup()

print('The marked up MRR is $%.2f' % mumrr)
print('The marked up NRR is $%.2f' % nrr)
