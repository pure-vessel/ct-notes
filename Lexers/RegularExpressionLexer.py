from pygments.lexer import RegexLexer, bygroups
from pygments.token import *
                
__all__ = ['RegularExpressionLexer']
                
class RegularExpressionLexer(RegexLexer):
    name = 'RegularExpression'
    aliases = ['RegularExpressionLexer']
    filenames = []
                
    tokens = {
        'root': [
            (r'\w+', Name),
            (r'\d+', Number),
            (r'[\s,:\-"\']+', Text),
            (r'[\$\^]', Token),
            (r'[\+\*\.\?]', Operator),
            (r'(\()([\?\<\>\!\=\:]{2,3}.+?)(\))', bygroups(Keyword.Namespace, Name.Function, Keyword.Namespace)),
            (r'(\()(\?\#.+?)(\))', bygroups(Comment, Comment, Comment)),
            (r'[\(\)]', Keyword.Namespace),
            (r'[\[\]]', Name.Class),
            (r'\\\w', Keyword),
            (r'[\{\}]', Operator),
        ],
    }