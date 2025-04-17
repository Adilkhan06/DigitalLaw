from django.shortcuts import render, redirect, get_object_or_404
from .models import Term
from django.db.models import Q
from .forms import FeedbackForm
from django.contrib import messages

def home(request):
    return render(request, 'terms/home.html')


def search(request):
    query = request.GET.get('q', '')
    number = request.GET.get('number', '')
    letter = request.GET.get('letter', '').upper()

    terms = Term.objects.all()

    if query:
        terms = terms.filter(
            Q(term_name__icontains=query) |
            Q(term_description__icontains=query)
        )
    elif number and letter:
        terms = terms.filter(term_name__iregex=rf'^{number}-бап\.\s*{letter}')
    elif number:
        terms = terms.filter(term_name__startswith=f"{number}-")
    elif letter:
        terms = terms.filter(term_name__iregex=rf'^\d+-бап\.\s*{letter}')

    return render(request, 'terms/search.html', {
        'terms': terms,
        'query': query,
        'number': number,
        'letter': letter,
        'all_letters': 'АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯ'
    })


def term_detail(request, term_id):
    term = get_object_or_404(Term, pk=term_id)
    return render(request, 'terms/term_detail.html', {'term': term})


def about(request):
    return render(request, 'terms/about.html')


def references(request):
    references_list = [
        "Қазақстан Республикасының Конституциясы",
        "Қазақстан Республикасының Азаматтық Кодексі",
        "Сүлейменов, М. К., & Басин, Ю. Г. (ред.). (2006). Қазақстан Республикасының Азаматтық кодексі (Ерекше бөлік): Түсіндірме (баптарға) (1-кітап, 406–767-баптар). Алматы: Қазақ гуманитарлық-заң университеті, Жеке құқық ғылыми-зерттеу институты, «Зангер» заң фирмасы."
    ]
    return render(request, 'terms/references.html', {'references': references_list})


def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение отправлено!')
            return redirect('contact')
    else:
        form = FeedbackForm()

    return render(request, 'terms/contact.html', {'form': form})