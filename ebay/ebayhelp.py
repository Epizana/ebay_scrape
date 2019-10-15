import pandas as pd
import numpy as np

def ebay_helper(ebay1):
    
    ebay1.loc[ebay1['bids'] == 0, 'format'] = 'BIN'
    ebay1.loc[ebay1['bids'] > 0, 'format'] = 'Auction'
    ebay1['brand']=ebay1['brand'].fillna('Unspecified')
    ebay1['title']=ebay1['title'].str.lower()
    
    #Process Hasbro
    hasre='Hasbro|hasbro|HASBRO|Toy Biz|Transformers|G1|ToyBiz|G.I. Joe|GI Joe|Hasbri|HABRO|H a s b r o'
    ebay1['brand'] = np.where(ebay1['brand'].str.contains(hasre,regex = True), 'Hasbro',ebay1['brand'])
    
    #Process Mattel
    matre = 'Mattel|MATTEL|Barbie|Masters of the Universe|Matel|motu|MOTU'
    ebay1['brand'] = np.where(ebay1['brand'].str.contains(matre,regex = True), 'Mattel',ebay1['brand'])
    
    #Process more brands: McFarlane
    macre = 'Mcfarlane|McFarlane'
    ebay1['brand'] = np.where(ebay1['brand'].str.contains(macre, regex = True), 'McFarlane Toys',\
    ebay1['brand'])
    
    #Process more brands: Playmates
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('Playmates|PLAYMATES', regex = True),\
    'Playmates Toys',ebay1['brand'])
    
    #Process more brands: Takara Tomy
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('TAKARA|Takara|takara|TOMY|Tomy',\
    regex = True), 'Takara TOMY',ebay1['brand'])
    
    #Process more brands: Bandai
    banre = 'Bandai|BANDAI|Tamashii Nations|SHF|Figuarts'
    ebay1['brand'] = np.where(ebay1['brand'].str.contains(banre, regex = True), 'Bandai',ebay1['brand'])
    
    #Process more brands: DC
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('DC'), 'DC',ebay1['brand'])
    
    #Process more brands: Fisher Price
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('Fisher Price|Fisher-Price|FISHER PRICE',\
    regex = True), 'Fisher Price',ebay1['brand'])
    
    #Process more brands: Funko
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('FUNKO|Funko',regex = True),\
    'Funko',ebay1['brand'])
    
    #Process more brands: Jakks
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('JAKKS|Jakks',regex = True),\
    'Jakks Pacific',ebay1['brand'])
    
    #Process more brands: Sideshow
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('Slideshow|Sideshow|SIDESHOW',regex = True),\
    'Sideshow Collectibles',ebay1['brand'])
    
    #Process more brands: Diamond
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('DIAMOND|Diamond',regex = True),\
    'Diamond Select',ebay1['brand'])
    
    #Process more brands: WWE
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('WWE|WWF',regex = True),\
    'WWE',ebay1['brand'])
    
    #Process more brands: Kenner
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('Kenner'), 'Kenner',ebay1['brand'])
    
    #Process more brands: Medicom
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('MEDICOM|Medicom|Medicos', regex = True),\
    'MEDICOM',ebay1['brand'])
    
    #Process more brands: Hot Toys
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('HOT TOYS|Hot Toys', regex = True),\
    'Hot Toys',ebay1['brand'])
    
    #Process more brands: Mezco
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('Mezco'), 'Mezco',ebay1['brand'])
    
    #Process more brands: NECA
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('NECA|NEC|neca', regex = True),\
    'NECA',ebay1['brand'])
    
    #Process more brands: Star Wars
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('Star Wars'), 'Star Wars', ebay1['brand'])
    
    #Process more brands: Unbranded
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('Unbranded|Unbrand|UNBRANDED|Unbrander',\
    regex = True), 'Unbranded', ebay1['brand'])
    
    #Process more brands: Fanstoys
    fanre = 'Fan Toys|Fans Toys|Fanstoys|Fan toys|Fans toys'
    ebay1['brand'] = np.where(ebay1['brand'].str.contains(fanre, regex = True),'Fanstoys',\
    ebay1['brand'])
    
    #Process more brands: Super7
    suprex = 'Super7|Super 7'
    ebay1['brand'] = np.where(ebay1['brand'].str.contains(suprex,regex = True),'Super7',ebay1['brand'])
                              
    #Process more brands: Marvel
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('Marvel|MARVEL', regex = True),\
    'Marvel', ebay1['brand'])
    
    #Process more brands: X-Plus
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('X- Plus|X-Plus', regex = True),\
    'X-Plus', ebay1['brand'])
                              
    #Process more brands: Maketoys
    ebay1['brand'] = np.where(ebay1['brand'].str.contains('Make Toys|Maketoys', regex = True),\
    'Maketoys', ebay1['brand'])
    