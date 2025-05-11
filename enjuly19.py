



import sys
import ast
import random
import zlib
import marshal
import base64
import bz2
import re
from pystyle import *
if sys.version_info < (3, 10):
    print("Install Python Version = 3.10 or > 3.10 To Use This Code ")
    sys.exit()

def _rd():
    return "".join(__import__("random").sample(
        [chr(i) for i in range(97, 122)], k=5))


def _rd1():
    return "".join(__import__("random").sample(
        [chr(i) for i in range(97, 122)], k=1))


def rd():
    return "_" + "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))


def randomint():
    return "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))


def _chrobf(x):
    return ord(x) + 0xFF78FF

def obfstr(v):
    global _join
    global _hexrun
    global obfint
    if v == "":
        return f"''"
    else:
        x = []
        r = list(v)
        for i in range(len(r)):
            x.append(_chrobf(r[i]))
        _str_ = f"(lambda  : (lambda : (lambda : {_join}(( {_list}({_map}({_hexrun}, {x})) )))())())()"
        return _str_

import random
"""
def obfstr(string):
    keys = []
    magic = random.randint(1000000, 9999999)
    
    for char in string:
        logic = random.randint(1, 4)
        if logic == 1:
            logic = '+'
        elif logic == 2:
            logic = '*'
        elif logic == 3:
            logic = '<<'
        else:
            logic = '^'
        
        key = ord(char)
        key2 = magic
        
        if logic == "^":
            key3 = ~key ^ ~magic
            keys.append(f"(lambda: chr({key2} ^ {key3}))()")
        elif logic == "<<":
            magic = random.randint(1, 19)
            key3 = key << magic
            PT = ">>"
            keys.append(f"(lambda: chr({key3} {PT} {magic}))()")
        else:
            if logic == "+":
                PT = "-"
            else:
                PT = "//"
            key3 = eval(f"{key} {logic} {magic}")
            keys.append(f"(lambda: chr({key3} {PT} {key2}))()")
    
    return f"(lambda: ''.join([{', '.join(keys)}]))()"

""" # USE IT IF U WANT POWER STRING
def _byte(v):
    byte_array = bytearray()
    byte_array.extend(v.to_bytes((v.bit_length() + 7) // 8, 'big'))
    return b"enjuly19/" + byte_array

def obfint(v):
    n = rd()
    if 'bool' in str(type(v)):
        if str(v)=='True':
            return f'(lambda: (lambda {n}: {n} + (lambda : H2SbF7({(1+0x7777)}))())(0) == 1)()'
        else:
            return f'(lambda: (lambda {n}: {n} - (lambda : H2SbF7(({(1+0x7777)} ) ) )())(0) == 1)()'
    else:
        #return f"""H2SbF7({(v+0x7777)}) if {_str}({_type}({_bool}(H2SbF7({(v+0x7777)})))) == {_str}({_type}({_int}({randomint()})>{_int}({randomint()})<{_int}({randomint()})>{_int}({randomint()}))) else H2SbF7({v+0x7777})"""
        #return f"""(lambda {rd()} : H2SbF7({(v+0x7777)})("datchuche")"""
        #return f"""(lambda : H2SbF7({(v+0x7777)})//eval({obfstr('1')}))()"""
        #print(fr""" unhexlify('{_byte(int(v))}') """)
        #return fr"""(lambda : """
        return f'(lambda: c2h6({_byte(int(v))}))()'


def varsobf(v):
    return f"""({(v)}) if bool(bool(bool({(v)}))) < bool(type(int({randomint()})>int({randomint()})<int({randomint()})>int({randomint()}))) and bool(str(str({randomint()})>int({randomint()})<int({randomint()})>int({randomint()}))) > 2 else {v}"""


_join = "h2o"
_lambda = "ᅠ"
_int = "h2so4"
_str = "co2"
_bool = "mol"
_type = "feo2"
_bytes = "feso4"
_vars = "agno3"
_ip = "hno3"
ngoac = "{"
_ngoac = "}"
___import__ = "ch2oh4p2so4"
_movdiv = "h2"
_hexrun = "o2"
_argshexrun = "h2so3"
__print = r"tryᅠ"
__input = r"exceptᅠ"
_eval = "h2o3"
_list = "agno4"
_map = "h3o"
def unicodeobf(x):
    b = []
    for i in x:
        j = ord(i) + 0xFF78FF
        b.append(j)
    return b


def _uni(x):
    return unicodeobf(x)


__bool = rd()
__exx = rd()
_temp = rd()
_temp1 = rd()
_wt = rd()
_exp = rd()

var = fr"""

globals()['{_bool}'] = {varsobf('bool')}
globals()['{_str}'] =  {varsobf('str')}
globals()['{_type}'] =  {varsobf('type')}
globals()['{_int}'] =  {varsobf('int')}
globals()['{_bytes}'] =  {varsobf('bytes')}
globals()['{_vars}'] =  {varsobf('vars')}
globals()['{_movdiv}'] =  {varsobf('callable')}
globals()['{_eval}'] =  {varsobf('eval')}
globals()['{_list}'] =  {varsobf('list')}
globals()['{_map}'] =  {varsobf('map')}

globals()['{___import__}'] =  {varsobf('__import__')}

globals()['tryᅠ'] =  {varsobf('print')}
globals()['exceptᅠ'] =  {varsobf('input')}
def {_join}(july,*k):
    if k:
        enjuly19 = '+'
        op = "+"
    else:
        enjuly19 = ''
        op = ''
    globals()['{__exx}'] = {obfint(True)}
    globals()['{_join}'] = {_join}
    globals()['{_str}'] = {_str}
    globals()['july'] = july
    for globals()['enjuly19_'] in globals()['july']:
        if not {__exx}:globals()['enjuly19_'] += (lambda : '')()
        enjuly19 += {_str}(enjuly19_);f = {obfint(True)}
    return enjuly19
def H2SbF7(x):
    return {_int}(x-0x7777)
def c2h6(e):
    br = bytearray(e[len(b"enjuly19/"):])
    r = 0
    for b in br:
        r = r * 256 + b
    return r
def longlongint(x):
    ar = []
    for i in x:
        ar.append({_eval}(i))
    return ar
if {obfint(True)}:
    def {_hexrun}({_argshexrun}):
        {_argshexrun} = {_argshexrun}-0xFF78FF
        if {_argshexrun} <= 0x7F:
                    return {_str}({_bytes}([{_argshexrun}]),"utf8")
        elif {_argshexrun} <= 0x7FF:
                    if 1<2:
                            b1 = 0xC0 | ({_argshexrun} >> 6)
                    b2 = 0x80 | ({_argshexrun} & 0x3F)
                    return {_str}({_bytes}([b1, b2]),"utf8")
        elif {_argshexrun} <= 0xFFFF:
                b1 = 0xE0 | ({_argshexrun} >> 12)
                if 2>1:
                    b2 = 0x80 | (({_argshexrun} >> 6) & 0x3F)
                b3 = 0x80 | ({_argshexrun} & 0x3F)
                return {_str}({_bytes}([b1, b2, b3]),"utf8")
        else:
            b1 = 0xF0 | ({_argshexrun} >> 18)
            if 2==2:
                b2 = 0x80 | (({_argshexrun} >> 12) & 0x3F)
            if 1<2<3:
                b3 = 0x80 | (({_argshexrun} >> 6) & 0x3F)
            b4 = 0x80 | ({_argshexrun} & 0x3F)
            return {_str}({_bytes}([b1, b2, b3, b4]),"utf8")
    def _hex(j):
        {_argshexrun} = ''
        for _hex in j:
            {_argshexrun} += ({_hexrun}(_hex))
        return {_argshexrun}
else:"enjuly19"
"""

antipycdc = ''
for i in range(5000):
    antipycdc += f"你器(你器(你器(你器(你器(你器('')))))),"
antipycdc = "try:ngocuyencoder=[" + antipycdc + "]\nexcept:pass"
ANTI_PYCDC = f"""
def 你器(你):
    return 你
try:pass
except:pass
finally:pass
{antipycdc}
finally:int(2008-2006)
"""

import ast
def _moreobf(tree):
    import random

    def rd():
        return str(random.randint(0x1E000000000, 0x7E000000000))

    def junk(en, max_value):
        cases = []
        line = max_value + 1
        for i in range(random.randint(1, 5)):
            case_name = "__"+rd()
            case_body = [
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=line)]
                    ), 
                    body=[
                        ast.Assign(
                            targets=[ast.Name(id=case_name)], 
                            value=ast.Constant(value=random.randint(0xFFFFF, 0xFFFFFFFFFFFF)), 
                            lineno=None
                        )
                    ], 
                    orelse=[]
                )
            ]
            cases.extend(case_body)
            line += 1
        return cases

    def bl(body):
        var = "__"+rd()
        en = "__"+rd()

        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id='MemoryError'), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id='MemoryError'), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        
        for i in body:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        
        tb[1].handlers[0].body.extend(junk(en, len(body) + 1))
        
        node = ast.Assign(
            targets=[ast.Name(id=var)], 
            value=ast.Constant(value=0), 
            lineno=None
        )
        
        return [node] + tb

    def _bl(node):
        olb = node.body

        var = "__"+rd()
        en = "__"+rd()

        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id='MemoryError'), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id='MemoryError'), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        for i in olb:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        tb[1].handlers[0].body.extend(junk(en, len(olb) + 1))
        node.body = [
            ast.Assign(
                targets=[ast.Name(id=var)], 
                value=ast.Constant(value=0), 
                lineno=None
            )
        ] + tb
        return node
    def on(node):
        if isinstance(node, ast.FunctionDef):
            return _bl(node)
        return node
    nb = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            nb.append(on(node))
        elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            nb.extend(bl([node]))
        elif isinstance(node, ast.Expr):
            nb.extend(bl([node]))
        else:
            nb.append(node)
    tree.body = nb
    return tree


def __moreobf(x):
    return ast.unparse(_moreobf(ast.parse(x)))

def fm(node: ast.JoinedStr) -> ast.Call:
    return ast.Call(
        func=ast.Attribute(
            value=ast.Constant(value="{}" * len(node.values)),
            attr="format",
            ctx=ast.Load(),
        ),
        args=[
            value.value if isinstance(value, ast.FormattedValue) else value
            for value in node.values
        ],
        keywords=[],
    )

def _syntax(x):
    def v(node):
        if node.name:
            for statement in node.body:
                ten = ast.Try(
                    body=[ast.parse(f"{_eval}('0/0')"),ast.parse(f"""if "ngocuyen" == "deptrai":{rd()},{rd()},{rd()},{rd()}\nelse:pass""")],
                    handlers=[
                        ast.ExceptHandler(
                            type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()),
                            name=None,
                            body=[z(statement)]
                        )
                    ],
                    orelse=[],
                    finalbody=[]
                )
                node.body[node.body.index(statement)] = ten
            return node
    def z(statement):
        return ast.Try(
            body=[ast.parse(f"{_eval}('0/0')")],
            handlers=[
                ast.ExceptHandler(
                    type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()),
                    name=None,
                    body=[statement]
                )
            ],
            orelse=[ast.Pass()],
            finalbody=[ast.parse("str(100)")]
        )
    tree = ast.parse(x)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            v(node)
    st = ast.unparse(tree)
    return st
def obfuscate(node):
    for i in ast.walk(node):
        if isinstance(i, ast.Global):
            continue
        if isinstance(i, ast.Nonlocal):
            continue
        for f, v in ast.iter_fields(i):
            if isinstance(v, list):
                ar = []
                for j in v:
                    try:
                        if isinstance(j, ast.Constant) and isinstance(j.value, str):
                            ar.append(ast.parse(obfstr(j.value)).body[0].value)
                        elif isinstance(j, ast.Constant) and isinstance(j.value, int):
                            ar.append(ast.parse(obfint(j.value)).body[0].value)
                        elif isinstance(j, ast.JoinedStr):
                            ar.append(fm(j))
                        elif isinstance(j, ast.AST):
                            ar.append(j)
                    except Exception as e:
                        print(f"Error processing node {j}: {e}")
                        ar.append(j)
                setattr(i, f, ar)
            else:
                try:
                    if isinstance(v, ast.Constant) and isinstance(v.value, str):
                        setattr(i, f, ast.parse(obfstr(v.value)).body[0].value)
                    elif isinstance(v, ast.Constant) and isinstance(v.value, int):
                        setattr(i, f, ast.parse(obfint(v.value)).body[0].value)
                    elif isinstance(v, ast.JoinedStr):
                        setattr(i, f, fm(v))
                except Exception as e:
                    print(f"Error processing field {f} with value {v}: {e}")
def rename_function(node, ol, nn):
    for i in ast.walk(node):
        if isinstance(i, ast.FunctionDef) and i.name == ol:
            i.name = nn
        elif isinstance(i, ast.Attribute) and isinstance(i.value, ast.Name) and i.value.id == ol:
            i.value.id = nn
        elif isinstance(i, ast.Call) and isinstance(i.func, ast.Name) and i.func.id == ol:
            i.func.id = nn
        elif isinstance(i, ast.Name) and i.id == ol:
            i.id = nn
    return node

def random_match_case():
    var1 = ast.Constant(value=randomint(), kind=None)
    var2 = ast.Constant(value=randomint(), kind=None)
    return ast.Match(
        subject=ast.Compare(
            left=var1,
            ops=[ast.Eq()],
            comparators=[var2],
        ),
        cases=[
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)),
                body=[
                    ast.Assign(
                        lineno=0,
                        col_offset=0,
                        targets=[],
                        value=[ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(id="MemoryError", ctx=ast.Load()),
                        args=[],
                        keywords=[ast.Str(s=[True])],
                    ),)],
                    )
                ],
            ),
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=False, kind=None)),
                body=[
                    ast.Assign(
                        lineno=0,
                        col_offset=0,
                        targets=[ast.Name(id=rd(), ctx=ast.Store())],
                        value=ast.Constant(value=[[True], [False]], kind=None),
                    ),
                    ast.Expr(
                        lineno=0,
                        col_offset=0,
                        value=ast.Call(
                            func=ast.Name(id=_str, ctx=ast.Load()),
                            args=[ast.Constant(value=[rd()], kind=None)],
                            keywords=[],
                        ),
                    ),
                ],
            ),
        ],
    )


def trycatch(body, loop):
    ar = []
    for x in body:
        j = x
        for _ in range(1): #use 2 if u want rip 
            j = ast.Try(
                body=[random_match_case(),

                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id="MemoryError", ctx=ast.Load()),
                        name=rd(),
                        body=[j],
                    )
                ],
                orelse=[],
                finalbody=[],
            )
            j.body.append(
                ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(id="MemoryError", ctx=ast.Load()),
                        args=[],
                        keywords=[ast.Str(s=[True])],
                    ),
                    cause=None,
                )
            )
        ar.append(j)
    return ar


def obf(code):
    def ps(x):
        return ast.parse(x)
    code = rename_function(ps(code),"print",__print)
    code = rename_function(ps(code),"input",__input)
    tree = ps(code)
    obfuscate(tree)
    tbd = trycatch(tree.body, 1)
    def ast_to_code(node):
        return ast.unparse(node)
    j = ast_to_code(tbd)
    return j


dark = Col.dark_gray
light = Col.light_gray
purple = Colors.StaticMIX((Col.green, Col.yellow))
bpurple = Colors.StaticMIX((Col.pink, Col.blue, Col.blue))

text = f"""
 ENJULY19 OBFUSCATOR
 POWERFULL AST
 STRING USE LAMBDA EXPRESSION
 INT AND BOOL USE TENARY EXPRESSION
 TRY CATCH , MATCH CASE [ADD TRASH VAR AND FUNCTION NOT DEFIND]


 MODE 1 : LOW OBF (FOR ALL FILE) (EZ TO DEOBF)
 MODE 2 : MEDIUM (BEST CHOICE) (FULL STRING,INT,BOOL OBF)
 MODE 3 : HIGH (NOT RECOMMEND) (IT IS MEDIUM MODE BUT X2 SPAM)

 ANTI HOOKING : BLOCK HOOKING
 COMPILER : WITH MARSHAL(ANTI PYC DECOMPILER),ZLIB,BZ2,BASE64
"""

banner = f"""

⠐⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⢀⣀⢀⠀⠀⣀⣀⣀⣀⠀⣀⣀⣀⣀⢀⡀⠀⠀⠀⠀⢀⡈⠢
⠀⠈⠭⣿⠏⠈⢻⣿⡿⠛⠉⠁⠀⠁⠀⠀⠀⠀⠀⢈⣈⣤⣤⣤⣀⡀⠀⠀⠀⠊⡊⠓⡦⡀⠀⠀⠀⠀⠀⠀⡇⠈
⠀⠀⠒⣧⣦⣠⠞⠁⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⠯⠽⠧⠼⠷⢶⠿⢓⣀⣀⣆⡀⣠⣈⠻⣦⡀⣀⣠⡀⠀⡇⠀
⠀⠰⣟⣷⡟⠁⠀⠀⠀⠀⠀⢀⡤⠖⢫⣍⢀⣾⣯⠀⣞⡆⠀⣏⢻⣠⣄⡀⠉⠙⣻⣿⡻⣷⡈⢻⣿⣿⣷⣾⡇⠀
⠀⢠⣶⡟⠁⠀⠀⠀⣀⣴⠚⠉⠀⣠⣿⠞⠋⠻⣿⡀⠀⠀⠀⠈⠙⢻⣟⠳⣆⠀⠙⢯⡛⣿⢻⡇⡟⢩⢟⡟⡇⠀
⠀⢸⣿⠀⠀⠀⡠⣾⣿⢉⡀⢀⡆⡿⢃⣀⠀⠀⠘⣷⣀⢠⡄⠀⠀⠀⣙⠓⣿⣶⡀⠀⠛⠻⣾⣴⣱⣣⢖⣱⡇⠀
⠀⠸⣿⣧⢤⡎⣰⣣⣶⡏⡧⣄⣵⡿⠭⠻⠃⠀⠀⢣⣹⠸⣿⣤⡐⠛⠛⠷⡆⠈⠑⠢⠤⣀⠹⣿⡿⠿⣿⡿⡇⠀
⠀⢈⡿⣻⠉⡇⡿⠟⢉⡇⠱⣿⡁⡇⠀⠀⢀⣀⠀⠸⣧⠰⡇⢈⣙⡧⣄⡰⣤⣀⣠⣶⠒⠉⠀⠈⣧⣀⠀⣿⡇⠀
⠀⠀⣀⠈⠶⣿⠁⠀⠘⠣⢻⠇⣳⣷⣶⣶⣿⡟⠀⠀⠙⢷⣿⠘⣽⣿⣿⣿⣿⣄⠀⢻⠀⠀⠀⠀⡸⡿⠤⣷⡇⠀
⠀⠐⠋⠀⢀⡿⠀⠘⠀⢰⢸⣿⡿⢿⣿⠏⢉⣇⠀⠀⠀⠀⠙⠃⣾⣿⣁⣈⡻⣿⣯⣿⡄⠀⠀⣶⣇⢹⣧⣿⡇⠀
⠀⠀⠄⠀⡹⣧⠄⠀⠀⠸⣿⣿⡁⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠸⢻⠇⠀⠀⠀⡼⣿⣼⣿⣿⡇⠀
⠀⠐⣦⡤⡁⣿⠰⢠⠀⠀⢙⣇⠁⠻⣯⣍⡬⠏⠀⠀⠀⠠⠀⠀⠻⣧⣀⠼⢳⣠⣿⡄⢀⣠⡞⣴⣿⣿⠋⢨⡇⠀
⠀⠀⠿⠂⠄⡟⣇⢸⡄⠀⠘⠛⣷⢴⣺⣿⡍⠀⠀⠀⠀⠀⠀⠀⠀⢠⠠⣵⣾⢟⣃⡠⢾⡏⣼⠏⢸⡟⠛⣿⡇⠀
⠀⠐⣒⣀⣀⡟⠛⠾⢧⠀⠀⠀⢽⡙⠉⠐⠁⠀⠀⠀⢀⣴⣄⠀⠀⠀⠃⠛⣿⣹⠋⢀⣾⡼⠁⠀⢸⣿⣥⡿⡇⠀
⠀⠈⠛⣿⢟⢣⠀⠀⠨⣧⡀⠀⠏⣧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣼⣿⠀⢸⣿⠀⠀⠀⢸⡏⠀⣷⡇⠀
⠀⠠⡖⠀⠀⢸⠀⠀⢠⣿⣧⠀⠀⠸⣿⣟⡷⣶⣦⣤⠤⢤⣤⣤⣶⣶⢿⡟⢽⣏⠀⢸⣿⠀⠀⠀⠀⣷⠯⢿⡇⠀
⠀⢠⣶⣶⣦⣼⣰⠀⠀⡿⠹⣧⠀⠀⣿⣸⣧⣿⣨⢿⠷⠒⠚⠛⠛⠛⠚⠛⠺⠯⠤⠚⠛⠓⠚⠓⠒⠻⣦⠀⡇⠀
⠀⢸⣟⣿⣿⣿⠁⠀⠀⡇⠀⠞⣷⠀⠘⢿⣽⣿⣵⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⡇⠀
⠀⢸⣿⣿⣿⣿⡆⠀⢀⣿⡷⡎⠉⢣⡀⠈⢿⡣⠻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣖⡇⠀
⠀⢸⣿⣿⣿⣿⠀⢠⠾⠃⠁⢸⡄⠀⢷⠀⠀⠻⣤⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀
⠠⣈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢁⠄
"""


banner = Add.Add(text, banner, center=True)

print(Colorate.Diagonal(Colors.DynamicMIX((purple, light)), banner))
def stage(text: str, symbol: str = 'ENJULY19', col1 = light, col2 = None) -> str:
    if col2 is None:
        col2 = light if symbol == 'ENJULY19' else purple
    return f""" {Col.Symbol(symbol, col1, dark)} {Colorate.Diagonal(Colors.DynamicMIX((purple, light)), text)}{light}"""

v = input
_v = print
def input(x):
    return v(stage(x))
def print(x,*k):
    return _v(stage(x),*k)



_file = input(" ENTER FILE: ")





while True:
    try:
        with open(_file, "r", encoding="utf8") as file:
            code = file.read()
        break
    except FileNotFoundError:

        _file = input(" ENTER FILE AGAIN (file not found): ")
        

while True:
    try:
        mode = int(input(" ENTER MODE: "))
        if mode < 4:
            break
    except ValueError:
        pass
moreobf = input(" DO YOU WANT MORE OBF? (y/n): ")

antidebug = input(" DO YOU WANT ANTI DEBUG? (y/n): ")

method = input(" DO YOU WANT COMPILE? (y/n): ")
#code = ast.unparse(_moreobf(ast.parse(code)))
check = 0
code = _syntax(code)
if moreobf.upper() == "Y":
    code = __moreobf(code)
    check = 5
checkver = f"""
import sys
if '{sys.version[0]+sys.version[1]+sys.version[2]+sys.version[3]}' not in sys.version:
    input("Your python version does not work on this code, please install {sys.version[0]+sys.version[1]+sys.version[2]+sys.version[3]}")
    __import__("sys").exit()
"""
author = f"""
((
    ((([["ENJULY19"],
    ["https://github.com/hngocuyen/enjuly19/"],
    ["PYTHON"],
    3.11
    ],
    [__import__("builtins").exec(
    {checkver.encode()})
    ])
                )
            )
        )
    )
"""
anti = r"""
import traceback, marshal

ch = set()
am = {'builtins', '__main__'}

def vv():
    raise MemoryError('>> GOOD LUCK!! CONMEMAY') from None

def cb(fn):
    if callable(fn) and fn.__module__ not in am:
        ch.add(fn.__module__)
        vv()

def ba(fn):
    def hi(*args, **kwargs):
        if args and args[0] in ch:
            vv()
        return fn(*args, **kwargs)
    return hi

def bh():
    stack = traceback.extract_stack()
    for frame in stack[:-2]:
        if frame.filename != __file__:
            vv()

def ck(fn, md):
    if callable(fn) and fn.__module__ != md:
        ch.add(md)
        raise ImportError(f'>> Detect [{fn.__name__}] call [{md}] ! <<') from None

def ic(md, nf):
    module = __import__(md)
    funcs = nf if isinstance(nf, list) else [nf]
    [ck(getattr(module, func, None), md) for func in funcs]

def lf(val, xy):
    return callable(val) and xy and val.__module__ != xy.__name__

def kt(lo):
    if any(lf(val, xy) for val, xy in lo):
        vv()

def ct(md, nf):
    module = __import__(md)
    func = getattr(module, nf, None)
    if func is None:
        vv()
    tg = type(func)
    def cf(func):
        if type(func) != tg:
            vv()
    cf(func)
    return func

def ic_type(md, nf):
    func = ct(md, nf)
    ck(func, md)

def nc():
    __import__('sys').settrace(lambda *args, **keys: None)
    __import__('sys').modules['marshal'] = None
    __import__('sys').modules['marshal'] = type(__import__('sys'))('marshal')
    __import__('sys').modules['marshal'].loads = marshal.loads

def sc():
    nk = {
        'marshal': 'loads'
    }
    [ic_type(md, nf) for md, nf in nk.items()]

    lo = [
        (__import__('marshal').loads, marshal)
    ]
    kt(lo)
    nc()

sc()
bh()
"""
if antidebug.upper() == "Y":
    code = anti+code

for i in range(mode):
    code = obf(code)


if method.upper() != "Y":
    code = var + code
    if check == 5:
        try:
            code = __moreobf(code)
        except:
            code = __moreobf(code)

else:
    if check == 5:
        try:
            code = __moreobf(code)
        except:
            code = __moreobf(code)
    code = ANTI_PYCDC + code
    code = marshal.dumps(compile(code, "", "exec"))
    code = zlib.compress(code)
    code = bz2.compress(code)
    code = base64.b85encode(code)
    l = len(code)
    part1 = code[: l // 4]
    part2 = code[l // 4: l // 2]
    part3 = code[l // 2: 3 * l // 4]
    part4 = code[3 * l // 4:]
    _f = "for"
    _i = "in"
    _t = rd()
    code = author + var + f"""

def bytecode():
    ngocuyencoder = globals().update
    if True:
        ngocuyencoder({ngoac}**{ngoac} _hex({_uni("en")}): {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("marshal")}))).items() if {_movdiv}({_temp}) and {_temp1} == _hex({_uni("loads")}){_ngoac}, **{ngoac}{_temp1}: {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("marshal")}))).items() if {_movdiv}({_temp}) and {_temp1} != _hex({_uni("loads")}){_ngoac}{_ngoac})
    else:"ngocuyencoder"
    if 1>2:
        {obfint(3)}
    else:
        ngocuyencoder({ngoac}**{ngoac}_hex({_uni("july")}): {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("zlib")}))).items() if {_movdiv}({_temp}) and {_temp1} == _hex({_uni("decompress")}){_ngoac}, **{ngoac}{_temp1}: {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("zlib")}))).items() if {_movdiv}({_temp}) and {_temp1} != _hex({_uni("decompress")}){_ngoac}{_ngoac})
    ngocuyencoder({ngoac}**{ngoac}_hex({_uni("birth")}): {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("bz2")}))).items() if {_movdiv}({_temp}) and {_temp1} == _hex({_uni("decompress")}){_ngoac}, **{ngoac}{_temp1}: {_temp} {_f} {_temp1}, {_temp} {_i} {_vars}({___import__}(_hex({_uni("bz2")}))).items() if {_movdiv}({_temp}) and {_temp1} != _hex({_uni("decompress")}){_ngoac}{_ngoac})
    ngocuyencoder()
    ngocuyencoder({ngoac}**{ngoac}_hex({_uni("_19")}): {_t} {_f} {_temp1}, {_t} {_i} {_vars}({___import__}(_hex({_uni("base64")}))).items() if {_movdiv}({_t}) and {_temp1} == _hex({_uni("b85decode")}){_ngoac}, **{ngoac}{_temp1}: {_t} {_f} {_temp1}, {_t} {_i} {_vars}({___import__}(_hex({_uni("base64")}))).items() if {_movdiv}({_t}) and {_temp1} != _hex({_uni("b85decode")}){_ngoac}{_ngoac})
    ngocuyencoder()
    ngocuyencoder({ngoac}**{ngoac}_hex({_uni("ngocuyencoder")}): {_t} {_f} {_temp1}, {_t} {_i} {_vars}({___import__}(_hex({_uni("builtins")}))).items() if {_movdiv}({_t}) and {_temp1} == _hex({_uni("exec")}){_ngoac}, **{ngoac}{_temp1}: {_t} {_f} {_temp1}, {_t} {_i} {_vars}({___import__}(_hex({_uni("builtins")}))).items() if {_movdiv}({_t}) and {_temp1} != _hex({_uni("eval")}){_ngoac}{_ngoac})
bytecode()

_en  {'  '* 999}={part1}
_july  {'  '* 999}={part2}
_birth  {'  '* 999}={part3}
__19  {'  '* 999}={part4}
try:
    ngocuyencoder(
    en(
    july(
    birth(
    _19(
    _en+_july+_birth+__19)))))
except Exception as e:
    print(e)

"""
open("enjuly-" + _file, "w", encoding="utf8").write(str(code))
print(" Save in ", "enjuly-" + _file)
