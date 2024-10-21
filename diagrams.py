# diagrams.py
from graphviz import Digraph
import inspect
from models.population import Population, Animal, Dog, Cat


def create_class_diagram():
    diagram = Digraph()

    # Fungsi untuk membuat label dalam format tabel
    def create_class_label(cls):
        class_label = f"""<<table border="0" cellborder="1" cellspacing="0">
<tr><td bgcolor="lightgrey"><b>{cls.__name__}</b></td></tr>"""

        # Menambahkan atribut dari konstruktor
        if hasattr(cls, "__init__"):
            init_method = cls.__init__
            params = inspect.signature(init_method).parameters
            for param in params:
                if param != "self":  # Abaikan parameter 'self'
                    # Anggap semua atribut bertipe str untuk contoh ini
                    class_label += f"<tr><td>- {param}: {params[param].annotation.__name__ if params[param].annotation != inspect.Parameter.empty else 'Any'}</td></tr>"

        # Menambahkan metode
        for name, obj in inspect.getmembers(cls):
            if inspect.isfunction(obj):  # Mengecek apakah itu sebuah fungsi
                class_label += f"<tr><td><i>+ {name}()</i></td></tr>"

        class_label += "</table>>"
        return class_label

    # Tambahkan kelas Population
    diagram.node("Population", label=create_class_label(Population), shape="none")

    # Tambahkan kelas Animal
    diagram.node("Animal", label=create_class_label(Animal), shape="none")

    # Tambahkan kelas Dog
    diagram.node("Dog", label=create_class_label(Dog), shape="none")

    # Tambahkan kelas Cat
    diagram.node("Cat", label=create_class_label(Cat), shape="none")

    # Menambahkan hubungan
    # Contoh relasi
    diagram.edge("Population", "Animal", label="has-a")  # Population has-a Animal
    diagram.edge("Animal", "Dog", label="inherits")  # Dog inherits Animal
    diagram.edge("Animal", "Cat", label="inherits")  # Cat inherits Animal

    # Menghasilkan diagram
    path = "./diagrams"
    diagram.render(f"{path}/population_diagram", format="png", cleanup=True)


if __name__ == "__main__":
    create_class_diagram()
