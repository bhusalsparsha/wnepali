import re
from pathlib import Path

def process_custom_names():
    names_file = Path("names.txt")
    if not names_file.exists():
        raise FileNotFoundError(f"Could not find {names_file}.")

    devanagari_pattern = re.compile(r"^[\u0900-\u097F]+$")
    
    print("1. Reading and tokenizing names.txt...")
    extracted_names = set()
    for line in names_file.read_text(encoding="utf-8").splitlines():

        tokens = line.strip().split()
        for token in tokens:
            clean_token = token.strip()
            if clean_token and devanagari_pattern.fullmatch(clean_token):
                extracted_names.add(clean_token)

    print(f"Found {len(extracted_names)} unique base name tokens.")

    print("2. Applying suffix expansions...") #Reference taken from SFX 15 in ne_NP.aff file
    sfx_15 = [
        "को",
        "की",
        "का",
        "मा", 
        "बाट", 
        "लाई"
    ]

    expanded_words = set(extracted_names)

    for name in extracted_names:
        expanded_words.add(name)
        for add_val in sfx_15:
            new_word = name + add_val
            if devanagari_pattern.fullmatch(new_word):
                expanded_words.add(new_word)

    print(f"Total words after applying suffixes: {len(expanded_words)}")

    print("3. Merging with existing 'wnepali' wordlist (if present)...")
    mpp_path = Path("wnepali")
    if mpp_path.exists():
        for line in mpp_path.read_text(encoding="utf-8").splitlines():
            w = line.strip()
            if w and devanagari_pattern.fullmatch(w):
                expanded_words.add(w)

    print("4. Sorting alphabetically and writing final output...")
    sorted_words = sorted(list(expanded_words))
    
    output_path = Path("wnepali_final")
    output_path.write_text("\n".join(sorted_words) + "\n", encoding="utf-8")

    print(f"Success! Final unified file 'wnepali_final' created with {len(sorted_words)} unique words.")

if __name__ == "__main__":
    process_custom_names()