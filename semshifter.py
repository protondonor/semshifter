import csd, pollex, prototai, clics, stedt, datsemshift


def semshift(search_term):
    meanings = csd.semshift(search_term) + pollex.semshift(search_term) + prototai.semshift(search_term) + \
               clics.semshift(search_term) + stedt.semshift(search_term) + stedt.semshift(datsemshift)
    return list(set(map(str.lower, meanings)))
