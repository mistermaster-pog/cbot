from lark import Lark

with open("grammar/cbot.lark") as f:
    grammar = f.read()

parser = Lark(grammar, start="program", parser="lalr")

code = """
extern void main()
{
    search(UraniumOre);
    grab();
}
"""

tree = parser.parse(code)
print(tree.pretty())
