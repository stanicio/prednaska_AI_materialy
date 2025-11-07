# 🔐 Caesarova šifra - Kompletní implementace v Pythonu

**Autor:** Kamil Stanek
**Datum:** 7. listopadu 2025
**Verze:** 1.0

---

## 📋 O projektu

Komplexní implementace **Caesarovy šifry** v Pythonu včetně:

- ✅ Základního šifrování a dešifrování
- ✅ Zobrazení všech 26 možných variant
- ✅ Automatického prolomení pomocí frekvenční analýzy
- ✅ Šifrování s číselným kódem (polyalfabetická substituce)
- ✅ Důkladné dokumentace a testů
- ✅ Interaktivních demo ukázek

---

## 🚀 Rychlý start

### 1. Spusťte testy (ověření funkčnosti)

```bash
python test_caesar_auto.py
```

**Očekávaný výstup:**
```
Uspesne: 6
Selhaly: 0
```

### 2. Vyzkoušejte demo (naučte se používat)

```bash
python demo_caesar.py
```

### 3. Použijte aplikaci (experimentujte)

```bash
python caesar_cipher.py
```

---

## 📁 Struktura projektu

| Soubor | Popis |
|--------|-------|
| `caesar_cipher.py` | **Hlavní aplikace** - Interaktivní menu s 6 funkcemi |
| `test_caesar_auto.py` | **Automatické testy** - 6 testů všech funkcí |
| `demo_caesar.py` | **Demonstrace** - 5 interaktivních ukázek |
| `priklad_pouziti.py` | **Příklady kódu** - Jak použít v vlastním kódu |
| `README_CAESAR.md` | **Detailní dokumentace** - 800+ řádků |
| `NAVOD.txt` | **Stručný návod** - Rychlá příručka |
| `PREHLED_PROJEKTU.txt` | **Přehled projektu** - Kompletní informace |
| `SPUST_APLIKACI.bat` | **Windows spouštěč** - Menu pro Windows |

---

## ⚙️ Funkce aplikace

### 1️⃣ Základní šifrování

```python
from caesar_cipher import CaesarCipher

cipher = CaesarCipher()
encrypted = cipher.caesar_shift("Ahoj svete", shift=3, decrypt=False)
# Výsledek: "Dkrm vyhwh"
```

### 2️⃣ Všech 26 variant

```python
cipher.show_all_shifts("Dkrm vyhwh")
# Zobrazí všech 26 možných dešifrování
```

### 3️⃣ Frekvenční analýza

```python
candidates = cipher.frequency_attack(encrypted_text)
# Automaticky odhadne správný posun
```

### 4️⃣ Číselný kód

```python
encrypted = cipher.cipher_with_numeric_key("AHOJ", "1234", decrypt=False)
# Každé písmeno má jiný posun
```

---

## 📊 Výsledky testů

```
TEST 1: ZAKLADNI SIFROVANI              ✓ OK
TEST 2: VSECH 26 VARIANT               ✓ OK
TEST 3: FREKVENCNI ANALYZA             ✓ OK
TEST 4: SIFROVANI S CISELNYM KODEM     ✓ OK
TEST 5: ZACHOVANI VELIKOSTI PISMEN     ✓ OK
TEST 6: ZACHOVANI SPECIALNICH ZNAKU    ✓ OK

SOUHRN: Uspesne: 6 | Selhaly: 0
```

---

## 🎓 Co je Caesarova šifra?

Caesarova šifra je **nejstarší známá šifrovací metoda**, pojmenovaná po **Juliu Caesarovi**.

### Princip:

```
Každé písmeno se posune o N pozic v abecedě.

Příklad s posunem 3:
A → D
B → E
C → F
...

Text:   AHOJ SVETE
Posun:  3
Šifra:  DKRM VYHWH
```

### Historický kontext:

Julius Caesar používal posun o **3 pozice** pro svou soukromou vojenskou korespondenci kolem roku **50 př. n. l.**

---

## 🔍 Frekvenční analýza - Jak prolomit šifru?

### Princip:

1. V češtině je nejčastější písmeno **E** (9.8%)
2. Caesarova šifra **zachovává frekvenci** písmen
3. Najdeme nejčastější písmeno v šifře → pravděpodobně je to zašifrované E
4. Vypočítáme posun a dešifrujeme

### Příklad:

```
Zašifrovaný text má nejčastější písmeno H
Předpoklad: H je zašifrované E
Výpočet posunu: H(7) - E(4) = 3
→ Dešifrujeme s posunem 3
```

### Limity:

- Funguje dobře u **delších textů** (50+ znaků)
- U krátkých textů může selhat
- Aplikace nabízí **více kandidátů** seřazených podle pravděpodobnosti

---

## 🔢 Šifrování s číselným kódem

Vylepšená verze Caesarovy šifry - **každé písmeno má jiný posun**:

```
Text:  A  H  O  J
Kód:   1  2  3  1  (opakuje se)

A + 1 → B
H + 2 → J
O + 3 → R
J + 1 → K

Výsledek: BJRK
```

### Výhody:

- ✅ Těžší prolomit než klasická Caesarova šifra
- ✅ Frekvenční analýza je složitější
- ✅ Každé E může být zašifrované jinak

---

## 💻 Technické požadavky

- **Python:** 3.6 nebo vyšší
- **Závislosti:** Pouze standardní knihovna (žádné externí balíčky)
- **Platformy:** Windows / Linux / macOS

---

## 📚 Příklady použití

### Příklad 1: Základní šifrování

```python
from caesar_cipher import CaesarCipher

cipher = CaesarCipher()

# Šifrování
text = "Ahoj svete"
encrypted = cipher.caesar_shift(text, shift=3, decrypt=False)
print(encrypted)  # "Dkrm vyhwh"

# Dešifrování
decrypted = cipher.caesar_shift(encrypted, shift=3, decrypt=True)
print(decrypted)  # "Ahoj svete"
```

### Příklad 2: Prolomení šifry

```python
# Máme zachycenou zprávu
encrypted = "Dkrm vyhwh"

# Metoda 1: Všech 26 variant
cipher.show_all_shifts(encrypted)

# Metoda 2: Automatická frekvenční analýza
candidates = cipher.frequency_attack(encrypted)
```

### Příklad 3: Pokročilé šifrování

```python
# Číselný kód
text = "TAJNE"
code = "12345"

encrypted = cipher.cipher_with_numeric_key(text, code, decrypt=False)
print(encrypted)  # "UCMRJ"
```

---

## ⚠️ DŮLEŽITÉ BEZPEČNOSTNÍ VAROVÁNÍ

```
╔═══════════════════════════════════════════════════════════╗
║  NIKDY nepoužívejte Caesarovu šifru pro skutečná data!   ║
╚═══════════════════════════════════════════════════════════╝
```

Caesarova šifra je:
- ❌ **Extrémně slabá** - prolomitelná za sekundy
- ❌ **Nevhodná** pro jakákoli citlivá data
- ❌ **Pouze pro vzdělávání** - ne pro produkční použití

Pro skutečné šifrování použijte:
- ✅ **AES-256** (symetrické šifrování)
- ✅ **RSA** (asymetrické šifrování)
- ✅ Moderní knihovny: `cryptography`, `PyCryptodome`

---

## 📖 Dokumentace

| Dokument | Obsah |
|----------|-------|
| `README_CAESAR.md` | Detailní technická dokumentace (800+ řádků) |
| `NAVOD.txt` | Rychlá příručka pro začátečníky |
| `PREHLED_PROJEKTU.txt` | Kompletní přehled projektu |

---

## 🎯 Vzdělávací hodnota

### Naučíte se:

1. **Kryptografie**
   - Základy substituční šifry
   - Symetrické šifrování
   - Kryptoanalýza

2. **Bezpečnost**
   - Slabiny jednoduchých šifer
   - Frekvenční analýza
   - Důležitost moderních algoritmů

3. **Programování**
   - Zpracování textu v Pythonu
   - Objektově orientované programování
   - Unit testing
   - Dokumentace kódu

---

## 🔧 Možná rozšíření

Nápady pro budoucí verze:

- [ ] Grafické rozhraní (GUI)
- [ ] Více šifer (Vigenère, Playfair)
- [ ] Práce se soubory
- [ ] Vizualizace frekvenční analýzy
- [ ] Vícejazyčná podpora
- [ ] Webová verze

---

## 📞 Kontakt

**Autor:** Kamil Stanek
**Projekt:** Caesarova šifra - Vzdělávací aplikace
**Datum:** 7. listopadu 2025

---

## 📜 Licence

Tento projekt je vytvořen pro **vzdělávací účely**.
Volně k použití a modifikaci.

---

## 📚 Další zdroje

### Knihy:
- "The Code Book" - Simon Singh
- "Applied Cryptography" - Bruce Schneier

### Online:
- Wikipedia: Caesar cipher
- Khan Academy: Cryptography course
- CrypTool: Educational crypto software

---

## ✨ Závěr

Projekt poskytuje **kompletní implementaci** Caesarovy šifry včetně:

✓ Všech požadovaných funkcí
✓ Důkladných testů (6/6 prošlo)
✓ Detailní dokumentace (2000+ řádků)
✓ Praktických ukázek a příkladů

**Přejeme hodně zábavy s objevováním tajů kryptografie!** 🔐

---

*Vytvořeno s 💻 v Pythonu*
