from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    if request.method == 'GET':
        form = CalcForm(request.GET)
        if form.is_valid():
            initial_fee = int(request.GET.get('initial_fee'))
            rate = int(request.GET.get('rate'))/100
            months_count = int(request.GET.get('months_count'))
            result = (initial_fee + initial_fee * rate) / months_count
            common_result = (initial_fee + initial_fee * rate)

    else:
        form = CalcForm

    context = {
                'form': form,
                'result': result,
                'common_result': common_result
            }
    return render(request, template, context)
