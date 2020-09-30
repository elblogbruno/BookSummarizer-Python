from BookSumarizer import BookSummarizer

if __name__ == "__main__":
    pages = [11,12]
    summarizer = BookSummarizer("C:/Users/elblo/Desktop/so-libro.pdf",pages,"SO-Resum")
    summarizer.summarizeBook()