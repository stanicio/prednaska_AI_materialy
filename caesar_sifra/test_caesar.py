"""
TESTOVACÍ SKRIPT PRO CAESAROVU ŠIFRU
=====================================

Autor: Kamil Stanek
Datum: 2025-11-07

Tento skript demonstruje všechny funkce aplikace caesar_cipher.py
"""

from caesar_cipher import CaesarCipher


def test_basic_encryption():
    """Test základního šifrování."""
    print("\n" + "="*80)
    print("TEST 1: ZÁKLADNÍ ŠIFROVÁNÍ")
    print("="*80)

    cipher = CaesarCipher()

    # Příklad: A → D (posun o 3)
    original = "AHOJ SVETE"
    shift = 3

    encrypted = cipher.caesar_shift(original, shift, decrypt=False)

    print(f"Původní text:      {original}")
    print(f"Posun:             {shift}")
    print(f"Zašifrovaný text:  {encrypted}")

    # Ověření zpětného dešifrování
    decrypted = cipher.caesar_shift(encrypted, shift, decrypt=True)
    print(f"Zpět dešifrováno:  {decrypted}")

    assert original == decrypted, "Dešifrování selhalo!"
    print("\n✓ Test úspěšný!")


def test_all_shifts():
    """Test zobrazení všech 26 variant."""
    print("\n" + "="*80)
    print("TEST 2: VŠECH 26 VARIANT DEŠIFROVÁNÍ")
    print("="*80)

    cipher = CaesarCipher()

    encrypted = "DKRM VYHWH"
    print(f"Zašifrovaný text: {encrypted}")

    results = cipher.show_all_shifts(encrypted)

    # Najdeme správnou variantu
    for shift, text in results:
        if "AHOJ SVETE" in text.upper():
            print(f"\n✓ Správná varianta nalezena při posunu {shift}: {text}")
            break


def test_frequency_analysis():
    """Test frekvenční analýzy."""
    print("\n" + "="*80)
    print("TEST 3: FREKVENČNÍ ANALÝZA")
    print("="*80)

    cipher = CaesarCipher()

    # Delší český text pro lepší analýzu
    original = """
    Ve světě informační bezpečnosti je Caesarova šifra považována za velmi
    jednoduchou a snadno prolomitelnou. Hlavní slabina této šifry spočívá
    v tom, že zachovává frekvenci výskytu jednotlivých písmen. V češtině
    je nejčastějším písmenem E, následované písmeny O, A, N a T. Pokud
    analyzujeme zašifrovaný text a najdeme nejčastější písmeno, můžeme
    předpokládat, že se jedná o zašifrované E.
    """

    shift = 7
    encrypted = cipher.caesar_shift(original, shift, decrypt=False)

    print(f"Původní text (ukázka): {original[:100]}...")
    print(f"\nPoužitý posun: {shift}")
    print(f"\nZašifrovaný text (ukázka): {encrypted[:100]}...")

    # Provedeme frekvenční analýzu
    candidates = cipher.frequency_attack(encrypted)

    # Zkontrolujeme, zda byl nalezen správný posun
    best_score, best_shift, best_text, _, _ = candidates[0]

    if best_shift == shift:
        print(f"\n✓ Správný posun {shift} byl úspěšně nalezen jako nejpravděpodobnější!")
    else:
        print(f"\n⚠ Nejpravděpodobnější posun je {best_shift}, správný je {shift}")
        print("  (Může se stát u kratších textů)")


def test_numeric_key():
    """Test šifrování s číselným kódem."""
    print("\n" + "="*80)
    print("TEST 4: ŠIFROVÁNÍ S ČÍSELNÝM KÓDEM")
    print("="*80)

    cipher = CaesarCipher()

    original = "AHOJ SVETE"
    numeric_key = "12345"

    print(f"Původní text:      {original}")
    print(f"Číselný kód:       {numeric_key}")

    # Ukážeme posun každého znaku
    print("\nPostup šifrování:")
    print("-" * 40)

    key_digits = [int(d) for d in numeric_key]
    key_index = 0

    for char in original:
        if char.upper() in cipher.alphabet:
            shift = key_digits[key_index % len(key_digits)]
            old_index = cipher.alphabet.index(char.upper())
            new_index = (old_index + shift) % 26
            new_char = cipher.alphabet[new_index]

            print(f"{char} + {shift} → {new_char}")
            key_index += 1
        else:
            print(f"{char} (mezera, beze změny)")

    encrypted = cipher.cipher_with_numeric_key(original, numeric_key, decrypt=False)
    print(f"\nZašifrovaný text:  {encrypted}")

    # Ověření zpětného dešifrování
    decrypted = cipher.cipher_with_numeric_key(encrypted, numeric_key, decrypt=True)
    print(f"Zpět dešifrováno:  {decrypted}")

    assert original == decrypted, "Dešifrování s číselným kódem selhalo!"
    print("\n✓ Test úspěšný!")


def demonstration_example():
    """Ukázkový příklad prolomení šifry."""
    print("\n" + "="*80)
    print("DEMONSTRACE: PROLOMENÍ NEZNÁMÉ ŠIFRY")
    print("="*80)

    cipher = CaesarCipher()

    # Tajná zpráva
    secret_message = """
    Toto je tajná zpráva zašifrovaná pomocí Caesarovy šifry.
    Obsahuje dostatek textu pro frekvenční analýzu. V češtině
    je nejčastějším písmenem E. Můžeme to využít k prolomení šifry.
    """

    secret_shift = 13  # ROT13

    encrypted = cipher.caesar_shift(secret_message, secret_shift, decrypt=False)

    print("Situace: Zachytili jste zašifrovanou zprávu:")
    print("-" * 80)
    print(encrypted)
    print("-" * 80)

    print("\nKrok 1: Zkusíme frekvenční analýzu...")
    candidates = cipher.frequency_attack(encrypted)

    print("\nKrok 2: Nejpravděpodobnější řešení:")
    best_score, best_shift, best_text, _, _ = candidates[0]

    print(f"\nOdhadnutý posun: {best_shift}")
    print(f"Dešifrovaná zpráva:")
    print("-" * 80)
    print(best_text)
    print("-" * 80)

    if best_shift == secret_shift:
        print("\n✓ Šifra byla úspěšně prolomená!")
    else:
        print(f"\n⚠ Odhadnutý posun {best_shift} se liší od skutečného {secret_shift}")


def main():
    """Spustí všechny testy."""
    print("\n" + "="*80)
    print("             TESTOVÁNÍ CAESAROVY ŠIFRY")
    print("="*80 + "\n")

    try:
        test_basic_encryption()
        input("\nStiskněte Enter pro pokračování...")

        test_all_shifts()
        input("\nStiskněte Enter pro pokračování...")

        test_frequency_analysis()
        input("\nStiskněte Enter pro pokračování...")

        test_numeric_key()
        input("\nStiskněte Enter pro pokračování...")

        demonstration_example()

        print("\n" + "="*80)
        print("VŠECHNY TESTY DOKONČENY")
        print("="*80)

    except Exception as e:
        print(f"\n❌ Chyba během testování: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
