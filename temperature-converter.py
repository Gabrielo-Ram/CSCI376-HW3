from nicegui import ui

ui.colors(
      primary='#4f10e3',
      secondary='#26D69A',
      accent='#9C27B0',
      positive='#21BA45',
      negative='#C10015',
      info='#31CCEC',
      warning='#F2C037'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: Changes the font color of any text in result_label to the color designated under positive in ui.colors()
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: Changes the font color of any text in result_label to the color designated under negative in ui.colors()

def slider_Conversion():
    try:
        temp = float(input_field2.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")


with ui.card().classes("w-screen h-screen p-6 shadow-xl mx-auto mt-10 rounded-xl bg-gray-100"):
    # w-100: Set element width to be fixed at 100
    # p-6: Adds padding equivlane to 6 units on all sides of the element
    # shadow-xl: Adds a shadow below the designated element
    # mx-auto: Adds automatic margins only on the left and right sides of the element; essentially centering the element in the middle of the screeen. 
    # mt-10: Adds a margin of 10 units to the top of the element
    # rounded-xl: Makes the corners of the card rounded. 
    ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4 mx-auto")
    # text-2xl: Makes the text inside this element larger. 
    # font-bold: Makes the text inside this element bold
    # text-accent: Changes the font color to the color designated under accent in ui.colors()
    # mb-4: Adds a margin of 4 units below the given element
    with ui.row().classes("mx-auto"):
        input_field = ui.input("Enter Temperature").props('type="number"').classes("mb-4 p-2 mx-auto text-lg border rounded")
        #Second slider input field
        input_field2 = ui.slider(min=0, max=100, value=50, on_change=lambda e: slider_Conversion())
        ui.label("Selected temperature is:").classes("text-lg")
        ui.label().bind_text_from(input_field2, 'value').classes("text-lg font-bold text-accent")
        ui.label("°").classes("text-lg")
    # w-full: Stretches the input field element so that its width matches the width of its container element
    # border: Adds a small border to the element
    # rounded: Makes the corners of the element slightly rounded
    conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4 mx-auto")
    convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded mx-auto")
    # text-white: Changes the font color inside the element to white
    # py-2: Adds vertical padding to the element by 2 units
    # px-4: Adds horiztonal padding to the element by 4 units.
    result_label = ui.label("").classes("text-lg mt-4 mx-auto")

ui.run()
