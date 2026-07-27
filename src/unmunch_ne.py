from pathlib import Path
import re
from spylls.hunspell import Dictionary

def unmunch(word, aff):
    """Generates all suffixed forms for one base word given its flags."""
    result = set()

    if aff.FORBIDDENWORD and aff.FORBIDDENWORD in word.flags:
        return result
    if not (aff.NEEDAFFIX and aff.NEEDAFFIX in word.flags):
        result.add(word.stem)

    suffixes = [s for flag in word.flags for s in aff.SFX.get(flag, [])
                if s.cond_regexp.search(word.stem)]
    prefixes = [p for flag in word.flags for p in aff.PFX.get(flag, [])
                if p.cond_regexp.search(word.stem)]

    for suffix in suffixes:
        root = word.stem[:-len(suffix.strip)] if suffix.strip else word.stem
        suffixed = root + suffix.add
        if not (aff.NEEDAFFIX and aff.NEEDAFFIX in suffix.flags):
            result.add(suffixed)
        for flag in suffix.flags:
            for suffix2 in aff.SFX.get(flag, []):
                if suffix2.cond_regexp.search(suffixed):
                    root2 = suffixed[:-len(suffix2.strip)] if suffix2.strip else suffixed
                    result.add(root2 + suffix2.add)

    for prefix in prefixes:
        root = word.stem[len(prefix.strip):]
        prefixed = prefix.add + root
        if not (aff.NEEDAFFIX and aff.NEEDAFFIX in prefix.flags):
            result.add(prefixed)

    return result


def main():
    print("Loading Hunspell dictionary rules...")
    dictionary = Dictionary.from_files('ne_NP')

    devanagari_pattern = re.compile(r"^[\u0900-\u097F]+$")
    valid_words = set()

    print("Expanding valid root words and their specified affixes...")
    for word in dictionary.dic.words:
        for form in unmunch(word, dictionary.aff):
            clean_word = form.strip()
            if clean_word and devanagari_pattern.fullmatch(clean_word):
                valid_words.add(clean_word)

    sorted_words = sorted(valid_words)
    Path("wnepali").write_text("\n".join(sorted_words) + "\n", encoding="utf-8")
    print(f"Success! Generated {len(sorted_words)} clean, controlled words.")

if __name__ == "__main__":
    main()