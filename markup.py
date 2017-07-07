mrc = input('What is the monthly recurring charge (MRC)?')
nrc = input('What is the non-recurring charge (NRC)?')
speed = input('What is the circuit speed (T1, 5, etc.)')
term_length = input('What is the desired term length (in years)?')

def mrc_markup(mrr):
    if isnumeric(speed) = False:
        mrr = ((mrc + nrc/10)+25)/0.65
    elif isnumeric(speed) = True and speed*3>=200:
        mrr = (((mrc + nrc/10)+25)+200)/0.65
    elif isnumeric(speed) = True and speed*3<200:
        mrr = (((mrc + nrc/10)+25)+speed*3)/0.65
    else:
        print "error"
    return mrr

    print 'the marked up monthly cost is $%s' % mrr
