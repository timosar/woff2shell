# woff2shell

Small proof-of-concept for crafting and parsing a malicious WOFF2 file using a vulnerable Brotli decoder.

This repository contains two scripts:

- `create.py` generates a `test.woff2` file with a crafted Brotli payload.
- `parse.py` reads that file, parses the WOFF2 header, and decompresses the embedded stream using `brotli.decompress()`.

## Requirements

- Python 3
- `brotli` package

Install:

```bash
pip install brotli
```

## Usage

```bash
python create.py
python parse.py
```

This will create `test.woff2` and print the decompressed content from the embedded Brotli stream.

## Notes

This is a minimal educational PoC and is meant for research/analysis of WOFF2/Brotli parsing behavior.
