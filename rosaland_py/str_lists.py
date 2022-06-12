seq = '2EeSPw63C39EcfI6qDlgozwwBUpPnmMSR03rjmuNH4ziJd2bWAYVwoZu7kR8w1oBubulcusipZdK11HIohG9MtVJYXcvbattersbyifDypwD9M3PlEFNFREHQXGQ2rLGi5tJvxOmFXLdN73TXOAVNbDCCg5SCi0mI1RCEO.'
cs1 = 63
ce1 = 70
cs2 = 92
ce2 = 101

def chopandslice(seq, s1, e1, s2, e2):
    str1 = seq[s1:e1+1]
    str2 = seq[s2:e2+1]
    return str1, str2

print(chopandslice(seq, cs1, ce1, cs2, ce2))