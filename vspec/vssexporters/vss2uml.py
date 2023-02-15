names_list = [
    "Vehicle.AngularVelocity",
    "Vehicle.Trailer",
    "Vehicle.CurrentLocation",
    "Vehicle.CurrentLocation.GNSSReceiver",
    "Vehicle.CurrentLocation.GNSSReceiver.MountingPosition",
    "Vehicle.OBD.Status",
    "Vehicle.OBD.Status.IsMILOn",
    "Vehicle.OBD.Status.DTCCount",
]

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def print(self):
        print(self.name)
        for child in self.children:
            child.print()
            
    def print_in_uml(self):
        """
        @startuml
        Class01 <|-- Class02
        Class01 <|-- Class03
        @enduml
        """
        result = ""
        for child in self.children:
            result += "\n{} <|-- {}".format(self.name, child.name)
            result += child.print_in_uml()
        return result
            
    def find_child(self, name_to_find):
        for child in self.children:
            if name_to_find == child.name:
                return child
        return None
            
    def add_data(self, data_name):
        prefix_suffix = data_name.split(".", 1)
        prefix = prefix_suffix[0]
        if len(prefix_suffix) > 1:
            suffix = prefix_suffix[1]
        else:
            suffix = None
        child_prefix = self.find_child(prefix)
        if child_prefix is None:
            new_child = Node(prefix)
            self.children.append(new_child)
            if suffix is not None:
                new_child.add_data(suffix)
        else:
            child_prefix.add_data(suffix)
            

tree = Node("Root")
for data_name in names_list:
    tree.add_data(data_name)

# tree.print()

print("@startuml" + tree.print_in_uml() + "\n@enduml")
