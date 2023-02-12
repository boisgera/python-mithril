import js
import pyodide
import pyodide.ffi

print(dir(pyodide.ffi))

print("Hullo!")
m = js._mithril

def o(my_dict): # Oh my ...
    return js.Object.fromEntries(pyodide.ffi.to_js(my_dict))

# TODO: support "style" value as a dict
# TODO: m.mount
# TODO: click events

m.render(js.document.body,
    m("div",
        m("p", "Hello from py!"),        
        m("p", "Hello from py!"),
        m("div", 
            o({"style": "height: 400px; width: 400px; background-color: red"})
        )
    )
)




    # m("div", 
    #     {"style": "height: 400px; width: 400px; background-color: 'red'"}
    # ))