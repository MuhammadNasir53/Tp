import flet as ft

def main(page: ft.Page):
    page.title = "ToDo & Pomodoro"
    page.window.width = 390
    page.window.height = 700
    page.adaptive = True

    # Function to handle page navigation
    def route_change(route):
        page.views.clear()

        if page.route == "/pomodoro":
            page.views.append(pomodoro_view())
        else:
            page.views.append(todo_view())

        page.update()

    # Define the Bottom Navigation Bar
    def nav_bar():
        return ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.LIST, label="To-Do"),
                ft.NavigationBarDestination(icon=ft.Icons.TIMER, label="Pomodoro"),
            ],
            on_change=lambda e: page.go(["/todo", "/pomodoro"][e.control.selected_index])
        )

    # Define the To-Do View
    def todo_view():
        return ft.View(
            route="/todo",
            bgcolor="black",
            controls=[
                ft.AppBar(title=ft.Text("ToDo App")),
                ft.Text("This is the To-Do App", color="white", animate_opacity=500),
                nav_bar(),
            ]
        )

    # Define the Pomodoro View
    def pomodoro_view():
        return ft.View(
            route="/pomodoro",
            bgcolor="white",
            controls=[
                ft.AppBar(title=ft.Text("Pomodoro App")),
                ft.Text("This is the Pomodoro Timer", animate_opacity=500),
                nav_bar(),
            ]
        )

    # Initialize the app
    page.on_route_change = route_change
    page.go("/todo")  # Default page

ft.app(target=main)
