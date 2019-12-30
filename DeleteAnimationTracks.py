import c4d
from c4d import gui
from c4d import documents


def main():
    doc = c4d.documents.GetActiveDocument()
    selection = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    doc.StartUndo()
    for sel in selection:
        tracks = GetAnimationTracks(sel)
        for track in tracks:
            print 'Deleting animationtrack ',track
            doc.AddUndo(c4d.UNDOTYPE_DELETE,track)
            track.Remove()
    doc.EndUndo()
    c4d.EventAdd()

def GetAnimationTracks(obj):
    tracks = obj.GetCTracks()
    return tracks



if __name__ == "__main__":
    main()