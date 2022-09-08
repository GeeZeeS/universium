from rest_framework import pagination


class MainPagination(pagination.PageNumberPagination):
    default_page = 0
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 100
    page_query_param = 'page'
