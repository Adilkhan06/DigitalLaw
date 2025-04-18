from django.shortcuts import render, redirect, get_object_or_404
from .models import Term
from django.db.models import Q
from .forms import FeedbackForm
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

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
        "Сүлейменов, М. К., & Басин, Ю. Г. (ред.). (2006). Қазақстан Республикасының Азаматтық кодексі (Ерекше бөлік): Түсіндірме (баптарға) (1-кітап, 406–767-баптар). Алматы: Қазақ гуманитарлық-заң университеті, Жеке құқық ғылыми-зерттеу институты, «Зангер» заң фирмасы.",
        "Лотереялар және     лотерея қызметі туралы Қазақстан Республикасының Заңы 2016 жылғы 9 сәуірдегі № 495-V ҚРЗ.",
        "Ойын бизнесі туралы Қазақстан Республикасының 2007 жылғы 12 қаңтардағы N 219 Заңы",
        "Жауапкершілігі шектеулі және қосымша жауапкершілігі бар серіктестіктер туралы Қазақстан Республикасының 1998 жылғы 22 сәуірдегі N 220-І Заңы",
        "Коммерциялық емес ұйымдар туралы Қазақстан Республикасының 2001 жылғы 16 қаңтардағы N 142 Заңы.",
        "Тауар белгілері, қызмет көрсету белгілері, географиялық нұсқамалар және тауарлар шығарылған жерлердің атаулары туралы Қазақстан Республикасының 1999 жылғы 26 шілдедегі N 456 Заңы.",
        "Интегралдық микросхемалар топологияларын құқықтық қорғау туралы Қазақстан Республикасының 2001 жылғы 29 маусымдағы N 217 Заңы.",
        "Селекциялық жетістіктерді қорғау туралы Қазақстан Республикасының 1999 жылғы 13 шілдедегі N 422 Заңы.",
        "Авторлық құқық және сабақтас құқықтар туралы Қазақстан Республикасының 1996 жылғы 10 маусымдағы N 6-I Заңы.",
        "Жарнама туралы Қазақстан Республикасының 2003 жылғы 19 желтоқсандағы N 508 Заңы.",
        "Қазақстан Республикасының Патент Заңы Қазақстан Республикасының 1999 жылғы 16 шілдедегі N 427 Заңы.",
        "Соттардың мұрагерлік туралы заңнаманы қолдануының кейбір мәселелері туралы Қазақстан Республикасы Жоғарғы Сотының 2009 жылғы 29 маусымдағы N 5 Нормативтік қаулысы.",
        "НЕКОТОРЫЕ АСПЕКТЫ УЧАСТИЯ РЕБЕНКА В ОТНОШЕНИЯХ НАСЛЕДСТВЕННОГО ПРЕЕМСТВА, Марина Викторовна Телюкина",
        "МҰРАГЕРЛІК ҚҰҚЫҚТАРДЫ ҚОРҒАУДЫ ЖҮЗЕГЕ АСЫРУДЫҢ КЕЙБІР МӘСЕЛЕРІ Жайлин Ғ.А, Мақсатов Н.Р",
        "АНАЛИЗ НЕКОТОРЫХ НОРМ ТРЕТЬЕЙ ЧАСТИ ГРАЖДАНСКОГО КОДЕКСА РФ, Е.А.Коршунова",
        "Признание наследника отпавшим, Ф.Сапарова ҚР заң шығару институтының жаршысы",
        "Халықаралық құқық ІІ"
    ]
    return render(request, 'terms/references.html', {'references': references_list})


def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение отправлено!', extra_tags='contact')
            return redirect('contact')
    else:
        form = FeedbackForm()

    return render(request, 'terms/contact.html', {'form': form})





def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пікіріңіз үшін рақмет!', extra_tags='reviews')
            return redirect('reviews')
    else:
        form = ReviewForm()

    reviews_list = Review.objects.all()
    return render(request, 'terms/reviews.html', {
        'reviews': reviews_list,
        'form': form
    })


from django.http import JsonResponse
from django.template.loader import render_to_string


def google_search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Term.objects.filter(
            Q(term_name__icontains=query) |
            Q(term_description__icontains=query)
        )[:10]

    if request.headers.get('HX-Request') == 'true':
        html = render_to_string('terms/search_results.html', {'results': results})
        return JsonResponse({'html': html})

    return render(request, 'terms/google_search.html', {
        'query': query,
        'results': results
    })