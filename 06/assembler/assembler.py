

def abreCodigo():
     
    global arquivo_original
    arquivo_original = open('Pong.asm')
    
   
    global codigo_original
    codigo_original = arquivo_original.readlines()

  
    arquivo_original.close()

    global codigo_sem_comentario
    codigo_sem_comentario = []

    global codigo_sem_labels
    codigo_sem_labels = []

    global codigo_sem_label_jump
    codigo_sem_label_jump = []

    global codigo_sem_variavel
    codigo_sem_variavel = []

    global codigo_instrucoes_bin
    codigo_instrucoes_bin = []

def removeComentario():

    linha_sem_espaco = []
    codigo_sem_espaco = codigo_original

    index_1 = 0
    index_2 = 0
    
    
    for linha in codigo_sem_espaco:
            if linha.find('//') == 0:
                codigo_sem_comentario.append(linha[0:linha.find('//')])
            elif linha.find('//') != -1:
                codigo_sem_comentario.append(linha[0:linha.find('//')] + '\n')
            else:
                codigo_sem_comentario.append(linha)        
                
def removeLabel():

    labels = {}

    index = 0

    aux = 0
    
    for linha in codigo_sem_comentario:
        if linha.find('(') != -1:
            labels[linha[1:len(linha)-2]] = index - aux
            aux += 1
        else:
            codigo_sem_labels.append(linha)
        index += 1

    for linha in codigo_sem_labels:
        for palavra in linha.split():
            if palavra[1:len(palavra)] in labels.keys():
                codigo_sem_label_jump.append('@'+str(labels[palavra[1:]])+'\n')
            else:
                codigo_sem_label_jump.append(linha)

def removeVariavel():

    variaveis = {"R0":0,
                 "R1":1,
                 "R2":2,
                 "R3":3,
                 "R4":4,
                 "R5":5,
                 "R6":6,
                 "R7":7,
                 "R8":8,
                 "R9":9,
                 "R10":10,
                 "R11":11,
                 "R12":12,
                 "R13":13,
                 "R14":14,
                 "R15":15,
                 "SP":0,
                 "LCL":1,
                 "ARG":2,
                 "THIS":3,
                 "THAT":4,
                 "SCREEN":16384,
                 "KBD":24576}

    index = 16

    for linha in codigo_sem_label_jump:
        if linha[0:1] == '@':
            if linha[1:len(linha)-1] not in variaveis.keys() and not str(linha[1:len(linha)-1]).isdigit():
                variaveis[linha[1:len(linha)-1]] = index
                index += 1
    for linha in codigo_sem_label_jump:
        if linha[:1] == '@':
            if linha[1:len(linha)-1] in variaveis.keys():
                codigo_sem_variavel.append('@'+str(variaveis[linha[1:len(linha)-1]])+'\n')
            else:
                codigo_sem_variavel.append(linha)
        else:
            codigo_sem_variavel.append(linha)

def converteInstrucoesBinario():

    instrucoes_comp_0 = {'0':'101010',
                         '1':'111111',
                         '-1':'111010',
                         'D':'001100',
                         'A':'110000',
                         '!D':'001101',
                         '!A':'110001',
                         '-D':'001111',
                         '-A':'110011',
                         'D+1':'011111',
                         'A+1':'110111',
                         'D-1':'001110',
                         'A-1':'110010',
                         'D+A':'000010',
                         'D-A':'010011',
                         'A-D':'000111',
                         'D&A':'000000',
                         'D|A':'010101'}

    instrucoes_comp_1 = {'M':'110000',
                         '!M':'110001',
                         '-M':'110011',
                         'M+1':'110111',
                         'M-1':'110010',
                         'D+M':'000010',
                         'D-M':'010011',
                         'M-D':'000111',
                         'D&M':'000000',
                         'D|M':'010101'}

    instrucoes_dest = {'null':'000',
                       'M':'001',
                       'D':'010',
                       'MD':'011',
                       'A':'100',
                       'AM':'101',
                       'AD':'110',
                       'AMD':'111'}

    instrucoes_jmp = {'null':'000',
                      'JGT':'001',
                      'JEQ':'010',
                      'JGE':'011',
                      'JLT':'100',
                      'JNE':'101',
                      'JLE':'110',
                      'JMP':'111'}

    for linha in codigo_sem_variavel:
        if linha.find('=') != -1:
            if linha[linha.find("=")+1:len(linha)-1] in instrucoes_comp_0:
                a = 0
                codigo_instrucoes_bin.append('111' + str(a) +
                                             instrucoes_comp_0[linha[linha.find("=")+1:len(linha)-1]] +
                                             instrucoes_dest[linha[:linha.find("=")]] +
                                             '000' + '\n'
                                             )
            else:
                a = 1
                codigo_instrucoes_bin.append('111' + str(a) +
                                             instrucoes_comp_1[linha[linha.find("=")+1:len(linha)-1]] +
                                             instrucoes_dest[linha[:linha.find("=")]] +
                                             '000' + '\n'
                                             )
        elif linha.find(';') != -1:
            if linha[:linha.find(";")] in instrucoes_comp_0:
                a = 0
                codigo_instrucoes_bin.append('111' + str(a) +
                                             instrucoes_comp_0[linha[:linha.find(";")]] +
                                             '000' +
                                             instrucoes_jmp[linha[linha.find(";")+1:len(linha)-1]] + '\n'
                                             )
            else:
                a = 1
                codigo_instrucoes_bin.append('111' + str(a) +
                                             instrucoes_comp_1[linha[:linha.find(";")]] +
                                             '000' +
                                             instrucoes_jmp[linha[linha.find(";") + 1:len(linha) - 1]] + '\n'
                                             )
        elif linha[0] == '@':
            codigo_instrucoes_bin.append(bin(int(linha[1:]))[2:].zfill(16) + '\n')
        else:
            codigo_instrucoes_bin.append(linha)

abreCodigo()
removeComentario()
removeLabel()
removeVariavel()
converteInstrucoesBinario()
arquivo = open('Pong.hack','w')
arquivo.writelines(codigo_instrucoes_bin)
arquivo.close()