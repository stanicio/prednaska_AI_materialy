### Odkazy používané na prezentaci i pro pozdější odzkoušení na rychlou orientaci účastníky

Claude CLI popis:
Aktuálně asi nejlepší řešení na CLI mód, ale nastavené jen pro Claude (Anthropic) modely
https://www.claude.com/product/claude-code


Gemini CLI popis:
Druhé asi nejlepší komerční/nekomerční řešení na CLI mód, ale nastavené jen pro Gemini (Google) modely
https://github.com/google-gemini/gemini-cli/blob/main/README.md

Gemini API Key:
Správa API klíčů pro Gemini se získáním free API klíče (ale i placených API)
https://aistudio.google.com/app/api-keys

Google AI studio:
Zkoušení modelů zpracování i multimédií, používá Google API klíče
https://aistudio.google.com/


Ollama CLI popis:
Výborný na API, dodá modely pro OpenCode
https://ollama.com/
https://github.com/ollama/ollama



LM Studio popis:
Vhodnější na chat, ale zvládá i API s OpenCode, perfektní na vyzkoušení si modelu
Větvení chatu se zachováním kontextu a nezničení původního vlákna
https://lmstudio.ai/
https://github.com/lmstudio-ai/lms



Open Code popis:
velmi oblíbený a často aktualizovaný Open Source CLI mód pro lokální i placené modely, doporučované pro lokální modely
https://opencode.ai/
https://github.com/sst/opencode



Aider (vyžaduje Python prostředí) popis:
https://aider.chat/
https://github.com/Aider-AI/aider
https://aider.chat/docs/install.html


Goose popis:
https://github.com/block/goose



Hugging Face popis:
https://huggingface.co/welcome

Vlastni GitHub:
https://github.com/stanicio

Claude Code na WWW promo PRO a MAX (250/1000):
https://support.claude.com/en/articles/12690958-claude-code-promotion

Claude Code na WWW:
https://claude.ai/code

Google AI PRO popis:
https://support.google.com/googleone/answer/14534406?hl=cs-CZ#zippy=%2Cdisk-google%2Cprezentace-google

Marp - Markdown Presentation Ecosystem:
Vytváření prezentací z MD souborů do PPTX, PDF
https://github.com/marp-team/marp-cli







### Instalace:

Marp-Team:
It can convert Marp / Marpit Markdown files into static HTML / CSS, PDF, PowerPoint document, and image(s) easily.
npm i @marp-team/marp-cli



### Příkazy:

##### Ollama:

Zobrazení všech modelů co jsou nainstalované
ollama list 



Gemini:
Instalace
npm install -g @google/gemini-cli@latest



Claude:
Instalace
irm https://claude.ai/install.ps1 | iex


Anaconda ucelené prostředí pro správu Conda enviromentů:
https://www.anaconda.com/download

Conda (python prostředí):
vytvoření nového prostředí Pythonu a aktivace
conda create -n prednaska_AI
conda activate prednaska_AI





Nápady na prompty a projekty:

Ukázka základní práce s Git:

* založení repozitáře
* propojení s projektem
* první commit, první Push
* úprava kódu
* chyba
* vrácení kódu
* úprava commit, push



Generování dokumentace:

* Načtení projektu
* analýza závislostí
* generování souhrnné dokumentace
* popsání komentářů v kódu
* výstup do více MD souborů
* práce s více zdroji v MD souborech
* práce s lokálními zdroji



Tvorba aplikace záznamy o předplatných v TXT režimu:

* ukládaní do CSV či TXT bez databáze
* přidávání záznamů o předplatném
* editace záznamů o předplatném
* seznam aktuálních předplatných
* výroba dokumentace celého projektu
* uživatelský návod na používání včetně instalace
* alternativně JAVA script a HTML místo TXT v pythonu, dělat až jako druhou verzi
* vše do Git



Tvorba testovací offline aplikace na výuku zvoleného předmětu dle dodaných materiálů

* načtení zdroje jako základních znalostí, konzistentní typy otázek dle materiálů
* vytvoření sady otázek včetně možných odpovědí, jen jedna správná
* vytvoření testovacího prostředí, pro výuku i testování
* ukládání výsledků pro pozdější načtení a vyhodnocení
* zobrazení statistik
* vše do Git



Aplikace na zpracování textu pomocí Caesarovy šifry (posun znaků o určený počet míst A bude třeba D)

* vytvořit šifrovací a dešifrovací program na text pomocí Ceasarovy šifry, jednoduchý posun
* zobrazit všech 26 možností dešifrovaného slova
* ukázat, že to jde lehce dohledat podle četnosti znaků v textu (v češtině je to znak e)
* přidat funkcionalitu na šifrování pomocí číselného kódu délka, číslo určuje posun znaku



##### Ukázky předchozích promptů a práce:

Gemini - ukázka tvorby dokumentace ze stránek Git do srozumitelné podoby s uložením a editaci souboru:
/chat  /resume 



Všechno co ukazujeme zde, má nějaký vývoj a tak to co se dnes dělá nějak, neznamená, že se to tak už bude dělat nastálo, nebo že to už někdo někam přímo neimplementoval. Třeba práce se soubory už se dá i přes lokální chat (Claude) a částečně i přes www chat.

