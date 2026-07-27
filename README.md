# wnepali: Nepali System Wordlist

A flat, sorted Nepali wordlist for Linux distributions and localized
utilities.

## Description

This wordlist (~601,000 entries) is generated from the Nepali Hunspell
dictionary (root words + affix rules) originally compiled by Madan
Puraskar Pustakalaya, expanded via automated affix unmunching, and
substantially extended with additional proper nouns and vocabulary
compiled by the packager.

## Build Process

1. `unmunch_ne.py` — expands `ne_NP.dic` / `ne_NP.aff` root words and
   affix rules into full surface-form words.
2. `process_names.py` — merges the unmunched output with `names.txt`
   (proper nouns and additional vocabulary), applies suffix expansion
   to the added entries, deduplicates, and sorts the result.
3. Output: `wnepali`, the final sorted wordlist.

## Attribution

### Original Hunspell Dictionary Data
Nepali SpellChecking Dictionary, Release 1.1 (2006-10-17)
Compiled by Madan Puraskar Pustakalaya, Lalitpur, Nepal

Contributors: Amar Gurung, Bal Krishna Bal, Basanta Karki,
Basanta Shrestha, Ishwor Sharma, Laxmi Prasad Khatiwada,
Paras Pradhan, Prajol Shrestha, Subir Pradhanang

Supported by the National University of Computer and Emerging
Sciences (NUCES), Pakistan, and the Pan Asia Networking (PAN)
program of the International Development Research Center (IDRC),
Canada.

### Wordlist Compilation, Names Data, and Tooling
Compiled and maintained by Sparsha Bhusal / www.github.com/bhusalsparsha

## License

Licensed under the GNU Lesser General Public License v2.1 (LGPL-2.1).
See `LICENSE` for the full text.