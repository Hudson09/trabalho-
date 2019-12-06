import random;

def gerar_pop_inicial(numPop , numCromossomos):
    p = [];
    for x in range(0 , numPop):
        i = [];
        for x in range(0 , numCromossomos):
            cromossomo = random.sample(range(0 , 2) , 1);
            i.append(cromossomo[0]);
        p.append(i);
    return p;

def calcular_fitness(populacao, numCromossomos):
    f = [];
    for x in range(0 , len(populacao)):
        i = populacao[x];
        fValor = 9 + (i[1] * i[4]) - (i[22] * i[13]) + (i[23] * i[3]) - (i[20] * i[9]);
        fValor = fValor + (i[35] * i[14]) - (i[10] * i[25]) + (i[15] * i[16]) + (i[2] * i[32]);
        fValor = fValor + (i[27] * i[18]) + (i[11] * i[33]) - (i[30] * i[31]) - (i[21] * i[24]);
        fValor = fValor + (i[34] * i[26]) - (i[28] * i[6]) + (i[7] * i[12]) - (i[5] * i[6]) + (i[17] * i[19]);
        fValor = fValor - (i[0] + i[29]) + (i[22] * i[3]) + (i[20] * i[14]) + (i[25] * i[15]) + (i[30] * i[11]);
        fValor = fValor + (i[24] * i[18]) + (i[6] * i[7]) + (i[8] * i[17]) + (i[0] + i[32]);
        f.append(fValor);
    return f;

def selecionar_pop(populacao, numPop, fitness, privilegio):
    p = [];
    numPrivilegio = int(privilegio * numPop);
    sortFitness = fitness;
    sortFitness.sort(reverse = True);
    for x in range(0 , numPrivilegio):
        max = sortFitness[x];
        for x in range(0 , len(fitness)):
            if max == fitness[x]:
                maxPosition = x;
                break;
        p.append(populacao[maxPosition]);
    randomVetorPosition = random.sample(range(0 , len(populacao) - numPrivilegio) , numPop - numPrivilegio);
    for x in range(0 , numPop - numPrivilegio):
        position = randomVetorPosition[x];
        if p.count(populacao[position]):
            while p.count(populacao[position]):
                position = random.randint(0 , len(populacao) - 1);
        p.append(populacao[position]);
    return p;

def cruzar_selecao(selecao, numCromossomos, taxaCruzamento):
    c = [];
    for x in range(0 , taxaCruzamento):
        randomVetorPai = random.sample(range(0 , len(selecao)) , len(selecao));
        for x in range(0 , len(selecao)):
            randomMae = random.randrange(len(selecao));
            while randomVetorPai[x] == randomMae:
                randomMae = random.randint(0 , len(selecao) - 1);
            randomVetorGenes = random.sample(range(0 , numCromossomos) , numCromossomos);
            pai = selecao[randomVetorPai[x]];
            mae = selecao[randomMae];
            filho = [];
            for x in range(0 , len(randomVetorGenes)):
                if(x % 2):
                    filho.append(pai[randomVetorGenes[x]]);
                else:
                    filho.append(mae[randomVetorGenes[x]]);
            c.append(filho);
    return c;

def mutar_cruzamento(cruzamento, taxaMutacao, numCromossomos):
    m = [];
    for x in range(0 , len(cruzamento)):
        c = cruzamento[x];
        if(0 == random.randint(0 , 10 - taxaMutacao * 10)):
            quantidadeCromossomos = random.randint(0 , numCromossomos);
            for x in range(0 , quantidadeCromossomos):
                cromossomo = random.randint(0 , numCromossomos - 1);
                c[cromossomo] = 1;
                '''if c[cromossomo]:
                    c[cromossomo] = 0;    
                else:
                    c[cromossomo] = c[cromossomo] + 1;'''
        m.append(c);
    return m;

def substituicao(populacao, mutacao):
    p = [];
    for x in range(0 , len(populacao)):
        p.append(populacao[x]);
    for x in range(0 , len(mutacao)):
        p.append(mutacao[x]);
    return p;

def calcular_melhor_fitness_position(fitness):
    mf = fitness[0];
    mp = 0;
    for x in range(0 , len(fitness)):
        if(mf < fitness[x]):
            mf = fitness[x];
            mp = x;
    return [mf , mp];

# Main
NUM_POP = 1000;
NUM_CROMOSSOMOS = 36;
TAXA_MUTACAO = 0.3;
TAXA_PRIVILEGIO = 0.8;
TAXA_CRUZAMENTO = 5;
FITNESS_DESEJADO = 25;

populacao = [];
fitness = [];
t = 0

populacao = gerar_pop_inicial(NUM_POP , NUM_CROMOSSOMOS);
print('populacao');
print(populacao);

fitness = calcular_fitness(populacao, NUM_CROMOSSOMOS);
print('fitness');
print(fitness);

while t < 1000:
    t = t + 1;
    selecao = selecionar_pop(populacao, NUM_POP, fitness, TAXA_PRIVILEGIO);
    #print('selecao');
    #print(selecao);
        
    cruzamento = cruzar_selecao(selecao, NUM_CROMOSSOMOS, TAXA_CRUZAMENTO);
    #print('cruzamento');
    #print(cruzamento);
        
    mutacao = mutar_cruzamento(cruzamento, TAXA_MUTACAO, NUM_CROMOSSOMOS);
    #print('mutacao');
    #print(mutacao);
    
    populacao = substituicao(populacao , mutacao);
    #print('populacao');
    #print(populacao);
    
    fitness = calcular_fitness(mutacao, NUM_CROMOSSOMOS);
    #print('fitness');
    #print(fitness);
    
    melhorFitness = calcular_melhor_fitness_position(fitness);
    print('melhor fitness');
    print(melhorFitness[0]);
    
    if melhorFitness[0] >= FITNESS_DESEJADO:
        position = melhorFitness[1];
        print('melhor resultado');
        print(populacao[position]);
        break;
        
    print('geracao');
    print(t);