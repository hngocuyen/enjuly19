import ast
import random
import zlib
import marshal
import base64
import bz2
import re
import sys
from pystyle import *



def _rd():
    return "".join(__import__("random").sample([chr(i) for i in range(97, 122)], k=5))
def _rd1():
    return "".join(__import__("random").sample([chr(i) for i in range(97, 122)], k=1))



def rd():
    return "_" + "".join(
        __import__("random").sample([str(i) for i in range(1, 20)], k=2)
    )


def randomint():
    return "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))


def _chrobf(x):
    return ord(x)+0xFF78FF


def obfstr(v):
    global _join
    global _hexrun
    if v == "":
        return f"''"
    else:
        x = []
        r = list(v)
        for i in range(len(r)):
            x.append(_chrobf(r[i]))
        _str_ = f"""(lambda {rd()} : (lambda {rd()} : (lambda {rd()} : {_join}(({_hexrun}({_lambda}) for {_lambda} in {x})))('19'))('07'))('2008')"""
        return _str_



def obfint(v):
    return f"""hexlamfia({(v+0x7777)}) if {_str}({_type}({_bool}({(v)}))) == {_str}({_type}({_int}({randomint()})>{_int}({randomint()})<{_int}({randomint()})>{_int}({randomint()}))) else {v}"""


def varsobf(v):
    return f"""({(v)}) if bool(bool(bool({(v)}))) < bool(type(int({randomint()})>int({randomint()})<int({randomint()})>int({randomint()}))) and bool(str(str({randomint()})>int({randomint()})<int({randomint()})>int({randomint()}))) > 2 else {v}"""


_join = "cmp"
_lambda = "ㅤ"
_int = "mov"
_str = "ret"
_bool = "cout"
_type = "endl"
_bytes = "add"
_vars = "sub"
_ip = "add"
ngoac = "{"
_ngoac = "}"
___import__ = "_break"
_movdiv = "_movdiv"
_hexrun = "ENJULY19"
_argshexrun = "hex"


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
var = rf"""
def {_bool}():
    globals()['{_bool}'] = {varsobf('bool')}
    bool(bool(bool(19)))
def {_str}():
    globals()['{_str}'] =  {varsobf('str')}
    str(str(str(7)))
def {_type}():
    globals()['{_type}'] =  {varsobf('type')}
    bool(str(float(int(str(int(str(2008)))))))
def {_int}():
    globals()['{_int}'] =  {varsobf('int')}
    float(int(str(int(str(19072008)))))
def {_bytes}():
    globals()['{_bytes}'] =  {varsobf('bytes')}
    float(int(str(int(str(19072008)))))
def {_vars}():
    globals()['{_vars}'] =  {varsobf('vars')}
    float(int(str(int(str(19072008)))))
def {_movdiv}():
    globals()['{_movdiv}'] =  {varsobf('callable')}
    float(int(str(int(str(19072008)))))
def {___import__}():
    globals()['{___import__}'] =  {varsobf('__import__')}
    float(int(str(int(str(19072008)))))
{_bool}()
{_str}()
{_type}()
{_int}()
{_bytes}()
{_vars}()
{_movdiv}()
{___import__}()
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
def hexlamfia(x):
    return {_int}(x-0x7777)
if {obfint(True)}:
    def {_hexrun}({_argshexrun}):
        {_argshexrun} = {_argshexrun}-0xFF78FF
        if {_argshexrun} <= 0x7F:
                    return {_str}({_bytes}([{_argshexrun}]),"utf8")
        elif {_argshexrun} <= 0x7FF:
                    if 1<2:
                            b1 = 0xC0 | ({_argshexrun} >> 6)
                    b2 = 0x80 | ({_argshexrun} & 0x3F)
                    return {_str}({_bytes}([b1, b2]),"")
        elif {_argshexrun} <= 0xFFFF:
                b1 = 0xE0 | ({_argshexrun} >> 12)
                if 2>1:
                    b2 = 0x80 | (({_argshexrun} >> 6) & 0x3F)
                b3 = 0x80 | ({_argshexrun} & 0x3F)
                return {_str}({_bytes}([b1, b2, b3]),"")
        else:   
            b1 = 0xF0 | ({_argshexrun} >> 18)
            if 2==2:
                b2 = 0x80 | (({_argshexrun} >> 12) & 0x3F)
            if 1<2<3:
                b3 = 0x80 | (({_argshexrun} >> 6) & 0x3F)
            b4 = 0x80 | ({_argshexrun} & 0x3F)
            return {_str}({_bytes}([b1, b2, b3, b4]),"")
    def _hex(j):
        {_argshexrun} = ''
        for _hex in j:
            {_argshexrun} += ({_hexrun}(_hex))
        return {_argshexrun}
else:"enjuly19"
"""


ANTI_PYCDC = f"""
try:pass
except:pass
else:pass
finally:int(2008-2006)
try:
    def ___(__, _: str, ngocuyen = True, deptrai = True) -> None:pass
except:pass
finally:pass
"""


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


def obfuscate(node):
    for i in ast.walk(node):
        if isinstance(i, ast.Global):
            continue
        for f, v in ast.iter_fields(i):
            if isinstance(v, list):
                ar = []
                for j in v:
                    if isinstance(j, ast.Constant) and isinstance(j.value, str):
                        ar.append(ast.parse(obfstr(j.value)).body[0].value)
                    elif isinstance(j, ast.Constant) and isinstance(j.value, int):
                        ar.append(ast.parse(obfint(j.value)).body[0].value)
                    elif isinstance(j, ast.JoinedStr):
                        ar.append(fm(j))
                    elif isinstance(j, ast.AST):
                        ar.append(j)
                if any(
                    isinstance(elem, ast.Constant) and isinstance(elem.value, bool)
                    for elem in v
                ):
                    setattr(i, f, v)
                else:
                    setattr(i, f, ar)
            elif isinstance(v, ast.Constant) and isinstance(v.value, str):
                setattr(i, f, ast.parse(obfstr(v.value)).body[0].value)
            elif isinstance(v, ast.Constant) and isinstance(v.value, int):
                setattr(i, f, ast.parse(obfint(v.value)).body[0].value)
            elif isinstance(v, ast.JoinedStr):
                setattr(i, f, fm(v))


def random_if_else():
    return ast.If(
        test=ast.Compare(
            left=ast.Constant(value=False, kind=None),
            ops=[ast.Lt()],
            comparators=[ast.Constant(value=True, kind=None)],
        ),
        body=[
            ast.Assign(
                lineno=0,
                col_offset=0,
                targets=[ast.Name(id=rd(), ctx=ast.Store())],
                value=ast.Constant(value=[[True], [False]], kind=None),
            )
        ],
        orelse=[
            ast.Assign(
                lineno=0,
                col_offset=0,
                targets=[ast.Name(id=rd(), ctx=ast.Store())],
                value=ast.Constant(value=['ngocuyencoder', 'tronvietname'], kind=None),
            ),
            ast.Assign(
                lineno=0,
                col_offset=0,
                targets=[ast.Name(id=rd(), ctx=ast.Store())],
                value=ast.Constant(value=[[4], [6]], kind=None),
            ),
            ast.Assign(
                lineno=0,
                col_offset=0,
                targets=[ast.Name(id=rd(), ctx=ast.Store())],
                value=ast.Constant(value=[2, 2], kind=None),
            ),
            ast.Assign(
                lineno=0,
                col_offset=0,
                targets=[ast.Name(id=rd(), ctx=ast.Store())],
                value=ast.Constant(value=[rd(), rd()], kind=None),
            ),
            
            ast.Expr(
                lineno=0,
                col_offset=0,
                value=ast.Call(
                    func=ast.Name(id=__bool, ctx=ast.Load()),
                    args=[ast.Constant(value=[False], kind=None)],
                    keywords=[],
                ),
            ),
        ],
    )


def random_match_case():
    return ast.Match(
        subject=ast.Compare(
            left=ast.Constant(value=False, kind=None),
            ops=[ast.Lt()],
            comparators=[ast.Constant(value=True, kind=None)],
        ),
        cases=[
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)),
                body=[
                    ast.Assign(
                        lineno=0,
                        col_offset=0,
                        targets=[ast.Name(id=rd(), ctx=ast.Store())],
                        value=ast.Constant(value=[[True], [False]], kind=None),
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
                            func=ast.Name(id=_rd(), ctx=ast.Load()),
                            args=[ast.Constant(value=[False], kind=None)],
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
        for _ in range(loop):
            j = ast.Try(
                body=[random_match_case()],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id="MemoryError", ctx=ast.Load()),
                        name=rd(),
                        body=[j],
                    )
                ],
                orelse=[],
                finalbody=[random_if_else()],
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
    tree = ast.parse(code)
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

print(f'{purple} {banner}')






    
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
        break
    except ValueError:
        pass

method = input(" DO YOU WANT COMPILE? (y/n): ")



checkver = f"""
import sys
if '{sys.version[0]+sys.version[1]+sys.version[2]+sys.version[3]}' not in sys.version:
    input("Your python version does not work on this code, please install python3.11")
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

for i in range(mode):
    code = obf(code)

if method.upper() != "Y":
    code = var + code



else:
    code = ANTI_PYCDC + code
    code = marshal.dumps(compile(code, "", "exec"))
    code = zlib.compress(code)
    code = bz2.compress(code)
    code = base64.b85encode(code)
    l = len(code)
    part1 = code[: l // 4]
    part2 = code[l // 4 : l // 2]
    part3 = code[l // 2 : 3 * l // 4]
    part4 = code[3 * l // 4 :]
    _f = "for"
    _i = "in"
    _t = rd()
    code = author+var+f"""
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
ngocuyencoder(
en(
july(
birth(
_19(
_en+_july+_birth+__19)))))
"""
open("enjuly-" + _file, "w", encoding="utf8").write(str(code))
print(" Save in ", "enjuly-" + _file)
