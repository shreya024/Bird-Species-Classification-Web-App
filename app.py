import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('./bird_classification_new_model.h5')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()

st.write("""
         # Bird Classification
         """
         )

file = st.file_uploader("Please upload an brain scan file", type=["jpg", "png"])
import cv2
from PIL import Image, ImageOps
import numpy as np
st.set_option('deprecation.showfileUploaderEncoding', False)

classes = ['WATTLED CURASSOW', 'CARMINE BEE-EATER', 'GAMBELS QUAIL', 'UMBRELLA BIRD', 'AMERICAN KESTREL', 'AMERICAN GOLDFINCH', 'DUSKY LORY', 'BLACK THROATED WARBLER', 'YELLOW CACIQUE', 'STRIPPED SWALLOW', 'VERMILION FLYCATHER', 'CAPE MAY WARBLER', 'RED TAILED HAWK', 'GURNEYS PITTA', 'INDIAN ROLLER', 'AZURE TANAGER', 'GREEN MAGPIE', 'BANDED BROADBILL', 'GREY PLOVER', 'TOUCHAN', 'HYACINTH MACAW', 'HARLEQUIN DUCK', 'ABYSSINIAN GROUND HORNBILL', 'CALIFORNIA QUAIL', 'BALD IBIS', 'RUBY THROATED HUMMINGBIRD', 'INDIGO BUNTING', 'ALBERTS TOWHEE', 'SORA', 'HOODED MERGANSER', 'CAPE ROCK THRUSH', 'BLUE COAU', 'CALIFORNIA CONDOR', 'BORNEAN PHEASANT', 'BARN SWALLOW', 'TAIWAN MAGPIE', 'SPLENDID WREN', 'BLACK THROATED BUSHTIT', 'CHINESE POND HERON', 'AFRICAN EMERALD CUCKOO', 'COMMON LOON', 'COMMON POORWILL', 'FIORDLAND PENGUIN', 'SUPERB STARLING', 'CUBAN TODY', 'TASMANIAN HEN', 'BLACK SWAN', 'WATTLED LAPWING', 'RED NAPED TROGON', 'AMERICAN PIPIT', 'EASTERN TOWEE', 'GYRFALCON', 'BLACK SKIMMER', 'RED BEARDED BEE EATER', 'ALBATROSS', 'SPOONBILL', 'MASKED LAPWING', 'MALABAR HORNBILL', 'OCELLATED TURKEY', 'PEREGRINE FALCON', 'CHINESE BAMBOO PARTRIDGE', 'IBISBILL', 'ROSY FACED LOVEBIRD', 'GREATOR SAGE GROUSE', 'CHATTERING LORY', 'HORNBILL', 'RUFOUS KINGFISHER', 'JABIRU', 'RED HONEY CREEPER', 'GREAT KISKADEE', 'GRAY KINGBIRD', 'GUINEAFOWL', 'NORTHERN MOCKINGBIRD', 'MALLARD DUCK', 'GILA WOODPECKER', 'MASKED BOOBY', 'AMERICAN BITTERN', 'CALIFORNIA GULL', 'CASPIAN TERN', 'EMERALD TANAGER', 'BANDED PITA', 'AZURE JAY', 'BARRED PUFFBIRD', 'ELEGANT TROGON', 'SNOWY EGRET', 'EUROPEAN TURTLE DOVE', 'CRESTED SHRIKETIT', 'SATYR TRAGOPAN', 'GANG GANG COCKATOO', 'AMETHYST WOODSTAR', 'RED HEADED WOODPECKER', 'MIKADO  PHEASANT', 'FIRE TAILLED MYZORNIS', 'SWINHOES PHEASANT', 'PARADISE TANAGER', 'OVENBIRD', 'MOURNING DOVE', 'BROWN NOODY', 'WALL CREAPER', 'ORIENTAL BAY OWL', 'DOWNY WOODPECKER', 'EMPEROR PENGUIN', 'WHITE TAILED TROPIC', 'OSPREY', 'HOUSE FINCH', 'AMERICAN COOT', 'GOLDEN PIPIT', 'PUFFIN', 'ARARIPE MANAKIN', 'RUDY KINGFISHER', 'BLACK-CAPPED CHICKADEE', 'PELICAN', 'ABBOTTS BABBLER', 'GREEN BROADBILL', 'KAKAPO', 'RAZORBILL', 'BLACK BAZA', 'ANTILLEAN EUPHONIA', 'BEARDED REEDLING', 'BELTED KINGFISHER', 'KILLDEAR', 'HELMET VANGA', 'BAR-TAILED GODWIT', 'CRESTED OROPENDOLA', 'STRIPPED MANAKIN', 'CAPE LONGCLAW', 'CREAM COLORED WOODPECKER', 'YELLOW BELLIED FLOWERPECKER', 'RED TAILED THRUSH', 'STEAMER DUCK', 'RED BELLIED PITTA', 'GRAY CATBIRD', 'GUINEA TURACO', 'RED WISKERED BULBUL', 'PATAGONIAN SIERRA FINCH', 'PHILIPPINE EAGLE', 'RED FODY', 'ANHINGA', 'BRANDT CORMARANT', 'SPOON BILED SANDPIPER', 'VULTURINE GUINEAFOWL', 'ENGGANO MYNA', 'BIRD OF PARADISE', 'LILAC ROLLER', 'BAIKAL TEAL', 'CINNAMON ATTILA', 'BANANAQUIT', 'CHUKAR PARTRIDGE', 'CRIMSON CHAT', 'EASTERN GOLDEN WEAVER', 'CACTUS WREN', 'BALD EAGLE', 'CAPE GLOSSY STARLING', 'NICOBAR PIGEON', 'KIWI', 'AFRICAN FIREFINCH', 'CRESTED NUTHATCH', 'GOLD WING WARBLER', 'WHITE BROWED CRAKE', 'COCKATOO', 'BLUE THROATED TOUCANET', 'EMU', 'FAIRY TERN', 'HARPY EAGLE', 'ANDEAN SISKIN', 'DOUBLE EYED FIG PARROT', 'CUBAN TROGON', 'VIOLET TURACO', 'BLONDE CRESTED WOODPECKER', 'ASHY THRUSHBIRD', 'BLUE HERON', 'EURASIAN MAGPIE', 'RED WINGED BLACKBIRD', 'BORNEAN BRISTLEHEAD', 'STRAWBERRY FINCH', 'CHESTNET BELLIED EUPHONIA', 'IBERIAN MAGPIE', 'SCARLET CROWNED FRUIT DOVE', 'ORANGE BRESTED BUNTING', 'SCARLET TANAGER', 'ANDEAN LAPWING', 'MAGPIE GOOSE', 'WHITE THROATED BEE EATER', 'TROPICAL KINGBIRD', 'BLACK FRANCOLIN', 'COLLARED ARACARI', 'CRESTED AUKLET', 'GLOSSY IBIS', 'NORTHERN CARDINAL', 'KAGU', 'PURPLE FINCH', 'ANDEAN GOOSE', 'HORNED SUNGEM', 'MYNA', 'COMMON HOUSE MARTIN', 'EURASIAN GOLDEN ORIOLE', 'NORTHERN SHOVELER', 'AVADAVAT', 'PARAKETT  AKULET', 'ANTBIRD', 'POMARINE JAEGER', 'APOSTLEBIRD', 'COPPERY TAILED COUCAL', 'ALEXANDRINE PARAKEET', 'CEDAR WAXWING', 'KING VULTURE', 'SAND MARTIN', 'SMITHS LONGSPUR', 'ALPINE CHOUGH', 'PYGMY KINGFISHER', 'GOULDIAN FINCH', 'CROW', 'HAMMERKOP', 'BROWN CREPPER', 'NOISY FRIARBIRD', 'CERULEAN WARBLER', 'WHITE CHEEKED TURACO', 'BARN OWL', 'STRIPED OWL', 'TAILORBIRD', 'IVORY GULL', 'OSTRICH', 'ROUGH LEG BUZZARD', 'RAINBOW LORIKEET', 'BAND TAILED GUAN', 'APAPANE', 'HIMALAYAN BLUETAIL', 'PARUS MAJOR', 'LONG-EARED OWL', 'CRESTED FIREBACK', 'MARABOU STORK', 'BLACK TAIL CRAKE', 'INCA TERN', 'PAINTED BUNTING', 'EASTERN BLUEBIRD', 'PALILA', 'HOOPOES', 'OKINAWA RAIL', 'CHIPPING SPARROW', 'ANNAS HUMMINGBIRD', 'CINNAMON TEAL', 'ROBIN', 'VENEZUELIAN TROUPIAL', 'HEPATIC TANAGER', 'MALEO', 'IWI', 'WHITE NECKED RAVEN', 'PINK ROBIN', 'BOBOLINK', 'MANDRIN DUCK', 'RED BROWED FINCH', 'NORTHERN PARULA', 'AMERICAN AVOCET', 'EVENING GROSBEAK', 'RED HEADED DUCK', 'TREE SWALLOW', 'COMMON GRACKLE', 'SCARLET MACAW', 'HORNED GUAN', 'CAPUCHINBIRD', 'CROWNED PIGEON', 'MANGROVE CUCKOO', 'CRAB PLOVER', 'CINNAMON FLYCATCHER', 'WILD TURKEY', 'VIOLET GREEN SWALLOW', 'BUSH TURKEY', 'LESSER ADJUTANT', 'GREEN JAY', 'ALTAMIRA YELLOWTHROAT', 'BEARDED BELLBIRD', 'FLAME BOWERBIRD', 'RUFUOS MOTMOT', 'CRESTED KINGFISHER', 'NORTHERN JACANA', 'ROADRUNNER', 'BLUE GROUSE', 'CAPPED HERON', 'TEAL DUCK', 'DARK EYED JUNCO', 'CLARKS NUTCRACKER', 'GILDED FLICKER', 'FLAMINGO', 'CHUCAO TAPACULO', 'BALI STARLING', 'GREAT GRAY OWL', 'ROCK DOVE', 'CHARA DE COLLAR', 'TOWNSENDS WARBLER', 'D-ARNAUDS BARBET', 'OYSTER CATCHER', 'VARIED THRUSH', 'SRI LANKA BLUE MAGPIE', 'LARK BUNTING', 'DOUBLE BARRED FINCH', 'FAIRY BLUEBIRD', 'CRIMSON SUNBIRD', 'HARLEQUIN QUAIL', 'HOUSE SPARROW', 'CRESTED CARACARA', 'NORTHERN GANNET', 'SCARLET IBIS', 'MALACHITE KINGFISHER', 'INDIAN PITTA', 'EASTERN MEADOWLARK', 'REGENT BOWERBIRD', 'WILSONS BIRD OF PARADISE', 'COMMON IORA', 'SHORT BILLED DOWITCHER', 'BLACK-THROATED SPARROW', 'NORTHERN FLICKER', 'BANDED STILT', 'PURPLE GALLINULE', 'CANARY', 'TAKAHE', 'JANDAYA PARAKEET', 'FLAME TANAGER', 'CURL CRESTED ARACURI', 'RED FACED CORMORANT', 'GREAT JACAMAR', 'ROYAL FLYCATCHER', 'NORTHERN FULMAR', 'EARED PITA', 'BULWERS PHEASANT', 'HORNED LARK', 'HAWFINCH', 'COCK OF THE  ROCK', 'TIT MOUSE', 'GRAY PARTRIDGE', 'ANIANIAU', 'WOOD DUCK', 'GROVED BILLED ANI', 'RED FACED WARBLER', 'HIMALAYAN MONAL', 'DEMOISELLE CRANE', 'CRESTED COUA', 'QUETZAL', 'NORTHERN GOSHAWK', 'GOLDEN CHLOROPHONIA', 'PURPLE SWAMPHEN', 'COMMON FIRECREST', 'TURQUOISE MOTMOT', 'CASSOWARY', 'INDIAN BUSTARD', 'KOOKABURRA', 'SANDHILL CRANE', 'RING-NECKED PHEASANT', 'EASTERN ROSELLA', 'PURPLE MARTIN', 'VICTORIA CROWNED PIGEON', 'SHOEBILL', 'SNOWY OWL', 'AFRICAN CROWNED CRANE', 'GREAT POTOO', 'STORK BILLED KINGFISHER', 'GOLDEN PHEASANT', 'AFRICAN OYSTER CATCHER', 'ASIAN CRESTED IBIS', 'LITTLE AUK', 'BLACK-NECKED GREBE', 'ABBOTTS BOOBY', 'BALTIMORE ORIOLE', 'COMMON STARLING', 'JAPANESE ROBIN', 'BLACKBURNIAM WARBLER', 'WHIMBREL', 'YELLOW HEADED BLACKBIRD', 'SPOTTED CATBIRD', 'BLACK COCKATO', 'SPANGLED COTINGA', 'MALAGASY WHITE EYE', 'HAWAIIAN GOOSE', 'PEACOCK', 'BEARDED BARBET', 'TURKEY VULTURE', 'JACK SNIPE', 'BLACK VULTURE', 'BROWN THRASHER', 'GOLDEN CHEEKED WARBLER', 'DOUBLE BRESTED CORMARANT', 'JAVA SPARROW', 'BAY-BREASTED WARBLER', 'AZURE TIT', 'BLACK & YELLOW  BROADBILL', 'HOATZIN', 'GO AWAY BIRD', 'ELLIOTS  PHEASANT', 'IMPERIAL SHAQ', 'BARROWS GOLDENEYE', 'FRIGATE', 'TRUMPTER SWAN', 'INLAND DOTTEREL', 'SAMATRAN THRUSH', 'BORNEAN LEAFBIRD', 'LAZULI BUNTING', 'EUROPEAN GOLDFINCH', 'AMERICAN REDSTART', 'CRANE HAWK', 'NORTHERN RED BISHOP', 'GOLDEN EAGLE']
def import_and_predict(image_data, model):
    
        img_size=(224,224)
        image = ImageOps.fit(image_data, img_size, Image.ANTIALIAS)
        img = cv2.resize(image, img_size)
        img = np.expand_dims(img, axis=0)
    
        prediction = model.predict(img)
        
        return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    score = tf.nn.softmax(predictions[0])
    st.write(predictions)
    st.write(score)
    index = np.argmax(predictions[0])
    class = classes[index]
    probability = predictions[0][index]*100
    print(
    "This image most likely belongs to {class} with a {probability:.2f} percent confidence."
)
