from src.util.color import Color

biru = Color.CBLUE2
ungu = Color.CPURPLE2
hijau = Color.CGREEN2
merah = Color.CRED2
hapus = Color.ENDC

def nomor(no):
    return f"[{ biru }{ no }{ hapus }]"

def title(sentence):
    return f"{ biru }{ sentence }{ hapus }"

def success(sentence):
    return f"{hijau}?{hapus} {sentence}"

def failed(sentence):
    return f"{ merah }?{ hapus } {sentence}"

def info(sentence):
    return f"{ungu}?{hapus} {sentence} "

def input_string(sentence):
    return f"{ungu}?{hapus} {sentence} > "