import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer


#article = """Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics"""
article ="""The Federal Government on Wednesday said it was not fighting corruption to impress civil society organisations, Transparency International, or any other anti-corruption watchdog. It said, rather, its anti-corruption drive was meant to ensure growth across all sectors of the nation’s economy. “We are not fighting corruption because we want to impress Transparency International or any organisation whatsoever,” the Minister of Information, Lai Mohammed, told State House correspondents after this week’s Federal Executive Council meeting chaired by the President at the Aso Rock Villa, Abuja. Transparency International on Tuesday released its 2022 Corruption Perceptions Index report, with Nigeria maintaining its 2021 score of 24 out of 100 points while ranking 150th among 180 countries. The 2022 CPI, released on January 31, 2023, ranks Denmark, Finland, New Zealand, Norway, Singapore, Sweden, Switzerland, Netherlands, Germany and Ireland in the top 10. According to the report, their scores range between 90 and 77; these countries are the “cleanest.” However, it ranked Burundi, Equatorial Guinea, Haiti, North Korea, Libya, Yemen, Venezuela, South Sudan, Syria and Somalia as the most corrupt 10, with scores ranging from 12 to 17 out of 100. The indices include bribery, diversion of public funds, public officials using public office for private gain without consequence, the ability of governments to contain corruption and enforce effective integrity mechanisms in the public sector, red tape and excessive bureaucratic burden, which may increase opportunities for corruption and meritocratic versus nepotistic appointments in the civil service. However, the Federal Government faulted TI’s template used in the survey. It advised the anti-corruption watchdog to modify its rating template, adding that the Buhari regime is tackling corruption seriously. According to the minister, “We are not fighting corruption because we want to impress Transparency International or any organisation. “We’re fighting corruption because we believe if we do not fight corruption, there’ll be no growth either in terms of the economy or even politics. “Therefore, what we do and what we’re putting in place to fight corruption is not because we want to be rated by anybody.” He questioned the template used for the survey saying, “Whatever template they’re using is clearly oblivious of what this administration is doing to fight corruption.” “Fighting corruption is not just by how many people you have arrested. How many people have you tried? How many people have you convicted? “So, we are not worried or bothered about the rating of Transparency International because we know that everything we do is to ensure that we fight corruption the best way we know how to do it. “If they are not seeing this, then I think they have to change their template. But again, we’re not fighting corruption to impress them.” Mohammed argued that the regime’s handling of the Abacha loot and the efforts of anti-graft agencies such as the Economic and Financial Crimes Commission have made corruption difficult. He said, “To me, this is one example of how to fight corruption—an example of how to ensure that people do not steal what has been recovered again. “I make proud to say that we have been more proactive in fighting corruption and people are not willing to see what we have put in place to fight corruption. “Again, the courage of this administration even to expose high-ranking officials of the administration who have run afoul of the law is evidence of our determination and courage to fight corruption.”"""
print(len(article))
print(len(str.split(article)))
parser = PlaintextParser.from_string(article,Tokenizer("english"))
summarizer = EdmundsonSummarizer()
#Summarize the document with 2 sentences
summary = summarizer(parser.document, 2)
result =""
for words in summary:
    result +=  str(words)

print(result)
print(len(result))
print(len(str.split(result)))
    
