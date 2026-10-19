def cria_cor (s):
    if s not in ("1","2","3","4","5","6"):
        raise ValueError("cria_cor: argumentos invalidos")
    return ("cor", int(s))

def eh_cor (c):
    return isinstance(c, tuple) and len(c) == 2 and c[0] == "cor" and type(c[1]) == int and 0<c[1]<=6

def cores_iguais (c1,c2):
    return eh_cor(c1) and eh_cor(c2) and c1 == c2

def cor_para_str (c):
    return str(c[1])

def str_para_cor (s):
    return cria_cor(s)

def cor_para_int (c):
    return(c[1])

def cria_movimento (s,b):
    if s not in ("U","L","F","R","B","D") or type(b) != bool:
        raise ValueError("cria_movimento: argumentos invalidos")
    return ("movimento",s,b)

def obtem_mov_face (m):
    return m[1]

def obtem_mov_sentido (m):
    return m[2]

def eh_movimento (m):
    return isinstance(m,tuple) and len(m) == 3 and m[0] == "movimento" and  \
    m[1] in ("U","L","F","R","B","D") and  type(m[2]) == bool

def movimentos_iguais (m1,m2):
    return eh_movimento(m1) and eh_movimento(m2) and m1 == m2

def movimento_para_str (m):
    if m[2]:
        return m[1]
    else:
        return m[1] + "'"

def str_para_movimento (s):
    if s not in ("U","L","F","R","B","D","U'","L'","F'","R'","B'","D'"):  
        raise ValueError("str_para_movimento: argumentos invalidos")
    if len(s)==2:
        return cria_movimento(s[0],False)
    return cria_movimento(s,True)

def movimento_inverso (m):
    return cria_movimento(obtem_mov_face(m), not obtem_mov_sentido(m))

def str_para_sequencia (s):
    seq = ()
    i = 0
    while i < len(s):
        if i+1 <len(s) and s[i+1] == "'":
            seq += (cria_movimento(s[i],False),)
            i+=2
        else:
            seq += (cria_movimento(s[i],True),)
            i+=1
    return seq

def sequencia_para_str (seq):
    s = ""
    for m in seq:
        if obtem_mov_sentido(m) == True:
            s += obtem_mov_face(m)
        else:
            s += obtem_mov_face(m)+"'"
    return s

def sequencia_inversa (seq):
    return seq[::-1]

def simplifica_sequencia (seq):
    i=0
    k=0
    r=()
    while(k<len(seq)):
        if k+2<len(seq) and seq[k] == seq[k+1] == seq[k+2]:
            r += (movimento_inverso(seq[k]),)
            k += 3
            i += 1
        elif k+1<len(seq) and seq[k] == movimento_inverso(seq[k+1]):
            k += 2 
            i += 1
        else:
            r += (seq[k],)
            k += 1
    if i > 0:
        return simplifica_sequencia(r)
    return r

