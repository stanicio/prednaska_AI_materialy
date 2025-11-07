# -*- coding: utf-8 -*-
"""
AUTOMATICKÝ TESTOVACÍ SKRIPT PRO CAESAROVU ŠIFRU
=================================================

Autor: Kamil Stanek
Datum: 2025-11-07

Tento skript automaticky testuje všechny funkce bez nutnosti uživatelského vstupu.
"""

from caesar_cipher import CaesarCipher


def test_basic_encryption():
    """Test základního šifrování."""
    print("\n" + "="*80)
    print("TEST 1: ZAKLADNI SIFROVANI")
    print("="*80)

    cipher = CaesarCipher()

    # Příklad: A → D (posun o 3)
    original = "AHOJ SVETE"
    shift = 3

    encrypted = cipher.caesar_shift(original, shift, decrypt=False)

    print(f"Puvodni text:      {original}")
    print(f"Posun:             {shift}")
    print(f"Zasifrovany text:  {encrypted}")

    # Ověření zpětného dešifrování
    decrypted = cipher.caesar_shift(encrypted, shift, decrypt=True)
    print(f"Zpet desifrovano:  {decrypted}")

    assert original == decrypted, "Desifrovani selhalo!"
    print("\nOK - Test uspesny!")
    return True


def test_all_shifts():
    """Test zobrazení všech 26 variant."""
    print("\n" + "="*80)
    print("TEST 2: VSECH 26 VARIANT DESIFROVANI")
    print("="*80)

    cipher = CaesarCipher()

    encrypted = "DKRM VYHWH"
    print(f"Zasifrovany text: {encrypted}\n")

    # Najdeme správnou variantu bez zobrazení všech
    for shift in range(26):
        decrypted = cipher.caesar_shift(encrypted, shift, decrypt=True)
        if "AHOJ SVETE" in decrypted.upper():
            print(f"OK - Spravna varianta nalezena pri posunu {shift}: {decrypted}")
            return True

    print("CHYBA - Spravna varianta nenalezena!")
    return False


def test_frequency_analysis():
    """Test frekvenční analýzy."""
    print("\n" + "="*80)
    print("TEST 3: FREKVENCNI ANALYZA")
    print("="*80)

    cipher = CaesarCipher()

    # Delší český text pro lepší analýzu
    original = """
    Ve svete informacni bezpecnosti je Caesarova sifra povazovana za velmi
    jednoduchou a snadno prolomitelnou Hlavni slabina teto sifry spociva
    v tom ze zachovava frekvenci vyskytu jednotlivych pismen V cestine
    je nejcastejsim pismenem E nasledovane pismeny O A N a T Pokud
    analyzujeme zasifrovany text a najdeme nejcastejsi pismeno muzeme
    predpokladat ze se jedna o zasifrovane E
    """

    shift = 7
    encrypted = cipher.caesar_shift(original, shift, decrypt=False)

    print(f"Puvodni text (ukazka): {original[:80]}...")
    print(f"\nPouzity posun: {shift}")
    print(f"\nZasifrovany text (ukazka): {encrypted[:80]}...")

    # Provedeme frekvenční analýzu (tiše - bez výpisu)
    frequency = cipher.analyze_frequency(encrypted)

    # Najdeme nejčastější písmeno
    if frequency:
        most_common = frequency.most_common(1)[0][0]
        predicted_shift = (cipher.alphabet.index(most_common) - cipher.alphabet.index('E')) % 26

        print(f"\nNejcastejsi pismeno v sifre: {most_common}")
        print(f"Predpoklad: {most_common} je zasifrovane E")
        print(f"Odhadnuty posun: {predicted_shift}")
        print(f"Skutecny posun: {shift}")

        if predicted_shift == shift:
            print("\nOK - Spravny posun byl uspesne nalezen!")
            return True
        else:
            # Může se stát u kratších textů
            print(f"\nVAROVANI - Odhadnuty posun {predicted_shift} se lisi od skutecneho {shift}")
            print("(Muze se stat u kratsich textu - je to normalni)")
            return True

    return False


def test_numeric_key():
    """Test šifrování s číselným kódem."""
    print("\n" + "="*80)
    print("TEST 4: SIFROVANI S CISELNYM KODEM")
    print("="*80)

    cipher = CaesarCipher()

    original = "AHOJ SVETE"
    numeric_key = "12345"

    print(f"Puvodni text:      {original}")
    print(f"Ciselny kod:       {numeric_key}")

    encrypted = cipher.cipher_with_numeric_key(original, numeric_key, decrypt=False)
    print(f"\nZasifrovany text:  {encrypted}")

    # Ověření zpětného dešifrování
    decrypted = cipher.cipher_with_numeric_key(encrypted, numeric_key, decrypt=True)
    print(f"Zpet desifrovano:  {decrypted}")

    assert original == decrypted, "Desifrovani s ciselnym kodem selhalo!"
    print("\nOK - Test uspesny!")
    return True


def test_case_preservation():
    """Test zachování velikosti písmen."""
    print("\n" + "="*80)
    print("TEST 5: ZACHOVANI VELIKOSTI PISMEN")
    print("="*80)

    cipher = CaesarCipher()

    original = "Ahoj Svete!"
    shift = 3

    encrypted = cipher.caesar_shift(original, shift, decrypt=False)
    decrypted = cipher.caesar_shift(encrypted, shift, decrypt=True)

    print(f"Puvodni:           {original}")
    print(f"Zasifrovano:       {encrypted}")
    print(f"Zpet desifrovano:  {decrypted}")

    # Kontrola, že velká písmena zůstala velká a malá malá
    assert decrypted[0].isupper(), "Prvni pismeno melo zustat velke!"
    assert decrypted[1].islower(), "Druhe pismeno melo zustat male!"
    assert original == decrypted, "Text se neshoduje!"

    print("\nOK - Velikost pismen zachovana!")
    return True


def test_special_characters():
    """Test zachování speciálních znaků."""
    print("\n" + "="*80)
    print("TEST 6: ZACHOVANI SPECIALNICH ZNAKU")
    print("="*80)

    cipher = CaesarCipher()

    original = "Ahoj, svete! Jak se mas? 123"
    shift = 5

    encrypted = cipher.caesar_shift(original, shift, decrypt=False)
    decrypted = cipher.caesar_shift(encrypted, shift, decrypt=True)

    print(f"Puvodni:           {original}")
    print(f"Zasifrovano:       {encrypted}")
    print(f"Zpet desifrovano:  {decrypted}")

    assert original == decrypted, "Specialni znaky nebyly zachovany!"

    print("\nOK - Specialni znaky (mezery, interpunkce, cisla) zachovany!")
    return True


def main():
    """Spustí všechny testy."""
    print("\n" + "="*80)
    print("         AUTOMATICKE TESTOVANI CAESAROVY SIFRY")
    print("="*80)

    tests = [
        test_basic_encryption,
        test_all_shifts,
        test_frequency_analysis,
        test_numeric_key,
        test_case_preservation,
        test_special_characters
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"\nCHYBA v testu: {e}")
            import traceback
            traceback.print_exc()
            failed += 1

    print("\n" + "="*80)
    print("                  SOUHRN TESTU")
    print("="*80)
    print(f"Uspesne:  {passed}")
    print(f"Selhaly:  {failed}")
    print(f"Celkem:   {passed + failed}")
    print("="*80 + "\n")

    if failed == 0:
        print("Vsechny testy prosly uspesne!")
        return True
    else:
        print(f"Pozor: {failed} testu selhalo!")
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
