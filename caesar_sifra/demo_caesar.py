# -*- coding: utf-8 -*-
"""
DEMONSTRACE CAESAROVY ŠIFRY
===========================

Autor: Kamil Stanek
Datum: 2025-11-07

Tento skript ukazuje praktické použití Caesarovy šifry s názornými příklady.
"""

from caesar_cipher import CaesarCipher


def demo_1_basic():
    """Ukázka základního šifrování - Caesarův klasický posun o 3."""
    print("\n" + "="*80)
    print("DEMO 1: KLASICKÁ CAESAROVA ŠIFRA (posun o 3)")
    print("="*80)
    print("\nHistorická poznámka:")
    print("Julius Caesar používal posun o 3 pozice pro svou soukromou korespondenci.")
    print("A → D, B → E, C → F, atd.\n")

    cipher = CaesarCipher()

    message = "Ahoj Caesar, jak se mas?"
    shift = 3

    print(f"Původní zpráva:  {message}")
    print(f"Posun:           {shift}")

    encrypted = cipher.caesar_shift(message, shift, decrypt=False)
    print(f"Zašifrováno:     {encrypted}")

    print("\nNyní dešifrování:")
    decrypted = cipher.caesar_shift(encrypted, shift, decrypt=True)
    print(f"Dešifrováno:     {decrypted}")


def demo_2_rot13():
    """ROT13 - speciální případ Caesarovy šifry."""
    print("\n" + "="*80)
    print("DEMO 2: ROT13 - SPECIÁLNÍ PŘÍPAD (posun o 13)")
    print("="*80)
    print("\nZajímavost:")
    print("ROT13 má unikátní vlastnost - šifrování a dešifrování je STEJNÁ operace!")
    print("(Protože 13 + 13 = 26, což vrací písmeno na původní pozici)\n")

    cipher = CaesarCipher()

    message = "Toto je tajemstvi"
    shift = 13

    print(f"Původní text:    {message}")

    encrypted = cipher.caesar_shift(message, shift, decrypt=False)
    print(f"Zasifrovano:     {encrypted}")

    # Aplikujeme ROT13 znovu - měli bychom dostat původní text
    back = cipher.caesar_shift(encrypted, shift, decrypt=False)
    print(f"ROT13 znovu:     {back}")
    print("\nVidíte? ROT13 aplikované dvakrát vrací původní text!")


def demo_3_attack():
    """Ukázka prolomení šifry."""
    print("\n" + "="*80)
    print("DEMO 3: PROLOMENÍ ŠIFRY BEZ ZNALOSTI POSUNU")
    print("="*80)
    print("\nScenář:")
    print("Zachytili jste zašifrovanou zprávu, ale neznáte posun...")
    print("Zkusíme ji prolomit dvěma způsoby:\n")

    cipher = CaesarCipher()

    # Původní tajná zpráva
    secret = "Ve ctvrtek ve dvacet hodin se sejdeme u fontany"
    unknown_shift = 7

    encrypted = cipher.caesar_shift(secret, unknown_shift, decrypt=False)

    print(f"Zachycená zpráva: {encrypted}")
    print("\n" + "-"*80)

    # Metoda 1: Brute force
    print("\nMETODA 1: Vyzkoušíme všech 26 možností")
    print("-"*80)

    found = False
    for shift in range(26):
        decrypted = cipher.caesar_shift(encrypted, shift, decrypt=True)
        # Hledáme text, který dává smysl
        if "ctvrtek" in decrypted.lower():
            print(f"Posun {shift:2d}: {decrypted}  ← Toto dává smysl!")
            found = True
        else:
            # Ukážeme jen pár prvních pokusů
            if shift < 3:
                print(f"Posun {shift:2d}: {decrypted}  (nesmysl)")

    if not found:
        print("...")
        for shift in range(5, 8):
            decrypted = cipher.caesar_shift(encrypted, shift, decrypt=True)
            if "ctvrtek" in decrypted.lower():
                print(f"Posun {shift:2d}: {decrypted}  ← Toto dává smysl!")

    # Metoda 2: Frekvenční analýza
    print("\n" + "-"*80)
    print("METODA 2: Frekvenční analýza (automatická)")
    print("-"*80)

    frequency = cipher.analyze_frequency(encrypted)
    if frequency:
        most_common = frequency.most_common(1)[0][0]
        predicted_shift = (cipher.alphabet.index(most_common) -
                          cipher.alphabet.index('E')) % 26

        print(f"\nNejčastější písmeno v šifře: {most_common}")
        print(f"Předpoklad: '{most_common}' je zašifrované 'E'")
        print(f"Vypočtený posun: {predicted_shift}")

        decrypted = cipher.caesar_shift(encrypted, predicted_shift, decrypt=True)
        print(f"\nDešifrovaný text: {decrypted}")

        if predicted_shift == unknown_shift:
            print("\nAutomat správně uhodl posun!")
        else:
            print(f"\n(Pro tento krátký text nemusel automat uhodnout - ale metoda funguje)")


def demo_4_numeric_key():
    """Ukázka šifrování s číselným kódem - složitější varianta."""
    print("\n" + "="*80)
    print("DEMO 4: ŠIFROVÁNÍ S ČÍSELNÝM KÓDEM")
    print("="*80)
    print("\nVylepšení Caesarovy šifry:")
    print("Každé písmeno má JINÝ posun podle číselného kódu.")
    print("Tím je šifra mnohem těžší k prolomení!\n")

    cipher = CaesarCipher()

    message = "UTOK ZACINA ZITRA"
    numeric_key = "314159"  # Začátek čísla π

    print(f"Zpráva:          {message}")
    print(f"Číselný kód:     {numeric_key}")
    print("\nŠifrování po znacích:")
    print("-"*40)

    # Ukážeme postup
    key_digits = [int(d) for d in numeric_key]
    result = []
    key_index = 0

    for i, char in enumerate(message):
        if char.upper() in cipher.alphabet:
            shift = key_digits[key_index % len(key_digits)]
            old_index = cipher.alphabet.index(char.upper())
            new_index = (old_index + shift) % 26
            new_char = cipher.alphabet[new_index]

            print(f"Pozice {i+1}: {char} + {shift} → {new_char}")
            result.append(new_char)
            key_index += 1
        else:
            print(f"Pozice {i+1}: {char} (mezera)")
            result.append(char)

    encrypted = cipher.cipher_with_numeric_key(message, numeric_key, decrypt=False)
    print(f"\nZašifrováno:     {encrypted}")

    decrypted = cipher.cipher_with_numeric_key(encrypted, numeric_key, decrypt=True)
    print(f"Dešifrováno:     {decrypted}")

    print("\nProč je to bezpečnější?")
    print("- Frekvenční analýza nefunguje (každé E má jiný posun)")
    print("- Je potřeba znát číselný kód")
    print("- Mnohem více možných kombinací")


def demo_5_frequency_detail():
    """Detailní ukázka frekvenční analýzy."""
    print("\n" + "="*80)
    print("DEMO 5: DETAILNÍ FREKVENČNÍ ANALÝZA")
    print("="*80)
    print("\nVysvětlení principu:")
    print("V každém jazyce mají různá písmena různou frekvenci výskytu.")
    print("Caesarova šifra tuto frekvenci ZACHOVÁVÁ!\n")

    cipher = CaesarCipher()

    # Použijeme delší text pro lepší statistiku
    long_text = """
    Kryptografie je veda o utajovani zprav Caesarova sifra je jedna
    z nejstarsich kryptografickych metod Ve sve dobe byla velmi efektivni
    protoze vetshina lidi neumet cist a psat Dnes je vsak tato metoda
    velmi snadno prolomitelna pomoci pocitace nebo i rucne Hlavni slabina
    spociva v zachovani frekvence pismen
    """

    shift = 9
    encrypted = cipher.caesar_shift(long_text, shift, decrypt=False)

    print("Původní text (úryvek):")
    print("-"*80)
    print(long_text[:100] + "...")

    print("\nZašifrovaný text (úryvek):")
    print("-"*80)
    print(encrypted[:100] + "...")

    # Analýza původního textu
    print("\n" + "="*80)
    print("FREKVENCE V PŮVODNÍM TEXTU:")
    print("="*80)

    freq_original = cipher.analyze_frequency(long_text)
    total_orig = sum(freq_original.values())

    print("\nTop 5 nejčastějších písmen:")
    for i, (letter, count) in enumerate(freq_original.most_common(5), 1):
        percentage = (count / total_orig) * 100
        print(f"{i}. {letter}: {count:3d}x ({percentage:5.2f}%)")

    # Analýza šifry
    print("\n" + "="*80)
    print("FREKVENCE V ZAŠIFROVANÉM TEXTU:")
    print("="*80)

    freq_encrypted = cipher.analyze_frequency(encrypted)
    total_enc = sum(freq_encrypted.values())

    print("\nTop 5 nejčastějších písmen:")
    for i, (letter, count) in enumerate(freq_encrypted.most_common(5), 1):
        percentage = (count / total_enc) * 100
        print(f"{i}. {letter}: {count:3d}x ({percentage:5.2f}%)")

    print("\n" + "-"*80)
    print("ZÁVĚR:")
    print("-"*80)
    print("Všimněte si, že frekvence jsou STEJNÉ - jen písmena jsou 'posunutá'!")
    print("To je slabina, kterou můžeme využít k prolomení šifry.")


def main():
    """Spustí všechny demonstrace."""
    print("\n" + "="*80)
    print("      DEMONSTRACE CAESAROVY SIFRY - PRAKTICKE PRIKLADY")
    print("="*80)

    demos = [
        ("Klasická Caesarova šifra", demo_1_basic),
        ("ROT13 - speciální případ", demo_2_rot13),
        ("Prolomení šifry", demo_3_attack),
        ("Číselný kód", demo_4_numeric_key),
        ("Frekvenční analýza", demo_5_frequency_detail),
    ]

    for i, (name, func) in enumerate(demos, 1):
        print(f"\n\n{'='*80}")
        print(f"DEMO {i}/{len(demos)}: {name}")
        input(f"\nStiskněte Enter pro spuštění...")

        try:
            func()
        except Exception as e:
            print(f"\nCHYBA: {e}")
            import traceback
            traceback.print_exc()

        if i < len(demos):
            input(f"\n{'='*80}\nStiskněte Enter pro další demo...")

    print("\n\n" + "="*80)
    print("         VŠECHNY DEMONSTRACE DOKONČENY")
    print("="*80)
    print("\nDěkujeme za pozornost!")
    print("Pro interaktivní práci spusťte: python caesar_cipher.py")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
