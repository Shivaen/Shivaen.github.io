#!/usr/bin/env python3
"""
Run this script once to look up precise coordinates for every restaurant
and update your index.html with accurate pin locations.

Usage:
  pip install requests
  python3 geocode_restaurants.py

You need a free Google Maps Geocoding API key:
  https://console.cloud.google.com/google/maps-apis/credentials
  Enable "Geocoding API" (free for small volumes)
"""

import json, time, re, sys
import urllib.request, urllib.parse

API_KEY = "AIzaSyD8a1YAI-LOooNvlKPU17SrFx94oFUrHIw"  # Replace this

HTML_FILE = "index.html"  # Path to your HTML file

RESTAURANTS = [
  ("4505 Burgers & BBQ", "705 Divisadero St, San Francisco, CA"),
  ("A La Turca", "A La Turca restaurant, San Francisco, CA"),
  ("Aaha Indian Cuisine", "Aaha Indian Cuisine, Mission, San Francisco, CA"),
  ("Akikos Sushi Bar", "431 Bush St, San Francisco, CA"),
  ("Akira Japanese Restaurant", "Akira Japanese Restaurant, Japantown, San Francisco, CA"),
  ("Al Carajo", "Al Carajo, Mission, San Francisco, CA"),
  ("Alimentos", "Alimentos, North Beach, San Francisco, CA"),
  ("Amoura", "Amoura restaurant, South San Francisco, CA"),
  ("Anthony's Cookies", "Anthony\'s Cookies, Mission, San Francisco, CA"),
  ("AP's Cafe", "AP\'s Cafe, Noe Valley, San Francisco, CA"),
  ("Aria", "Aria Korean, Nob Hill, San Francisco, CA"),
  ("Arizmendi", "Arizmendi Bakery, Mission, San Francisco, CA"),
  ("Arsicault", "Arsicault Bakery, 397 Arguello Blvd, San Francisco, CA"),
  ("Aziza", "Aziza restaurant, 5800 Geary Blvd, San Francisco, CA"),
  ("B. Patisserie", "B. Patisserie, 2821 California St, San Francisco, CA"),
  ("Bahn Mi Viet", "Bahn Mi Viet, Alamo Square, San Francisco, CA"),
  ("Bansang", "Bansang, Japantown, San Francisco, CA"),
  ("Basa Seafood Express", "Basa Seafood Express, Mission, San Francisco, CA"),
  ("Base Camp", "Base Camp restaurant, Union Square, San Francisco, CA"),
  ("Beeps Burgers", "Beep\'s Burgers, 1051 Ocean Ave, San Francisco, CA"),
  ("Beit Rima", "Beit Rima, 138 Church St, San Francisco, CA"),
  ("Besharam", "Besharam restaurant, 1275 Minnesota St, San Francisco, CA"),
  ("Big Apple Pizza N Grill", "Big Apple Pizza, Tenderloin, San Francisco, CA"),
  ("Bodega North Beach", "Bodega SF, North Beach, San Francisco, CA"),
  ("Bones Bagels", "Bones Bagels, Noe Valley, San Francisco, CA"),
  ("Bottega", "Bottega SF, Mission, San Francisco, CA"),
  ("Breadbelly", "Breadbelly, 353 Arguello Blvd, San Francisco, CA"),
  ("Breakfast Little", "Breakfast Little, Mission, San Francisco, CA"),
  ("Brenda's French Soul Food", "Brenda\'s French Soul Food, 652 Polk St, San Francisco, CA"),
  ("Brothers Restaurant", "Brothers Korean BBQ, Richmond, San Francisco, CA"),
  ("Burma Love", "Burma Love, Valencia St, San Francisco, CA"),
  ("Buster's Cheesesteaks", "Buster\'s Cheesesteaks, North Beach, San Francisco, CA"),
  ("Capital Restaurant", "Capital Restaurant, Chinatown, San Francisco, CA"),
  ("Capo", "Capo pizza, North Beach, San Francisco, CA"),
  ("Caseys Pizza", "Casey\'s Pizza, Mission Bay, San Francisco, CA"),
  ("Cheeseboard Collective", "Cheeseboard Pizza Collective, 1512 Shattuck Ave, Berkeley, CA"),
  ("Cheung Hing", "Cheung Hing BBQ, Clement St, San Francisco, CA"),
  ("Chicken G's", "Chicken G\'s, FiDi, San Francisco, CA"),
  ("China Live", "China Live, 644 Broadway, San Francisco, CA"),
  ("Cholita Linda's", "Cholita Linda, Ferry Building, San Francisco, CA"),
  ("Chong Qing Xiao Mian", "Chong Qing Xiao Mian, North Beach, San Francisco, CA"),
  ("Chubby Noodle", "Chubby Noodle, North Beach, San Francisco, CA"),
  ("Ciccio", "Ciccio restaurant, Yountville, CA"),
  ("Cocobang", "Cocobang, Tenderloin, San Francisco, CA"),
  ("Copra", "Copra restaurant, 1700 Post St, San Francisco, CA"),
  ("Cordon Bleu", "Le Cordon Bleu, California St, Nob Hill, San Francisco, CA"),
  ("Cracked and Battered", "Cracked and Battered, Potrero Hill, San Francisco, CA"),
  ("Crepevine", "Crepevine, Burlingame, CA"),
  ("Dabao", "Dabao restaurant, SOMA, San Francisco, CA"),
  ("Daeho Kalbijim & Beef Soup", "Daeho, 1620 Post St, San Francisco, CA"),
  ("Dalida", "Dalida restaurant, Presidio, San Francisco, CA"),
  ("De Afghanan Kabob House", "De Afghanan Kabob House, Financial District, San Francisco, CA"),
  ("Deli Board", "Deli Board, 1058 Brannan St, San Francisco, CA"),
  ("Detroit Square Pizza", "Detroit Square Pizza, Mission, San Francisco, CA"),
  ("Dolores Deluxe", "Dolores Deluxe, Mission, San Francisco, CA"),
  ("Don Chuys Mexi-Mercado", "Don Chuy\'s, Mission, Excelsior, San Francisco, CA"),
  ("Don Pepe's", "Don Pepe\'s, Castro Valley, CA"),
  ("Dumpling Home", "Dumpling Home, 298 Gough St, San Francisco, CA"),
  ("Dumpling House", "Dumpling House, Castro, San Francisco, CA"),
  ("Dumpling Specialist", "Dumpling Specialist, Sunset, San Francisco, CA"),
  ("Dumpling Zone", "Dumpling Zone, West Portal, San Francisco, CA"),
  ("El Castillito", "El Castillito, Church St, San Francisco, CA"),
  ("El Farolito", "El Farolito, Mission, San Francisco, CA"),
  ("El Gallo Giro", "El Gallo Giro, Mission, San Francisco, CA"),
  ("El Mil Amores", "El Mil Amores, Mission, San Francisco, CA"),
  ("Elephant Sushi", "Elephant Sushi, Hayes Valley, San Francisco, CA"),
  ("Empire Pizza", "Empire Pizza, Union Square, San Francisco, CA"),
  ("Falafel City", "Falafel City, Tenderloin, San Francisco, CA"),
  ("Fil-Am Cuisine", "Fil-Am Cuisine, Daly City, CA"),
  ("Fiorella", "Fiorella, Irving St, San Francisco, CA"),
  ("Fire Sign Cafe", "Fire Sign Cafe, South Lake Tahoe, CA"),
  ("Fish.", "Fish restaurant, 350 Harbor Dr, Sausalito, CA"),
  ("Fleming's Prime Steakhouse", "Fleming\'s Steakhouse, Santa Clara, CA"),
  ("Flour + Water Pizzeria", "Flour and Water Pizzeria, North Beach, San Francisco, CA"),
  ("Fondue Chinoise", "Fondue Chinoise, North Beach, San Francisco, CA"),
  ("Funky Elephant", "Funky Elephant Thai, Mission, San Francisco, CA"),
  ("Gao Viet", "Gao Viet, Irving St, San Francisco, CA"),
  ("Garaje", "Garaje restaurant, Mission, San Francisco, CA"),
  ("Gioia Pizzeria", "Gioia Pizzeria, Hayes Valley, San Francisco, CA"),
  ("Go Duck Yourself Sitdown", "Go Duck Yourself, Bernal Heights, San Francisco, CA"),
  ("Go Duck Yourself Takeout", "Go Duck Yourself Takeout, Chinatown, San Francisco, CA"),
  ("Golden Boy Pizza", "Golden Boy Pizza, 542 Green St, San Francisco, CA"),
  ("Golden Gate Bakery", "Golden Gate Bakery, Chinatown, San Francisco, CA"),
  ("Good Luck Dim Sum", "Good Luck Dim Sum, Clement St, San Francisco, CA"),
  ("Good Mong Kok Bakery", "Good Mong Kok Bakery, Stockton St, San Francisco, CA"),
  ("Great Eastern", "Great Eastern Restaurant, Chinatown, San Francisco, CA"),
  ("Greens Restaurant", "Greens Restaurant, Fort Mason, San Francisco, CA"),
  ("Gumbo Social", "Gumbo Social, Bayview, San Francisco, CA"),
  ("Ham and Cheese Deli", "Ham and Cheese Deli, Richmond, San Francisco, CA"),
  ("Hang Ah Tearoom", "Hang Ah Tea Room, Chinatown, San Francisco, CA"),
  ("Happy Donuts", "Happy Donuts, Noe Valley, San Francisco, CA"),
  ("Hawaiian Drive-In", "Hawaiian Drive-In, Excelsior, San Francisco, CA"),
  ("Henry's Hunan", "Henry\'s Hunan, Noe Valley, San Francisco, CA"),
  ("Hi Hat Pizza", "Hi Hat Pizza, Valencia St, San Francisco, CA"),
  ("Hinodeya", "Hinodeya Ramen, Japantown, San Francisco, CA"),
  ("Hon's Wun-Tun House", "Hon\'s Wun-Tun House, Chinatown, San Francisco, CA"),
  ("Hong Kong Claypot Restaurant", "Hong Kong Claypot Restaurant, Chinatown, San Francisco, CA"),
  ("Hook Fish", "Hook Fish Co, Irving St, Outer Sunset, San Francisco, CA"),
  ("Horn BBQ", "Horn Barbecue, Oakland, CA"),
  ("Hot Sauce and Panko", "Hot Sauce and Panko, Nob Hill, San Francisco, CA"),
  ("House of Nanking", "House of Nanking, 919 Kearny St, San Francisco, CA"),
  ("House of Pancakes", "House of Pancakes SF, Sunset, San Francisco, CA"),
  ("House of Xi'an Dumpling", "House of Xian Dumpling, Chinatown, San Francisco, CA"),
  ("Hy Ki Mi Gia", "Hy Ki Mi Gia, Tenderloin, San Francisco, CA"),
  ("i'a poke", "ia poke, Fillmore, San Francisco, CA"),
  ("Ideale", "Ideale restaurant, North Beach, San Francisco, CA"),
  ("Il Casaro", "Il Casaro, North Beach, San Francisco, CA"),
  ("Il Cilentano", "Il Cilentano, North Beach, San Francisco, CA"),
  ("Il Pollaio", "Il Pollaio, North Beach, San Francisco, CA"),
  ("In-N-Out", "In-N-Out, Fisherman\'s Wharf, San Francisco, CA"),
  ("INDO", "Indo restaurant, University Ave, Palo Alto, CA"),
  ("Jupiter", "Jupiter restaurant, Shattuck Ave, Berkeley, CA"),
  ("Khao Tiew", "Khao Tiew, West Portal, San Francisco, CA"),
  ("Kin Khao", "Kin Khao, 55 Cyril Magnin St, San Francisco, CA"),
  ("King of Noodles", "King of Noodles, Irving St, San Francisco, CA"),
  ("Kingdom of Dumpling", "Kingdom of Dumpling, Sunset, San Francisco, CA"),
  ("Kogi Gogi", "Kogi Gogi, Irving St, Sunset, San Francisco, CA"),
  ("L&G Vietnamese Sandwich", "L&G Vietnamese Sandwich, Tenderloin, San Francisco, CA"),
  ("La Corneta Taqueria", "La Corneta Taqueria, Glen Park, San Francisco, CA"),
  ("La Palma Mexicatessen", "La Palma Mexicatessen, 2884 24th St, San Francisco, CA"),
  ("La Taqueria", "La Taqueria, 2889 Mission St, San Francisco, CA"),
  ("La Torta Gorda", "La Torta Gorda, Mission, San Francisco, CA"),
  ("Leo's Tacos", "Leo\'s Tacos, Sunset, San Francisco, CA"),
  ("LH Restaurant", "LH Restaurant, Clement St, San Francisco, CA"),
  ("Lime Tree", "Lime Tree Southeast Asian Kitchen, Irving St, San Francisco, CA"),
  ("Lokma", "Lokma restaurant, Richmond, San Francisco, CA"),
  ("Long Bridge Pizza", "Long Bridge Pizza, Dogpatch, San Francisco, CA"),
  ("Lovely's", "Lovely\'s restaurant, Cole Valley, San Francisco, CA"),
  ("Lush Gelato", "Lush Gelato, Columbus Ave, North Beach, San Francisco, CA"),
  ("Maillards", "Maillards burger, Sunset, San Francisco, CA"),
  ("Mama's on Washington Square", "Mama\'s on Washington Square, 1701 Stockton St, San Francisco, CA"),
  ("Mandalay", "Mandalay Burmese, California St, San Francisco, CA"),
  ("Manna", "Manna Korean, Irving St, San Francisco, CA"),
  ("Mantra India Restaurant", "Mantra India Restaurant, Mountain View, CA"),
  ("Mario's Bohemian Cigar Store and Cafe", "Mario\'s Bohemian Cigar Store, 566 Columbus Ave, San Francisco, CA"),
  ("Marufuku", "Marufuku Ramen, 1581 Webster St, San Francisco, CA"),
  ("Marugame Udon", "Marugame Udon, Stonestown Galleria, San Francisco, CA"),
  ("Maykadeh", "Maykadeh Persian, Green St, San Francisco, CA"),
  ("Mel's Drive-in", "Mel\'s Drive-in, Mission St, San Francisco, CA"),
  ("Memphis Minnie's", "Memphis Minnie\'s BBQ, Haight St, San Francisco, CA"),
  ("Mensho", "Mensho Tokyo, Geary St, San Francisco, CA"),
  ("Mini Potstickers", "Mini Potstickers, Inner Sunset, San Francisco, CA"),
  ("Mo's Burgers", "Mo\'s Burgers, Grant Ave, North Beach, San Francisco, CA"),
  ("Molinari's", "Molinari Delicatessen, 373 Columbus Ave, San Francisco, CA"),
  ("Mr. Szechuan", "Mr Szechuan, Noriega St, San Francisco, CA"),
  ("Mykonos", "Mykonos restaurant, Burlingame, CA"),
  ("Mylapore", "Mylapore restaurant, San Jose, CA"),
  ("New Golden Daisy", "New Golden Daisy, Chinatown, San Francisco, CA"),
  ("New Lun Ting Cafe", "New Lun Ting Cafe, Chinatown, San Francisco, CA"),
  ("New Red Jade", "New Red Jade, Castro, San Francisco, CA"),
  ("New Woey Loy Goey", "New Woey Loy Goey, Chinatown, San Francisco, CA"),
  ("Niku", "Niku Steakhouse, Design District, San Francisco, CA"),
  ("Nojo Ramen House", "Nojo Ramen, Franklin St, Hayes Valley, San Francisco, CA"),
  ("Nopa", "Nopa restaurant, 560 Divisadero St, San Francisco, CA"),
  ("Noren Izakaya", "Noren Izakaya, North Beach, San Francisco, CA"),
  ("North Beach Gyro", "North Beach Gyro, Columbus Ave, San Francisco, CA"),
  ("Oceanview Diner To-go", "Oceanview Diner, North Berkeley, CA"),
  ("Old Jerusalem", "Old Jerusalem, SOMA, San Francisco, CA"),
  ("Oren's Hummus", "Oren\'s Hummus, Third St, San Francisco, CA"),
  ("Original Joe's", "Original Joe\'s, North Beach, San Francisco, CA"),
  ("Outta Sight Pizza", "Outta Sight Pizza, Tenderloin, San Francisco, CA"),
  ("Outta Sight Pizza II", "Outta Sight Pizza, Chinatown, San Francisco, CA"),
  ("Ozumo", "Ozumo restaurant, Steuart St, San Francisco, CA"),
  ("Palermo", "Palermo Deli, Columbus Ave, North Beach, San Francisco, CA"),
  ("Panchita's Pupuseria #2", "Panchita\'s Pupuseria, 16th St, Mission, San Francisco, CA"),
  ("Parada 22", "Parada 22, Haight St, San Francisco, CA"),
  ("Pho Bahn Mi", "Pho Banh Mi, Palo Alto, CA"),
  ("Pineapple King Bakery", "Pineapple King Bakery, Irving St, San Francisco, CA"),
  ("Pizzahacker", "Pizzahacker, Bernal Heights, San Francisco, CA"),
  ("Pizzelle di North Beach", "Pizzelle di North Beach, Columbus Ave, San Francisco, CA"),
  ("Poboy Kitchen", "Poboy Kitchen, Potrero Hill, San Francisco, CA"),
  ("Pokebola", "Pokebola, Civic Center, San Francisco, CA"),
  ("Portofino", "Portofino Caffe, Columbus Ave, North Beach, San Francisco, CA"),
  ("Prubechu", "Prubechu, Mission, San Francisco, CA"),
  ("Puranpoli", "Puranpoli, Santa Clara, CA"),
  ("R & G Lounge", "R&G Lounge, 631 Kearny St, San Francisco, CA"),
  ("Reem's (Ferry Building)", "Reem\'s California, Ferry Building, San Francisco, CA"),
  ("Regent Thai", "Regent Thai, Noe Valley, San Francisco, CA"),
  ("Rice Roll Express", "Rice Roll Express, Chinatown, San Francisco, CA"),
  ("Rinconcito Salvadoreno", "Rinconcito Salvadoreno, Bernal Heights, San Francisco, CA"),
  ("Saigon Sandwich", "Saigon Sandwich, Larkin St, San Francisco, CA"),
  ("Sam Wo", "Sam Wo Restaurant, Clay St, San Francisco, CA"),
  ("Sam's Pizza and Burgers", "Sam\'s Pizza, Stockton St, North Beach, San Francisco, CA"),
  ("San Tung", "San Tung, 1031 Irving St, San Francisco, CA"),
  ("Sandy's", "Sandy\'s restaurant, Haight St, San Francisco, CA"),
  ("Saru Sushi Bar", "Saru Sushi Bar, 3856 24th St, San Francisco, CA"),
  ("Sasa", "Sasa restaurant, Japantown, San Francisco, CA"),
  ("Schroeders", "Schroeder\'s, Front St, San Francisco, CA"),
  ("Se7enbuds", "Se7enbuds, Polk Gulch, San Francisco, CA"),
  ("SF Chicken Box", "SF Chicken Box, North Beach, San Francisco, CA"),
  ("Shanghai Dumpling King", "Shanghai Dumpling King, San Francisco, CA"),
  ("Slice House by Tony Gemignani", "Slice House Tony Gemignani, Haight, San Francisco, CA"),
  ("Sodini's Restaurant", "Sodini\'s, Green St, North Beach, San Francisco, CA"),
  ("Sotto Mare", "Sotto Mare, 552 Green St, San Francisco, CA"),
  ("Square Pie Guys", "Square Pie Guys, SOMA, San Francisco, CA"),
  ("State Bird Provisions", "State Bird Provisions, 1529 Fillmore St, San Francisco, CA"),
  ("Stella", "Stella restaurant, Burlingame, CA"),
  ("Straits", "Straits restaurant, Santana Row, San Jose, CA"),
  ("Super Duper Burgers", "Super Duper Burgers, Market St, San Francisco, CA"),
  ("Super Star Restaurant", "Super Star Restaurant, Excelsior, San Francisco, CA"),
  ("Surisan", "Surisan, Lombard St, San Francisco, CA"),
  ("Szechuan Cuisine", "Szechuan Cuisine, Noriega St, San Francisco, CA"),
  ("Tacos Del Barrio", "Tacos Del Barrio, Mission, San Francisco, CA"),
  ("Tacos El Charro", "Tacos El Charro, Mission St, San Francisco, CA"),
  ("Tacos El Patron", "Tacos El Patron, Mission, San Francisco, CA"),
  ("Taishan Cuisine", "Taishan Cuisine, Chinatown, San Francisco, CA"),
  ("Tajines Restaurant", "Tajines, Broadway, North Beach, San Francisco, CA"),
  ("Taqueria Cancun", "Taqueria Cancun, Mission St, San Francisco, CA"),
  ("Taqueria Guadalajara", "Taqueria Guadalajara, 22nd St, Mission, San Francisco, CA"),
  ("Taqueria Zorro", "Taqueria Zorro, North Beach, San Francisco, CA"),
  ("Tartine Bakery", "Tartine Bakery, 600 Guerrero St, San Francisco, CA"),
  ("Terra Cotta Warrior", "Terra Cotta Warrior, Irving St, San Francisco, CA"),
  ("The Anchovy Bar", "The Anchovy Bar, Post St, San Francisco, CA"),
  ("The Bird", "The Bird SF, New Montgomery St, San Francisco, CA"),
  ("The Fatted Calf", "The Fatted Calf, Ferry Building, San Francisco, CA"),
  ("The Good Life Pizza", "The Good Life Pizza, Hyde St, Marina, San Francisco, CA"),
  ("The Laundromat", "The Laundromat SF, Clement St, San Francisco, CA"),
  ("The Little Chihuahua", "The Little Chihuahua, Sanchez St, Noe Valley, San Francisco, CA"),
  ("The Pizza Place on Noriega", "The Pizza Place on Noriega, San Francisco, CA"),
  ("The Pizza Shop", "The Pizza Shop, 16th St, Mission, San Francisco, CA"),
  ("Three Babes Bakeshop", "Three Babes Bakeshop, Mission, San Francisco, CA"),
  ("Three Star Restaurant", "Three Star Restaurant, Irving St, Sunset, San Francisco, CA"),
  ("Tony's Coal Fired Pizza", "Tony\'s Coal Fired Pizza, Stockton St, North Beach, San Francisco, CA"),
  ("Tony's Pizza Napoletana", "Tony\'s Pizza Napoletana, 1570 Stockton St, San Francisco, CA"),
  ("Tortas Los Picudos", "Tortas Los Picudos, Mission St, San Francisco, CA"),
  ("Toy Boat by Jane", "Toy Boat Dessert Cafe, Clement St, San Francisco, CA"),
  ("Toyose", "Toyose, Noriega St, San Francisco, CA"),
  ("Trattoria Contadina", "Trattoria Contadina, Mason St, North Beach, San Francisco, CA"),
  ("TRULY Mediterranean", "TRULY Mediterranean, 16th St, Mission, San Francisco, CA"),
  ("Turquaz", "Turquaz, South Park, San Francisco, CA"),
  ("Uncle Titos", "Uncle Tito\'s, Mission, San Francisco, CA"),
  ("Viva Goa", "Viva Goa, Lombard St, San Francisco, CA"),
  ("Volcano Curry", "Volcano Curry, Clement St, San Francisco, CA"),
  ("Watani Spot", "Watani Spot, Burlingame, CA"),
  ("Yarsa", "Yarsa, Washington St, North Beach, San Francisco, CA"),
  ("Yuanbao Jiaozi", "Yuanbao Jiaozi, 9th Ave, Inner Sunset, San Francisco, CA"),
  ("Yuet Lee", "Yuet Lee, Stockton St, Chinatown, San Francisco, CA"),
  ("Z and Y", "Z and Y restaurant, Jackson St, Chinatown, San Francisco, CA"),
  ("Zante Pizza and Indian Cuisine", "Zante Pizza, 16th St, Mission, San Francisco, CA"),
  ("Zentarou Sushi", "Zentarou Sushi, Judah St, Sunset, San Francisco, CA"),
  ("Zushi Puzzle", "Zushi Puzzle, Lombard St, Marina, San Francisco, CA"),
  ("ZZAN", "ZZAN Korean, Union Square, San Francisco, CA"),
  ("La Cheve Bakery and Brews", "La Cheve Bakery, Napa, CA"),
  ("Red Hot Chili Pepper", "Red Hot Chili Pepper Indian Chinese, San Carlos, CA"),
  ("Horn BBQ", "Horn Barbecue, 2534 Mandela Pkwy, Oakland, CA"),
]

def geocode(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?" + urllib.parse.urlencode({
        "address": address,
        "key": API_KEY
    })
    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read())
    if data["status"] == "OK":
        loc = data["results"][0]["geometry"]["location"]
        return round(loc["lat"], 6), round(loc["lng"], 6)
    return None

results = {}
for name, address in RESTAURANTS:
    coords = geocode(address)
    if coords:
        results[name] = coords
        print(f"✓ {name}: {coords}")
    else:
        print(f"✗ {name}: not found")
    time.sleep(0.05)  # small delay to be polite

# Update index.html
with open(HTML_FILE, "r") as f:
    html = f.read()

# Build new PRECISE_COORDS block
lines = ["const PRECISE_COORDS = {\n"]
for name, (lat, lng) in results.items():
    escaped = name.replace("'", "\\'")
    lines.append(f"  \'{escaped}\': [{lat}, {lng}],\n")
lines.append("};\n")
new_precise = "".join(lines)

html = re.sub(r"const PRECISE_COORDS = \{[^}]+\};\n", new_precise, html, flags=re.DOTALL)

with open(HTML_FILE, "w") as f:
    f.write(html)

print(f"\nDone! Updated {len(results)} restaurant coordinates in {HTML_FILE}")
