
from graphviz import Source


src = Source("""digraph G { 
    //  
    // Defaults
    //  
    // Box for entities
    node [shape=record, margin=0]

    // One-to-many relation (from one, to many)

    //  
    // Entities
    //  
    Article [label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="lightblue">Article</td></tr>
            <tr><td align="left">id: int(11)</td></tr>
            <tr><td align="left">author: int(11)</td></tr>
            <tr><td align="left">title: varchar(255)</td></tr>
            <tr><td align="left">content: longtext</td></tr>
            <tr><td align="left">created: datetime</td></tr>
            <tr><td align="left">modified: datetime</td></tr>
        </table>
    >]

    Comment [label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="lightblue">Comment</td></tr>
            <tr><td align="left">id: int(11)</td></tr>
            <tr><td align="left">author: int(11)</td></tr>
            <tr><td align="left">content: longtext</td></tr>
            <tr><td align="left">created: datetime</td></tr>
            <tr><td align="left">modified: datetime</td></tr>
        </table>
    >]  

Dog [label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="lightblue">Dog</td></tr>
            <tr><td align="left">id: int(11)</td></tr>
            <tr><td align="left">author: int(11)</td></tr>
            <tr><td align="left">title: varchar(255)</td></tr>
            <tr><td align="left">content: longtext</td></tr>
            <tr><td align="left">created: datetime</td></tr>
            <tr><td align="left">modified: datetime</td></tr>
        </table>
    >]

Food [label=<
        <table border="0" cellborder="1" cellspacing="0" cellpadding="4">
            <tr><td bgcolor="lightblue">Food</td></tr>
            <tr><td align="left">id: int(11)</td></tr>
            <tr><td align="left">author: int(11)</td></tr>
            <tr><td align="left">content: longtext</td></tr>
            <tr><td align="left">created: datetime</td></tr>
            <tr><td align="left">modified: datetime</td></tr>
        </table>
    >]  
    //  
    // Relationships
    //  
    //eats [shape=box]
    about [shape = box]
    has [shape=box]
    gets [shape = box]
    // Food -> eats [arrowhead=none, arrowtail=crow,dir=both];
    //Dog -> eats [arrowhead=none, arrowtail=tee,dir=both];
    
    Food -> about [arrowhead=none, arrowtail=odot,dir=both];
    Article -> about [arrowhead=none, arrowtail=tee,dir=both];
    
    Article->has [arrowhead=none, arrowtail=crowodot,dir=both];
    Comment->has [arrowhead=none, arrowtail=crowtee,dir=both];
    
    Dog -> gets [arrowhead=none, arrowtail=crow,dir=both]
    Comment -> gets [arrowhead=none, arrowtail=none,dir=both]
}""").render('test-output/holy-grenade.gv', view=True)