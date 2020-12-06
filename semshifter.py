import csd, pollex, prototai, clics, stedt, datsemshift


def semshift(search_term):
    dss = datsemshift.DatSemShift()
    meanings = csd.semshift(search_term) + pollex.semshift(search_term) + prototai.semshift(search_term) + \
               clics.semshift(search_term) + stedt.semshift(search_term) + dss.semshift(search_term)
    return list(set(map(str.lower, meanings)))
