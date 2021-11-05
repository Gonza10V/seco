import sbol3
import tyto
from typing import List

# creating parts

def promoter(
    name : str,
    description : str,
    sequence : str
): #-> List[sbol3.TopLevel]:
    '''
    Creates a default promoter with a sequence.
    '''
    promoter_seq = sbol3.Sequence(f'{name}_seq')
    promoter_seq.elements= sequence
    promoter_seq.encoding = 'https://identifiers.org/edam:format_1207'

    promoter = sbol3.Component(name, sbol3.SBO_DNA)
    promoter.name = name
    promoter.description = description
    promoter.roles. append(sbol3.SO_PROMOTER)
    promoter.sequences.append(promoter_seq)
    return promoter, promoter_seq

def rbs(
    name : str,
    description : str,
    sequence : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default rbs with a sequence.
    '''
    rbs_seq = sbol3.Sequence(f'{name}_seq')
    rbs_seq.elements= sequence
    rbs_seq.encoding = 'https://identifiers.org/edam:format_1207'

    rbs = sbol3.Component(name, sbol3.SBO_DNA)
    rbs.name = name
    rbs.description = description
    rbs.roles. append(sbol3.SO_RBS)
    rbs.sequences.append(rbs_seq)
    return rbs, rbs_seq

def cds(
    name : str,
    description : str,
    sequence : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default cds with a sequence.
    '''
    cds_seq = sbol3.Sequence(f'{name}_seq')
    cds_seq.elements= sequence
    cds_seq.encoding = 'https://identifiers.org/edam:format_1207'

    cds = sbol3.Component(name, sbol3.SBO_DNA)
    cds.name = name
    cds.description = description
    cds.roles. append(sbol3.SO_CDS)
    cds.sequences.append(cds_seq)
    return cds, cds_seq

def terminator(
    name : str,
    description : str,
    sequence : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default terminator with a sequence.
    '''
    terminator_seq = sbol3.Sequence(f'{name}_seq')
    terminator_seq.elements= sequence
    terminator_seq.encoding = 'https://identifiers.org/edam:format_1207'

    terminator = sbol3.Component(name, sbol3.SBO_DNA)
    terminator.name = name
    terminator.description = description
    terminator.roles. append(sbol3.SO_TERMINATOR)
    terminator.sequences.append(terminator_seq)
    return terminator, terminator_seq

def deg_tag(
    name : str,
    description : str,
    sequence : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default degradation tag with a sequence.
    '''
    deg_tag_seq = sbol3.Sequence(f'{name}_seq')
    deg_tag_seq.elements= sequence
    deg_tag_seq.encoding = 'https://identifiers.org/edam:format_1207'

    deg_tag = sbol3.Component(name, sbol3.SBO_DNA)
    deg_tag.name = name
    deg_tag.description = description
    deg_tag.roles. append(tyto.SO.protein_stability_element)
    deg_tag.sequences.append(deg_tag_seq)
    return deg_tag, deg_tag_seq

def transcriptional_unit(
    name : str,
    description : str,
    sequence : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default transcriptional unit with a sequence.
    '''
    transcriptional_unit_seq = sbol3.Sequence(f'{name}_seq')
    transcriptional_unit_seq.elements= sequence
    transcriptional_unit_seq.encoding = 'https://identifiers.org/edam:format_1207'

    transcriptional_unit = sbol3.Component(name, sbol3.SBO_DNA)
    transcriptional_unit.name = name
    transcriptional_unit.description = description
    transcriptional_unit.roles.append(sbol3.SO_ENGINEERED_REGION)
    return transcriptional_unit, transcriptional_unit_seq

def engineered_region(
    name = str,
    description = str,
    sequence = str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default engineered region with a sequence.
    '''
    engineered_region_seq = sbol3.Sequence(f'{name}_seq')
    engineered_region_seq.elements= sequence
    engineered_region_seq.encoding = 'https://identifiers.org/edam:format_1207'

    engineered_region = sbol3.Component(name, sbol3.SBO_DNA)
    engineered_region.name = name
    engineered_region.description = description
    engineered_region.roles.append(sbol3.SO_ENGINEERED_REGION)
    return engineered_region, engineered_region_seq

def plasmid_vector(
    name : str,
    description : str,
    sequence : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default plasmid vector with a sequence.
    '''
    plasmid_vector_seq = sbol3.Sequence(f'{name}_seq')
    plasmid_vector_seq.elements= sequence
    plasmid_vector_seq.encoding = 'https://identifiers.org/edam:format_1207'

    plasmid_vector = sbol3.Component(name, sbol3.SBO_DNA)
    plasmid_vector.name = name
    plasmid_vector.description = description
    plasmid_vector.roles. append(tyto.SO.plasmid_vector)
    plasmid_vector.sequences.append(plasmid_vector_seq)
    return plasmid_vector, plasmid_vector_seq

# creating experiments

def media(
    name : str,
    description : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default media.
    '''
    media = sbol3.Component(name, sbol3.SBO_FUNCTIONAL_ENTITY)
    media.name = name
    media.description = description
    media.roles.append(tyto.NCIT.Media)
    return media

def strain(
    name : str,
    description : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default strain.
    '''
    strain = sbol3.Component(name, sbol3.SBO_FUNCTIONAL_ENTITY)
    strain.name = name
    strain.description = description
    strain.roles.append(tyto.NCIT.Strain)
    return strain

def plasmid(
    name : str,
    description : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default plasmid with a sequence.
    '''
    plasmid = sbol3.Component(name, sbol3.SBO_DNA)
    plasmid.name = name
    plasmid.description = description
    plasmid.roles. append(tyto.SO.plasmid)
    #build using sequence or components?
    return plasmid 

def simple_chemical(
    name : str,
    description : str,
    #chemid : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default simple chemical.
    '''
    simple_chemical = sbol3.Component(name, sbol3.SBO_SIMPLE_CHEMICAL)
    simple_chemical.name = name
    simple_chemical.description = description
    return  simple_chemical

def basic_linker(
    name : str,
    description : str,
    sequence : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default basic linker with a sequence.
    '''
    basic_linker_seq = sbol3.Sequence(f'{name}_seq')
    basic_linker_seq.elements= sequence
    basic_linker_seq.encoding = 'https://identifiers.org/edam:format_1207'

    basic_linker = sbol3.Component(name, sbol3.SBO_DNA)
    basic_linker.name = name
    basic_linker.description = description
    #replace with tyto linear and double-stranded
    basic_linker.roles = ['http://identifiers.org/SO:0000987', 'http://identifiers.org/SO:0000985']
    basic_linker.sequences.append(basic_linker_seq)
    return basic_linker, basic_linker_seq

def basic_part(
    name : str,
    description : str,
    sequence : str
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default BASIC part with a sequence.
    '''
    basic_part_seq = sbol3.Sequence(f'{name}_seq')
    basic_part_seq.elements= sequence
    basic_part_seq.encoding = 'https://identifiers.org/edam:format_1207'

    basic_part = sbol3.Component(name, sbol3.SBO_DNA)
    basic_part.name = name
    basic_part.description = description
    #replace with tyto linear and double-stranded
    basic_part.roles = ['http://identifiers.org/SO:0000987', 'http://identifiers.org/SO:0000985']
    basic_part.sequences.append(basic_part_seq)
    return basic_part, basic_part_seq

def basic_clip(
    name : str,
    clip : [] # Linker1, Part, Linker2
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default BASIC Clip with a sequence.
    '''
    basic_clip_seq = sbol3.Sequence(f'{name}_seq')
    # look for sequences on clip
    # get the assembly sequence, reomve overlaping sequences
    # sequence = clip[0].sequence + clip[1].sequence + clip[2].sequence
    basic_clip_seq.elements= sequence
    basic_clip_seq.encoding = 'https://identifiers.org/edam:format_1207'

    basic_clip = sbol3.Component(name, sbol3.SBO_DNA)
    basic_clip.name = name
    basic_clip.description = f'BASIC Clip product from P-linker {clip[0].name}, Part {clip[1]}, S-linker {clip[2]}'
    #replace with tyto linear and double-stranded
    basic_clip.roles = ['http://identifiers.org/SO:0000987', 'http://identifiers.org/SO:0000985']
    basic_clip.sequences.append(basic_clip_seq)
    return basic_clip, basic_clip_seq


def basic_assembly(
    name = str,
    assembly = [] # basic_clip
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default plasmid with a sequence using BASIC Clips.
    '''
    basic_assembly_seq = sbol3.Sequence(f'{name}_seq')
    #look for sequences on assembly
    basic_assembly_seq.elements= sequence
    basic_assembly_seq.encoding = 'https://identifiers.org/edam:format_1207'

    basic_assembly = sbol3.Component(name, sbol3.SBO_DNA)
    basic_assembly.name = name
    basic_assembly.description = description
    basic_assembly.roles. append(tyto.SO.plasmid)    
    basic_assembly.sequences.append(basic_assembly_seq)
    return basic_assembly, basic_assembly_seq

def moclo_assembly(
    name = str,
    assembly = [] # moclo_part
):#-> List[sbol3.TopLevel]:
    '''
    Creates a default plasmid with a sequence using MoClo parts.
    '''
    moclo_assembly_seq = sbol3.Sequence(f'{name}_seq')
    #look for sequences on assembly
    moclo_assembly_seq.elements= sequence
    moclo_assembly_seq.encoding = 'https://identifiers.org/edam:format_1207'

    moclo_assembly = sbol3.Component(name, sbol3.SBO_DNA)
    moclo_assembly.name = name
    moclo_assembly.description = description
    moclo_assembly.roles. append(tyto.SO.plasmid)    
    moclo_assembly.sequences.append(moclo_assembly_seq)
    return moclo_assembly, moclo_assembly_seq

def generate_protocol_ot2(
    # this can be an object
    name : str,
    description : str,
    plasmids = [],
    mag_mod = ['magnetic module', '1'],
    mag_mod_plate = 'nest_96_wellplate_100ul_pcr_full_skirt',
    temp_mod = ['temperature module', '3'],
    temp_mod_block = 'opentrons_24_aluminumblock_nest_1.5ml_snapcap',
    tc_mod = 'thermocycler module',
    tc_mod_plate = 'nest_96_wellplate_100ul_pcr_full_skirt',
):
    # extract parts and URIs from plasmids
    # layout all the parts needed to assemble the plasmids
    # calculate reactive volumes, max volume, etc
    # calculate tips needed
    # define if is a valid protocol
    
    metadata = {
    'protocolName': name, # example 'Automated Golden Gate'
    'author': 'Gonzalo_Vidal <gsvidal@uc.cl>', # discuss ways to obtain this
    'description': description, # generate description like 'Golden Gate automated using OT2 generated by SECO'
    'apiLevel': '2.10' # stablish apilevel
}

    # protocol run function. the part after the colon lets your editor know
    # where to look for autocomplete suggestions
    # modules needs a gen, review invoice!

    # input or detect assembly estrategy moclo or basic or gibson
    assembly_strategy = 'MoClo' 
    # check assembly strategy with part sequences
    if assembly_strategy == 'MoClo':
        # generate MoClo assembly, see if necesary mulptiple protocols to include purification and transformation 
        def run(protocol: protocol_api.ProtocolContext):
            # get variables into the function

            # labware
            mag_mod = protocol.load_module(mag_mod[0], mag_mod[1])
            mag_mod_plate = mag_mod.load_labware(mag_mod_plate)

            temp_mod = protocol.load_module(temp_mod[0], temp_mod[1])
            temp_mod_block = temp_mod.load_labware(temp_mod_block)

            tc_mod = protocol.load_module(tc_mod) 
            tc_mod_plate = tc_mod.load_labware(tc_mod_plate)
            #by default on slots 7,8,10,11

            #plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '6')
            tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', '9')
            
            # pipettes
            left_pipette = protocol.load_instrument(
                'p20_single_gen2', 'left', tip_racks=[tiprack])

            # reactives
            bsai = temp_mod_block['A1']
            t4_DNA_lig = temp_mod_block['A2']
            t4_buffer = temp_mod_block['A3']
            dd_H2O = temp_mod_block['A4']

            # parts

            prom = temp_mod_block['B1'] # Add URI
            rbs = temp_mod_block['B2'] # Add URI
            cds = temp_mod_block['B3'] # Add URI
            term = temp_mod_block['B4'] # Add URI
            acc_vec = temp_mod_block['B5'] # Add URI

            # volumes (can be a function of [DNA]) min vol = 1 uL
            volume_total = 10

            # all parts should be in the needed concentration to pick 1 uL
            volume_part = 1 #set all parts to equal [] or dynamic?
            number_parts = 5
            #volume_acc_vec = 0.50
            #volume_prom = 0.50
            #volume_rbs = 0.50
            #volume_cds = 0.50
            #volume_term = 0.50
            volume_parts = volume_part * number_parts #volume_acc_vec + volume_prom + volume_rbs + volume_cds + volume_term

            # make 10 uL (or necesary to be aspirated) of a .5 dilution
            volume_bsai = 1 # 0.50
            volume_t4_DNA_lig = 1 # 0.50
            volume_t4_buffer = 2 # 1
            volume_reactives = volume_bsai + volume_t4_DNA_lig + volume_t4_buffer
            volume_dd_H2O = volume_total - (volume_parts + volume_reactives) # if less than 1 error
            
            # assemblies
            assemblies = []
            #replicates = 3
            tu1 = [prom, rbs, cds, term, acc_vec]
            assemblies.append(tu1)

            # setup
            temp_mod.set_temperature(4) #puases protocol until temperature is reached
            tc_mod.open_lid()
            tc_mod.set_block_temperature(4)
            #left_pipette.flow_rate.aspirate = 3.78
            #left_pipette.flow_rate.dispense = 3.78

            # By default, the OT-2 will aspirate and dispense 1mm above the bottom of a well.


            # commands master mix
            for i in range(len(assemblies)):
                left_pipette.pick_up_tip()
                left_pipette.aspirate(volume_dd_H2O, dd_H2O)
                left_pipette.dispense(volume_dd_H2O, tc_mod_plate['B2']) # define where in the tc
                left_pipette.drop_tip()

                left_pipette.pick_up_tip()
                left_pipette.aspirate(volume_t4_buffer, dd_H2O)
                left_pipette.dispense(volume_t4_buffer, tc_mod_plate['B2']) # define where in the tc
                left_pipette.drop_tip()

                left_pipette.pick_up_tip()
                left_pipette.aspirate(volume_t4_DNA_lig, t4_DNA_lig)
                left_pipette.dispense(volume_t4_DNA_lig, tc_mod_plate['B2']) # define where in the tc
                left_pipette.drop_tip()

                left_pipette.pick_up_tip()
                left_pipette.aspirate(volume_bsai, bsai)
                left_pipette.dispense(volume_bsai, tc_mod_plate['B2']) # define where in the tc
                left_pipette.drop_tip()
            for tu in assemblies:
                for part in tu:
                    left_pipette.pick_up_tip()
                    left_pipette.aspirate(volume_part, part)
                    left_pipette.dispense(volume_part, tc_mod_plate['B2']) # define where in the tc
                    left_pipette.drop_tip()

            # thermocycler

            # check tc status if statement can be added
            tc_mod.lid_temperature_status
            tc_mod.block_temperature_status
            tc_mod.set_lid_temperature(45)

            tc_mod.close_lid()

            # cycles
            profile = [
                {'temperature': 42, 'hold_time_minutes': 2},
                {'temperature': 16, 'hold_time_minutes': 5}]
            tc_mod.execute_profile(steps=profile, repetitions=30, block_max_volume=30)

            profile = [
                {'temperature': 60, 'hold_time_minutes': 10},
                {'temperature': 80, 'hold_time_minutes': 10}]
            tc_mod.execute_profile(steps=profile, repetitions=1, block_max_volume=30)

            tc_mod.open_lid()
            tc_mod.set_block_temperature(4)
    return run



#plate_reader
#flow_cytometer
#96_well_plate
#OT-2
# implement()