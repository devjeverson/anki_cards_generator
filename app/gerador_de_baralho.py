import tkinter as tk
from tkinter import messagebox
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


# Configurações do modelo e baralho
modelo_basico = genanki.Model(
    1607392319,
    'Modelo Simples',
    fields=[{'name': 'Frente'}, {'name': 'Verso'}],
    templates=[{
        'name': 'Card Básico',
        'qfmt': '{{Frente}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Verso}}',
    }],
)

baralho = genanki.Deck(
    2059400110,
    'Meu Baralho Exemplo'
)


# Função chamada ao clicar no botão
def adicionar_card():
    frente = entrada_frente.get("1.0", tk.END).strip()
    verso = entrada_verso.get("1.0", tk.END).strip()

    if frente and verso:
        nota = genanki.Note(
            model=modelo_basico,
            fields=[frente, verso]
        )
        baralho.add_note(nota)
        entrada_frente.delete("1.0", tk.END)
        entrada_verso.delete("1.0", tk.END)
        messagebox.showinfo("Sucesso", "Card adicionado!")
    else:
        messagebox.showerror("Erro", "Preencha frente e verso.")


def salvar_baralho():
    genanki.Package(baralho).write_to_file('meu_baralho.apkg')
    messagebox.showinfo("Sucesso", "Arquivo 'meu_baralho.apkg' salvo!")


# Interface gráfica
root = tk.Tk()
root.title("Criador de Flashcards para Anki")

tk.Label(root, text="Frente (Pergunta):").pack()
entrada_frente = tk.Text(root, height=4, width=50)
entrada_frente.pack()

tk.Label(root, text="Verso (Resposta):").pack()
entrada_verso = tk.Text(root, height=4, width=50)
entrada_verso.pack()

tk.Button(root, text="Adicionar Card", command=adicionar_card).pack(pady=5)
tk.Button(root, text="Salvar Baralho", command=salvar_baralho).pack(pady=5)

root.mainloop()
