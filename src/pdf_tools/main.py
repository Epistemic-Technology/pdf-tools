import json
import sys
from typing import Optional

from jsonrpcserver import Success, dispatch, method
from pydantic import BaseModel


class Source(BaseModel):
    path: Optional[str] = None
    url: Optional[str] = None
    bytes_b64: Optional[str] = None


class Ops(BaseModel):
    ocr: bool = False
    tables: bool = False
    images: bool = False
    lang_hint: Optional[str] = None


class PageRange(BaseModel):
    start: Optional[int] = None
    end: Optional[int] = None


@method
def process_pdf(source: Source, ops: Ops, page_range: PageRange):
    print(f"Processing PDF with source={source}, ops={ops}, page_range={page_range}")
    return Success(json.dumps({"status": "success"}))


def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        response = dispatch(line)
        sys.stdout.write(json.dumps(response))


if __name__ == "__main__":
    main()
