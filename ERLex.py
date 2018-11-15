import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN
import Entity as ent
import ERDrawer as drawer
from graphviz import Source
import sys

if sys.version_info[0] >= 3:
    raw_input = input

cardinality = (
    'many',
    'one',
    'a',
)

modality = (
    'must',
    'can',
    'maynot',
)

composition = (
    'composed',
    'composedof'
)
tokens = (
    'CHARACTER',
    'DIGIT',
    'DELIMITER',
    'CARDINALITY',
    'MODALITY',
    'COMPOSITION',
    'ID'
)
t_CHARACTER = r'[a-zA-Z]'
t_DIGIT = r'[0-9]'
t_DELIMITER = r',|;'
identifier = r'(composed\sof)|(may\snot) | (' + t_CHARACTER + r'(' + t_DIGIT + r'|' + t_CHARACTER + r')*)'


@TOKEN(identifier)
def t_ID(t):
    if t.value in cardinality:
        t.type = 'CARDINALITY'
    elif t.value in modality:
        t.type = 'MODALITY'
    elif t.value in composition:
        t.type = 'COMPOSITION'
    elif t.value == 'may not':
        t.type = 'MODALITY'
    elif t.value == 'composed of':
        t.type = 'COMPOSITION'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t'

lex.lex()


# data = ' many hell0 , composed of may not w0rld'

# Give the lexer some input
# lexer.input(data)

# Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)


# import token map from lexer
d_instance = ent.Diagram()
def p_expression(p):
    """expression : definition
       | assignment"""

    if p[1]:
        p[0] = p[1]
    elif p[2]:
        p[0] = p[2]


def p_definition_modality(p):
    """definition : CARDINALITY entity MODALITY relation CARDINALITY entity"""
    p[0] = ('definition with Cardinality', p[1], p[2], p[3], p[4], p[5], p[6])
    # print(p[0])
    d_instance._add_relationship(p[2], p[6], p[4], p[1], p[5],p[3])



def p_definition(p):
    """definition : CARDINALITY entity relation CARDINALITY entity"""
    p[0] = ('definition without cardinality', p[1], p[2], p[3], p[4], p[5])
    d_instance._add_relationship(p[2], p[5], p[3], p[1], p[4], 'can')



def p_assignment(p):
    """assignment : entity COMPOSITION attributelist"""
    p[0] = ('assignment', p[1], p[2], p[3])
    entity = d_instance._get_entity(p[1])
    if entity is not None:
        entity.add_attribute(p[3])
    else:
        new_entity = d_instance._add_entity(p[1])
        new_entity.add_attribute(p[3])


def p_entity(p):
    """entity : ID"""
    p[0] = p[1]


def p_relation(p):
    """relation : ID"""
    p[0] = p[1]


def p_attributelist(p):
    """attributelist : attributelist DELIMITER ID
   | ID """

    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]


def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

# while True:
#     try:
s = 'elephants composed of apples, pears, butterfly, dung, magic'
s2 = 'children composed of diapers, tears, hellfire, hopes, dreams'
s1 = 'one elephants can have one children'
s3 = 'many manatees can alsohave many children'
s4 = 'a sheep must regret one children'
s5 = 'sheep composed of darkmatter, solace, evil, satan'
# except EOFError:
#     print("EOF")
#     break
# if not s:
#     print(s)
#     break  pears, butterfly, dung, magic
print(s1)
result = parser.parse(s1)
print(result)
print('\n' + s)
result = parser.parse(s)
print(result)
result = parser.parse(s2)
print(result)
result = parser.parse(s3)
print(result)
result = parser.parse(s4)
print(result)
result = parser.parse(s5)
print(result)

erScript = drawer.heading
relations = []
for e in d_instance:
    erScript += e.get_name() + drawer.entityLabel + e.get_name() + drawer.endRow
    for a in e.get_attributes():
        erScript += drawer.startAttribute + a + drawer.endRow
    erScript += drawer.entityEnd

    for r in e:
        if r[0] not in relations:
            print('in relations')
            print(r[0])
            relations.append(r[0])
            erScript += r[0] + drawer.relationBox
        erScript += e.get_name() + ' -> ' + r[0] + drawer.arrowtailB+drawer.getCardinality(r[1]['cardinality'])+ drawer.getModality(r[1]['modality']) + drawer.arrowtailE
        print(e.get_name(), '\t\n', e.get_attributes(), '\t\n', r[0], '\t\n', r[1]['cardinality'], '\t\n', r[1]['modality'], '\t\n', r[1]['entity'])

erScript += drawer.end
print(erScript)
src = Source(erScript)
src.render('test-output/holy-grenade.gv', view=True)
