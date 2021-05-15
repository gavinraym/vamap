#colors
portal_color = 'red'
road_color = 'green'

nodes = [
    {'label':'Elder Hub', 'title' : 'Great place to fish.'},
    {'label': 'Beach House', 'title' : 'Food and drink at the Inn.'},
    {'label': 'Fort Smelter','title' : 'Large workshop here.'},
    {'label': 'Market', 'title' : 'Come and buy something!'},
    {'label': 'Bridge', 'title' : 'This old bridge allows for travel between Fort Smelter and the god portals.'},
    {'label':'Eikthyr', 'title' : 'god.'},
    {'label':'Bonemass', 'title' : 'Cores and iron here too.'},
    {'label':'Moder', 'title' : 'She is alive and mining stone like the strongest.'},
    {'label':'Alter', 'title' : 'Under construction.'},
    {'label':'Spiral', 'title' : 'A spiritual place.'}
]

edges = {
    ('Elder Hub','Beach House'): {'color':portal_color, 'title':'House'},
    ('Elder Hub', 'Fort Smelter'): {'color': portal_color, 'title' : 'Fort'},
    ('Elder Hub', 'Bridge'): {'color':portal_color, 'title' : 'Bridge'},
    ('Beach House', 'Market'): {'color':portal_color, 'title': 'Market'},
    ('Beach House', 'Farm'): {'color':portal_color, 'title': 'Farm'},
    ('Fort Smelter', 'Bridge'): {'color': road_color, 'title':'road'},
    ('Fort Smelter' , 'Fort Smelter'): {'color': portal_color, 'title':' '},
    ('Fort Smelter', 'Spiral') : {'color' : portal_color, 'title':'exp'},
    ('Fort Smelter', 'Exploratory Location') : {'color' : portal_color, 'title':'exp'},
    ('Fort Smelter', 'Exploratory Location') : {'color' : portal_color, 'title':'exp'},
    ('Bridge', 'Eikthyr' ) : {'color': portal_color, 'title': 'Eikthyr' },
    ('Bridge', 'Elder') : {'color': portal_color, 'title':'Elder' },
    ('Bridge', 'Bonemass' ) : {'color': portal_color, 'title': 'Bonemass'},
    ('Bridge', 'Moder') : {'color': portal_color, 'title': 'Moder'},
    ('Bridge', 'Alter') : {'color': portal_color, 'title': 'Alter'},
    ('Bridge', 'Bridge' ) : {'color': portal_color, 'title': '  '},
    
}