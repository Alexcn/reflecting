from django.contrib.sitemaps import Sitemap
from blog.models import Article


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Article.objects.filter(status=0)

    def lastmod(self, obj):
        return obj.created_time

    def location(self, item):
        return '/article/%s' % item.url
