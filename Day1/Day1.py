from textblob import TextBlob

para = TextBlob("Lorem ipsum dolor sit amet, putent facete officiis sit et, impedit omittam appellantur eam eu, ne quaestio urbanitas vix. Eum an omnes officiis sapientem, illud consetetur te cum. At vix dicat denique, eu sea veritus adipiscing, iusto utroque placerat ius ea. Ius ubique cetero id. Prompta assentior eam an,  mel alia essent copiosae.")

sent = para.sentences



for i in sent:
    print i

allwords = para.words

for i in allwords:
    print i


noun = para.noun_phrases



