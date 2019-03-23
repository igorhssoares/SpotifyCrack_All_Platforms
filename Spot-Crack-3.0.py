#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import os, platform
import time 
sistema = platform.system()
 
print('''
 ███████╗██████╗  ██████╗ ████████╗               ██████╗██████╗  █████╗  ██████╗██╗  ██╗    
 ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝              ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    
 ███████╗██████╔╝██║   ██║   ██║       █████╗    ██║     ██████╔╝███████║██║     █████╔╝     
 ╚════██║██╔═══╝ ██║   ██║   ██║       ╚════╝    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗     
 ███████║██║     ╚██████╔╝   ██║                 ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    
 ╚══════╝╚═╝      ╚═════╝    ╚═╝                  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    


 :================================================================:                                                              
 :  - GITHUB : https://github.com/JustAbP                         :
 :================================================================:                                                            

                                                                 ''')


time.sleep(1)
                                                                
print('\n [!] OSB: Rode o Script em um Prompt/Terminal como ADM/ROOT!')

print('\n [!] Baixando pacotes necessários...')
time.sleep(1)

print('\n [!] TUDO PRONTO, DIVIRTA-SE! :D')

time.sleep(1)

def main():
    print('++++++++++++++++++++++++++++++++++++++++')
    print('+      [!] ELE APENAS TIRA OS ADs      +')
    print('+______________________________________+')
    print('+--------------------------------------+')
    print('+       [!] ESCOLHA UMA OPÇÃO          +')  
    print('+  [1] CRACKEAR                        +')
    print('+  [2] REMOVER CRACK                   +')
    print('+  [3] VERIFICAR SE JÁ ESTá CRACKEADO  +')
    print('+  [4] SAIR                            +')
    print('++++++++++++++++++++++++++++++++++++++++')
print('\n')
 
###### DEFINIÇAO DOS CRACKS
crack = """
0.0.0.0 adclick.g.doublecklick.net
0.0.0.0 googleads.g.doubleclick.net
0.0.0.0 http://www.googleadservices.com
0.0.0.0 pubads.g.doubleclick.net
0.0.0.0 securepubads.g.doubleclick.net
0.0.0.0 pagead2.googlesyndication.com
0.0.0.0 spclient.wg.spotify.com
0.0.0.0 audio2.spotify.com
"""

crack_other_os = """
127.0.0.1 media-match.com
127.0.0.1 adclick.g.doublecklick.net
127.0.0.1 www.googleadservices.com
127.0.0.1 open.spotify.com
127.0.0.1 pagead2.googlesyndication.com
127.0.0.1 desktop.spotify.com
127.0.0.1 googleads.g.doubleclick.net
127.0.0.1 pubads.g.doubleclick.net
127.0.0.1 audio2.spotify.com
127.0.0.1 www.omaze.com
127.0.0.1 omaze.com
127.0.0.1 bounceexchange.com
"""
#### FIM DA DEFINIÇAO DOS CRACKS

if sistema == 'Windows':
    print('\n [X] Sistema Windows..')
    main()
    try:
        escolha = int(input('[>>]'))
        while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
            escolha = int(input('[>>]'))
        if escolha == 1:
            diretorio = os.chdir('C:\Windows\System32\drivers\etc')
            with open('hosts','a') as crack:
                crack.write("""
0.0.0.0 adclick.g.doublecklick.net
0.0.0.0 googleads.g.doubleclick.net
0.0.0.0 http://www.googleadservices.com
0.0.0.0 pubads.g.doubleclick.net
0.0.0.0 securepubads.g.doubleclick.net
0.0.0.0 pagead2.googlesyndication.com
0.0.0.0 spclient.wg.spotify.com
0.0.0.0 audio2.spotify.com
    """)
                print('\n [!] Crackeado com sucesso!')
        elif escolha == 2:
            diretorio = os.chdir('C:\Windows\System32\drivers\etc')
            with open('hosts','w') as remove:
                remove.write("""
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host
# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
    """)
                print('\n [!] Remoção de ADS concluída! Voltando ao original!')
                exit()
        elif escolha == 3:
            os.chdir('C:\Windows\System32\drivers\etc')
            abrir = open('hosts','r')
            if crack in abrir.read():
                print("\n [!] Seu Spotify já está Crackeado!")
                exit()
            else:
                print("\n [-] Seu Spotify não está Crackeado.")
                exit()
        elif escolha == 4:
            exit()

    except ValueError:
        print('\n [!] Verifique sua escolha novamente.')
    except KeyboardInterrupt:
        print('\n [!] Você cancelou. Saindo..')
        exit()
    except PermissionError:
        print('\n [!] RODE O SCRIPT NO PROMPT/TERMINAL COMO ADMIN/ROOT')
    except FileNotFoundError:
        print('\n [?] Há algum arquivo faltando para completar o Crack : hosts')
#############################################################################
        
else: ##### OUTRO SISTEMA OPERACIONAL
    if sistema == 'Linux':
        print('\n [X] Sistema Linux.')
    else:
        print('\n [!] Sistema diferente de Windows..')
    main()
    try:
        esc = int(input('[>>]'))
        while esc != 1 and esc != 2 and esc != 3 and esc != 4:
            esc = int(input('[>>]'))
        if esc == 1: #########  ESCOLHA 1
            diretorio = '/etc/' # /etc/hosts
            os.chdir(diretorio) # navega ate o diretorio
            verifica = os.listdir(diretorio) # verifica se o arquivo host ta disponivel
            if 'hosts' or 'hosts.txt' in verifica:
                with open('hosts','a') as injeta:
                    injeta.write("""
127.0.0.1 media-match.com
127.0.0.1 adclick.g.doublecklick.net
127.0.0.1 www.googleadservices.com
127.0.0.1 open.spotify.com
127.0.0.1 pagead2.googlesyndication.com
127.0.0.1 desktop.spotify.com
127.0.0.1 googleads.g.doubleclick.net
127.0.0.1 pubads.g.doubleclick.net
127.0.0.1 audio2.spotify.com
127.0.0.1 www.omaze.com
127.0.0.1 omaze.com
127.0.0.1 bounceexchange.com
    """)
                    print('\n [!] Crackeado com sucesso!')
                    exit()
            else:
                print('\n [-] Arquivo para Crack não encontrado.')
                exit()
        elif esc == 2:
            diretorio = '/etc/' # /etc/hosts
            os.chdir(diretorio) # navega ate o diretorio
            nome = gethostname() ## NOME DE HOST DO PC
            with open('hosts','w') as remove:
                remove.write("""
127.0.0.1	localhost
127.0.0.1   {}
# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
    """.format(nome))
                print('\n [!] Remoção de ADs concluída! Voltando ao original.')
                exit()
        elif esc == 3:
            os.chdir('/etc/')
            ler = open('hosts','r')
            if crack_other_os in ler.read():
                print('\n [!] Seu Spotify já está Crackeado!')
            else:
                print('\n [-] Seu Spotify não está Crackeado.')
        elif esc == 4:
            exit()
    except NameError:
        exit()
    except KeyboardInterrupt:
        print('\n [!] Saindo..')
    except IOError:
        print('\n [!] EXECUTE COMO ADMINISTRADOR/ROOT!')
