import turtle as tt

def mot_et_score(lettre : str, resultat) -> str :
    tt.up()
    tt.goto(300, 400)
    tt.down()
    tt.write(' NEW %s = %s pts.' %(lettre, resultat), font =('Calibri', 16, 'italic'))