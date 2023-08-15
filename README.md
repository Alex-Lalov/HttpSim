# HttpSim
This is a test repository where: A client would like to access the Resource API behind an Authroization Server, therefore, the client must first authenticate with the Authroization Server in order to retrieve information from the Resource API.

There are two classes used to initialize both a client and the server app which is responsible for both authenticating and delivering the API data that the user requests. The authentication happens through confirming their id and pass, then creating a time-sensitive token for access to the API.

<img src="HttpSim.svg" alt="SVG Diagram" />