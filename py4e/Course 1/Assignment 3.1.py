hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
ntime = 40
otime = h - ntime
ovr = r * 1.5
if h <= ntime:
    npay = h * r
    print(npay)
else :
    opay = (ntime * r) + (otime * ovr)
    print(opay)