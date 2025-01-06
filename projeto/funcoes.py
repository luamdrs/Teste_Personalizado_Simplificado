def cor_texto(texto, cor):
    cores = {
        'vermelho': '\033[91m',
        'roxo': '\033[94m',
        'rosa': '\033[95m',
        'resetar': '\033[0m'
    }

    return f'{cores.get(cor, cores["resetar"])}{texto}{cores['resetar']}'


# Função que imprime uma frase formatada com bordas
def frase(msg):
    print(f'{'=' * len(msg)}\n{msg}\n{'=' * len(msg)}')


# Função para cadastrar o nome da pessoa
def cadastrar_pessoa():
    try:
        nome = input('Digite seu nome: ').strip()
        if not nome:
            # Levanta erro manualmente se nome for vazio
            raise ValueError('Nome não pode ser vazio.')
    except ValueError as ve:
        print(cor_texto (ve, 'magenta')) # Exibe a mensagem de erro
        return cadastrar_pessoa() # Solicita o nome novamente
    except KeyboardInterrupt:
        print(cor_texto('O usuário preferiu não informar os dados!', 'vermelho'))
        return None # Retorna None se o usuário interromper o programa com Ctrl+C
    else:
        return nome

    
# Função que simula a realização de um teste de personalidade, coletando respostas
def realizar_teste():
    perguntas = [
        'Você se considera uma pessoa mais introvertida ou extrovertida?',
        'Você prefere planejar tudo ou ser mais espontâneo?',
        'Você se considera uma pessoa mais emocional ou racional?'
    ]

    respostas = []
    for pergunta in perguntas:
        while True:
            print(f'\n{pergunta}')
            resposta = input('Responda (introvertido(a)/extrovertido(a), planejado(a)/espontâneo(a), emocional/racional): ').strip().lower()
            if resposta in ['introvertido', 'introvertida', 'extrovertido', 'extrovertida', 'espontâneo', 'espontânea', 'planejado', 'planejada', 'emocional', 'racional']:
                respostas.append(resposta)
                break
            else:
                print(cor_texto('Resposta inválida. Tente novamente!', 'vermelho'))

    return respostas


# Função que irá gerar um perfil com base nas respostas fornecidas
def gerar_perfil(respostas):
    if ('introvertido' in respostas or 'introvertida' in respostas) and ('planejado' in respostas or 'planejada' in respostas):
        perfil = 'Perfil Analítico!'
        descricao = (
            '\nCaracterísticas: Pessoas com perfil analítico tendem a ser detalhistas, lógicas e orientadas para dados. Eles valorizam a precisão e a objetividade.\nComportamento: Costumam se basear em fatos e números para tomar decisões, preferindo análises profundas antes de agir. Muitas vezes, são vistos como críticos e metódicos.\nPontos Fortes: Habilidade para resolver problemas complexos, pensar de forma crítica e analisar informações.\nDesafios: Podem ser excessivamente críticos ou hesitantes em situações que exigem decisões rápidas, e podem ter dificuldades em se conectar emocionalmente com os outros.'
        )
        return cor_texto(perfil, 'roxo') + '\n' + descricao
    
    elif ('extrovertido' in respostas or 'extrovertida' in respostas) and ('espontâneo' in respostas or 'espontânea' in respostas):
        perfil = 'Perfil Comunicativo!'
        descricao = (
            '\nCaracterísticas: Indivíduos com perfil comunicativo são extrovertidos, sociáveis e persuasivos. Eles são frequentemente vistos como carismáticos e entusiásticos.\nComportamento: Gostam de interagir com os outros, expressar suas ideias e envolver as pessoas em conversas. Valorizam o feedback e são bons em construir relacionamentos.\nPontos Fortes: Excelentes habilidades de comunicação, capacidade de motivar e inspirar os outros, e habilidades interpessoais.\nDesafios: Podem ter dificuldades em se concentrar em detalhes, ser percebidos como superficiais ou se distrair facilmente durante tarefas que exigem foco.'
        )
        return cor_texto(perfil, 'roxo') + '\n' + descricao
        
    else:
        perfil = 'Perfil Balanceado!'
        descricao = (
            '\nCaracterísticas: Pessoas com perfil balanceado são flexíveis, adaptáveis e equilibradas em suas abordagens. Eles combinam características dos perfis analítico e comunicativo.\nComportamento: Sabem quando ser analíticos e quando se comunicar, adaptando seu estilo de acordo com a situação. Eles tendem a ser diplomáticos e mediadores em conflitos.\nPontos Fortes: Capacidade de ver o quadro geral enquanto presta atenção aos detalhes, facilidade em trabalhar em equipe e resolver conflitos.\nDesafios: Podem ser indecisos ou ter dificuldades em se comprometer totalmente com uma abordagem, o que pode levar à incerteza em algumas situações.'
        )
        return cor_texto(perfil, 'roxo') + descricao