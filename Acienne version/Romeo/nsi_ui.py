# coding: utf-8

#
# Bibliotheque d'interface utilisateur pour le manuel NSI de 1ere.
# v1.0 / avril 2021 / M. Beaudouin-Lafon
#
# Extensions de turtle (disponibles seulement si la bibliotheque turtle a ete importee avant celle-ci) :
#   ondrag(commande) - remplace turtle.ondrag avec une version reentrante
#   write_text(t) - affiche le texte t
#   set_font(f) - change la police pour write_text
#   set_size(s) - change la taille pour write_text
#   set_style(s) - change le style pour write_text
#   set_align(a) - change l'alignement pour write_text
#
# Fonctions d'interface (les parametres entre crochets sont optionels]) :
#   c = begin_horizontal/vertical() - ouvrir un conteneur
#   end_horizontal/vertical() - fermer le conteneur
#
#   b = button(titre, commande, [parametre]) - creation de bouton
#   s = slider(titre, min, max, [commande]) - creation de slider
#   e = entry(titre, commande) - creation de champ de saisie de texte
#   l = label(titre) - creation d'un texte non editable
#
#   lb = listbox(titre, liste, [commande]) - creation d'une liste
#   update_list(lb, liste) - mise a jour du contenu d'une liste
#
#   m = option_menu(titre, liste, [commande]) - creation d'un menu d'options
#   update_options(m, liste) - mise a jour du contenu d'un menu d'options
#
#   s = get_string(w) - recuperer la valeur d'un interacteur sous forme de chaine
#   i = get_int(w) - recuperer la valeur d'un interacteur sous forme d'entier
#   f = get_float(w) - recuperer la valeur d'un interacteur sous forme de flottant
#
#   set_value(w, v) - changer la valeur d'un interacteur (v peut etre entier, flottant ou chaine)
#   set_text(w, txt) - changer le texte d'un label, d'un bouton ou d'un champ d'entree de texte
#   set_width(w, taille) - changer la largeur d'un interacteur
#   set_height(w, taille) - changer la hauteur d'un interacteur
#   set_background(w, couleur) - changer la couleur de fond d'un interacteur
#   set_right_click(w, commande, [parametre]) - associer une commande a un clic droit sur l'interacteur
#
#   animate(f, [delai]) - appeler f tous les delai ms
#   stop_animate() - arreter l'animation
#   animated() - retour vrai si l'animaion est active
#
#   start_ui() (ou main_loop()) - lancer l'interface

import sys
if 'ipykernel' in sys.modules:
    from ipywidgets import widgets

    # ======== CONTAINERS ========

    def _init_ui():
        global _hlayout, _vlayout, _root, _side, _frames, _sides
        _hlayout = widgets.Layout(align_items="center")
        _vlayout = widgets.Layout(flex_flow="column nowrap", align_items="center")
        _root = widgets.HBox([], layout=_hlayout)

        _side = 'left'
        _frames = []    # la pile des conteneurs
        _sides = []     # l'orientation associée

    def _add_child(w):
        _root.children = tuple(list(_root.children) + [w])

    def begin_horizontal():
        """ Ouvre un conteneur horizontal """
        global _root, _side
        box = widgets.HBox([], layout=_hlayout)
        _add_child(box)
        _frames.append(_root)
        _sides.append(_side)
        _root = box
        _side = 'left'
        return _root

    def end_horizontal():
        """ Ferme un conteneur horizontal """
        global _root, _side
        if (_side != 'left'):
            print('end_horizontal() dans un conteneur vertical: ignoré')
        if len(_frames) == 0:
            print('end_horizontal() sans conteneur ouvert: ignoré')
            return
        _root = _frames.pop()
        _side = _sides.pop()

    def begin_vertical():
        """ Ouvre un conteneur vertical """
        global _root, _side
        box = widgets.VBox([], layout=_vlayout)
        _add_child(box)
        _frames.append(_root)
        _sides.append(_side)
        _root = box
        _side = 'top'
        return _root

    def end_vertical():
        """ Ferme un conteneur vertical """
        global _root, _side
        if (_side != 'top'):
            print('end_vertical() dans un conteneur horizontal: ignoré')
        if len(_frames) == 0:
            print('end_vertical() sans conteneur ouvert: ignoré')
            return
        _root = _frames.pop()
        _side = _sides.pop()

    # ======== BUTTON ========

    def button(title, command, param=None):
        """ Cree un bouton et l'ajoute a l'interface """
        b = widgets.Button(description=title)
        def cb(b):
            if param is None:
                command()
            else:
                command(param)
        b.on_click(cb)
        _add_child(b)
        return b


    # ======== SLIDER ========

    def slider(label, from_, to, command=None):
        """ Cree un slider et l'ajoute a l'interface """
        l = widgets.Label(label, layout=widgets.Layout(height='20px'))

        # l'indicateur de valeur
        vlayout = widgets.Layout(height='20px')
        v = widgets.Label('valeur', layout=vlayout) # pour afficher la valeur

        # la tirette elle-meme
        slayout = widgets.Layout(width='200px')
        if type(from_) is int and type(to) is int:
            s = widgets.IntSlider(min=from_, max=to, readout=False, layout=slayout)
        else:
            s = widgets.FloatSlider(min=from_, max=to, readout=False, layout=slayout)
        _add_child(widgets.VBox([l, v, s]))

        # afficher la valeur (a peu pres) au-dessus de la tirette
        def set_value(val):
            set_text(v, val)
            val = (val - from_)/(to - from_) * (int(slayout.width[:-2]) - 9*len(str(to)))
            vlayout.margin = '2px 2px 2px '+str(val)+'px'
        # reafficher la valeur lorsqu'elle change
        s.observe(lambda ch: set_value(ch['new']), names='value')
        # reafficher la valeur lorsque la taille du slider change
        slayout.observe(lambda ch: set_value(s.value), names='width')
        # afficher la valeur au début
        set_text(v, from_)

        if command is not None:
            def on_value_change(change):
                command(change['new'])
            s.observe(on_value_change, names='value')
        return s


    # ======== TEXT ENTRY ========

    def _entry_command(command):
        def cb(ev):
            command(ev.widget.get())
        return cb

    def entry(label, command=None):
        """ Cree un champs de saisie de texte et l'ajoute a l'interface """
        l = widgets.Label(label)
        e = widgets.Text(continuous_update=False)
        _add_child(widgets.VBox([l, e]))

        if command is not None:
            def on_value_change(change):
                command(change['new'])
            e.observe(on_value_change, names='value')
        return e

    # ======== LABEL ========

    def label(text):
        """ Cree un champs d'affichage de texte et l'ajoute a l'interface """
        l = widgets.Label(value=str(text))
        _add_child(l)
        return l

    def set_text(w, text):
        if isinstance(w, widgets.widget_string.Text) or isinstance(w, widgets.widget_string.Label):
            w.value = str(text)
        elif isinstance(w, widgets.widget_button.Button):
            w.description = str(text)


    # ======== LISTBOX ========

    def listbox(label, list, command=None):
        """ Cree une liste avec comme options le contenu de `list` (liste ou dictionnaire) """
        l = widgets.Label(label)
        lb = widgets.Select(options=list)
        _add_child(widgets.VBox([l, lb]))
        if command is not None:
            def on_value_change(change):
                command(change['new'])
            lb.observe(on_value_change, names='value')
        return lb

    def update_list(lb, list):
        """" Met a jour le contenu de la liste """
        if type(list) is dict:
            list = list.keys()
        lb.options = list

    # ======== OPTION MENU ========

    def option_menu(label, list, command=None):
        """ Cree un menu avec comme options le contenu de `list` (liste ou dictionnaire) """
        l = widgets.Label(label)
        om = widgets.Dropdown(options=list)
        _add_child(widgets.VBox([l, om]))
        if command is not None:
            def on_value_change(change):
                command(change['new'])
            om.observe(on_value_change, names='value')
        return om

    def update_options(om, list):
        """ Met a jour le contenu du menu """
        if type(list) is dict:
            list = list.keys()
        lb.options = list

    # ======== ACCES AUX VALEURS ========

    # widgets.widget_button.Button
    # widgets.widget_int.IntSlider
    # widgets.widget_float.FloatSlider
    # widgets.widget_string.Text
    # widgets.widget_string.Label
    # widgets.widget_selection.Select
    # widgets.widget_selection.Dropdown

    def get_string(w):
        """ Retourne la valeur de l'interacteur `w` sous forme de chaine """
        if isinstance(w, widgets.widget_button.Button):
            return w.description
        return str(w.value)

    def get_int(w):
        """ Retourne la valeur de l'interacteur `w` sous forme d'entier """
        if isinstance(w, widgets.widget_button.Button):
            return int(w.description)
        return int(w.value)

    def get_float(w):
        """ Retourne la valeur de l'interacteur `w` sous forme de flottant """
        if isinstance(w, widgets.widget_button.Button):
            return float(w.description)
        return float(w.value)

    # set widget value
    def set_value(w, val):
        """ Change la valeur de l'interacteur `w`. `val` peut etre un entier, un flottant ou une chaine """
        if isinstance(w, widgets.widget_button.Button):
            w.description = str(val)
        elif isinstance(w, widgets.widget_int.IntSlider):
            w.value = int(val)
        elif isinstance(w, widgets.widget_float.FloatSlider):
            w.value = float(val)
        elif isinstance(w, widgets.widget_string.Text) or isinstance(w, widgets.widget_string.Label):
            w.value = str(val)
        elif isinstance(w, widgets.widget_selection.Select) or isinstance(w, widgets.widget_selection.Dropdown):
            try:
                w.value = str(val)
            except ValueError:  # val pas dans les options
                pass

    # ======== TAILLE ET COULEUR ========

    def set_width(w, width):
        """ Change la largeur d'un interacteur """
        if isinstance(w, widgets.widget_int.IntSlider) or isinstance(w, widgets.widget_float.FloatSlider):
            w.layout.width = str(width)+'px'
            w.value = w.value
        else:  # largeur en caractères (approximativement)
            w.layout.width = str(width*10)+'px'


    def set_height(w, height):
        """ Change la hauteur d'un interacteur """
        w.layout.height = str(height)+'px'

    def set_background(w, color):
        """ Change la couleur de fond d'un interacteur """
        if isinstance(w, widgets.widget_button.Button):
            w.style.button_color = color

    # ======== INTERACTION ========

    def set_right_click(w, command, parameter=None):
        """ Associe une commande, avec un parametre eventuel, a un clic droit sur l'interacteur w """
        pass

    # ======== ANIMATION ========

    import threading
    from time import sleep

    _running = False
    _step = None
    _delay = 100    # en millisecondes

    def _run_thread_animation():
        while _running:
            _step()
            sleep(_delay / 1000)

    def stop_animate():
        """ Arrête l'animation """
        global _running, _step
        _running = False
        _step = None

    def animate(fun, delay=50):
        """ Lance une animation: appeler `fun` tous les `delay` ms """
        global _running, _step, _delay
        _step = fun
        _delay = delay
        if _running:
            return
        _running = True
        thread = threading.Thread(target=_run_thread_animation)
        thread.start()

    def animated():
        """ Retourne True si une animation est active """
        return _running

    # ======== BOUCLE PRINCIPALE ========

    def clear_ui():
        """ Efface l'interface de la cellule courante """
        global _root, _side, _frames, _sides
        _root.close()
        _root = widgets.HBox([], layout=_hlayout)
        _side = 'left'
        _frames = []    # la pile des conteneurs
        _sides = []     # l'orientation associée

    def start_ui():
        """ Lance l'interface """
        display(_root)
        _init_ui()

    # il vaut mieux utiliser start_ui() par souci de cohérence
    def main_loop():
        """ Lance la boucle d'interaction """
        display(_root)
        _init_ui()

    _init_ui()

else:
    # Eviter le bug qui plante MacOS avec TkInter et Python3 !
    import platform
    if platform.mac_ver()[0] != '' and platform.python_version_tuple()[0] != '2':
        exit('TkInter est incompatible avec Python3 sur ce Macintosh. Utiliser Python 2.x')

    # Importer la bonne version de TkInter
    if (platform.python_version_tuple()[0] == '2'):
        import Tkinter as tk
    else:
        import tkinter as tk


    if 'turtle' in sys.modules:
        import turtle
        # Acceder a la racine de l'interface pour pouvoir y ajouter des widgets
        _screen = turtle.Screen()
        _root = tk.Frame(turtle.Turtle._screen._root)
        _root.pack(side="left")

        # Redefinition du `ondrag` de `turtle` pour eviter les appels reentrants a la callback
        _dragging = False

        def ondrag(f):
            """ Appelle f avec comme parametre la position x,y du curseur lorsque l'on deplace la souris avec le bouton appuye """
            def myf(x, y):
                global _dragging
                if _dragging:
                    return
                _dragging = True
                f(x, y)
                _dragging = False
            turtle.ondrag(myf)

        turtle.listen()
        turtle.speed(0)

        # Fonctions pour ecrire du texte dans la fenetre tortue et controler son style
        _style = {
            'turtle': False,
            'font': 'Times',
            'size': 10,
            'style': 'normal',
            'align': 'left'
        }

        def write_text(s):
            """ Afficherle texte s a la position de la tortue """
            turtle.write(s, _style['turtle'], _style['align'],
                (_style['font'], _style['size'], _style['style']))

        def set_font(f):
            """ Change la police d'affichage du texte """
            _style['font'] = f

        def set_size(s):
            """ Change la taille de l'affichage de texte """
            _style['size'] = int(s)

        def set_style(s):
            """ Change le style (normal/bold/italid) de l'affichage de texte """
            _style['style'] = s

        def set_align(a):
            """ Change l'alignement (left/center/right) de l'affichage de texte par rapport a la position de la tortue """
            _style['align'] = a

    else:
        _root = tk.Tk()

    _side = 'left'

    # ======== CONTAINERS ========

    _frames = []    # la pile des conteneurs
    _sides = []     # l'orientation associee

    def begin_horizontal():
        """ Ouvre un conteneur horizontal """
        global _root, _side
        _frames.append(_root)
        _sides.append(_side)
        _root = tk.Frame(_root)
        _root.pack(side=_side)
        _side = 'left'
        return _root

    def end_horizontal():
        """ Ferme un conteneur horizontal """
        global _root, _side
        if (_side != 'left'):
            print('end_horizontal() dans un conteneur vertical: ignore')
        if len(_frames) == 0:
            print('end_horizontal() sans conteneur ouvert: ignore')
            return
        _root = _frames.pop()
        _side = _sides.pop()

    def begin_vertical():
        """ Ouvre un conteneur vertical """
        global _root, _side
        _frames.append(_root)
        _sides.append(_side)
        _root = tk.Frame(_root)
        _root.pack(side=_side)
        _side = 'top'
        return _root

    def end_vertical():
        """ Ferme un conteneur vertical """
        global _root, _side
        if (_side != 'top'):
            print('end_vertical() dans un conteneur horizontal: ignore')
        if len(_frames) == 0:
            print('end_vertical() sans conteneur ouvert: ignore')
            return
        _root = _frames.pop()
        _side = _sides.pop()

    # ======== BUTTON ========

    def _button_command(command, param):
        def cb():
            v = param
            if isinstance(param, tk.Entry):
                v = param.get()
            elif isinstance(param, tk.Scale):
                v = float(param.get())
            command(v)
        return cb

    def button(title, command, param=None):
        """ Cree un bouton et l'ajoute a l'interface """
        if param is None:
            b = tk.Button(_root, text=title, command=command)
        else:
            b = tk.Button(_root, text=title, command=_button_command(command, param))
        b.pack(side=_side)
        return b

    # ======== SLIDER ========

    def slider(label, from_, to, command=None):
        """ Cree un slider et l'ajoute a l'interface """
        length = 200

        if type(from_) is int and type(to) is int:
            resolution = 1
        else:
            resolution = 0.1

        if command is None:
            convert = None
        else:
            # appeler command avec la conversion de la valeur en flottant
            def convert(v):
                command(float(v))
        s = tk.Scale(_root, from_=from_, to=to, label=label, resolution=resolution,
                  length=length, orient=tk.HORIZONTAL, command=convert)
        s.pack(side=_side)
        return s

    # ======== TEXT ENTRY ========

    def _entry_command(command):
        def cb(ev):
            command(ev.widget.get())
        return cb

    def entry(label, command=None):
        """ Cree un champs de saisie de texte et l'ajoute a l'interface """
        if label != "":
            f = tk.Frame(_root)
            e = tk.Entry(f)
            l = tk.Label(f, text=label)
            l.pack(side="top")
            e.pack(side="top")
            f.pack(side=_side)
        else:
            e = tk.Entry(_root)
            e.pack(side=_side)
        if command is not None:
            e.bind('<Return>', _entry_command(command))
        return e

    # ======== LABEL ========

    def label(text):
        """ Cree un champs d'affichage de texte et l'ajoute a l'interface """
        l = tk.Label(_root, text=str(text))
        l.pack(side=_side)
        return l

    def set_text(w, text):
        if isinstance(w, tk.Label) or isinstance(w, tk.Button):
            w['text'] = str(text)
        elif isinstance(w, tk.Entry):
            w.delete('0', 'end')
            w.insert('0', str(text))

    # ======== LISTBOX ========

    def _listbox_command(command):
        def cb(ev):
            lb = ev.widget
            command(lb.get(lb.curselection()))
        return cb

    def listbox(label, list, command=None):
        """ Cree une liste avec comme options le contenu de `list` (liste ou dictionnaire) """
        f = tk.Frame(_root)
        lb = tk.Listbox(f)
        l = tk.Label(f, text=label)
        if command is not None:
            lb.bind("<Double-Button-1>", _listbox_command(command))
        update_list(lb, list)
        l.pack(side="top")
        lb.pack(side="top")
        f.pack(side="left")
        return lb

    def update_list(lb, list):
        """" Met a jour le contenu de la liste """
        if type(list) is dict:
            list = list.keys()
        lb.delete(0, tk.END)
        for item in list:
            lb.insert(tk.END, item)

    # ======== OPTION MENU ========

    def _options_command(command, option):
        def cb(var, idx, mode):
            command(option.get())
        return cb

    def option_menu(label, list, command=None):
        """ Cree un menu avec comme options le contenu de `list` (liste ou dictionnaire) """
        option = tk.StringVar(_root)
        f = tk.Frame(_root)
        om = tk.OptionMenu(f, option, "_")
        l = tk.Label(f, text=label)
        om._optionvar = option
        update_options(om, list)
        if command is not None:
            option.trace('w', _options_command(command, option))
        l.pack(side="top")
        om.pack(side="top")
        f.pack(side="left")
        return om

    def update_options(om, list):
        """ Met a jour le contenu du menu """
        if type(list) is dict:
            list = list.keys()
        om['menu'].delete(0, tk.END)
        for item in list:
            om['menu'].add_command(label=item, command=tk._setit(om._optionvar, item))

    # ======== ACCES AUX VALEURS ========

    def get_string(w):
        """ Retourne la valeur de l'interacteur `w` sous forme de chaine """
        if isinstance(w, tk.Entry):
            return w.get()
        if isinstance(w, tk.Scale):
            return str(w.get())
        if isinstance(w, tk.Listbox):
            item = w.curselection()
            return w.get(item)
        if isinstance(w, tk.OptionMenu):
            return w._optionvar.get()
        return ""

    def get_int(w):
        """ Retourne la valeur de l'interacteur `w` sous forme d'entier """
        if isinstance(w, tk.Scale):
            return int(w.get())
        if isinstance(w, tk.Entry):
            return int(w.get())
        if isinstance(w, tk.Listbox):
            item = w.curselection()
            return int(w.get(item))
        if isinstance(w, tk.OptionMenu):
            return int(w._optionvar.get())
        return 0

    def get_float(w):
        """ Retourne la valeur de l'interacteur `w` sous forme de flottant """
        if isinstance(w, tk.Scale):
            return float(w.get())
        if isinstance(w, tk.Entry):
            return float(w.get())
        if isinstance(w, tk.Listbox):
            item = w.curselection()
            return float(w.get(item))
        if isinstance(w, tk.OptionMenu):
            return float(w._optionvar.get())
        return 0.0

    # set widget value
    def set_value(w, val):
        """ Change la valeur de l'interacteur `w`. `val` peut etre un entier, un flottant ou une chaine """
        if isinstance(w, tk.Entry):
            w.set(str(val))
        elif isinstance(w, tk.Scale):
            w.set(float(val))
        elif isinstance(w, tk.Listbox):
            w.set(str(val))
        elif isinstance(w, tk.OptionMenu):
            w._optionvar.set(str(val))

    # ======== TAILLE ET COULEUR ========

    def set_width(w, width):
        """ Change la largeur d'un interacteur """
        if isinstance(w, tk.Scale):
            w.configure({"length": width})
        else:
            w.configure({"width": width})

    def set_height(w, height):
        """ Change la hauteur d'un interacteur """
        if not isinstance(w, tk.Scale):
            w.configure({"height": height})

    def set_background(w, color):
        """ Change la couleur de fond d'un interacteur """
        w.configure(highlightbackground=color)

    # ======== INTERACTION ========

    def set_right_click(w, command, parameter=None):
        """ Associe une commande, avec un parametre eventuel, a un clic droit sur l'interacteur w """
        if parameter is None:
            w.bind("<Button-2>", lambda _: command())
            w.bind("<Button-3>", lambda _: command())
        else:
            w.bind("<Button-2>", lambda _: command(parameter))
            w.bind("<Button-3>", lambda _: command(parameter))

    # ======== ANIMATION ========

    _running = False
    _step = None
    _delay = 100    # en millisecondes

    _threading = True
    import threading
    from time import sleep

    def _run_thread_animation():
        while _running:
            _step()
            sleep(_delay / 1000)

    def _run_tk_animation():
        if not _running:
            return
        _step()
        _root.after(_delay, _run_tk_animation)

    def stop_animate():
        """ Arrete l'animation """
        global _running, _step
        _running = False
        _step = None

    def animate(fun, delay=50):
        """ Lance une animation: appeler `fun` tous les `delay` ms """
        global _running, _step, _delay
        _step = fun
        _delay = delay
        if _running:
            return
        _running = True
        if _threading:
            thread = threading.Thread(target=_run_thread_animation)
            thread.start()
        else:
            _root.after(_delay, _run_tk_animation)

    def animated():
        """ Retourne True si une animation est active """
        return _running

    # ======== BOUCLE PRINCIPALE ========

    def clear_ui():
        """ Ne fait rien ! (seulement pour compatibilite avec la version Jupyter) """
        pass

    def start_ui():
        """ Lance l'interface """
        tk.mainloop()

    # il vaut mieux utiliser start_ui() par souci de coherence
    def main_loop():
        """ Lance la boucle d'interaction """
        tk.mainloop()
