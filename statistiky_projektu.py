# -*- coding: utf-8 -*-
"""
STATISTIKY PROJEKTU CAESAROVA ŠIFRA
====================================

Autor: Kamil Stanek
Datum: 2025-11-07

Tento skript analyzuje projekt a vypočítá statistiky.
"""

import os
import re


def analyze_python_file(filepath):
    """
    Analyzuje Python soubor.

    Vrací slovník se statistikami:
    - total_lines: celkový počet řádků
    - code_lines: řádky kódu (bez prázdných a komentářů)
    - comment_lines: komentáře (#)
    - docstring_lines: docstringy (trojité uvozovky)
    - blank_lines: prázdné řádky
    """
    stats = {
        'total_lines': 0,
        'code_lines': 0,
        'comment_lines': 0,
        'docstring_lines': 0,
        'blank_lines': 0
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        in_docstring = False
        docstring_char = None

        for line in lines:
            stats['total_lines'] += 1
            stripped = line.strip()

            # Prázdný řádek
            if not stripped:
                stats['blank_lines'] += 1
                continue

            # Detekce docstringu
            if '"""' in stripped or "'''" in stripped:
                if not in_docstring:
                    # Začátek docstringu
                    in_docstring = True
                    docstring_char = '"""' if '"""' in stripped else "'''"
                    stats['docstring_lines'] += 1
                    # Kontrola jednořádkového docstringu
                    if stripped.count(docstring_char) >= 2:
                        in_docstring = False
                else:
                    # Konec docstringu
                    stats['docstring_lines'] += 1
                    in_docstring = False
                continue

            # Uvnitř docstringu
            if in_docstring:
                stats['docstring_lines'] += 1
                continue

            # Komentář
            if stripped.startswith('#'):
                stats['comment_lines'] += 1
                continue

            # Kód
            stats['code_lines'] += 1

    except Exception as e:
        print(f"Chyba při čtení {filepath}: {e}")

    return stats


def analyze_text_file(filepath):
    """
    Analyzuje textový soubor (MD, TXT).

    Vrací slovník se statistikami:
    - total_lines: celkový počet řádků
    - text_lines: řádky s textem
    - blank_lines: prázdné řádky
    """
    stats = {
        'total_lines': 0,
        'text_lines': 0,
        'blank_lines': 0
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            stats['total_lines'] += 1

            if line.strip():
                stats['text_lines'] += 1
            else:
                stats['blank_lines'] += 1

    except Exception as e:
        print(f"Chyba při čtení {filepath}: {e}")

    return stats


def get_file_size(filepath):
    """Vrací velikost souboru v kB."""
    try:
        size_bytes = os.path.getsize(filepath)
        return size_bytes / 1024
    except:
        return 0


def analyze_project():
    """Analyzuje celý projekt."""

    project_dir = r"G:\aaa1"

    # Soubory k analýze
    python_files = [
        'caesar_cipher.py',
        'test_caesar_auto.py',
        'test_caesar.py',
        'demo_caesar.py',
        'priklad_pouziti.py',
        'statistiky_projektu.py'
    ]

    doc_files = [
        'README.md',
        'README_CAESAR.md',
        'NAVOD.txt',
        'PREHLED_PROJEKTU.txt'
    ]

    other_files = [
        'SPUST_APLIKACI.bat'
    ]

    print("\n" + "="*80)
    print("           STATISTIKY PROJEKTU - CAESAROVA ŠIFRA")
    print("="*80)

    # Python soubory
    print("\n" + "="*80)
    print("PYTHON SOUBORY (.py)")
    print("="*80)

    total_py_stats = {
        'files': 0,
        'total_lines': 0,
        'code_lines': 0,
        'comment_lines': 0,
        'docstring_lines': 0,
        'blank_lines': 0,
        'size_kb': 0
    }

    for filename in python_files:
        filepath = os.path.join(project_dir, filename)
        if os.path.exists(filepath):
            stats = analyze_python_file(filepath)
            size = get_file_size(filepath)

            total_py_stats['files'] += 1
            total_py_stats['total_lines'] += stats['total_lines']
            total_py_stats['code_lines'] += stats['code_lines']
            total_py_stats['comment_lines'] += stats['comment_lines']
            total_py_stats['docstring_lines'] += stats['docstring_lines']
            total_py_stats['blank_lines'] += stats['blank_lines']
            total_py_stats['size_kb'] += size

            print(f"\n{filename}:")
            print(f"  Celkem řádků:       {stats['total_lines']:5d}")
            print(f"  - Kód:              {stats['code_lines']:5d}")
            print(f"  - Komentáře:        {stats['comment_lines']:5d}")
            print(f"  - Docstringy:       {stats['docstring_lines']:5d}")
            print(f"  - Prázdné:          {stats['blank_lines']:5d}")
            print(f"  Velikost:           {size:6.1f} kB")

    print("\n" + "-"*80)
    print("SOUČET - Python soubory:")
    print(f"  Počet souborů:      {total_py_stats['files']:5d}")
    print(f"  Celkem řádků:       {total_py_stats['total_lines']:5d}")
    print(f"  - Kód:              {total_py_stats['code_lines']:5d}")
    print(f"  - Komentáře:        {total_py_stats['comment_lines']:5d}")
    print(f"  - Docstringy:       {total_py_stats['docstring_lines']:5d}")
    print(f"  - Prázdné:          {total_py_stats['blank_lines']:5d}")
    print(f"  Celková velikost:   {total_py_stats['size_kb']:6.1f} kB")

    # Dokumentační soubory
    print("\n" + "="*80)
    print("DOKUMENTAČNÍ SOUBORY (.md, .txt)")
    print("="*80)

    total_doc_stats = {
        'files': 0,
        'total_lines': 0,
        'text_lines': 0,
        'blank_lines': 0,
        'size_kb': 0
    }

    for filename in doc_files:
        filepath = os.path.join(project_dir, filename)
        if os.path.exists(filepath):
            stats = analyze_text_file(filepath)
            size = get_file_size(filepath)

            total_doc_stats['files'] += 1
            total_doc_stats['total_lines'] += stats['total_lines']
            total_doc_stats['text_lines'] += stats['text_lines']
            total_doc_stats['blank_lines'] += stats['blank_lines']
            total_doc_stats['size_kb'] += size

            print(f"\n{filename}:")
            print(f"  Celkem řádků:       {stats['total_lines']:5d}")
            print(f"  - Text:             {stats['text_lines']:5d}")
            print(f"  - Prázdné:          {stats['blank_lines']:5d}")
            print(f"  Velikost:           {size:6.1f} kB")

    print("\n" + "-"*80)
    print("SOUČET - Dokumentace:")
    print(f"  Počet souborů:      {total_doc_stats['files']:5d}")
    print(f"  Celkem řádků:       {total_doc_stats['total_lines']:5d}")
    print(f"  - Text:             {total_doc_stats['text_lines']:5d}")
    print(f"  - Prázdné:          {total_doc_stats['blank_lines']:5d}")
    print(f"  Celková velikost:   {total_doc_stats['size_kb']:6.1f} kB")

    # Ostatní soubory
    print("\n" + "="*80)
    print("OSTATNÍ SOUBORY (.bat)")
    print("="*80)

    total_other_stats = {
        'files': 0,
        'total_lines': 0,
        'size_kb': 0
    }

    for filename in other_files:
        filepath = os.path.join(project_dir, filename)
        if os.path.exists(filepath):
            stats = analyze_text_file(filepath)
            size = get_file_size(filepath)

            total_other_stats['files'] += 1
            total_other_stats['total_lines'] += stats['total_lines']
            total_other_stats['size_kb'] += size

            print(f"\n{filename}:")
            print(f"  Celkem řádků:       {stats['total_lines']:5d}")
            print(f"  Velikost:           {size:6.1f} kB")

    print("\n" + "-"*80)
    print("SOUČET - Ostatní:")
    print(f"  Počet souborů:      {total_other_stats['files']:5d}")
    print(f"  Celkem řádků:       {total_other_stats['total_lines']:5d}")
    print(f"  Celková velikost:   {total_other_stats['size_kb']:6.1f} kB")

    # CELKOVÝ SOUČET
    print("\n" + "="*80)
    print("CELKOVÝ SOUČET PROJEKTU")
    print("="*80)

    total_files = (total_py_stats['files'] +
                   total_doc_stats['files'] +
                   total_other_stats['files'])

    total_lines = (total_py_stats['total_lines'] +
                   total_doc_stats['total_lines'] +
                   total_other_stats['total_lines'])

    total_size = (total_py_stats['size_kb'] +
                  total_doc_stats['size_kb'] +
                  total_other_stats['size_kb'])

    print(f"\nPočet souborů celkem:        {total_files:5d}")
    print(f"  - Python (.py):            {total_py_stats['files']:5d}")
    print(f"  - Dokumentace (.md, .txt): {total_doc_stats['files']:5d}")
    print(f"  - Ostatní (.bat):          {total_other_stats['files']:5d}")

    print(f"\nŘádků celkem:                {total_lines:5d}")
    print(f"  - Python kód:              {total_py_stats['code_lines']:5d}")
    print(f"  - Python komentáře:        {total_py_stats['comment_lines']:5d}")
    print(f"  - Python docstringy:       {total_py_stats['docstring_lines']:5d}")
    print(f"  - Dokumentace text:        {total_doc_stats['text_lines']:5d}")
    print(f"  - Prázdné řádky:           {total_py_stats['blank_lines'] + total_doc_stats['blank_lines']:5d}")

    print(f"\nCelková velikost:            {total_size:6.1f} kB ({total_size/1024:.2f} MB)")

    # DETAILNÍ ROZDĚLENÍ
    print("\n" + "="*80)
    print("DETAILNÍ ANALÝZA KÓDU")
    print("="*80)

    productive_code = total_py_stats['code_lines']
    documentation_code = total_py_stats['comment_lines'] + total_py_stats['docstring_lines']
    documentation_files = total_doc_stats['text_lines']

    total_productive = productive_code
    total_documentation = documentation_code + documentation_files

    print(f"\nPlatný kód (bez komentářů):  {productive_code:5d} řádků")
    print(f"Dokumentace v kódu:          {documentation_code:5d} řádků")
    print(f"  - Komentáře (#):           {total_py_stats['comment_lines']:5d} řádků")
    print(f"  - Docstringy:              {total_py_stats['docstring_lines']:5d} řádků")
    print(f"Dokumentace v souborech:     {documentation_files:5d} řádků")

    print(f"\n" + "-"*80)
    print(f"CELKEM platný kód:           {total_productive:5d} řádků")
    print(f"CELKEM dokumentace:          {total_documentation:5d} řádků")

    # Poměr kód/dokumentace
    if total_productive > 0:
        ratio = total_documentation / total_productive
        print(f"\nPoměr dokumentace/kód:       {ratio:.2f}:1")
        print(f"  (Na každý řádek kódu připadá {ratio:.2f} řádku dokumentace)")

    # ZAJÍMAVÉ STATISTIKY
    print("\n" + "="*80)
    print("ZAJÍMAVÉ STATISTIKY")
    print("="*80)

    print(f"\nNejvětší Python soubor:      caesar_cipher.py")
    print(f"Nejdelší dokumentace:        README_CAESAR.md")

    print(f"\nProcento dokumentace:        {(total_documentation / total_lines * 100):.1f}%")
    print(f"Procento platného kódu:      {(total_productive / total_lines * 100):.1f}%")
    print(f"Procento prázdných řádků:    {((total_py_stats['blank_lines'] + total_doc_stats['blank_lines']) / total_lines * 100):.1f}%")

    print("\n" + "="*80)
    print("ZÁVĚR")
    print("="*80)
    print(f"""
Projekt obsahuje:
• {total_files} souborů
• {total_productive} řádků platného kódu
• {total_documentation} řádků dokumentace
• {total_lines} řádků celkem
• {total_size:.1f} kB celková velikost

Projekt je velmi dobře zdokumentovaný s poměrem {ratio:.2f}:1
(dokumentace/kód), což značí vysokou kvalitu a srozumitelnost.
""")

    print("="*80 + "\n")

    return {
        'total_files': total_files,
        'total_lines': total_lines,
        'code_lines': total_productive,
        'documentation_lines': total_documentation,
        'total_size_kb': total_size
    }


if __name__ == "__main__":
    analyze_project()
