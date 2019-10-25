import c4d
from c4d import gui
from c4d import documents


def main():
    doc = c4d.documents.GetActiveDocument()
    selection = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    for sel in selection:
        print "object = ", sel
        track = GetAnimationTracks(sel)
        print track.GetTypeName()

    """
    temp_var_obj = obj[:]
    for i, o in enumerate(temp_var_obj):
        if o.GetTypeName() == 'Null':
            obj.remove(o)
    """


def GetAnimationTracks(selection):
    tracks = []
    if not isinstance(selection,list):
        selection = [selection]
    for i,sel in enumerate(selection):
        tracks.append(sel.GetCTracks())
    return tracks



if __name__ == "__main__":
    main()