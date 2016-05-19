from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


from django.views.generic.list import ListView

from cms.models import Book, Impression
from cms.forms import BookForm, ImpressionForm

def book_list(request):
    """$B=q@R$N0lMw(B"""
#    return HttpResponse('$B=q@R$N0lMw(B')
    books = Book.objects.all().order_by('id')
    return render(request,
                  'cms/book_list.html',     # $B;HMQ$9$k%F%s%W%l!<%H(B
                  {'books': books})         # $B%F%s%W%l!<%H$KEO$9%G!<%?(B

def book_edit(request, book_id=None):
    """$B=q@R$NJT=8(B"""
#     return HttpResponse('$B=q@R$NJT=8(B')
    if book_id:   # book_id $B$,;XDj$5$l$F$$$k(B ($B=$@5;~(B)
        book = get_object_or_404(Book, pk=book_id)
    else:         # book_id $B$,;XDj$5$l$F$$$J$$(B ($BDI2C;~(B)
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # POST $B$5$l$?(B request $B%G!<%?$+$i%U%)!<%`$r:n@.(B
        if form.is_valid():    # $B%U%)!<%`$N%P%j%G!<%7%g%s(B
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:    # GET $B$N;~(B
        form = BookForm(instance=book)  # book $B%$%s%9%?%s%9$+$i%U%)!<%`$r:n@.(B

    return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))

def book_del(request, book_id):
    """$B=q@R$N:o=|(B"""
#     return HttpResponse('$B=q@R$N:o=|(B')
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('cms:book_list')


class ImpressionList(ListView):
    """$B46A[$N0lMw(B"""
    context_object_name='impressions'
    template_name='cms/impression_list.html'
    paginate_by = 2  # $B#1%Z!<%8$O:GBg(B2$B7o$:$D$G%Z!<%8%s%0$9$k(B

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['book_id'])  # $B?F$N=q@R$rFI$`(B
        impressions = book.impressions.all().order_by('id')   # $B=q@R$N;R6!$N!"46A[$rFI$`(B
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, book=book)    
        return self.render_to_response(context)

def impression_edit(request, book_id, impression_id=None):
    """$B46A[$NJT=8(B"""
    book = get_object_or_404(Book, pk=book_id)  # $B?F$N=q@R$rFI$`(B
    if impression_id:   # impression_id $B$,;XDj$5$l$F$$$k(B ($B=$@5;~(B)
        impression = get_object_or_404(Impression, pk=impression_id)
    else:               # impression_id $B$,;XDj$5$l$F$$$J$$(B ($BDI2C;~(B)
        impression = Impression()

    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)  # POST $B$5$l$?(B request $B%G!<%?$+$i%U%)!<%`$r:n@.(B
        if form.is_valid():    # $B%U%)!<%`$N%P%j%G!<%7%g%s(B
            impression = form.save(commit=False)
            impression.book = book  # $B$3$N46A[$N!"?F$N=q@R$r%;%C%H(B
            impression.save()
            return redirect('cms:impression_list', book_id=book_id)
    else:    # GET $B$N;~(B
        form = ImpressionForm(instance=impression)  # impression $B%$%s%9%?%s%9$+$i%U%)!<%`$r:n@.(B

    return render(request,
                  'cms/impression_edit.html',
                  dict(form=form, book_id=book_id, impression_id=impression_id))

def impression_del(request, book_id, impression_id):
    """$B46A[$N:o=|(B"""
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list', book_id=book_id)
