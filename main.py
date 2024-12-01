from flask import Flask 
 
# создание обьекта Flask / приложения 
 
app = Flask(__name__) 
 
 
# global variables 
weather = {"astana": -10.3, "almaty": -6.3, "vienna": 0} 
todos = [] 
 
 
@app.route("/") 
def welcome(): 
    return "Это мое первое API" 
 
 
@app.route("/name") 
def name(): 
    return "Привет, Aitbek" 
 
 
@app.route("/todos/new/<title>") 
def append_title(title): 
    todos.append(title) 
    return f"Title: '{title}' succesfully has been append to list todos" 
 
 
@app.route("/todos") 
def return_todos(): 
    return todos 
 
 
@app.route("/city/<city_name>") 
def weather_by_city(city_name): 
    for i in weather: 
        if i == city_name.lower(): 
            return f"Твой город: {city_name} \n Температура твоего города в C: {weather[i]}" 
    return "Твой город не найден" 
 

@app.route("/todos/remove/<index>") 
def remove_element_of_todos(index): 
    if (len(todos) < (int(index) + 1)) or (int(index) < -len(todos)): 
        return "Индекс не найден сорри" 
    del todos[int(index)] 
    return todos

@app.route('/todos/get/<index>')
def get_index(index):
    index = int(index)
    if -len(todos) <= index < len(todos):
        return f'Your element is - {todos[index]}'
    return f'Sorry, but finding by {index} is impossible'


@app.route('/todos/edit/<index>/<new_title>')
def edit_by_index(index, new_title):
    index = int(index)
    if -len(todos) <= index < len(todos):
        todos[index] = new_title
        return todos
    return 'Error, please enter a correct index'

# @app.route("/todos/remove/<index>") 
# def remove_element_of_todos(index): 
#     if todos.pop(int(index)) == -1: 
#         return "Error" 
#     return todos 
 
 
if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)