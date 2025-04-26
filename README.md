
# 🃏 Anki Deck Generator

This project allows you to **generate Anki decks (`.apkg` files)** using **Python** and the **genanki** library.

You can easily create flashcards with multi-line questions and answers, and import them directly into Anki.

---

## 📦 Project Structure

```
anki_cards/
├── venv/                # Virtual environment (not included in Git)
├── gerador_de_baralho.py # Python script to generate the deck
├── README.md             # Project documentation
```

---

## 🚀 How to Set Up

1. Clone or download this repository.

2. Open the project folder in VS Code.

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

4. Install the required library:
   ```bash
   pip install genanki
   ```

5. Run the script to generate the `.apkg` file:
   ```bash
   python gerador_de_baralho.py
   ```

---

## 🛠 Features

- Create simple question/answer cards.
- Support for **multi-line questions and answers**.
- Ready-to-import `.apkg` file for Anki.
- Fully isolated environment (using `venv`).

---

## ✍️ Example Card

| Front                         | Back                                              |
| ------------------------------ | ------------------------------------------------- |
| What is the capital of France? | Paris                                             |
| Write a short poem.            | Roses are red,<br>Violets are blue,<br>Knowledge blooms,<br>In gardens of truth. |

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

> Created with 💻 and ☕ by Jeverson Oliveira
