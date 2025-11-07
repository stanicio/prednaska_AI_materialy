# CAESAROVA ŠIFRA - Aplikace pro šifrování a dešifrování textu

**Autor:** Kamil Stanek
**Datum:** 7. listopadu 2025
**Verze:** 1.0

---

## 📋 OBSAH

1. [Úvod](#úvod)
2. [Co je Caesarova šifra](#co-je-caesarova-šifra)
3. [Funkce aplikace](#funkce-aplikace)
4. [Instalace a spuštění](#instalace-a-spuštění)
5. [Použití](#použití)
6. [Princip frekvenční analýzy](#princip-frekvenční-analýzy)
7. [Šifrování s číselným kódem](#šifrování-s-číselným-kódem)
8. [Příklady použití](#příklady-použití)

---

## 📖 ÚVOD

Tato aplikace implementuje **Caesarovu šifru** - jednu z nejstarších a nejjednodušších šifrovacích metod v historii. Aplikace slouží k:

- Šifrování a dešifrování textu
- Demonstraci slabiny substituční šifry
- Vzdělávacím účelům v oblasti kryptografie
- Ukázce frekvenční analýzy textu

---

## 🔐 CO JE CAESAROVA ŠIFRA

**Caesarova šifra** je typ substituční šifry, kde každé písmeno v textu je nahrazeno jiným písmenem, které se nachází o pevný počet pozic dále v abecědě.

### Princip:

```
Posun o 3:
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

### Historický kontext:

Pojmenována po **Juliu Caesarovi**, který ji používal ve své soukromé korespondenci. Caesar používal posun o 3 pozice (A→D, B→E, atd.).

### Příklad:

```
Původní text:  AHOJ SVETE
Posun o 3:     DKRM VYHWH
```

---

## ⚙️ FUNKCE APLIKACE

### 1. Základní šifrování a dešifrování

- Šifrování textu s pevným posunem (1-25)
- Dešifrování při znalosti posunu
- Zachování velikosti písmen
- Nešifrování mezer a interpunkce

### 2. Zobrazení všech 26 variant

- Automatické zobrazení všech možných dešifrování
- Užitečné pro manuální nalezení správné varianty
- Rychlé prolomení krátkých zpráv

### 3. Frekvenční analýza

- Automatické prolomení šifry bez znalosti posunu
- Analýza četnosti písmen
- Porovnání s typickou frekvencí v češtině
- Zobrazení pravděpodobných řešení

### 4. Šifrování s číselným kódem

- Každý znak má jiný posun
- Vyšší bezpečnost než klasická Caesarova šifra
- Ukázka polyalfabetické substituce

---

## 💻 INSTALACE A SPUŠTĚNÍ

### Požadavky:

- Python 3.6 nebo vyšší
- Žádné externí knihovny (používá pouze standardní knihovnu)

### Spuštění hlavní aplikace:

```bash
cd G:\aaa1
python caesar_cipher.py
```

### Spuštění testů:

```bash
python test_caesar.py
```

---

## 📚 POUŽITÍ

### Interaktivní menu:

Po spuštění `caesar_cipher.py` se zobrazí menu:

```
================================================================================
CAESAROVA ŠIFRA - Hlavní menu
================================================================================
1. Zašifrovat text (pevný posun)
2. Dešifrovat text (známý posun)
3. Zobrazit všech 26 variant dešifrování
4. Prolomit šifru pomocí frekvenční analýzy
5. Šifrovat pomocí číselného kódu
6. Dešifrovat pomocí číselného kódu
0. Konec
================================================================================
```

### Použití v kódu:

```python
from caesar_cipher import CaesarCipher

cipher = CaesarCipher()

# Šifrování
encrypted = cipher.caesar_shift("AHOJ SVETE", shift=3, decrypt=False)
# Výsledek: "DKRM VYHWH"

# Dešifrování
decrypted = cipher.caesar_shift("DKRM VYHWH", shift=3, decrypt=True)
# Výsledek: "AHOJ SVETE"

# Všechny varianty
variants = cipher.show_all_shifts("DKRM VYHWH")

# Frekvenční analýza
candidates = cipher.frequency_attack("DKRM VYHWH...")

# Číselný kód
encrypted = cipher.cipher_with_numeric_key("AHOJ", "123", decrypt=False)
```

---

## 📊 PRINCIP FREKVENČNÍ ANALÝZY

### Proč funguje?

V každém jazyce mají písmena různou frekvenci výskytu. Caesarova šifra tuto frekvenci **zachovává** - pouze "posune" písmena.

### Frekvence v češtině:

| Písmeno | Frekvence |
|---------|-----------|
| E       | 9.8%      |
| O       | 7.4%      |
| A       | 7.0%      |
| N       | 6.5%      |
| T       | 5.9%      |

### Algoritmus:

1. **Spočítáme četnost** všech písmen v šifře
2. **Najdeme nejčastější** písmeno (např. H)
3. **Předpokládáme**, že H je zašifrované E
4. **Vypočítáme posun**: (H - E) = (7 - 4) = 3
5. **Dešifrujeme** s posunem 3

### Příklad:

```
Zašifrovaný text:
"DKRM VYHWH REUDCXMH VH GQHV FDHVDURYD VLIUD"

Frekvence písmen v šifře:
H: 15.4%  ← nejčastější
D: 12.8%
V: 10.3%

Předpoklad: H je zašifrované E
Posun: H(7) - E(4) = 3

Dešifrováno s posunem 3:
"AHOJ SVETE OBRAZUJE SE DNES CAESAROVA SIFRA"
```

### Výhody metody:

✓ Funguje **bez znalosti posunu**
✓ Spolehlivá pro **delší texty** (50+ znaků)
✓ Automatická - nevyžaduje ruční zkoušení

### Omezení:

✗ Méně přesná pro **krátké texty**
✗ Nemusí fungovat pro **speciální texty** (bez častých písmen)
✗ První pokus nemusí být správný - aplikace nabídne více kandidátů

---

## 🔢 ŠIFROVÁNÍ S ČÍSELNÝM KÓDEM

### Princip:

Namísto jednoho pevného posunu používáme **sekvenci posunů** definovanou číselným kódem.

### Příklad:

```
Text:        A  H  O  J
Kód:         1  2  3  1  (opakuje se)
             ↓  ↓  ↓  ↓
Posuny:      +1 +2 +3 +1
             ↓  ↓  ↓  ↓
Výsledek:    B  J  R  K
```

### Výhody oproti klasické Caesarově šifře:

1. **Vyšší bezpečnost** - každé písmeno má jiný posun
2. **Těžší prolomení** - frekvenční analýza je složitější
3. **Více variant** - různé délky a kombinace kódů
4. **Flexibilní** - kód může být libovolně dlouhý

### Použití:

```python
cipher = CaesarCipher()

# Šifrování
encrypted = cipher.cipher_with_numeric_key(
    text="AHOJ SVETE",
    numeric_key="12345",
    decrypt=False
)
# Výsledek: "BJSP XYJYJ"

# Dešifrování (musíme znát kód!)
decrypted = cipher.cipher_with_numeric_key(
    text="BJSP XYJYJ",
    numeric_key="12345",
    decrypt=True
)
# Výsledek: "AHOJ SVETE"
```

### Bezpečnostní poznámka:

I tato metoda **není bezpečná** pro moderní použití! Slouží pouze k **vzdělávacím účelům**.

---

## 📝 PŘÍKLADY POUŽITÍ

### Příklad 1: Základní šifrování

```
Volba: 1 (Zašifrovat text)

Zadejte text: Ahoj svete
Zadejte posun: 3

Výsledek: Dkrm vyhwh
```

### Příklad 2: Zobrazení všech variant

```
Volba: 3 (Všech 26 variant)

Zadejte text: Dkrm vyhwh

Posun  0: Dkrm vyhwh
Posun  1: Cjql uwgvg
Posun  2: Bipk tvfuf
Posun  3: Ahoj svete  ← správná varianta!
Posun  4: Zgni ruesd
...
```

### Příklad 3: Frekvenční analýza

```
Volba: 4 (Frekvenční analýza)

Zadejte text: [dlouhý zašifrovaný text]

Četnost písmen v šifře:
H: 12.3%
G: 9.1%
D: 8.7%
...

Nejpravděpodobnější dešifrování:
1. Předpoklad: 'H' je 'E'
   Posun: 3
   Text: Ahoj svete...
```

### Příklad 4: Číselný kód

```
Volba: 5 (Číselný kód)

Zadejte text: TAJNE
Zadejte kód: 54321

Postup:
T + 5 → Y
A + 4 → E
J + 3 → M
N + 2 → P
E + 1 → F

Výsledek: YEMPF
```

---

## 🎓 VZDĚLÁVACÍ HODNOTA

### Co se naučíte:

1. **Základy kryptografie**
   - Substituční šifry
   - Symetrické šifrování
   - Rozdíl mezi šifrováním a kódováním

2. **Bezpečnostní analýza**
   - Slabiny substitučních šifer
   - Frekvenční analýza
   - Důležitost délky klíče

3. **Programování v Pythonu**
   - Zpracování textu
   - Algoritmy
   - Objektově orientované programování
   - Statistická analýza

---

## ⚠️ BEZPEČNOSTNÍ VAROVÁNÍ

**NIKDY nepoužívejte Caesarovu šifru pro skutečné utajení dat!**

Tato šifra je:
- ❌ Extrémně snadná k prolomení
- ❌ Nevhodná pro jakoukoli citlivá data
- ❌ Může být prolomená za sekundy až minuty

Pro skutečné šifrování použijte:
- ✓ AES (Advanced Encryption Standard)
- ✓ RSA (asymetrické šifrování)
- ✓ Moderní knihovny (PyCryptodome, cryptography, atd.)

---

## 📂 STRUKTURA SOUBORŮ

```
G:\aaa1\
├── caesar_cipher.py          # Hlavní aplikace
├── test_caesar.py            # Testovací skript
└── README_CAESAR.md          # Tato dokumentace
```

---

## 🔧 TECHNICKÉ DETAILY

### Třída CaesarCipher:

**Hlavní metody:**

- `caesar_shift()` - Základní šifrování/dešifrování
- `show_all_shifts()` - Zobrazení všech 26 variant
- `frequency_attack()` - Frekvenční analýza
- `cipher_with_numeric_key()` - Šifrování s číselným kódem
- `analyze_frequency()` - Analýza četnosti písmen

**Atributy:**

- `CZECH_FREQ` - Frekvence písmen v češtině
- `alphabet` - Anglická abeceda (A-Z)

### Zachování formátování:

Aplikace zachovává:
- ✓ Velikost písmen (velká/malá)
- ✓ Mezery
- ✓ Interpunkci
- ✓ Číslice
- ✓ Speciální znaky

Šifrují se **pouze písmena** A-Z (case-insensitive).

---

## 🚀 MOŽNÁ ROZŠÍŘENÍ

Nápady pro budoucí verze:

1. **Grafické rozhraní** (Tkinter, PyQt)
2. **Podpora češtiny** s diakritikou (á, č, ď, ...)
3. **Další šifry** (Vigenère, Playfair, atd.)
4. **Export/import** souborů
5. **Vizualizace** frekvenční analýzy (grafy)
6. **Brute-force útok** s časovým měřením
7. **Vícejazyčná podpora** (angličtina, němčina, ...)

---

## 📜 LICENCE

Tento projekt je vytvořen pro vzdělávací účely.
Volně k použití a modifikaci.

---

## 📞 KONTAKT

**Autor:** Kamil Stanek
**Projekt:** Demonstrace Caesarovy šifry
**Datum:** 7. listopadu 2025

---

## 📖 REFERENCE

1. **Julius Caesar** - Používal posun o 3 ve své korespondenci
2. **De Vita Caesarum (Suetonius)** - První písemná zmínka o šifře
3. **The Code Book (Simon Singh)** - Populární kniha o historii kryptografie
4. **Applied Cryptography (Bruce Schneier)** - Klasická kniha o kryptografii

---

**Vytvořeno s 💻 v Pythonu**
