from time import sleep
from projeto.funcoes import cadastrar_pessoa, frase, gerar_perfil, realizar_teste, cor_texto


def main():
    frase('~ TESTE DE PERSONALIDADE SIMPLIFICADO ~')
    sleep(1)

    nome = cadastrar_pessoa()
    sleep(0.5)
    print(f"\nOlá, {cor_texto(nome, 'rosa')}! Bem-vindo ao Teste de Personalidade.")
    sleep(1)
    print(f'\nVamos iniciar o nosso teste!')
    sleep(1)
    
    respostas = realizar_teste()
    perfil = gerar_perfil(respostas)
    sleep(1)
    
    print(f"\n{nome}, o seu perfil de personalidade é:\n{perfil}")
    
    frase('>> FIM DO PROGRAMA. VOLTE SEMPRE! <<')

if __name__ == "__main__":
    main()
