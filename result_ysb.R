install.packages("KoNLP")
install.packages("RCOlorBrewer")
install.packages("wordcloud")

library(KoNLP)
library(RColorBrewer)
library(wordcloud)

useSejongDic()

pal2 <- brewer.pal(8,"Dark2")

text <- readLines(file.choose())

text
