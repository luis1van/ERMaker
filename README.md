## Final Report
[Final Report](https://drive.google.com/open?id=1eB2naox96PNpPuj6PmeTIWg4CF8UD_3Z)

## Motivation
Entity Relationship diagrams(ER-diagrams) are typically used in computing to organize data within databases and information systems. These graphical representations of entities and their relationships to each other are particularly useful during the conceptual-design and review phases of databases. 

Often drag and drop software as to other programming languages are tedious to use, resulting in complex learning processes and time consumption. ERMaker is a high-level programing language developed as an alternative for drawing ER-diagrams. 


## Language Features
ERmaker will allow the user to draw, through a console, the following major components of an ER-diagram:
1. Rectangles divided into two parts: These will represent entity sets. The top part will represent the name of the entity set. The      bottom part will contain the names of the attributes corresponding to that particular entity set.
2. Small Rectangles: These will represent relationship sets.
3. Lines: link relationship sets to entity sets.
4. Mapping cardinality:The user will be able to specify if the cardinality is one-to-one, one-to-many, many-to-one or many-to-many.
5. Modality: State whether an entity’s participation in a relationship is mandatory or optional.

## Video
<video src="
https://r3---sn-hp57kn7z.c.drive.google.com/videoplayback?id=7c3ee3c6fa822a51&itag=22&source=webdrive&requiressl=yes&mm=30&mn=sn-hp57kn7z&ms=nxu&mv=u&pl=24&sc=yes&ttl=transient&ei=FCoQXImcFpLWqwXGuKnABA&susc=dr&driveid=1NfOmJEIu9PFFBdDMsXo0N5gToadCiTGb&app=texmex&mime=video/mp4&dur=62.833&lmt=1544562249071471&mt=1544562970&ip=136.145.214.12&ipbits=0&expire=1544577620&cp=QVNJVkZfVlZQQVhOOkpXam1oU2F3TVhR&sparams=ip,ipbits,expire,id,itag,source,requiressl,mm,mn,ms,mv,pl,sc,ttl,ei,susc,driveid,app,mime,dur,lmt,cp&signature=27C6B22B2E862B5C3661D402A86D123D037C5A47241DDB0699455A43CDFD93FB.CF8E28E7170C75ED46D1C7E0D2869BED966DA0CEB190E8D94DEF00BC0B5917FF&key=us0&cpn=8CLowfImqAIsaq2u&c=WEB_EMBEDDED_PLAYER&cver=20181208" width="600" height="380" controls preload></video>
```markdown
Sample Code:

>> many Professor can teach many course
>> many Student take many Course
>> a university has many Student
>> a University Offers many Course
>> a University employs many Professor
>> Student composed of ID, Name, Phone
>> University composed of Name, Address
>> Professor composed of ID, Name
>> Course composed of Name, Subject, Section

```
<img src="https://lh5.googleusercontent.com/iomq-4IDmWhDuy-nu2uBgDCxCxHak9yW0JFcCbDmv2Ul3PGQWpLPvQxl2NoTSM6eK3gDvfILeVDo3tI-aWQ5=w958-h830-rw" alt="hi" class="inline"/>
## Approach

### Modules and Interfaces

The libraries that comprise the application are PLY and Graphviz . PLY contains the Yacc and the Lex modules that are used as the base for the implementation of the parser and lexer. Then, the Graphviz library was used to render the graphs by using raw dot language to describe them. 

Our custom modules include ERLex, ERModel and ERGraph. The ERLex module contains the main code of the application, which implements the different elements of the language in the lexer using Lex and the grammatical elements using Yacc.  The ERModel module contains the definition and implementation of the graph object used to store the model for the ER. It consists of methods to instantiate a graph and  add, edit, and traverse through the nodes and edges, where nodes represent entities and edges represent relations.The ERGraph module contains the elements needed for the construction of the raw dot structure, required to draw the graph in graphviz.


### Development Environment

- Python 3: the language used for development.
- PLY: Lexer and parser used.
- Grphviz: rendering engine for ER graphs.
- PyCharm: the main IDE used for development.
- Github: used as our Version Control to track changes and as a collaborative tool.



## Team

ER Maker team is comprised of Luis Padro and Lumaris Rios. This project was developed as part of the Programming Language course (ICOM4036) directed by Dr. Wilson Rivera.
