from pygments.lexer import RegexLexer
import pygments.token as tok

class PseudoLexer(RegexLexer):
    name = 'Pseudocode'
    aliases = ['pseudo']
    filenames = []

    tokens = {
        'root' : [
            (r'\b(for|while|if|else|in|return|break|null)\b', tok.Keyword),
            (r'[-\[\]\(\)\.\+,=\{\}<>;:&|/!@%^\*]+', tok.Operator),
            (r'\b(?:[1-9][0-9]*|(?<![0-9])0(?![0-9]))\b', tok.Number),
            (r'\b(min|infinity|inf|swap|len|bool)\b', tok.Name.Builtin),
            (r'[ \t\v\r\n\f]', tok.Whitespace),
            (r'\b[A-Za-z_][A-Za-z_0-9]*\b', tok.Name),
            (r'#.*', tok.Comment),
        ]
    }