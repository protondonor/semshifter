import csd, pollex, prototai, clics, stedt, datsemshift

dss = datsemshift.DatSemShift()

def semshift(search_term):
    meanings = csd.semshift(search_term) + pollex.semshift(search_term) + prototai.semshift(search_term) + \
               clics.semshift(search_term) + stedt.semshift(search_term) + dss.semshift(search_term)
    return list(set(map(str.lower, meanings)))


def reverse(search_term):
    meanings = pollex.reverse(search_term) + stedt.reverse(search_term) + clics.reverse(search_term) + \
               dss.reverse(search_term)

    return list(set(map(str.lower, meanings)))