from django.shortcuts import redirect
from django.views import View


class IndexView(View):
    def get(self, _):
        return redirect('/static/index.html')


index_view = IndexView.as_view()
