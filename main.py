import flet as ft

def main(page: ft.Page):
    page.title = "Examen Final - Registro de Participantes"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    
    titulo = ft.Text(
        "Registro de Participantes",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    nombre = ft.TextField(label="Nombre completo")
    correo = ft.TextField(label="Correo electrónico")
    
    taller = ft.Dropdown(
        label="Taller de interés",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ]
    )
    
    modalidad_pago = ft.RadioGroup(
        content=ft.Column([
            ft.Text("Modalidad de pago:"),
            ft.Radio(value="Pago completo", label="Pago completo"),
            ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
        ]),
        value="Pago completo"
    )
    
    requiere_portatil = ft.Checkbox(label="Requiere computadora portátil")
    
    nivel_texto = ft.Text("Nivel: 1")
    def slider_changed(e):
        nivel_texto.value = f"Nivel: {int(e.control.value)}"
        page.update()

    nivel_experiencia = ft.Slider(
        min=1,
        max=5,
        divisions=4,
        value=1,
        label="{value}",
        on_change=slider_changed
    )
    
    resumen = ft.Text(size=16, color=ft.Colors.BLUE_900)
    
    def mostrar_resumen(e):
        resumen.value = (
            "--- FICHA DEL PARTICIPANTE ---\n\n"
            f"Nombre: {nombre.value}\n\n"
            f"Email: {correo.value}\n\n"
            f"Taller: {taller.value}\n\n"
            f"Pago: {modalidad_pago.value}\n\n"
            f"Requiere Portátil: {'Sí' if requiere_portatil.value else 'No'}\n\n"
            f"Nivel de Experiencia: {int(nivel_experiencia.value)}\n\n"
            "--- Gracias por su registro ---"
        )
        page.update()
        
    boton = ft.Row(
        controls=[
            ft.ElevatedButton(
                text="Mostrar Ficha del Participante",
                bgcolor=ft.Colors.GREEN_400,
                on_click=mostrar_resumen
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    page.add(
        ft.Column(
            controls=[
                titulo,
                nombre,
                correo,
                taller,
                modalidad_pago,
                requiere_portatil,
                nivel_texto,
                nivel_experiencia,
                boton,
                resumen
            ],
            spacing=15
        )
    )
    
ft.app(target=main)
