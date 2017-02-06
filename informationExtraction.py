import nltk
import re

### noun parsing
grammer = """
          NP: {<NN><NN>}"""
grammer = "NP: {<NN>*}"

cp = nltk.RegexpParser(grammer)    
nouns = [('money', 'NN'), ('market', 'NN'), ('fund', 'NN')]



## more complex noun parsing
grammer = r"""
       NP: {<DT|PP\$>?<JJ>*<NN>}
       {<NNP>+}
       """
cp = nltk.RegexpParser(grammer)
sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"),
            ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"),
            ("hair", "NN")]
print cp.parse(sentence)


