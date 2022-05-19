import re

pattern_int = re.compile("^-?\d+$")
pattern_float = re.compile("^-?\d*[.]\d+$")

def parse(text):
    if text.count("(") != text.count(")"):
        print("O texto da mensagem tem parênteses não correspondentes: " + str(text))
        return
    result = []
    indent = 0
    s = []
    in_string = False
    prev_c = None
    for c in text:
        if c == '"' and prev_c != "\\":
            in_string = not in_string
        elif c == "(" and not in_string:
            cur = result
            for i in range(indent):
                cur = cur[-1]
            if len(s) > 0:
                val = ''.join(s)
                if pattern_int.match(val):
                    cur.append(int(val))
                elif pattern_float.match(val):
                    cur.append(float(val))
                else:
                    cur.append(val)
                s = []
            cur.append([])
            indent += 1
        elif c == ")" and not in_string:
            if len(s) > 0:
                cur = result
                for i in range(indent):
                    cur = cur[-1]
                val = ''.join(s)
                if pattern_int.match(val):
                    cur.append(int(val))
                elif pattern_float.match(val):
                    cur.append(float(val))
                else:
                    cur.append(val)
                s = []
            indent -= 1
        elif c != " ":
            s.append(c)
        elif c == " " and len(s) > 0:
            cur = result
            for i in range(indent):
                cur = cur[-1]
            val = ''.join(s)
            if pattern_int.match(val):
                cur.append(int(val))
            elif pattern_float.match(val):
                cur.append(float(val))
            else:
                cur.append(val)
            s = []
        prev_c = c
    return result[0]
