from django.shortcuts import render, HttpResponse
from django.db import connection
from .forms import SqlQueryForm
from django.core.paginator import Paginator
from .queries import predefined_queries

# Create your views here.
def home(request):
    print("Rendering home view...")
    return render(request, "home.html")

def execute_sql_query(request):
    form = SqlQueryForm(request.POST or None)
    result = None
    columns = None
    page_obj = None
    query = None

    if request.method == "POST":
        selected_query_key = request.POST.get('predefined_query', '')
        if selected_query_key in predefined_queries:
            query = predefined_queries[selected_query_key]
        elif form.is_valid():
            query = form.cleaned_data['query']

    if query:
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                paginator = Paginator(result, 30)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
        except Exception as e:
            result = f"Error executing query: {e}"

    return render(request, 'execute_sql.html', {
        'form': form,
        'result': result,
        'columns': columns,
        'page_obj': page_obj,
        'query': query,
        'predefined_queries': predefined_queries
    })
