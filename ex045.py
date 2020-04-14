import random
import time
import playsound

comp=('pedra', 'papel', 'tesoura', 'lagarto', 'spock')

print('\033[0;35m-=-' * 20)
print('\033[0;34mVamos jogar Pedra, Papel, Tesoura, Lagarto, Spock?!')
print('\033[0;35m-=-' * 20)

time.sleep(1)
pergunta=str(input('\033[0;33mPrimeiro, você sabe jogar?[S/N] ')).upper().strip()[0]
if pergunta not in 'SN':
    pergunta = str(input('\033[0;33mPerdão, não entendi...? ')).upper().strip()[0]
if pergunta in 'N':
    playsound.playsound('regras.mp3') #audio das regras
input('\033[0;34mMuito bem, vamos prosseguir! ')
playsound.playsound('chamada.mp3') #chamada 'PEDRA PAPEL TESOURA LAGARTO SPOCK'

print('\033[0;35m-=-' * 20)
print('\033[0;34mVamos escolher juntos!')
print('\033[0;35m-=-' * 20)

while True:
   escolha=str(input('\033[0;33mVocê escolhe: ').lower())
   while escolha not in comp:
       escolha = str(input('\033[0;33mPerdão...não entendi... ').lower())
   jogo = random.choice(comp)
   print(f'\033[0;34mEu escolhi {jogo}!')
   if escolha == 'lagarto':
       if jogo == 'papel':
          time.sleep(1)
          print('\033[0;31mQUEEE! Você ganhou >:( ! Lagarto esdaçalha papel!!')
          playsound.playsound('dammit.mp3')
       elif jogo == 'pedra':
          time.sleep(1)
          print('\033[0;31mPEERDEEEEUUU! Pedra esmaga lagarto :D !!')
          playsound.playsound('YESSS.mp3')
       elif jogo == 'tesoura':
          time.sleep(1)
          print('\033[0;31mPEERDEEEEUUU! Tesoura corta lagarto :D !!')
          playsound.playsound('YESSS.mp3')
       elif jogo == 'spock':
          time.sleep(1)
          print('\033[0;31mQUEEE! Você ganhou >:( ! Lagarto devora Spock!!')
          playsound.playsound('dammit.mp3')
       elif jogo == 'lagarto':
          time.sleep(1)
          print('\033[0;31mAHHH! Empate!, que merda >:( !!')

   if escolha == 'spock':
       if jogo == 'papel':
          time.sleep(1)
          print('\033[0;31mPEERDEEEEUUU! Papel reprova Spock :D !!')
          playsound.playsound('YESSS.mp3')
       elif jogo == 'pedra':
          time.sleep(1)
          print('\033[0;31mQUEEE! Você ganhou >:( ! Spock vaporiza pedra!!')
          playsound.playsound('dammit.mp3')
       elif jogo == 'tesoura':
          time.sleep(1)
          print('\033[0;31mQUEEE! Você ganhou >:( ! Spock quebra tesoura!!')
          playsound.playsound('dammit.mp3')
       elif jogo == 'spock':
          time.sleep(1)
          print('\033[0;31mAHHH! Empate!, que merda >:( !!')
       elif jogo == 'lagarto':
          time.sleep(1)
          print('\033[0;31mPEERDEEEEUUU! Lagarto devóra Spock :D !!')
          playsound.playsound('YESSS.mp3')

   if escolha == 'tesoura':
       if jogo == 'papel':
          time.sleep(1)
          print('\033[0;31mQUEEE!Você ganhou >:( ! Tesoura corta papel!')
          playsound.playsound('dammit.mp3')
       elif jogo == 'pedra':
          time.sleep(1)
          print('\033[0;31mPERDEUUU!! Pedra quebra tesoura :D !!')
          playsound.playsound('YESSS.mp3')
       elif jogo == 'tesoura':
          time.sleep(1)
          print('\033[0;31mAHHH! Empate!, que merda >:( !!')
       elif jogo == 'lagarto:':
          time.sleep(1)
          print('\033[0;31mQUEEE! Você ganhou >:( ! Tesoura decapita lagarto!!')
          playsound.playsound('dammit.mp3')
       elif jogo == 'spock':
          time.sleep(1)
          print('\033[0;31mPEERDEEEEUUU! Spock quebra tesoura :D !!')
          playsound.playsound('YESSS.mp3')

   if escolha == 'papel':
       if jogo == 'pedra':
          time.sleep(1)
          print('\033[0;31mQUEEE! Você ganhou >:( ! Papel enrola pedra!!')
          playsound.playsound('dammit.mp3')
       elif jogo == 'tesoura':
          time.sleep(1)
          print('\033[0;31mPERDEUUU!! Pedra quebra tesoura :D !!')
          playsound.playsound('YESSS.mp3')
       elif jogo == 'papel':
          time.sleep(1)
          print('\033[0;31mAHHH! Empate!, que merda >:( !!')
       elif jogo == 'lagarto':
          time.sleep(1)
          print('\033[0;31mPEERDEEEEUUU! Lagarto come papel :D !!')
          playsound.playsound('YESSS.mp3')
       elif jogo == 'spock':
          time.sleep(1)
          print('\033[0;31mQUEEE! Você ganhou >:( ! Papel reprova Spock!!')
          playsound.playsound('dammit.mp3')

   if escolha == 'pedra':
       if jogo == 'tesoura':
          time.sleep(1)
          print('\033[0;31mQUEEE! Você ganhou >:( ! Pedra quebra tesoura!!')
          playsound.playsound('dammit.mp3')
       elif jogo == 'papel':
          time.sleep(1)
          print('\033[0;31mPEERDEEEEUUU! Papel enrola pedra :D !!')
          playsound.playsound('YESSS.mp3')
       elif jogo == 'pedra':
          time.sleep(1)
          print('\033[0;31mAHHH! Empate!, que merda >:( !!')
       elif jogo == 'lagarto':
          time.sleep(1)
          print('\033[0;31mQUEEE! Você ganhou >:( ! Pedra esmaga lagarto!!')
          playsound.playsound('dammit.mp3')
       elif jogo == 'spock':
          time.sleep(1)
          print('\033[0;31mPEERDEEEEUUU! Spock vaporiza pedra :D !!')
          playsound.playsound('YESSS.mp3')

   print('\033[0;35m-=-' * 20)
   p=str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
   if p not in 'NS':
       p = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
   if p in 'N':
       break
   print('\033[0;35m-=-' * 20)

print('\033[0;35m-=-' * 20)
print('Volte depois, então! Amei jogar com você :D ')