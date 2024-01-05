import logging

from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import render


# Create your views here.
def quadratzahlen(request, base_number=None):
    content = ""

    try:
        base_number = int(base_number)
        for i in range(1, base_number + 1):
            content += f"{i} * {i} = {i * i}\n"

        context = {"content": content}

    except ValueError:
        messages.error(request, "Cannot quad a str")
        return render(request, "exams/quadratzahlen.html")

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    logger.info(content)

    return render(request, "exams/quadratzahlen.html", context)
