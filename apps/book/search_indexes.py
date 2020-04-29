import datetime

from haystack import indexes
from apps.book.models import Book

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """对Article模型类中部分字段建立索引"""
    text = indexes.CharField(document=True, use_template=True, template_name='search/book_text.txt')

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        """当Article模型类中的索引有更新时调用"""
        return self.get_model().objects.all()
