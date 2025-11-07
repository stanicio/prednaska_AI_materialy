# -*- coding: utf-8 -*-
"""
PŘÍKLAD POUŽITÍ CAESAROVY ŠIFRY V KÓDU
=======================================

Tento soubor ukazuje, jak použít třídu CaesarCipher ve vlastním kódu.
"""

from caesar_cipher import CaesarCipher


def priklad_1_zakladni_pouziti():
    """Nejjednodušší použití - šifrování a dešifrování."""
    print("\n" + "="*60)
    print("PŘÍKLAD 1: Základní použití")
    print("="*60)

    # Vytvoříme instanci třídy
    cipher = CaesarCipher()

    # Šifrování
    text = "Ahoj svete!"
    zasifrovany = cipher.caesar_shift(text, shift=5, decrypt=False)
    print(f"Puvodni:     {text}")
    print(f"Zasifrovany: {zasifrovany}")

    # Dešifrování
    desifrovany = cipher.caesar_shift(zasifrovany, shift=5, decrypt=True)
    print(f"Desifrovany: {desifrovany}")


def priklad_2_vsechny_varianty():
    """Získání všech možných dešifrování."""
    print("\n" + "="*60)
    print("PŘÍKLAD 2: Všechny varianty")
    print("="*60)

    cipher = CaesarCipher()
    zasifrovany = "Dkrm vyhwh"

    # Získáme všechny varianty (bez vypsání)
    varianty = []
    for shift in range(26):
        desifrovany = cipher.caesar_shift(zasifrovany, shift, decrypt=True)
        varianty.append((shift, desifrovany))

    # Vypíšeme jen pár ukázek
    print(f"Zasifrovany text: {zasifrovany}\n")
    for shift, text in varianty[:5]:
        print(f"Posun {shift:2d}: {text}")
    print("...")
    # Najdeme tu správnou
    for shift, text in varianty:
        if "ahoj" in text.lower():
            print(f"Posun {shift:2d}: {text} <- Spravna!")


def priklad_3_frekvencni_analyza():
    """Automatické prolomení šifry."""
    print("\n" + "="*60)
    print("PŘÍKLAD 3: Frekvenční analýza")
    print("="*60)

    cipher = CaesarCipher()

    # Původní text
    text = "V kryptografii je Caesarova sifra velmi znama"
    zasifrovany = cipher.caesar_shift(text, shift=8, decrypt=False)

    print(f"Zasifrovany: {zasifrovany}\n")

    # Provedeme analýzu četnosti
    frekvence = cipher.analyze_frequency(zasifrovany)

    # Najdeme nejčastější písmeno
    if frekvence:
        nejcastejsi = frekvence.most_common(1)[0][0]
        odhadnuty_posun = (
            cipher.alphabet.index(nejcastejsi) -
            cipher.alphabet.index('E')
        ) % 26

        print(f"Nejcastejsi pismeno: {nejcastejsi}")
        print(f"Odhadnuty posun: {odhadnuty_posun}")

        # Dešifrujeme
        desifrovany = cipher.caesar_shift(
            zasifrovany,
            odhadnuty_posun,
            decrypt=True
        )
        print(f"Desifrovany: {desifrovany}")


def priklad_4_ciselny_kod():
    """Šifrování s číselným kódem."""
    print("\n" + "="*60)
    print("PŘÍKLAD 4: Číselný kód")
    print("="*60)

    cipher = CaesarCipher()

    text = "TAJNE"
    kod = "12345"

    print(f"Text: {text}")
    print(f"Kod:  {kod}\n")

    # Šifrování
    zasifrovany = cipher.cipher_with_numeric_key(
        text,
        kod,
        decrypt=False
    )
    print(f"Zasifrovany: {zasifrovany}")

    # Dešifrování
    desifrovany = cipher.cipher_with_numeric_key(
        zasifrovany,
        kod,
        decrypt=True
    )
    print(f"Desifrovany: {desifrovany}")


def priklad_5_zpracovani_souboru():
    """Zpracování celého souboru."""
    print("\n" + "="*60)
    print("PŘÍKLAD 5: Zpracování souboru")
    print("="*60)

    cipher = CaesarCipher()

    # Simulujeme čtení ze souboru
    obsah = """
    Toto je tajny dokument.
    Obsahuje dulezite informace.
    Nesmí se dostat do spatnych rukou.
    """

    print("Puvodni obsah:")
    print(obsah)

    # Zašifrujeme
    zasifrovany = cipher.caesar_shift(obsah, shift=10, decrypt=False)

    print("\nZasifrovany obsah:")
    print(zasifrovany)

    # V reálném případě bychom uložili do souboru:
    # with open('zasifrovany.txt', 'w', encoding='utf-8') as f:
    #     f.write(zasifrovany)


def priklad_6_vlastni_funkce():
    """Vytvoření vlastní utility funkce."""
    print("\n" + "="*60)
    print("PŘÍKLAD 6: Vlastní funkce")
    print("="*60)

    def rychle_sifrovani(text, posun):
        """Jednoduchá wrapper funkce."""
        cipher = CaesarCipher()
        return cipher.caesar_shift(text, posun, decrypt=False)

    def rychle_desifrovani(text, posun):
        """Jednoduchá wrapper funkce."""
        cipher = CaesarCipher()
        return cipher.caesar_shift(text, posun, decrypt=True)

    # Použití
    zprava = "Ahoj jak se mas"
    sifra = rychle_sifrovani(zprava, 7)
    zpet = rychle_desifrovani(sifra, 7)

    print(f"Puvodni:  {zprava}")
    print(f"Sifra:    {sifra}")
    print(f"Zpet:     {zpet}")


def priklad_7_statistiky():
    """Získání statistik o textu."""
    print("\n" + "="*60)
    print("PŘÍKLAD 7: Statistiky textu")
    print("="*60)

    cipher = CaesarCipher()

    text = "Ahoj ahoj ahoj svete svete"

    # Analýza
    frekvence = cipher.analyze_frequency(text)
    celkem = sum(frekvence.values())

    print(f"Text: {text}\n")
    print("Cetnost pismen:")
    for pismeno, pocet in frekvence.most_common():
        procenta = (pocet / celkem) * 100
        print(f"  {pismeno}: {pocet:2d}x ({procenta:5.1f}%)")


def priklad_8_validace():
    """Validace a ošetření chyb."""
    print("\n" + "="*60)
    print("PŘÍKLAD 8: Validace vstupu")
    print("="*60)

    cipher = CaesarCipher()

    # Test s různými vstupy
    testy = [
        ("Normalni text", "12345", True),
        ("Text", "abc", False),  # Neplatný kód
        ("Text", "", False),     # Prázdný kód
    ]

    for text, kod, ma_fungovat in testy:
        try:
            vysledek = cipher.cipher_with_numeric_key(
                text,
                kod,
                decrypt=False
            )
            if ma_fungovat:
                print(f"[OK] '{text}' + '{kod}' -> '{vysledek}'")
            else:
                print(f"[CHYBA] Melo selhat, ale fungovalo!")
        except ValueError as e:
            if not ma_fungovat:
                print(f"[OK] Zachycena chyba: {e}")
            else:
                print(f"[CHYBA] Neocekavana chyba: {e}")


def main():
    """Spustí všechny příklady."""
    print("\n" + "="*60)
    print("   PŘÍKLADY POUŽITÍ CAESAROVY ŠIFRY V KÓDU")
    print("="*60)

    priklady = [
        priklad_1_zakladni_pouziti,
        priklad_2_vsechny_varianty,
        priklad_3_frekvencni_analyza,
        priklad_4_ciselny_kod,
        priklad_5_zpracovani_souboru,
        priklad_6_vlastni_funkce,
        priklad_7_statistiky,
        priklad_8_validace,
    ]

    for priklad in priklady:
        priklad()

    print("\n" + "="*60)
    print("Všechny příklady dokončeny!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
