# Mission 07 — Computer Networking

## 1. Task / objective

The objective of this mission was to understand networking concepts, perform a connectivity test, use DNS lookup and explain how a website communicates with a server.

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | Local Area Network covering a small geographical area | Home or college computer lab network |
| MAN | Metropolitan Area Network covering a city or large campus | A city-wide network |
| WAN | Wide Area Network covering large geographical areas | The Internet |
| DNS | Domain Name System translates domain names into IP addresses | Resolving example.com |
| Router | Connects networks and forwards data between them | Home Wi-Fi router |
| Protocol | A set of rules that devices follow to communicate | HTTP and HTTPS |
| Packet switching | Divides data into packets that travel across a network | Sending data over the Internet |
| Client-server | A model in which a client requests a service and a server provides it | A browser requesting a webpage |

### Task 7.2 — Observe network information

**Connectivity test**

Used the following command:

```bash
ping -c 4 example.com
```

Observed results:

- Packets transmitted: 4
- Packets received: 4
- Packet loss: 0%
- Average response time: 43.837 ms

This test confirmed that my computer could communicate with the example website during the test.

**DNS lookup**

Used:

```bash
nslookup example.com
```

Observed IPv4 addresses:

- 104.20.23.154
- 172.66.147.243

DNS helps translate a website's domain name into an IP address so that a device can locate the correct server.

### Task 7.3 — What happens when you open a website?

1. The user enters a website address into a web browser.
2. The browser checks whether it already has the required information available.
3. DNS resolves the domain name into an IP address if needed.
4. The client device sends a request through the network and router.
5. The request reaches the website's server using suitable communication protocols.
6. The server processes the request and sends a response to the client.
7. The browser receives the response and displays the webpage to the user.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `ping -c 4 example.com` | Tests connectivity with a public domain |
| `nslookup example.com` | Looks up DNS information for a domain |
| Terminal | Used to execute networking commands |

## 4. My understanding

A computer network allows devices to communicate and exchange information. LAN, MAN and WAN describe networks based on their geographical coverage. DNS translates domain names into IP addresses, while routers forward data between networks. Protocols define communication rules, and packet switching allows information to travel in smaller packets. The client-server model explains how browsers request information from website servers.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-07-networking/README.md`
- Successful ping test with four packets received.
- Successful DNS lookup for example.com.

## 8. Commit details

- Commit message: `Explain networking concepts and website communication`
- Push status: Pending GitHub verification.