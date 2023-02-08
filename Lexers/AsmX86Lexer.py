from pygments.lexer import RegexLexer
import pygments.token as tok

class AsmX86Lexer(RegexLexer):
    name = 'AsmX86'
    aliases = ['asm']
    filenames = []

    tokens = {
        'root' : [
            (r'\b(MOV|ADD|SUB|AND|OR|XOR|INC|DEC|NEG|NOT|LEA|(J|CMOV)(N?[EGLABZOSC])|CMP|JMP|CWD|CQO|S[HA][LR]|I?MUL|I?DIV|PUSH|POP|CALL|RET|HLT)\b', tok.Keyword),
            (r'[-\[\]\(\)\.\+,=\{\}<>:&|/!@%^\*]+', tok.Operator),
            (r'\b(?:[1-9][0-9]*|(?<![0-9])0(?![0-9]))\b', tok.Number),
            (r'\b([ER][A-D]X|[A-D][HLX]|[ER]?([SB]P|[SD]I)|R([89]|1[0-5])[DWB]?|byte|word|dword|qword|XMM([0-9]|1[0-5]))\b', tok.Name.Builtin),
            (r'[ \t\v\r\n\f]', tok.Whitespace),
            (r'\b[A-Za-z_][A-Za-z_0-9]*\b', tok.Name),
            (r';.*', tok.Comment),
        ]
    }