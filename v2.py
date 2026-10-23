FACES = ('U', 'L', 'F', 'R', 'B', 'D')

#----------------
# PARTE 1: CORES
#----------------

# cria_cor: str -> cor
def cria_cor(digito):
    """
    Recebe um carácter ’1’ a ’6’ e devolve a cor correspondente. 
    Gera ValueError com ’cria_cor: argumentos invalidos’ se o argumento não for válido.
    """
    if digito not in ("1","2","3","4","5","6"):
        raise ValueError ("cria_cor: argumentos invalidos")
    #Escolhi um tuplo para representar as cores simplesmente porque é um tipo imutável e facilita a leitura
    #Desta forma, sei que o tuplo é uma cor porque o primeiro elemento é obrigatoriamente "cor"
    #Para saber o valor da cor basta olhar para o segundo elemento
    return ("cor", int(digito))

# eh_cor: universal -> booleano
def eh_cor(arg):
    """
    devolve True se o argumento corresponde a uma cor e False caso contrário. Nunca gera erros.
    """
    #arg é abreviação para argumento
    #As verificações vão do caso mais geral ao mais particular porque o and para no primeiro False
    #Desta forma, se arg não for um tuplo de comprimento 2, arg[0] e arg[1] nunca chegam a ser executados 
    #Usar type(...) exclui True e False, que em python também são int
    return isinstance(arg,tuple) and len(arg) == 2 and arg[0] == "cor" and type(arg[1]) == int and 0 < arg[1] <= 6

# cores_iguais: universal x universal -> Booleano
def cores_iguais(arg1, arg2):
    """
    Devolve True se ambos os argumentos forem cores que representam o mesmo dígito.
    """
    #Usei apenas funções definidas no código, de forma a não recorrer à representação interna das cores
    return eh_cor(arg1) and eh_cor(arg2) and cor_para_int(arg1) == cor_para_int(arg2)

# cor_para_str: cor -> str
def cor_para_str(cor):
    """
    Converte uma cor para a sua representação externa (dígito que a identifica).
    """
    #O segundo elemento do tuplo é o inteiro que identifica a cor. O código apenas retorna-o como uma str
    return str(cor[1])

# str_para_cor: str -> cor
def str_para_cor(digito):
    """
    Converte a representação externa de uma cor (dígito que identifica) para uma cor.
    """
    #Recorre a uma função já criada para não repetir código desnecessariamente
    return cria_cor(digito)

# cor_para_int: cor -> int
def cor_para_int(cor):
    """
    Devolve o inteiro 1 a 6 que identifica a cor
    """
    #O segundo elemento do tuplo é o inteiro que identifica a cor
    return cor[1]

#---------------------
# PARTE 2: MOVIMENTOS
#---------------------

# cria_movimento: str x booleano -> movimento
def cria_movimento(f, s):
    """
    Recebe uma face f (’U’,’L’,’F’,’R’,’B’,’D’) e um sentido s (True horário, False anti-horário), devolvendo 
    o movimento correspondente.
    Gera ValueError com ’cria_movimento: argumentos invalidos’ se os argumentos não forem válidos.
    """
    if f not in FACES or not isinstance(s,bool):
        raise ValueError("cria_movimento: argumentos invalidos")
    #De forma semelhante às cores, estou a usar um tuplo para representar os movimentos já que este é imutável
    #Sei que o tuplo é um movimento e não uma cor porque o primeiro elemento é obrigatoriamente "movimento"
    #Para saber a face ou o sentido basta ver o segundo e terceiro elemento do tuplo respetivamente
    return ("movimento", f, s)

# obtem_mov_face: movimento -> str
def obtem_mov_face(m):
    """
    Devolve a face do movimento recebido como argumento.
    """
    #m é a abreviação de movimento
    #O segundo elemento de um movimento é a face
    return m[1]

# obtem_mov_sentido: movimento -> booleano
def obtem_mov_sentido(m):
    """
    Devolve o sentido do movimento recebido como argumento (True se horário e False se anti-horário).
    """
    #O terceiro elemento de um movimento é o sentido
    return m[2]

# eh_movimento: universal -> booleano
def eh_movimento(arg):
    """
    Devolve True se o argumento corresponde a um movimento, e False caso contrário. Nunca gera erros.
    """
    #As verificações vão do caso mais geral ao mais particular porque o and para no primeiro False
    #Desta forma, se arg não for um tuplo de comprimento 3, arg[0], arg[1] e arg[2] não chegam a ser executados 
    return isinstance(arg,tuple) and len(arg) == 3 and arg[0] == "movimento" and arg[1] in FACES and isinstance(arg[2], bool)

# movimentos_iguais: universal x universal -> booleano
def movimentos_iguais(m1,m2):
    """
    Devolve True se os dois argumentos são movimentos com a mesma face e sentido.
    """
    #O processo pode exigir um pouco mais de computação desta forma
    #mas assim não precisa aceder à representação interna de um movimento
    return eh_movimento(m1) and eh_movimento(m2) and obtem_mov_face(m1) == obtem_mov_face(m2) \
    and obtem_mov_sentido(m1) == obtem_mov_sentido(m2)

# movimento_para_str: movimento ->str
def movimento_para_str(m):
    """
    Converte um movimento na sua representação externa ("U" ou "U’").
    """
    if obtem_mov_sentido(m):
        return obtem_mov_face(m)
    else:
        return obtem_mov_face(m) + "'"

# str_para_movimento: str -> movimento
def str_para_movimento(rep):
    """
    Converte a representação externa de um movimento no movimento correspondente. 
    Gera ValueError com ’str_para_movimento: argumentos invalidos’ se o argumento não for válido.
    """
    #rep é abreviação de representação (externa do movimento)
    if rep not in ("U","L","F","R","B","D","U'","L'","F'","R'","B'","D'"):  
        raise ValueError("str_para_movimento: argumentos invalidos")
    #Se rep é uma representação válida com comprimento 2 sabemos que tem de ter sentido anti-horário
    #Se rep é válido só pode ter comprimento de 1 ou de 2
    if len(rep)==2:
        return cria_movimento(rep[0],False)
    return cria_movimento(rep,True)

# movimento_inverso: movimento -> movimento
def movimento_inverso(m):
    """
    Devolve o movimento inverso (U↔U’).
    """
    #A única diferença entre movimentos inversos é o sentido
    return cria_movimento(obtem_mov_face(m), not obtem_mov_sentido(m))

# str_para_sequencia: str -> tuplo
def str_para_sequencia(rep):
    """
    Converte uma string como "L'RUU'" num tuplo de movimentos.
    """
    seq = ()
    #seq será o tuplo resultante da conversão
    i = 0
    #É preciso de um contador i que guarda em que posição da string o ciclo se encontra
    #naturalmente, o contador começa em 0
    while i < len(rep):
        if i+1 <len(rep) and rep[i+1] == "'": #verifica se é o último elemento da string e caso contrário
            #se tem um apóstrofe à sua frente
            seq += (cria_movimento(rep[i],False),)
            i+=2
            #O contador salta duas unidades porque tem de saltar a letra da face mais o apóstrofe
        else: 
            #se não houver nenhum apóstrofe à frente, só pode ser um movimento de sentido horário
            seq += (cria_movimento(rep[i],True),)
            i+=1
    return seq

# sequencia_para_str: tuplo -> str
def sequencia_para_str(seq):
    """
    Converte um tuplo de movimentos na sua representação externa
    """
    s = ""
    #s será a string resultante da conversão
    for m in seq:
        if obtem_mov_sentido(m):
            s += obtem_mov_face(m)
        else:
            s += obtem_mov_face(m)+"'"
            #Caso o sentido seja anti-horário é necessário adicionar um apóstrofe
    return s

# sequencia_inversa: tuplo -> tuplo
def sequencia_inversa(seq):
    """
    inverte a ordem e cada movimento
    """
    r =() #r será o resultado da função
    for m in seq[::-1]: #seq[::-1] é o tuplo seq só que com a ordem invertida
        r += (movimento_inverso(m),) #Adiciona a r o inverso de cada elemento
    return r

# simplifica_sequencia: tuplo -> tuplo
def simplifica_sequencia(seq):
    """
    Junta voltas consecutivas da mesma face módulo 4 (UU’ anula-se, UUU reduz a U’). 
    A simplificação continua sobre movimentos que se tornem adjacentes em consequência de reduções anteriores,
    até não serem possíveis novas reduções (RUU’R’ anula-se por completo).
    """
    k=0
    #k é um contador que guarda em que posição da sequência a ser simplificada estamos
    alt = False
    #alt guarda se alguma simplificação foi aplicada ao longo da aplicação do código (vai ser importante)
    r=()
    #r será sequência simplificada
    while(k<len(seq)):
        if k+3<len(seq) and seq[k] == seq[k+1] == seq[k+2] == seq[k+3]:  #Caso hajam 4 movimentos iguais seguidos
            k += 4 #Salta 4 movimentos
            #Não adiciona nada a r, já que os movimentos se cancelam
            alt = True
        elif k+2<len(seq) and seq[k] == seq[k+1] == seq[k+2]: #Caso hajam 3 movimentos iguais seguidos
            r += (movimento_inverso(seq[k]),) #Adiciona o movimento inverso a r
            k += 3 #Salta 3 movimentos
            alt = True
        elif k+1<len(seq) and seq[k] == movimento_inverso(seq[k+1]): #Caso haja um movimento seguido do seu inverso
            k += 2 #Salta 2 movimentos
            #Não adiciona nada a r, já que os movimentos se cancelam
            alt = True
        
        else:
            r += (seq[k],) #Adiciona o movimento como estava, já que não houve simplificação
            k += 1 #Salta 1 movimento (caso normal)
    if alt:
        #Se foi necessária alguma simplificação tentamos simplificar a sequência obtida novamente.
        #Isto é necessário porque uma redução qualquer pode dar origem a uma sequência nova que também pode ser simplificada
        return simplifica_sequencia(r)
    return r

#----------------
# PARTE 3: CUBO
#----------------

#Posição onde começa cada face na representação interna do cubo
INICIO_FACE = {'U': 0, 'L': 4, 'F': 8, 'R': 12, 'B': 16, 'D': 20}
 
#Este dicionário define para que posição cada autocolante vai ao realizar o movimento horário de cada face
TROCAS = {'U': {0: 1, 1: 3, 3: 2, 2: 0, #Troca de posições na própria face
                9: 5, 5: 17, 17: 13, 13: 9, #Troca de posição nas faces adjacentes
                8: 4, 4: 16, 16: 12, 12: 8}, #Troca de posição nas faces adjacentes
          'L': {4: 5, 5: 7, 7: 6, 6: 4,
                0: 8, 8: 20, 20: 19, 19: 0,
                2: 10, 10: 22, 22: 17, 17: 2},
          'F': {8: 9, 9: 11, 11: 10, 10: 8,
                2: 12, 12: 21, 21: 7, 7: 2,
                3: 14, 14: 20, 20: 5, 5: 3},
          'R': {12: 13, 13: 15, 15: 14, 14: 12,
                9: 1, 1: 18, 18: 21, 21: 9,
                11: 3, 3: 16, 16: 23, 23: 11},
          'B': {16: 17, 17: 19, 19: 18, 18: 16,
                1: 4, 4: 22, 22: 15, 15: 1,
                0: 6, 6: 23, 23: 13, 13: 0},
          'D': {20: 21, 21: 23, 23: 22, 22: 20,
                11: 15, 15: 19, 19: 7, 7: 11,
                10: 14, 14: 18, 18: 6, 6: 10}}
 
#Posições dos autocolantes em cada linha da rede do cubo (ver Figura 1 do enunciado)
LINHAS_REDE = ((0, 1), (2, 3), (4, 5, 8, 9, 12, 13, 16, 17), (6, 7, 10, 11, 14, 15, 18, 19), (20, 21), (22, 23))
 
#Movimentos que o gerador de baralha_cubo escolhe, pela ordem da tabela do enunciado
MOVIMENTOS_BARALHAR = ("U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'")
 
# cria_cubo: {} -> cubo
def cria_cubo():
    """
    Devolve um cubo resolvido.
    """
    #Um cubo é uma lista de 24 cores, pela ordem das posições do enunciado.
    #Escolhi uma lista (e não um tuplo) porque o enunciado trata uma lista de 24 cores como sendo um cubo
    #Além disso, poder alterar o cubo será útil mais à frente e isso só é possível com uma lista
    #Cada face tem apenas a sua cor quando o cubo está resolvido (1 para U, 2 para L, ..., 6 para D)
    return cria_cubo_de_str("111122223333444455556666")
 
# cria_cubo_de_str: str -> cubo
def cria_cubo_de_str(rep):
    """
    Devolve o cubo representado por uma string de 24 dígitos (’1’ a ’6’).
    Gera ValueError com ’cria_cubo_de_str: argumentos invalidos’ se o argumento não for válido.
    """
    #rep é abreviação de representação (externa do cubo)
    #isinstance vem primeiro porque len só faz sentido para strings
    if not isinstance(rep, str) or len(rep) != 24:
        raise ValueError("cria_cubo_de_str: argumentos invalidos")
    c = [] #c será o cubo resultante
    for d in rep:
        if d not in ("1","2","3","4","5","6"):
            raise ValueError("cria_cubo_de_str: argumentos invalidos")
        c += [str_para_cor(d)]
    return c
 
# cria_copia_cubo: cubo -> cubo
def cria_copia_cubo(c):
    """
    Devolve uma cópia nova do cubo.
    """
    #c é a abreviação de cubo
    #Basta copiar superficialmente a lista, porque as cores (tuplos) são imutáveis
    return c.copy()
 
# obtem_cor_face: cubo x str -> tuplo
def obtem_cor_face(c, f):
    """
    Devolve o tuplo das 4 cores da face f, na ordem de leitura.
    Gera ValueError com ’obtem_cor_face: argumentos invalidos’ se a face não for válida.
    """
    #Verifica-se com FACES (um tuplo) e não com INICIO_FACE para não gerar outro erro se f for, por exemplo, uma lista
    if f not in FACES:
        raise ValueError("obtem_cor_face: argumentos invalidos")
    inicio = INICIO_FACE[f]
    return tuple(c[inicio:inicio+4])

# roda_cubo: cubo x movimento -> cubo
def roda_cubo(c, m):
    """
    Aplica o movimento m ao cubo c e devolve o cubo resultante (c não é alterado).
    """
    c_novo = cria_copia_cubo(c) #As posições que o movimento não toca ficam como estavam
    tabela = TROCAS[obtem_mov_face(m)] 
    #Cada "tabela" contem a posição inicial de cada autocolante associada à posição final, após o movimento
    for p_inicial in tabela:
        p_final = tabela[p_inicial]
        if obtem_mov_sentido(m):
            c_novo[p_final] = c[p_inicial] #horário: o autocolante vai de p_inicial para p_final
        else:
            c_novo[p_inicial] = c[p_final] #anti-horário: faz o caminho contrário, de p_final para p_inicial
    return c_novo
 
# eh_cubo: universal -> booleano
def eh_cubo(arg):
    """
    Devolve True se o argumento corresponde a um cubo, e False caso contrário. Nunca gera erros.
    """
    #Um cubo é uma lista de 24 cores (não exige que cada cor apareça 4 vezes, isso é verificado em eh_cubo_valido)
    #Primeiro verifica-se o tipo e o tamanho. Depois verifica-se se todo o elemento é uma cor
    if not isinstance(arg, list) or len(arg) != 24:
        return False
    for cor in arg:
        if not eh_cor(cor):
            return False
    return True
 
# eh_cubo_valido: cubo -> booleano
def eh_cubo_valido(c):
    """
    Devolve True se cada cor aparece exatamente 4 vezes no cubo.
    """
    if not eh_cubo(c):
        return False
    for digito in range(1, 7): #são 6 cores representadas por 6 digitos de 1 a 6
        num = 0 #número de vezes que a cor aparece
        for cor in c:
            if cor_para_int(cor) == digito:
                num += 1
        if num != 4: #depois de verificar todos os elementos, a cor a ser analisada tem de ter aparecido 4 vezes
            return False
    return True
 
# cubos_iguais: universal x universal -> booleano
def cubos_iguais(arg1, arg2):
    """
    Devolve True se os dois argumentos são cubos com as mesmas cores em todas as posições.
    """
    if not(eh_cubo(arg1) and eh_cubo(arg2)): #Ambos os argumentos têm de ser cubos
        return False
    for i in range(24):
        if not cores_iguais(arg1[i], arg2[i]): #Cada elemento do cubo tem de ter exatamente a mesma cor
            return False
    #Ao usar apenas funções já definidas, não preciso de recorrer à representação interna do cubo
    return True
 
# cubo_para_str: cubo -> str
def cubo_para_str(c):
    """
    Devolve a rede (planificação) do cubo, uma linha por cada linha de autocolantes.
    """
    texto = ""
    for posicoes in LINHAS_REDE:
        #As linhas de U e D só têm 2 autocolantes e ficam alinhadas com a coluna de F (depois de L, 6 caracteres)
        if len(posicoes) == 2:
            texto += "      " #Espaços de forma a alinhar com a coluna de F
        for p in posicoes:
            texto += "[" + cor_para_str(c[p]) + "]" #Adiciona cada autocolante entre parênteses retos
        texto += "\n"
    return texto[:-1] #tira o último "\n", que não faz parte da rede
 
# aplica_sequencia: cubo x tuplo -> cubo
def aplica_sequencia(c, seq):
    """
    Aplica a sequência de movimentos seq ao cubo c e devolve o cubo resultante (c não é alterado).
    """
    novo = cria_copia_cubo(c)
    for m in seq:
        novo = roda_cubo(novo, m)
    return novo
 
# numero_faces_resolvidas: cubo -> int
def numero_faces_resolvidas(c):
    """
    Devolve o número de faces do cubo com uma única cor (resolvida).
    """
    total = 0 #total será o número de faces com uma única cor
    for f in FACES:
        cores = obtem_cor_face(c, f)
        igual = True #igual guarda se todos os autocolantes da face têm a cor do primeiro
        for cor in cores:
            if not cores_iguais(cor, cores[0]):
                igual = False
        if igual: #igual == True significa que a face tem todas as cores iguais
            total += 1
    return total
 
# esta_resolvido: cubo -> booleano
def esta_resolvido(c):
    """
    Devolve True se o cubo está resolvido (todas as 6 faces com uma única cor).
    """
    return numero_faces_resolvidas(c) == 6
 
# baralha_cubo: cubo x int x int -> tuplo
def baralha_cubo(c, n, semente):
    """
    Aplica ao cubo c n movimentos pseudo-aleatórios, gerados a partir da semente (inteiro de 1 a 12),
    e devolve o tuplo desses movimentos, pela ordem em que foram gerados (sem simplificação).
    Gera ValueError com ’baralha_cubo: argumentos invalidos’ se os argumentos não forem válidos.
    """
    #type(...) == int exclui True e False, que em python também são int
    if not eh_cubo(c) or type(n) != int or type(semente) != int or n < 0 or not (0 < semente <= 12):
        raise ValueError("baralha_cubo: argumentos invalidos")
    movimentos = () #movimentos será o tuplo dos movimentos gerados
    s = semente #s é o estado do gerador, sempre entre 1 e 12
    for i in range(n):
        s = 2 * s % 13 #o estado atualiza-se antes de ser convertido em movimento
        movimentos += (str_para_movimento(MOVIMENTOS_BARALHAR[s - 1]),)
    novo = aplica_sequencia(c, movimentos)
    #Copia-se posição a posição para o cubo recebido ficar mesmo baralhado (roda_cubo devolve sempre um cubo novo)
    for j in range(24):
        c[j] = novo[j]
        #Se simplesmente usasse c = aplica_sequencia(c, movimentos), o cubo original não seria alterado
        #Isso apenas alteraria um cubo local c
    return movimentos

#--------------------------
# PARTE 4: TESTES PRÓPRIOS
#--------------------------

def testes_proprios():
    #Teste de várias funções implementadas no código para ver se os resultados estão corretos
    # 1. PARTE: CORES (cria_cor, eh_cor, cores_iguais, cor_para_str, str_para_cor, cor_para_int)
    c1 = cria_cor('2')
    c2 = str_para_cor('2')
    print("1. Cores:", eh_cor(c1), cores_iguais(c1, c2), cor_para_str(c1), cor_para_int(c1))
    
    try:
        cria_cor('9')
    except ValueError:
        print("   Erro em cria_cor ('9') capturado com sucesso.")

    # 2. PARTE: MOVIMENTOS (cria_movimento, obtem_mov_face, obtem_mov_sentido, eh_movimento, movimentos_iguais, movimento_para_str, str_para_movimento, movimento_inverso, str_para_sequencia, sequencia_para_str, sequencia_inversa, simplifica_sequencia)
    m1 = cria_movimento('U', True)
    m2 = str_para_movimento("U")
    m_anti = movimento_inverso(m1)
    
    print("2. Movimentos:", eh_movimento(m1), movimentos_iguais(m1, m2), obtem_mov_face(m1), obtem_mov_sentido(m1))
    print("   Movimento para str e inverso:", movimento_para_str(m1), movimento_para_str(m_anti))

    seq = str_para_sequencia("RUU'R'")
    seq_str = sequencia_para_str(seq)
    seq_inv = sequencia_inversa(seq)
    seq_simp = simplifica_sequencia(seq)
    print("   Sequências:", seq_str, sequencia_para_str(seq_simp))

    try:
        str_para_movimento("Z")
    except ValueError:
        print("   Erro em str_para_movimento ('Z') capturado com sucesso.")

    # 3. PARTE: CUBO (cria_cubo, cria_cubo_de_str, cria_copia_cubo, obtem_cor_face, roda_cubo, eh_cubo, eh_cubo_valido, cubos_iguais, cubo_para_str, aplica_sequencia, numero_faces_resolvidas, esta_resolvido, baralha_cubo)
    cubo = cria_cubo()
    print("3. Cubo Base:", eh_cubo(cubo), eh_cubo_valido(cubo), esta_resolvido(cubo), numero_faces_resolvidas(cubo))

    # Ver representação do cubo resolvido
    print("\nREPRESENTAÇÃO DO CUBO RESOLVIDO")
    print(cubo_para_str(cubo))

    # Testar cópia, string para cubo e igualdade
    cubo_str = cria_cubo_de_str("111122223333444455556666")
    cubo_copia = cria_copia_cubo(cubo)
    print("\n   Cópia e Str:", cubos_iguais(cubo_str, cubo), (cubo_copia is cubo), cubos_iguais(cubo_copia, cubo))

    # Testar obtenção de cor de face e rotação
    face_u = obtem_cor_face(cubo, 'U')
    print("   Face U:", tuple(cor_para_str(x) for x in face_u))

    cubo_rodado = roda_cubo(cubo, str_para_movimento('F'))
    print("   Faces resolvidas após rodar F:", numero_faces_resolvidas(cubo_rodado))

    print("\nREPRESENTAÇÃO APÓS RODA_CUBO ('F')")
    print(cubo_para_str(cubo_rodado))

    # Testar aplicação de sequência
    seq_teste = str_para_sequencia("L'RUU")
    cubo_seq = aplica_sequencia(cria_cubo(), seq_teste)
    print("   Aplica sequência executada com sucesso.")

    # Testar baralhar cubo e ver representação
    cubo_baralhado = cria_cubo()
    movs_baralhar = baralha_cubo(cubo_baralhado, 5, 3)
    print("   Baralhar cubo:", sequencia_para_str(movs_baralhar), esta_resolvido(cubo_baralhado))

    print("\nREPRESENTAÇÃO DO CUBO BARALHADO")
    print(cubo_para_str(cubo_baralhado))

    # Testar erros de cubo
    try:
        cria_cubo_de_str("123")
    except ValueError:
        print("\n   Erro em cria_cubo_de_str capturado com sucesso.")

    try:
        baralha_cubo(cria_cubo(), 1, 13)
    except ValueError:
        print("   Erro em baralha_cubo (semente inválida) capturado com sucesso.")

testes_proprios()