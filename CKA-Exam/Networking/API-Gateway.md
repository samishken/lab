# Gateway-API
- Focuses on layer 4 and layer 7 routing
- it solves ingress limitations

##### GatewayClass
- The infrastructure providers configure the gateway class.
- GatewayClass defines what the underlying network infrastructure would be, such as the Nginx traffic or other load blancers

##### Gateway
- Cluster operators configure the gateway.
- Gateways are instances of the gatewayClass, and then we have the A CTP routes created by the application developers.

##### HTTPRoute
- Gateways create HTTPS route.

##### Ingess-Limitations
- - - - multi tenancy situations (different teams accessing different infrustructure)
- - - - 