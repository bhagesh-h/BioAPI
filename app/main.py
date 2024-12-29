import re
from typing import Annotated
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.get('/')
async def root():
    return {'API WORKS':110}

@app.post("/read/")
async def create_upload_file(file: UploadFile):
    with file.file as f: contents = f.read()
    return {"filename": file.filename, "contents": contents, "file_size": len(contents)}

@app.get('/cleanfasta/{fasta}')
async def clean_fasta(fasta:str):
    fasta_raw = {}
    for value in fasta.split('|'):
        if value.startswith('>'):
            key = ''
            key = value.lstrip('>')
        else:
            if key not in fasta_raw:
                fasta_raw[key] = ''
            fasta_raw[key] += ''.join(char for char in value if char.isalnum())
    filtered_fasta_dict =  dict(list(fasta_raw.items()))
    output_list_fasta = []
    for key,val in filtered_fasta_dict.items():
        output_list_fasta.append(key)
        output_list_fasta.append(val)
    return '\n'.join(output_list_fasta)

@app.get('/upper/{fasta}')
async def convert_to_upper(fasta:str):
    """
    """
    fasta_raw = {}
    for value in fasta.split('|'):
        if value.startswith('>'):
            key = ''
            key = value.lstrip('>')
        else:
            fasta_raw[key] = value.upper()
    output_list_fasta = []
    for key,val in fasta_raw.items():
        output_list_fasta.append(key)
        output_list_fasta.append(val)
    return '\n'.join(output_list_fasta)

@app.get('/nfasta/{n}/{fasta}')
async def get_n_fasta_from_fasta(n:int,fasta:str):
    """
    Function To Get n Number of Fasta from Multi Fasta File.
    Usage:
        make api call using request/wget using the following command:
            http://localhost/nfasta/n/$(cat file.fasta| tr '\n' '|')
        Example URL:
            http://localhost/nfasta/1/>seq1|CATGCGGcccTTccc|C>seq2|CATGCtcggcgstcstc
    """
    fasta_raw = {}
    for value in fasta.split('|'):
        if value.startswith('>'):
            key = ''
            key = value.lstrip('>')
        else:
            fasta_raw[key] = value
    filtered_fasta_dict =  dict(list(fasta_raw.items())[:n])
    output_list_fasta = []
    for key,val in filtered_fasta_dict.items():
        output_list_fasta.append(key)
        output_list_fasta.append(val)
    return '\n'.join(output_list_fasta)

@app.get('/revcomp/{fasta}')
async def convert_to_upper(fasta:str):
    """
    """
    reverse_complement = lambda d: ''.join(iupac.get(base, base)[::-1] for base in d)
    iupac = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'R': 'Y', 'Y': 'R', 'S': 'S', 'W': 'W', 'K': 'M', 'M': 'K', 'B': 'V', 'D': 'H', 'V': 'B', 'H': 'D', 'N': 'N', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a', 'r': 'y', 'y': 'r', 's': 's', 'w': 'w', 'k': 'm', 'm': 'k', 'b': 'v', 'd': 'h', 'v': 'b', 'h': 'd', 'n': 'n'}
    fasta_raw = {}
    for value in fasta.split('|'):
        if value.startswith('>'):
            key = ''
            key = value.lstrip('>') + '_revcomp'
        else:
            fasta_raw[key] = reverse_complement(value)
    output_list_fasta = []
    for key,val in fasta_raw.items():
        output_list_fasta.append(key)
        output_list_fasta.append(val)
    return '\n'.join(output_list_fasta)

@app.get('/shortheader/{n}/{fasta}')
async def shorten_fasta_header(n:int,fasta:str):
    fasta_raw = {}
    for value in fasta.split('|'):
        if value.startswith('>'):
            key = ''
            key = value.lstrip('>')[:n]
        else:
            fasta_raw[key] = value
    filtered_fasta_dict =  dict(list(fasta_raw.items()))
    output_list_fasta = []
    for key,val in filtered_fasta_dict.items():
        output_list_fasta.append(key)
        output_list_fasta.append(val)
    return '\n'.join(output_list_fasta)


