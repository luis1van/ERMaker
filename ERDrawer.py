from graphviz import Source

heading = """digraph G { 
    //  
    // Defaults
    //  
    // Box for entities
    
    // One-to-many relation (from one, to many)
    //  
    // Entities
    //  
    """

entityLabel = """[ shape=record, margin=0, label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="lightblue">"""

endRow = "</td></tr>"
startAttribute = '<tr><td align="left">'
relationBox = '[shape = box]'
entityEnd = """"</table>
    >]"""
end = "}"
src = Source("""digraph G { 
 
    // Entities
    //  
    splines = ortho;
    University [shape=record,margin=0,label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="lightblue">University</td></tr>
            <tr><td align="left">Name</td></tr>
            <tr><td align="left">Address</td></tr>
        </table>
    >];
    Student [shape=record,margin=0,label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="lightblue">Student</td></tr>
            <tr><td align="left">S_ID</td></tr>
            <tr><td align="left">Name</td></tr>
            <tr><td align="left">Phone</td></tr>
        </table>
    >] ; 
Course [shape=record,margin=0,label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="lightblue">Course</td></tr>
            <tr><td align="left">Name</td></tr>
            <tr><td align="left">Subject</td></tr>
            <tr><td align="left">Section</td></tr>
        </table>
    >];
Professor [shape=record,margin=0,label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="lightblue">Professor</td></tr>
            <tr><td align="left">P_ID</td></tr>
            <tr><td align="left">Name</td></tr>
        </table>
    >] ;
    

    //  

    // Relationships
    //  
        University -> has [arrowhead=none, arrowtail=tee,dir=both];
        employs -> University [arrowhead=tee, arrowtail=none,dir=both];
        Student -> takes [arrowhead=none, arrowtail=crowtee,dir=both];
        has -> Student [arrowhead=crowtee, arrowtail=none,dir=both];
    
        takes  -> Course [arrowhead=crowtee, arrowtail=none,dir=both];
        Course -> teaches [arrowhead=none, arrowtail=crowodot,dir=both];
     
        Professor -> employs [arrowhead=none, arrowtail=crowtee,dir=both];
        teaches -> Professor [arrowhead=crowtee, arrowtail=none,dir=both];

        offers -> Course [arrowhead=crowtee, arrowtail=none,dir=both];
        University -> offers [arrowhead=none, arrowtail=tee,dir=both];

    overlap = false;
    takes [shape=box];
    offers [shape = box];
    has [shape=box];
    employs [shape = box];
    teaches [shape = box];
   rankdir=LR;
   
   
}\n""")

arrowtailB = ' [arrowhead=none, arrowtail='
arrowtailE = ' ,dir=both]'


def getCardinality(card):
    if card == 'one' or card == 'a':
        return ''
    elif card == 'many':
        return 'crow'
    else:
        return 'none'


def getModality(card):
    if card == 'must':
        return 'tee'
    elif card == 'may\snot':
        return 'odot'
    else:
        return 'none'
src.render('test-output/holy-grenade13.gv', view=True)