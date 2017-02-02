import nltk
import re
grammer = r"""
       NP: {<DT|PP\$>?<JJ>*<NN>}{<NNP>+}
       """
cp = nltk.RegexpParser(grammer)
sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"),
            ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"),
            ("hair", "NN")]
print cp.parse(sentence)
