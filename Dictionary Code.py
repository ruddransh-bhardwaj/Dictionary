# Dictionary Code

import requests
import json
import os
import sys
from datetime import datetime

# -------------------------
# INSTALL RICH IF MISSING
# -------------------------
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt
    from rich import box
except ImportError:
    print("Installing required package: rich...")
    os.system(f'"{sys.executable}" -m pip install rich')

    # Import again after installation
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt
    from rich import box

# =========================
# HIGH-END WORD LOOKUP DICTIONARY
# Powered by Free Dictionary API
# API: https://dictionaryapi.dev/
# =========================

console = Console()

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
CACHE_FILE = "dictionary_cache.json"
HISTORY_FILE = "search_history.txt"


class DictionaryApp:
    def __init__(self):
        self.cache = self.load_cache()

    # -------------------------
    # CACHE HANDLING
    # -------------------------
    def load_cache(self):
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as file:
                    return json.load(file)
            except:
                return {}
        return {}

    def save_cache(self):
        with open(CACHE_FILE, "w", encoding="utf-8") as file:
            json.dump(self.cache, file, indent=4)

    # -------------------------
    # API REQUEST
    # -------------------------
    def fetch_word_data(self, word):
        word = word.lower().strip()

        # Cache Check
        if word in self.cache:
            console.print("\n[green]✓ Loaded from local cache[/green]")
            return self.cache[word]

        try:
            response = requests.get(API_URL + word, timeout=10)

            if response.status_code == 200:
                data = response.json()
                self.cache[word] = data
                self.save_cache()
                return data

            elif response.status_code == 404:
                console.print(
                    f"\n[bold red]❌ Word '{word}' not found.[/bold red]"
                )
                return None

            else:
                console.print(
                    f"\n[bold red]⚠ API Error: {response.status_code}[/bold red]"
                )
                return None

        except requests.exceptions.ConnectionError:
            console.print("\n[bold red]❌ No internet connection.[/bold red]")
            return None

        except requests.exceptions.Timeout:
            console.print("\n[bold red]❌ Request timed out.[/bold red]")
            return None

        except Exception as e:
            console.print(f"\n[bold red]Unexpected Error: {e}[/bold red]")
            return None

    # -------------------------
    # DISPLAY WORD INFO
    # -------------------------
    def display_word_data(self, data):
        if not data:
            return

        entry = data[0]

        word = entry.get("word", "N/A")
        phonetic = entry.get("phonetic", "Not Available")

        console.print(
            Panel.fit(
                f"[bold cyan]{word.upper()}[/bold cyan]\n\n"
                f"[yellow]Phonetic:[/yellow] {phonetic}",
                title="📘 Dictionary Result",
                border_style="bright_blue"
            )
        )

        meanings = entry.get("meanings", [])

        for meaning_index, meaning in enumerate(meanings, start=1):

            pos = meaning.get("partOfSpeech", "Unknown")

            console.print(
                "\n[bold magenta]━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold magenta]"
            )
            console.print(
                f"[bold yellow]{meaning_index}. Part of Speech:[/bold yellow] {pos}"
            )

            definitions = meaning.get("definitions", [])

            for def_index, definition_data in enumerate(definitions, start=1):

                definition = definition_data.get(
                    "definition", "No definition"
                )
                example = definition_data.get(
                    "example", "No example available"
                )
                synonyms = definition_data.get("synonyms", [])
                antonyms = definition_data.get("antonyms", [])

                table = Table(
                    title=f"Definition {def_index}",
                    box=box.ROUNDED,
                    show_lines=True
                )

                table.add_column("Field", style="cyan", width=18)
                table.add_column("Details", style="white")

                table.add_row("Definition", definition)
                table.add_row("Example", example)

                if synonyms:
                    table.add_row(
                        "Synonyms",
                        ", ".join(synonyms[:10])
                    )

                if antonyms:
                    table.add_row(
                        "Antonyms",
                        ", ".join(antonyms[:10])
                    )

                console.print(table)

        # Audio Pronunciation
        phonetics = entry.get("phonetics", [])
        audio_links = []

        for p in phonetics:
            audio = p.get("audio")
            if audio:
                audio_links.append(audio)

        if audio_links:
            console.print(
                "\n[bold green]🔊 Pronunciation Audio:[/bold green]"
            )
            for i, audio in enumerate(audio_links[:3], start=1):
                console.print(f"{i}. {audio}")

    # -------------------------
    # SEARCH HISTORY
    # -------------------------
    def save_history(self, word):
        with open(HISTORY_FILE, "a", encoding="utf-8") as file:
            file.write(f"{datetime.now()} - {word}\n")

    # -------------------------
    # VIEW HISTORY
    # -------------------------
    def view_history(self):
        if not os.path.exists(HISTORY_FILE):
            console.print("[red]No history found.[/red]")
            return

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = file.readlines()

        if not history:
            console.print("[red]History empty.[/red]")
            return

        console.print(
            Panel(
                "".join(history[-10:]),
                title="Recent Searches",
                border_style="green"
            )
        )

    # -------------------------
    # MAIN LOOP
    # -------------------------
    def run(self):

        console.print(
            Panel.fit(
                "[bold bright_green]HIGH-END WORD LOOKUP DICTIONARY[/bold bright_green]\n"
                "Powered by Free Dictionary API",
                border_style="green"
            )
        )

        while True:

            console.print("\n[bold cyan]Options:[/bold cyan]")
            console.print("[1] Search a Word")
            console.print("[2] View Cached Words")
            console.print("[3] View Search History")
            console.print("[4] Exit")

            choice = Prompt.ask(
                "\nEnter your choice",
                choices=["1", "2", "3", "4"]
            )

            if choice == "1":

                word = Prompt.ask(
                    "\nEnter a word to search"
                ).strip()

                if not word:
                    console.print(
                        "[red]Word cannot be empty.[/red]"
                    )
                    continue

                self.save_history(word)

                console.print(
                    "\n[yellow]Searching dictionary...[/yellow]"
                )

                data = self.fetch_word_data(word)
                self.display_word_data(data)

            elif choice == "2":

                if not self.cache:
                    console.print(
                        "\n[red]No cached words available.[/red]"
                    )
                else:
                    table = Table(
                        title="Cached Words",
                        box=box.DOUBLE_EDGE
                    )

                    table.add_column("#", style="cyan")
                    table.add_column("Word", style="green")

                    for index, word in enumerate(
                        self.cache.keys(),
                        start=1
                    ):
                        table.add_row(str(index), word)

                    console.print(table)

            elif choice == "3":
                self.view_history()

            elif choice == "4":
                console.print(
                    "\n[bold green]Thank you for using the dictionary app![/bold green]"
                )
                sys.exit()


# -------------------------
# PROGRAM ENTRY
# -------------------------
if __name__ == "__main__":
    app = DictionaryApp()
    app.run()