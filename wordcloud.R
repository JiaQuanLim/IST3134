# Reading the word_count_output.csv
wordcount <- read.csv("/Users/jiaquanlim/Downloads/word_count_output.csv", stringsAsFactors = FALSE)

set.seed(1234) # for reproducibility 

# Plotting wordcloud
wordcloud(words = wordcount$Word, freq = wordcount$Count, min.freq = 8000,
          max.words=500, random.order=FALSE, rot.per=0.35,
          colors=brewer.pal(8, "Dark2"))
