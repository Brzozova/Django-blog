from django.shortcuts import render

def post_list(request): #funkcja pobiera request
    return render(request, 'blog/post_list.html', {})
    #zwraca funkcję render, która złoży w całość szablon "....html"
