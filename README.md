# HttpSim
This is a test repository where: A client would like to access the Resource API behind an Authroization Server, therefore, the client must first authenticate with the Authroization Server in order to retrieve information from the Resource API.

There are two classes used to initialize both a client and the server app which is responsible for both authenticating and delivering the API data that the user requests. The authentication happens through confirming their id and pass, then creating a time-sensitive token for access to the API.

```xml
<mxfile host="app.diagrams.net" modified="2023-08-15T11:04:13.415Z" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0" etag="iZK7VFny68Y3KHihJ6qJ" version="21.6.8">
  <diagram name="Page-1" id="jYjiMla6c40iE5C-QNtF">
    <mxGraphModel dx="1221" dy="733" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="413" pageHeight="291" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="a7vI6LvmLqN712RE4e46-7" value="App" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=none;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="55" y="200" width="300" height="260" as="geometry" />
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-9" value="A class to start the app&lt;br&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; Attributes&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; ----------&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; users : List[Client]&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; a list of clients that are in the database&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; tokens : List[(int, datetime)]&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; a list of tokens and the time they were initialized&lt;br&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; Methods&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; -------&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; setup_routes(self)&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; sets up both the server and the resource API&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; run(self)&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; starts the server of port 5000" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="a7vI6LvmLqN712RE4e46-7">
          <mxGeometry y="26" width="300" height="234" as="geometry" />
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-13" value="Client" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=none;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="490" y="157" width="280" height="280" as="geometry" />
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-22" value="initializes one" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="a7vI6LvmLqN712RE4e46-13" target="a7vI6LvmLqN712RE4e46-19">
          <mxGeometry width="80" relative="1" as="geometry">
            <mxPoint x="140" as="sourcePoint" />
            <mxPoint x="139.5" y="-60" as="targetPoint" />
            <Array as="points">
              <mxPoint x="140" y="-87" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-14" value="A class to create clients&lt;br&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; Attributes&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; ----------&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; id : str&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; a string containing the id/name of a client&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; password : str&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; the pass or secret that is used&lt;br&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; Methods&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; -------&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; __eq__(self, other)&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; Overloads the equivelance of the class&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp; getClientData(self)&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; Returns client json data" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="a7vI6LvmLqN712RE4e46-13">
          <mxGeometry y="26" width="280" height="254" as="geometry" />
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-18" value="Use" style="endArrow=open;endSize=12;dashed=1;html=1;rounded=0;entryX=0;entryY=0.413;entryDx=0;entryDy=0;entryPerimeter=0;exitX=1.01;exitY=0.346;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="1" source="a7vI6LvmLqN712RE4e46-9" target="a7vI6LvmLqN712RE4e46-14">
          <mxGeometry width="160" relative="1" as="geometry">
            <mxPoint x="340" y="230" as="sourcePoint" />
            <mxPoint x="500" y="230" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-19" value="main" style="html=1;whiteSpace=wrap;" vertex="1" parent="1">
          <mxGeometry x="575" y="40" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-20" value="Server" style="html=1;whiteSpace=wrap;" vertex="1" parent="1">
          <mxGeometry x="150" y="40" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-21" value="instance of" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=elbowEdgeStyle;elbow=horizontal;curved=0;rounded=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="a7vI6LvmLqN712RE4e46-7" target="a7vI6LvmLqN712RE4e46-20">
          <mxGeometry width="80" relative="1" as="geometry">
            <mxPoint x="170" y="140" as="sourcePoint" />
            <mxPoint x="250" y="140" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-23" value="" style="endArrow=block;startArrow=block;endFill=1;startFill=1;html=1;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="a7vI6LvmLqN712RE4e46-20" target="a7vI6LvmLqN712RE4e46-19">
          <mxGeometry width="160" relative="1" as="geometry">
            <mxPoint x="330" y="60" as="sourcePoint" />
            <mxPoint x="490" y="60" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="a7vI6LvmLqN712RE4e46-24" value="Get/Post" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="a7vI6LvmLqN712RE4e46-23">
          <mxGeometry x="0.1746" y="1" relative="1" as="geometry">
            <mxPoint x="-31" as="offset" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

```