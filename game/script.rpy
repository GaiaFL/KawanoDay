# The script of the game goes in this file.

#personagens
define k = Character("Kawano")
define f = Character("Flocos", color='#a59b9a')
define f_amarelo = Character("Furry Amarelo", color='#fab30b')
define n = Character("Nicolas Cage", color='#71262a')
define a = Character("Atena", color='#603e92')
define shun = Character("Shun", color='#45e79b')
define elsa = Character("Elsa", color='#e70251')
define anna = Character("Anna", color='#e70251')
define darth = Character("Darth Vader", color='#b7a7cc')
define robbie = Character("Robbie Rotten", color='#b7a7cc')

#imagens personagens
image FCK = Image("FlocosCageKawano.png")
image ST = Image("Sportacus.png")

#cenários
image black = Image("black.png")
image white = Image("white.png")
image C1 = Image("F 1.jpg")
image C2 = Image("F 2.jpg")
image C4 = Image("F 4.png")
image C6 = Image("F 6.png")
image C7 = Image("F 7.jpg")
image C9 = Image("F 9.jpg")

image C11 = Image("F 11.jpg")
image C12 = Image("F 12.jpg")
image C13 = Image("F 13.png")
image C14 = Image("F 14.png")
image C15 = Image("F 15.jpg")
image C16 = Image("F 16.jpg")
image C18 = Image("F 18.jpg")
image C19 = Image("F 19.jpg")

image C21 = Image("F 21.jpg")
image C22 = Image("F 22.jpg")
image C23 = Image("F 23.jpg")
image C24 = Image("F 24.jpg")
image C25 = Image("F 25.jpg")
image C26 = Image("F 26.jpg")
image C27 = Image("F 27.jpg")
image C28 = Image("F 28.jpg")
image C29 = Image("F 29.jpg")

image C30 = Image("F 30.jpg")
image C31 = Image("F 31.jpg")
image C32 = Image("F 32.png")
image C33 = Image("F 33.jpg")
image C34 = Image("F 34.0.jpg")
image C34_1 = Image("F 34.1.jpg")
image C34_2 = Image("F 34.2.jpg")
image C35 = Image("F 35.jpg")
image C36 = Image("F 36.0.jpg")
image C36_1 = Image("F 36.1.jpg")
image C36_2 = Image("F 36.2.jpg")
image C36_3 = Image("F 36.3.jpg")
image C37 = Image("F 37.jpg")
image C38 = Image("F 38.jpg")
image C39 = Image("F 39.0.jpg")
image C39_1 = Image("F 39.1.jpg")

image C40 = Image("F 40.jpg")
image C42 = Image("F 42.jpg")
image C43 = Image("F 43.jpg")
image C44 = Image("F 44.jpg")
image C45 = Image("F 45.jpg")
image C46 = Image("F 46.jpg")
image C47 = Image("F 47.jpg")
image C48 = Image("F 48.jpg")
image C49 = Image("F 49.jpg")

image C53 = Image("F 53.jpg")
image C54 = Image("F 54.jpg")
image C58 = Image("F 58.jpg")
image C59 = Image("F 59.jpg")

init python:
    config.use_cpickle = False
    config.save_dump = True

transform my_left:
    xalign 0.0
    yalign 1.0

transform my_right:
    xalign 1.5
    yalign 1.0  

transform my_center:
    xalign 0.7
    yalign 1.0 

transform sp_left:     
    xalign 0.0
    yalign -0.5 

transform sp_center:     
    xalign 0.7
    yalign -0.5 

transform sp_right:     
    xalign 1.3
    yalign 1.0

# Inicio
label start:
    #1
    play music "audio/Musics/1 Abertura 20th Century Fox.mp3"
    scene C1
    pause 5
    with dissolve
    scene C2
    pause 5
    with dissolve


    play music "audio/Musics/2 Slice of life.mp3"
    #4
    scene C4 with fade

    #5
    scene C4
    k "Nossa, ninguém veio hoje…"

    #6
    scene C6

    k "Ninguém por aqui também…"

    #7
    scene C7

    k "Que estranho..."
    
    #8
    play sound "audio/Cachorro Latindo.mp3"

    #9
    stop music
    play music "audio/Musics/3 Suspense Music Minecraft.mp3"
    scene C9 with dissolve
    k "Olha um AU AU! {w}\nEspera... é o meu AU AU!!!"

    #10
    k "FLOCOS DANIEL ?!{w}\nCOMO VOCÊ VEIO PARAR AQUI ?!"

    #11
    scene C11 with fade
    play sound "audio/Estralo Limp.mp3"
    pause 2

    #12
    stop sound
    scene C12 with vpunch
    k "AAAAAAAAAAAAAAAA"

    #13
    stop music
    play music "audio/Musics/4 Pelados em santos 8 bits.mp3"
    scene C13 with irisout
    k "O que aconteceu? Onde estamos?!"

    #14
    scene C14 with dissolve
    k " Oh! Parece que cheguei no Paraíso! Huhuhuhuhu"

    #15
    scene C15 with dissolve
    play sound "audio/Cachorro Latindo.mp3"
    f "AU AU AU AU AU"
    
    k "Flocos, volta aqui!"

    #16
    scene C16 
    k "Uou! Ele capturou o Flocos!"

    "Você está preparado para o duelo?"
    menu:
        "Sim!":
            jump pokemon
        "Com certeza!":
            jump pokemon

label pokemon:
    play music "audio/Musics/5 Pokemon Battle music.mp3"
    #17
        

    #18
    play music "audio/Musics/6 Victory music Pokemon.mp3"
    scene C18 with dissolve
    k "Eu venci! Me devolva o Flocos"
    f_amarelo "Me desculpe…{w}\nEstava me sentindo sozinho e Flocos parecia ser um grande amigo"
    k "Puxa…{w}Está tudo bem?"
    f_amarelo "Na verdade, não!"

    #19
    play music "audio/Musics/7 All Stars 8bit.mp3"
    scene C19 with fade
    k "NICOLAS CAGE?!"
    n "Sim, Kawano. {w}Sou eu."

    #20
    n "Será que poderia me ajudar?\n{w}Larguei tudo para vir até a Peludos em Santos e agora estou sozinho e morrendo de fome."
    n "Pode comprar algo para que eu continue com energia para o evento?"
    k "Claro! {w}Que tal um pouco de nesfit e suco de laranja!"
    n "Minha refeição favorita!"
    k "Perfeito! Vamos até a loja mais próxima!"
    

    #21
    play music "audio/Musics/8 Lets go to the mall today 8bits.mp3"
    scene C21 with wipeleft
    pause 3

    #22
    scene C22 with wipeleft
    pause 3
    k "Que vazio… {w}Mas o que é aquela luz no fundo?"

    #23
    scene C23 with wipeleft
    k "Vamos seguir a luz! {w}O que poderia dar errado ?"

    #24
    scene C24 with fade

    #25
    play music "audio/Musics/9 Pegasus Fantasy 8bits.mp3"
    scene C25 with dissolve
    

    #26
    scene C26 with dissolve
    a "Olá!"
    k "Atena! {w}O que você está fazendo aqui?"
    a "Eu que pergunto, o que fazem aqui?"
    k "Estamos procurando nesfit e suco de laranja."

    #27
    scene C27 with dissolve
    a "Nossa, que bom que vocês tão desocupados!{w}\nVocês podem devolver esse colar para a pessoa a quem pertence?"
    a "Aproveitem e levem esse rolo de papel crepom, por favor."
    k "Tudo bem!"

    #28
    scene C28 with dissolve
    show FCK at my_left with dissolve
    pause 2
    show FCK at my_center with dissolve
    pause 2
    show FCK at my_right with dissolve
    pause 2

    #29
    scene C29 with wipeleft
    k "Shun! Finalmente encontramos você!"
    k "Atena pediu para te entregar isso!"
    shun "Obrigado, Kawano! {w}Já estava na hora de fazer um retoque mesmo rs rs"
    k "De nada!"

    #30
    scene C30 with wipeleft
    k "Que frio congelante!"

    #31
    scene C31 with fade
    k "Ah, não! Olha o que aconteceu!"
    shun "Corram!{w}\nDeixem que eu cuido dele!"
    shun "Antes que seja tarde demais!"

    menu:
        "Partir, e deixar o Shun cuidar do Nicolas Cage":
            jump neve
        "Partir, e deixar o Nicolas Cage ser cuidado pelo Shun":
            jump neve

label neve:
    play music "audio/Musics/10 Let it go 8bit.mp3"
    #32
    scene C32 with fade
    k "Espera, acho que conheço muito bem esse lugar…"    

    #33
    scene C33 with dissolve 
    elsa "Kawano, você chegou!"
    anna "Aah, finalmente! {w}Vamos logo para dentro."
    k "Para dentro?"
    elsa "É, para o castelo!"

    #34
    scene C34 with wipeleft
    anna "Chegamos!"
    k "Vocês moram aqui? {w}Desde quando isso aconteceu?"
    elsa "Ué, Kawano, você não lembra?"
    anna "Eu sei o que pode refrescar a memória dele!"
    "[elsa] & [anna]" "Assistir Sailor Moon juntos!"
    scene C34_1 with wipeleft
    k "...."
    k "É...{w}é tão lindo!"
    scene C34_2 with wipeleft
    elsa "Mas Kawano, daonde você tirou essa roupa?"
    anna "Acho que está na hora de nós nos transformarmos também, irmã!"

    #35
    play sound "audio/fire-1.ogg" 
    scene C35 with fade
    elsa "Bem melhor"
    k "Nossa, é por causa do terno ou tá ficando quente?"
    anna "Ah, não, será que isso é culpa dela, irmã?"
    elsa "Isso é coisa da Moana!\n{w}Ela é a favor do aquecimento global para que todo o planeta tenha apenas mar para ela poder navegar!"

    #36
    stop sound 
    play music "audio/Musics/11 Sailor moon 8bit.mp3"
    play sound "audio/VistulaShort.mp3"
    scene C36 with fade
    pause 3
    scene C36_1 with dissolve
    pause 3
    scene C36_2 with dissolve
    pause 3
    scene C36_3 with dissolve
    pause 3

    #37
    stop sound
    scene C37 with fade
    play sound "audio/Socos.mp3"
    pause 2

    #38
    stop sound
    play sound "audio/VistulaShort.mp3"
    scene C38 with dissolve
    k "Meu trabalho aqui está feito."

    #39
    stop sound
    scene C39 with dissolve
    "[elsa] & [anna]" "Mas você não fez nada!"
    scene C39_1 with dissolve
    pause 3

    #40
    scene C40 with fade
    play sound "audio/ledge2.flac"
    k "AAAAAA"

    #41
    scene black with fade

    #42
    play music "audio/Musics/12 Doki Doki 8 bits.mp3"
    scene C42 with dissolve
    k "Caramba!{w}O que aconteceu de novo?"

    #43
    scene C43 with fade
    pause 2

    #44
    scene C44 with dissolve
    pause 2

    #45
    scene C45 with wipeleft
    pause 3

    #46
    scene C46 with pixellate
    

    #47
    play music "audio/Musics/13 Life is a Highway 8 bits.mp3"
    scene C47 with dissolve
    pause 2

    #48
    

    #49
    scene C49 with fade

    #50
    darth "Nossa, que calor em Radiators Springs, né não meu filho?"

    #51
    darth "Que cara de assustado é essa, eu sou seu pai, não sabia não?"

    #52
    darth "….{w}\nOkay, okay, você me pegou, eu sou..."

    #53
    play music "audio/Musics/14 We are number 1 8bits.mp3"
    scene C53 with fade
    robbie "O Robbie Rotten!"

    #54
    scene C54 with dissolve
    pause 2

    #55
    robbie "Agora, se me dá licença, eu vou comer o meu bolo."

    #56
    scene C54 with dissolve
    show ST at sp_left with dissolve
    pause 2
    show ST at sp_center with dissolve
    pause 2
    scene C53 with dissolve
    show ST at sp_right with dissolve
    pause 2
    
    #57
    robbie "Esse sportacus me paga!{w}\nMas tudo bem, eu sei onde conseguir mais, é no ponto de encontro."

    #58
    scene C58 with wipeleft 
    robbie "É aqui."

    #59
    scene C59 with fade
    pause 2

    #60
    scene black with fade
    play sound "audio/closing door.ogg"

    #61
    play music "audio/Musics/15 Evangelion 8 bits.mp3"
    scene saraiva
    "Todos" "Você chegou, Kawano!"
    "Todos" "Bora tirar uma foto!"

    #62

    #63
    scene black
    centered "{size=+75}{cps=8}Feliz aniversário Menino Jawano!{/cps}{/size}{p=5.0}{nw}"
    with dissolve

    return
