import view
import importieren
import export 

def start():

    while True:
        match view.get_type():
            case 0: 
                importieren.record()
            case 1:
                export.importierennNot()
            case 2:
                export.sortedID()
            case 3:
                export.sodtedDate()
            case 4:
                export.delete_note()
            case 5:
                export.changelist()
            case 6: break
