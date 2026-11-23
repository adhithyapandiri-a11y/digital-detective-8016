# Mission 5 - Numbers and data

## 1. Task / objective

Convert numbers by hand, check them in Python, write a converter and look at how text is stored.

## 2. Work completed

| Conversion | Working and answer | Python check |
| --- | --- | --- |
| 13 to binary | `8 + 4 + 0 + 1 = 13`, so `1101`. | `bin(13)` gave `0b1101`. |
| 25 to binary | `16 + 8 + 0 + 0 + 1 = 25`, so `11001`. | `bin(25)` gave `0b11001`. |
| Binary 1010 to decimal | `1×8 + 0×4 + 1×2 + 0×1 = 10`. | `int("1010", 2)` gave `10`. |
| Binary 1101 to decimal | `1×8 + 1×4 + 0×2 + 1×1 = 13`. | `int("1101", 2)` gave `13`. |
| Hex A to decimal | A is 10, so `10×1 = 10`. | `int("A", 16)` gave `10`. |
| Hex 1F to decimal | F is 15, so `1×16 + 15×1 = 31`. | `int("1F", 16)` gave `31`. |
| Binary 1111 to hex | `8 + 4 + 2 + 1 = 15`, which is F in hex. | `hex(int("1111", 2))` and `hex(15)` both gave `0xf`. |

All the Python results matched my answers.

| Converter input | Binary | Hex |
| --- | --- | --- |
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 31 | `0b11111` | `0x1f` |

ASCII uses 65 for `A` and 97 for `a`. An encoding tells programs which bytes stand for which characters. UTF-8 can store characters like `é`, which is outside basic ASCII.

## 3. Commands / tools used

I checked the answers in `python3` and used `ord()` for the letter codes. I ran the script with `python3 number_converter.py`. It uses `input()` to read the number, `int()` to make it an integer, and `bin()` and `hex()` to show it in binary and hex.

## 4. My understanding

A number has the same value in every base. 31 in decimal is 11111 in binary and 1F in hex.

## 5. Difficulties faced

Python's answers had prefixes and used lowercase letters for hex.

## 6. How I resolved them

I checked that `0b` means binary and `0x` means hex. Lowercase `f` and uppercase `F` both mean 15.

## 7. Evidence / files

[Number converter](number_converter.py). The working and test results are above.

## 8. Commit details

Local. Commit and push pending.
