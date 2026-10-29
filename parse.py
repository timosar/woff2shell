# takes the crafted brotli-encoded woff2 file, parses it and decodes the stream using the vulnerable brotli version (v1.2.0)
import struct
import brotli

HEADER_FMT = ">II I H H I I H H I I I I I"
HEADER_SIZE = 48

with open("test.woff2", "rb") as f:
    data = f.read()

header = struct.unpack(
    HEADER_FMT,
    data[:HEADER_SIZE]
)

(
    signature,
    flavor,
    length,
    num_tables,
    reserved,
    total_sfnt_size,
    total_compressed_size,
    major_version,
    minor_version,
    meta_offset,
    meta_length,
    meta_orig_length,
    priv_offset,
    priv_length,
) = header

print(f"signature = {signature:#x}")
print(f"flavor = {flavor:#x}")
print(f"length = {length}")
print(f"compressed_size = {total_compressed_size}")

compressed = data[HEADER_SIZE:]

print(f"actual compressed bytes = {len(compressed)}")

decompressed = brotli.decompress(compressed)

print("decompressed length =", len(decompressed))
print("contents =", decompressed)
