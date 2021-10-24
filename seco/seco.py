import sbol3
import tyto

def media(
    name = str
    description = str
):
    media = sbol3.Component(name, tyto.NCIT.Media)
    media.name = name
    media.description = description

def strain(
    name = str
    description = str
):
    strain = sbol3.Component(name, tyto.NCIT.Strain)
    strain.name = name
    strain.description = description

def plasmid(
    name = str
    description = str
):
    plasmid = sbol3.Component(name, sbol3.SBO_DNA)
    plasmid.name = name
    plasmid.description = description
    plasmid.roles = tyto.SO.plasmid

def simple_chemical(
    name = str
    description = str
):
    simple_chemical = sbol3.Component(name, sbol3.SBO_SIMPLE_CHEMICAL)
    simple_chemical.name = name
    simple_chemical.description = description
