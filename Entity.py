class Entity:
    def __init__(self, name):
        self.eName = name
        self.attributes = []
        # Relationships nameoftherelationship = {cardinality=, modality =}
        self.relationships = {}

    def add_relationship(self, rName, cardinality, modality):
        self.relationships[rName] = {"cardinality": cardinality, "modality": modality}

    def get_relationships(self):
        return self.relationships.keys()

    def __iter__(self):
        return iter(self.relationships.keys())

    # We coulld add primary key and other type of attributes as keys in a dictionary instead of a list.
    def add_attribute(self, aName):
        if isinstance(aName, str) and aName not in self.attributes:
            self.attributes.append(aName)
        else:
            for attribute in aName:
                if attribute not in self.attributes:
                    self.attributes.extend(aName)

    def get_attributes(self):
        return self.attributes

    def get_name(self):
        return self.eName


class Diagram:
    _instance = None

    class __Diagram:

        def __init__(self):
            self.entity_dict = {}
            self.num_entities = 0

        def __iter__(self):
            return iter(self.entity_dict.values())

        def add_entity(self, eName):
            self.num_entities = self.num_entities + 1
            new_entity = Entity(eName)
            self.entity_dict[eName] = new_entity
            return new_entity

        def get_entity(self, eName):
            if eName in self.entity_dict:
                return self.entity_dict[eName]
            else:
                return None

        def add_relationship(self, fr, to, cardinality1, cardinality2, modality):
            if fr not in self.entity_dict:
                self.add_entity(fr)
            if to not in self.entity_dict:
                self.add_entity(to)

            # Esto hay que cambiarlo porque la cardinalidad y la modalidad de la entidad FROM a la entidad TO no es necesariamente igual a la de la entidad TO a la entidad FROM.
            # Tambien hay que cambiar el metodo add_relationship
            self.entity_dict[fr].add_relationship(to, cardinality1, modality)
            self.entity_dict[to].add_relationship(fr, cardinality2, 'must')

        def get_entities(self):
            return self.entity_dict.keys()

    def __init__(self):
        if not Diagram._instance:
            Diagram._instance = Diagram.__Diagram()

    def __getattr__(self, name):
        return getattr(self._instance, name)

    def _add_entity(self, eName):
        return self._instance.add_entity(eName)

    def _get_entity(self, eName):
        return self._instance.get_entity(eName)

    def _add_relationship(self, fr, to, cardinality1, cardinality2, modality):
        self._instance.add_relationship(fr, to, cardinality1, cardinality2, modality)

    def _get_entities(self):
        return self._instance.get_entities()

    def __iter__(self):
        return self._instance.__iter__()


# testing
d1 = Diagram()
print('good')
d1._add_entity('School')
i = ['name', 'city']
d1._get_entity('School').add_attribute(i)
print(d1._get_entity('School').get_attributes())
d1._get_entity('School').add_attribute(i)
print(d1._get_entity('School').get_attributes())
f = ['district']
d1._get_entity('School').add_attribute('district')
print(d1._get_entity('School').get_attributes())
d1._add_entity('Student')
d1._add_relationship('School', 'Student', 'one', 'many', 'may')

for e in d1:
    for r in e:
        print(e.get_name(), r)
