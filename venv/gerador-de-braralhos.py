import genanki


# Use: source venv/bin/activate - para ativar o ambiente virtual
# Crie um ambiente virtual com o comando:
# python3 -m venv venv
# Depois, ative o ambiente virtual com o comando: source venv/bin/activate
# Instale a biblioteca genanki: pip install genanki

# Este script cria um arquivo .apkg que pode ser importado no Anki
# O Anki é um software de flashcards que ajuda na memorização
# O arquivo .apkg é o formato de exportação do Anki
#Use: deactivate - para sair do ambiente virtual


# Depois, você pode importar o arquivo .apkg no Anki e começar a estudar!


# Define o modelo do card (estrutura de frente e verso)
modelo_basico = genanki.Model(
    1607392319,  # ID aleatório (não repita entre modelos)
    'Modelo Simples',
    fields=[
        {'name': 'Frente'},
        {'name': 'Verso'},
    ],
    templates=[
        {
            'name': 'Card Básico',
            'qfmt': '{{Frente}}',  # Front side (pergunta)
            'afmt': '{{FrontSide}}<hr id="answer">{{Verso}}',  # Back side (resposta)
        },
    ]
)

# Cria o baralho
baralho = genanki.Deck(
    2059400110,  # ID aleatório (não repita entre baralhos)
    'Meu Baralho Exemplo'
)

# Lista de cards
cards = [
    ["Pergunta1?", "Resposta1"],
    ["Pergunta2?", "Resposta2"],
    ["Pergunta3?", "Resposta3"],
    ["Pergunta4?", "Resposta4"],
    ["Pergunta5?", "Resposta5"],
    ["Pergunta6?", "Resposta6"],
    ["Pergunta7?", "Resposta7"],
    ["Pergunta8?", "Resposta8"],
    ["Pergunta9?", "Resposta9"],
    ["Pergunta10?", "Resposta10"],
    ["Pergunta11?", "Resposta11"],
    ["Pergunta12?", "Resposta12"],
    ["Pergunta13?", "Resposta13"],
    ["Pergunta14?", "Resposta14"],
    ["Pergunta15?", "Resposta15"],
    ["Pergunta16?", "Resposta16"],
    ["Pergunta17?", "Resposta17"],
    ["Pergunta18?", "Resposta18"],
    ["Pergunta19?", "Resposta19"],
    ["Pergunta20?", "Resposta20"],
    ["Pergunta21?", "Resposta21"],
    ["Pergunta22?", "Resposta22"],
    ["Pergunta23?", "Resposta23"],
    ["Pergunta24?", "Resposta24"],
    ["Pergunta25?", "Resposta25"],
    ["Pergunta26?", "Resposta26"],
    ["Pergunta27?", "Resposta27"],
    ["Pergunta28?", "Resposta28"],
    ["Pergunta29?", "Resposta29"],
    ["Pergunta30?", "Resposta30"],
    ["Pergunta31?", "Resposta31"],
    ["Pergunta32?", "Resposta32"],
    ["Pergunta33?", "Resposta33"],
    ["Pergunta34?", "Resposta34"],
    ["Pergunta35?", "Resposta35"],
    ["Pergunta36?", "Resposta36"],
    ["Pergunta37?", "Resposta37"],
    ["Pergunta38?", "Resposta38"],
    ["Pergunta39?", "Resposta39"],
    ["Pergunta40?", "Resposta40"],
    ["Pergunta41?", "Resposta41"],
    ["Pergunta42?", "Resposta42"],
    ["Pergunta43?", "Resposta43"],
    ["Pergunta44?", "Resposta44"],
    ["Pergunta45?", "Resposta45"],
    ["Pergunta46?", "Resposta46"],
    ["Pergunta47?", "Resposta47"],
    ["Pergunta48?", "Resposta48"],
    ["Pergunta49?", "Resposta49"],
    ["Pergunta50?", "Resposta50"],
    ["Pergunta51?", "Resposta51"],
    ["Pergunta52?", "Resposta52"],
    ["Pergunta53?", "Resposta53"],
    ["Pergunta54?", "Resposta54"],
    ["Pergunta55?", "Resposta55"],
    ["Pergunta56?", "Resposta56"],
    ["Pergunta57?", "Resposta57"],
    ["Pergunta58?", "Resposta58"],
    ["Pergunta59?", "Resposta59"],
    ["Pergunta60?", "Resposta60"],
    ["Pergunta61?", "Resposta61"],
    ["Pergunta62?", "Resposta62"],
    ["Pergunta63?", "Resposta63"],
    ["Pergunta64?", "Resposta64"],
    ["Pergunta65?", "Resposta65"],
    ["Pergunta66?", "Resposta66"],
    ["Pergunta67?", "Resposta67"],
    ["Pergunta68?", "Resposta68"],
    ["Pergunta69?", "Resposta69"],
    ["Pergunta70?", "Resposta70"],
    ["Pergunta71?", "Resposta71"],
    ["Pergunta72?", "Resposta72"],
    ["Pergunta73?", "Resposta73"],
    ["Pergunta74?", "Resposta74"],
    ["Pergunta75?", "Resposta75"],
    ["Pergunta76?", "Resposta76"],
    ["Pergunta77?", "Resposta77"],
    ["Pergunta78?", "Resposta78"],
    ["Pergunta79?", "Resposta79"],
    ["Pergunta80?", "Resposta80"],
    ["Pergunta81?", "Resposta81"],
    ["Pergunta82?", "Resposta82"],
    ["Pergunta83?", "Resposta83"],
    ["Pergunta84?", "Resposta84"],
    ["Pergunta85?", "Resposta85"],
    ["Pergunta86?", "Resposta86"],
    ["Pergunta87?", "Resposta87"],
    ["Pergunta88?", "Resposta88"],
    ["Pergunta89?", "Resposta89"],
    ["Pergunta90?", "Resposta90"],
    ["Pergunta91?", "Resposta91"],
    ["Pergunta92?", "Resposta92"],
    ["Pergunta93?", "Resposta93"],
    ["Pergunta94?", "Resposta94"],
    ["Pergunta95?", "Resposta95"],
    ["Pergunta96?", "Resposta96"],
    ["Pergunta97?", "Resposta97"],
    ["Pergunta98?", "Resposta98"],
    ["Pergunta99?", "Resposta99"],
    ["Pergunta100?", "Resposta100"],
]

# Adiciona os cards no baralho
for frente, verso in cards:
    nota = genanki.Note(
        model=modelo_basico,
        fields=[frente, verso]
    )
    baralho.add_note(nota)

# Salva como arquivo .apkg
genanki.Package(baralho).write_to_file('meu_baralho.apkg')

print("Arquivo 'meu_baralho.apkg' criado com sucesso!")

