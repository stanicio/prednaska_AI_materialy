"""
CAESAROVA ŠIFRA - Aplikace pro šifrování a dešifrování textu
=============================================================

Autor: Kamil Stanek
Datum: 2025-11-07

POPIS:
------
Aplikace implementuje Caesarovu šifru s následujícími funkcemi:
1. Základní šifrování/dešifrování s pevným posunem
2. Zobrazení všech 26 možných dešifrovaných variant
3. Analýza četnosti znaků pro automatické prolomení šifry
4. Šifrování pomocí číselného kódu (různé posuny pro různé znaky)

CAESAROVA ŠIFRA:
---------------
Princip: Každé písmeno v textu je posunuto o N pozic v abecedě.
Příklad: Posun o 3 → A→D, B→E, C→F, atd.

ŠIFROVÁNÍ POMOCÍ ČÍSELNÉHO KÓDU:
---------------------------------
Každý znak textu je šifrován s posunem určeným odpovídajícím číslem v kódu.
Kód se opakuje, pokud je text delší než kód.
Příklad: Text "AHOJ", Kód "123" → A posun 1, H posun 2, O posun 3, J posun 1
"""

from collections import Counter
import string


class CaesarCipher:
    """
    Třída pro práci s Caesarovou šifrou.

    Atributy:
    ---------
    CZECH_FREQ : dict
        Frekvence písmen v českém jazyce (v procentech)
    """

    # Četnost písmen v českém jazyce (aproximace)
    CZECH_FREQ = {
        'E': 9.8, 'O': 7.4, 'A': 7.0, 'N': 6.5, 'T': 5.9,
        'I': 5.8, 'S': 5.3, 'L': 4.2, 'V': 4.1, 'R': 3.9,
        'K': 3.5, 'D': 3.4, 'U': 2.9, 'M': 2.8, 'P': 2.7,
        'C': 2.1, 'H': 1.8, 'Z': 1.7, 'J': 1.6, 'B': 1.5,
        'Y': 1.4, 'F': 0.3, 'G': 0.2, 'W': 0.1, 'Q': 0.1, 'X': 0.1
    }

    def __init__(self):
        """Inicializace šifry."""
        self.alphabet = string.ascii_uppercase

    def caesar_shift(self, text, shift, decrypt=False):
        """
        Základní Caesarova šifra s pevným posunem.

        Parametry:
        ----------
        text : str
            Text k zašifrování/dešifrování
        shift : int
            Počet pozic posunu (1-25)
        decrypt : bool
            True pro dešifrování, False pro šifrování

        Vrací:
        ------
        str : Zašifrovaný/dešifrovaný text

        Poznámka:
        ---------
        Zachovává malá/velká písmena a nešifruje znaky mimo abecedu.
        """
        if decrypt:
            shift = -shift

        result = []

        for char in text:
            if char.upper() in self.alphabet:
                # Zjistíme, zda je znak malý nebo velký
                is_lower = char.islower()
                char = char.upper()

                # Najdeme pozici v abecedě (0-25)
                old_index = self.alphabet.index(char)

                # Posuneme o shift pozic (modulo 26 pro cyklický posun)
                new_index = (old_index + shift) % 26

                # Získáme nový znak
                new_char = self.alphabet[new_index]

                # Vrátíme původní velikost písmene
                if is_lower:
                    new_char = new_char.lower()

                result.append(new_char)
            else:
                # Nešifrujeme znaky mimo abecedu (mezery, čísla, interpunkce)
                result.append(char)

        return ''.join(result)

    def show_all_shifts(self, encrypted_text):
        """
        Zobrazí všech 26 možných dešifrovaných variant.

        Parametry:
        ----------
        encrypted_text : str
            Zašifrovaný text

        Vrací:
        ------
        list : Seznam tuple (posun, dešifrovaný_text)

        Poznámka:
        ---------
        Užitečné pro ruční analýzu - uživatel může vizuálně najít správnou variantu.
        """
        results = []

        print("\n" + "="*80)
        print("VŠECH 26 MOŽNÝCH DEŠIFROVANÝCH VARIANT:")
        print("="*80)

        for shift in range(26):
            decrypted = self.caesar_shift(encrypted_text, shift, decrypt=True)
            results.append((shift, decrypted))
            print(f"Posun {shift:2d}: {decrypted}")

        print("="*80 + "\n")
        return results

    def analyze_frequency(self, text):
        """
        Analyzuje četnost písmen v textu.

        Parametry:
        ----------
        text : str
            Text k analýze

        Vrací:
        ------
        Counter : Objekt s četností jednotlivých písmen

        Princip:
        --------
        V každém jazyce mají některá písmena vyšší frekvenci výskytu.
        V češtině je to 'E' (cca 9.8%), následované 'O', 'A', 'N', atd.
        Porovnáním nejčastějšího písmene v šifře s 'E' můžeme odhadnout posun.
        """
        # Pouze písmena, převedeme na velká
        letters_only = [char.upper() for char in text if char.upper() in self.alphabet]

        # Spočítáme četnost
        frequency = Counter(letters_only)

        return frequency

    def frequency_attack(self, encrypted_text):
        """
        Automatické prolomení šifry pomocí frekvenční analýzy.

        Parametry:
        ----------
        encrypted_text : str
            Zašifrovaný text

        Vrací:
        ------
        list : Seznam tuple (pravděpodobnost, posun, dešifrovaný_text)
               seřazený podle pravděpodobnosti (nejvyšší první)

        Algoritmus:
        -----------
        1. Spočítáme četnost písmen v šifře
        2. Najdeme nejčastější písmeno
        3. Předpokládáme, že to je zašifrované 'E' (nejčastější v češtině)
        4. Vypočítáme posun: shift = (pozice_nejčastějšího - pozice_E) % 26
        5. Vyzkoušíme i další možnosti (druhé, třetí nejčastější písmeno)
        """
        frequency = self.analyze_frequency(encrypted_text)

        print("\n" + "="*80)
        print("FREKVENČNÍ ANALÝZA:")
        print("="*80)

        # Zobrazíme četnost písmen
        print("\nČetnost písmen v šifře:")
        total_letters = sum(frequency.values())

        for letter, count in frequency.most_common():
            percentage = (count / total_letters) * 100
            print(f"{letter}: {count:4d} ({percentage:5.2f}%)")

        print("\nOčekávaná četnost v češtině:")
        print("E: 9.8%, O: 7.4%, A: 7.0%, N: 6.5%, T: 5.9%")

        # Zkusíme několik nejčastějších písmen
        candidates = []

        # Pro top 5 nejčastějších písmen v šifře
        for rank, (most_common_letter, count) in enumerate(frequency.most_common(5), 1):
            # Předpokládáme, že to je 'E'
            shift = (self.alphabet.index(most_common_letter) - self.alphabet.index('E')) % 26
            decrypted = self.caesar_shift(encrypted_text, shift, decrypt=True)

            # Spočítáme "score" - korelaci s českou frekvencí
            score = self._calculate_frequency_score(decrypted)

            candidates.append((score, shift, decrypted, most_common_letter, rank))

        # Seřadíme podle score (nejvyšší první)
        candidates.sort(reverse=True)

        print("\n" + "="*80)
        print("NEJPRAVDĚPODOBNĚJŠÍ DEŠIFROVÁNÍ:")
        print("="*80)

        for i, (score, shift, decrypted, letter, rank) in enumerate(candidates[:3], 1):
            print(f"\n{i}. Předpoklad: '{letter}' (#{rank} nejčastější) je 'E'")
            print(f"   Posun: {shift}")
            print(f"   Score: {score:.4f}")
            print(f"   Text: {decrypted[:100]}{'...' if len(decrypted) > 100 else ''}")

        print("="*80 + "\n")

        return candidates

    def _calculate_frequency_score(self, text):
        """
        Vypočítá score na základě podobnosti s českou frekvencí.

        Parametry:
        ----------
        text : str
            Text k vyhodnocení

        Vrací:
        ------
        float : Score (vyšší = lepší shoda s češtinou)

        Metoda:
        -------
        Používá chi-squared test pro porovnání frekvence.
        """
        frequency = self.analyze_frequency(text)
        total = sum(frequency.values())

        if total == 0:
            return 0

        score = 0
        for letter in self.alphabet:
            expected = self.CZECH_FREQ.get(letter, 0.05) / 100  # Normalizováno
            observed = frequency.get(letter, 0) / total

            # Chi-squared komponenta
            if expected > 0:
                score -= ((observed - expected) ** 2) / expected

        return score

    def cipher_with_numeric_key(self, text, numeric_key, decrypt=False):
        """
        Šifrování pomocí číselného kódu (různé posuny).

        Parametry:
        ----------
        text : str
            Text k zašifrování/dešifrování
        numeric_key : str
            Číselný kód (např. "12345")
        decrypt : bool
            True pro dešifrování

        Vrací:
        ------
        str : Zašifrovaný/dešifrovaný text

        Princip:
        --------
        Každé číslo v kódu určuje posun pro odpovídající znak textu.
        Kód se cyklicky opakuje, pokud je text delší.

        Příklad:
        --------
        Text: "AHOJ"
        Kód: "123"

        A → posun 1 → B
        H → posun 2 → J
        O → posun 3 → R
        J → posun 1 → K (kód se opakuje)

        Výsledek: "BJRK"
        """
        # Převedeme klíč na seznam čísel
        try:
            key_digits = [int(d) for d in numeric_key if d.isdigit()]
        except ValueError:
            raise ValueError("Klíč musí obsahovat pouze čísla!")

        if not key_digits:
            raise ValueError("Klíč musí obsahovat alespoň jednu číslici!")

        result = []
        key_index = 0

        for char in text:
            if char.upper() in self.alphabet:
                # Zjistíme aktuální posun z klíče
                shift = key_digits[key_index % len(key_digits)]

                if decrypt:
                    shift = -shift

                # Zachováme velikost písmene
                is_lower = char.islower()
                char = char.upper()

                # Posuneme
                old_index = self.alphabet.index(char)
                new_index = (old_index + shift) % 26
                new_char = self.alphabet[new_index]

                if is_lower:
                    new_char = new_char.lower()

                result.append(new_char)
                key_index += 1
            else:
                # Nešifrujeme mezery a interpunkci
                result.append(char)

        return ''.join(result)


def main():
    """
    Hlavní funkce aplikace s interaktivním menu.
    """
    cipher = CaesarCipher()

    while True:
        print("\n" + "="*80)
        print("CAESAROVA ŠIFRA - Hlavní menu")
        print("="*80)
        print("1. Zašifrovat text (pevný posun)")
        print("2. Dešifrovat text (známý posun)")
        print("3. Zobrazit všech 26 variant dešifrování")
        print("4. Prolomit šifru pomocí frekvenční analýzy")
        print("5. Šifrovat pomocí číselného kódu")
        print("6. Dešifrovat pomocí číselného kódu")
        print("0. Konec")
        print("="*80)

        choice = input("\nVaše volba: ").strip()

        if choice == '0':
            print("\nDěkuji za použití aplikace!")
            break

        elif choice == '1':
            # Šifrování
            text = input("\nZadejte text k zašifrování: ")
            try:
                shift = int(input("Zadejte posun (1-25): "))
                if not 1 <= shift <= 25:
                    print("Posun musí být mezi 1 a 25!")
                    continue
            except ValueError:
                print("Neplatné číslo!")
                continue

            encrypted = cipher.caesar_shift(text, shift, decrypt=False)
            print(f"\nPůvodní text: {text}")
            print(f"Posun: {shift}")
            print(f"Zašifrovaný text: {encrypted}")

        elif choice == '2':
            # Dešifrování se známým posunem
            text = input("\nZadejte text k dešifrování: ")
            try:
                shift = int(input("Zadejte posun (1-25): "))
                if not 1 <= shift <= 25:
                    print("Posun musí být mezi 1 a 25!")
                    continue
            except ValueError:
                print("Neplatné číslo!")
                continue

            decrypted = cipher.caesar_shift(text, shift, decrypt=True)
            print(f"\nZašifrovaný text: {text}")
            print(f"Posun: {shift}")
            print(f"Dešifrovaný text: {decrypted}")

        elif choice == '3':
            # Všech 26 variant
            text = input("\nZadejte zašifrovaný text: ")
            cipher.show_all_shifts(text)
            input("Stiskněte Enter pro pokračování...")

        elif choice == '4':
            # Frekvenční analýza
            text = input("\nZadejte zašifrovaný text: ")
            if len(text.strip()) < 50:
                print("\nVarování: Pro přesnou frekvenční analýzu je doporučeno")
                print("použít delší text (alespoň 50-100 znaků).")

            cipher.frequency_attack(text)
            input("Stiskněte Enter pro pokračování...")

        elif choice == '5':
            # Šifrování pomocí číselného kódu
            text = input("\nZadejte text k zašifrování: ")
            numeric_key = input("Zadejte číselný kód (např. 12345): ")

            try:
                encrypted = cipher.cipher_with_numeric_key(text, numeric_key, decrypt=False)
                print(f"\nPůvodní text: {text}")
                print(f"Číselný kód: {numeric_key}")
                print(f"Zašifrovaný text: {encrypted}")
            except ValueError as e:
                print(f"\nChyba: {e}")

        elif choice == '6':
            # Dešifrování pomocí číselného kódu
            text = input("\nZadejte text k dešifrování: ")
            numeric_key = input("Zadejte číselný kód (např. 12345): ")

            try:
                decrypted = cipher.cipher_with_numeric_key(text, numeric_key, decrypt=True)
                print(f"\nZašifrovaný text: {text}")
                print(f"Číselný kód: {numeric_key}")
                print(f"Dešifrovaný text: {decrypted}")
            except ValueError as e:
                print(f"\nChyba: {e}")

        else:
            print("\nNeplatná volba! Zkuste to znovu.")


if __name__ == "__main__":
    print("\n" + "="*80)
    print("                      CAESAROVA SIFRA")
    print("                 Aplikace pro sifrovani textu")
    print("="*80)
    print("\nAutor: Kamil Stanek")
    print("Datum: 2025-11-07")
    print("\nFunkce aplikace:")
    print("- Zakladni sifrovani a desifrovani s pevnym posunem")
    print("- Zobrazeni vsech 26 moznych variant desifrovani")
    print("- Automaticke prolomeni sifry pomoci frekvencni analyzy")
    print("- Sifrovani pomoci ciselneho kodu (ruzne posuny)")
    print("="*80 + "\n")

    main()
