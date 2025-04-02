import numpy as np

"""These variable names might be bad, especially using the symbol for pi instead of writing \"pi.\""""
def single_diff_pol(o0, oπ, e0, eπ):
    
    o0_avg = np.average(o0, axis=0)
    oπ_avg = np.average(oπ, axis=0)
    e0_avg = np.average(e0, axis=0)
    eπ_avg = np.average(eπ, axis=0)

    Q_zero = o0_avg - e0_avg
    Q_π = oπ_avg - eπ_avg

    sing_diff_pol = (1/2)*(Q_zero - Q_π)

    return sing_diff_pol

def intensity(o0, oπ, e0, eπ):

    o0_avg = np.average(o0, axis=0)
    oπ_avg = np.average(oπ, axis=0)
    e0_avg = np.average(e0, axis=0)
    eπ_avg = np.average(eπ, axis=0)

    I = (1/2)*(o0_avg + oπ_avg + e0_avg + eπ_avg)

    return I

if __name__ == "__main__":
    pass