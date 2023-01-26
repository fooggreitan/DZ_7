import view
import importieren
import export 

def start():

    while True:
        match view.get_type():
            case 0: 
                importieren.record()
            case 2:
                export.importierenn()
            case 1:
                export.importierennNot()
            case 3:
                export.importierennNoet()
            case 4: break
