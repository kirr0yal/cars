from django.http import HttpRequest, HttpResponse


def name(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        name = request.POST.get("name", "")
        age = int(request.POST.get("age", 0))
        return HttpResponse(f"""
            thank you, {name}
            <br>
            you are {age} years old
        """)
    return HttpResponse("""
    <form method="POST">
        {% csrf_token %}
        <label for="name">What is your name?</label>
        <input id="name" name="name" value="Bill" type="text">
        <br>
        <label for="age">What is your age?</label>
        <input id="age" name="age" value="50" type="number">
        <br>
        <button type="submit">OK</button>
    </form>
    """)
