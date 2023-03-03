# Lab assignment 2:
The main focus of the mandatory assignment is to build and test a multi-threaded server. You will
implement:
* a server that can simultaneously handle multiple clients.
* a client that will connect to the server.
## Task 
      - implement a function named broadcast to:
          1. notify everyone when a client joins (except the client who joined).
          2. to broadcast a message from a client to everyone.
          
        Based on the server’s requirements, A client should:
          * connect to the server
          * receive broadcast message from a server
          * send a message to the server for broadcast
