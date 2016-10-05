from util import hook
from PIL import Image, ImageDraw, ImageFont
import os
import random
import base64
import requests
import json
from imgurpython import ImgurClient
import pycorpora

t_interps = pycorpora.get_file('divination', 'tarot_interpretations')
card_names = []
card_keywords = []
card_lmeaning = []
card_dmeaning = [] 


def organizesomeshit(position):
    global card_names
    global card_keywords
    global card_lmeaning
    global card_dmeaning
    
    keywords = ", ".join(card_keywords[position])
    keywords = "Keywords: "+keywords

    lmeanings = ", ".join(card_lmeaning[position][0:2])

    dmeanings = ", ".join(card_dmeaning[position][0:2])

    lmeanings = "[+] Meanings: "+lmeanings
    dmeanings = "[-] Meanings: "+dmeanings
    #return keywords
    return keywords,lmeanings, dmeanings

    
def rendertext(img):
    global card_names
    global card_keywords
    global card_lmeaning
    global card_dmeaning
    font = ImageFont.truetype("plugins/ARLRDBD.TTF", 45)
    draw = ImageDraw.Draw(img)
    
    carrierfeed=20
    counter = 1

    position_description = ["Position 1: The central issue or fundamental problem.","Position 2: The opposing factor to Position 1.", "Position 3: The root cause or source.", "Position 4: Past influence.", "Position 5: Attitude and beliefs.", "Position 6: Future influence.", "Position 7: You as you are.", "Position 8: That which surrounds you, environment.","Position 9: Source of guidance.", "Position 10: Overall outcome."]
    
    for i in range(0,10):
        card = card_names[i]
        position = organizesomeshit(i)
        pd = position_description[i] + "--" +card.upper()
        draw.text((1750, carrierfeed), str(pd), (255,255,255), font=font)
        carrierfeed +=50
        draw.text((1750, carrierfeed), str(position[0]), (255,255,255), font=font)
        carrierfeed+=40
        #draw.text((1750, carrierfeed), str(position[1]), (255,255,255), font=font)
        #carrierfeed += 30
        #draw.text((1750, carrierfeed), str(position[2]), (255,255,255), font=font)
        #carrierfeed += 40
        draw.text((1750, carrierfeed), " ", (255,255,255), font=font)
        carrierfeed += 50
        counter += 1
    return 
    
    
def meaning_cleanup(card1, card2):
    global card_names
    global card_keywords
    global card_lmeaning
    global card_dmeaning
    C_first = card_names[card1]
    lmeaning = random.choice(card_lmeaning[card1])
    dmeaning = random.choice(card_dmeaning[card1])
    c1meaning = []
    c1meaning.append(lmeaning)
    c1meaning.append(dmeaning)
    final_meaning1 = random.choice(c1meaning)
    C_second = card_names[card2]
    lmeaning = random.choice(card_lmeaning[card2])
    dmeaning = random.choice(card_dmeaning[card2])
    c2meaning = []
    c2meaning.append(lmeaning)
    c2meaning.append(dmeaning)
    final_meaning2 = random.choice(c2meaning)
    return final_meaning1, final_meaning2   
    
    
def rendertext2(img):
    global card_names
    global card_keywords
    global card_lmeaning
    global card_dmeaning
    font = ImageFont.truetype("plugins/ARLRDBD.TTF", 45)
    draw = ImageDraw.Draw(img)
        
    carrierfeed=1500
    title_comp1 = 'The Central Dynamic | '+card_names[0].upper()+" & "+card_names[1].upper() + ":"
    final = meaning_cleanup(0,1)
    comp1 = 'How does '+final[0].lower()+" relate with..."
    comp1a = final[1].lower()+"?"
    
    final = meaning_cleanup(2,4)
    title_comp2 = 'Your Internal Struggle | '+card_names[2].upper()+" & "+card_names[4].upper() + ":"
    comp2 = 'How does '+final[0].lower()+" relate with..."
    comp2a = final[1].lower()+"?"
    
    final = meaning_cleanup(3,5)
    title_comp3 = 'The Flow of Events | '+card_names[3].upper()+" & "+card_names[5].upper() + ":"
    comp3 = 'How does '+final[0].lower()+" relate with..."
    comp3a = final[1].lower()+"?"
    
    final = meaning_cleanup(6,7)
    title_comp4 = 'Your Environmental Relationship | '+card_names[6].upper()+" & "+card_names[7].upper() + ":"
    comp4 = 'How does '+final[0].lower()+" relate with..."
    comp4a = final[1].lower()+"?"
    
    final = meaning_cleanup(5,9)
    title_comp5 = 'Near Future vs. Alt. Outcome | '+card_names[5].upper()+" & "+card_names[9].upper() + ":"
    comp5 = 'How does '+final[0].lower()+" relate with..."
    comp5a = final[1].lower()+"?"
    
    draw.text((1750, carrierfeed), str(title_comp1), (255,255,255), font=font)
    carrierfeed +=50
    draw.text((1750, carrierfeed), str(comp1), (255,255,255), font=font)
    carrierfeed +=50
    draw.text((1750, carrierfeed), str(comp1a), (255,255,255), font=font)
    carrierfeed +=70
    
    draw.text((1750, carrierfeed), str(title_comp2), (255,255,255), font=font)
    carrierfeed +=50
    draw.text((1750, carrierfeed), str(comp2), (255,255,255), font=font)
    carrierfeed +=50
    draw.text((1750, carrierfeed), str(comp2a), (255,255,255), font=font)    
    carrierfeed +=70
    
    draw.text((1750, carrierfeed), str(title_comp3), (255,255,255), font=font)
    carrierfeed +=50
    draw.text((1750, carrierfeed), str(comp3), (255,255,255), font=font)
    carrierfeed +=50
    draw.text((1750, carrierfeed), str(comp3a), (255,255,255), font=font)    
    carrierfeed +=70
    
    draw.text((1750, carrierfeed), str(title_comp4), (255,255,255), font=font)
    carrierfeed +=50
    draw.text((1750, carrierfeed), str(comp4), (255,255,255), font=font)
    carrierfeed +=50
    draw.text((1750, carrierfeed), str(comp4a), (255,255,255), font=font)    
    carrierfeed +=70
    
    draw.text((1750, carrierfeed), str(title_comp5), (255,255,255), font=font)
    carrierfeed +=50
    draw.text((1750, carrierfeed), str(comp5), (255,255,255), font=font)
    carrierfeed +=50    
    draw.text((1750, carrierfeed), str(comp5a), (255,255,255), font=font)
    return
    
def carddata(inp):
    global card_names
    global card_keywords
    global card_lmeaning
    global card_dmeaning
    cd = [i.strip(".jpg") for i in inp]
    card_names = [t_interps['tarot_interpretations'][int(i)]['name'] for i in cd]
    card_keywords = [t_interps['tarot_interpretations'][int(i)]['keywords'] for i in cd]
    card_lmeaning = [t_interps['tarot_interpretations'][int(i)]['meanings']['light'] for i in cd]
    card_dmeaning = [t_interps['tarot_interpretations'][int(i)]['meanings']['shadow'] for i in cd]
    return card_names

    
@hook.command('tarot', autohelp=False) 
def tarot(inp):
    '!tarot - Provides a random tarot spread. '
    global card_names
    global card_keywords
    panelwidth = 2000*2
    panelheight = 2400
    cardlist=[i for i in os.listdir('./plugins/cards')]
    randsamp=random.sample(cardlist, 10)
    card_names = carddata(randsamp)
    print card_names
    #print randsamp
    #print card_names
    im = Image.new("RGBA", (panelwidth, panelheight), ("black"))
    rendertext(im)
    im1 = Image.open("./plugins/cards/"+str(randsamp[0]))
    im2 = Image.open("./plugins/cards/"+str(randsamp[1]))
    im3 = Image.open("./plugins/cards/"+str(randsamp[2]))
    im4 = Image.open("./plugins/cards/"+str(randsamp[3]))
    im5 = Image.open("./plugins/cards/"+str(randsamp[4]))
    im6 = Image.open("./plugins/cards/"+str(randsamp[5]))
    im7 = Image.open("./plugins/cards/"+str(randsamp[6]))
    im8 = Image.open("./plugins/cards/"+str(randsamp[7]))
    im9 = Image.open("./plugins/cards/"+str(randsamp[8]))
    im10 = Image.open("./plugins/cards/"+str(randsamp[9]))
    
    im2 = im2.rotate(270)
    rendertext2(im)
    im.paste(im5, (525, 350))
    im.paste(im1, (525,950))
    im.paste(im3, (525,1550))
    im.paste(im4, (175,950))
    im.paste(im6, (875, 950))
    im.paste(im10, (1375, 0)) 
    im.paste(im9, (1375, 600))
    im.paste(im8, (1375, 1200))
    im.paste(im7, (1375, 1800))
    im.paste(im2, (400, 1075))
    
    im.save('tarot.jpg')
   
   
    
    basewidth = 1150
    img = Image.open("./tarot.jpg")
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save("resized_image.jpg")
    image_path= "./resized_image.jpg"
    client_id = 'cb63be4ff89eb57'
    client_secret = '63112dbe4862926af3ac2da563cb2162e1e5ea15'
    client = ImgurClient(client_id, client_secret)
    ihavenoidea = client.upload_from_path(image_path, config=None, anon=True)
    link=ihavenoidea['link']
    
    return "Your reading is here: "+ link
