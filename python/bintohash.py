"""
第一引数にファイルパス、第二引数に生成するファイル名を指定します。
ルート直下にファイルが生成され、第一引数に指定されたファイルのハッシュが書き込まれます
"""

import hashlib
import os
import sys

# fpに指定したファイルのハッシュを、
# ルートディレクトリに上のnameという名前のファイルに書き込む
def bintohash(fp: str, name: str) -> None:
	with open(fp, mode="rb") as sf:
		sf_hash = hashlib.sha256(sf.read()).digest()
	with open(name, "wb") as df:
		df.write(sf_hash)

def __main__():
    bintohash(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    __main__()
