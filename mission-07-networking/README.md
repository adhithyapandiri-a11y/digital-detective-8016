# Mission 7 - Networking

## 1. Task / objective

Learn the basic network terms and check how a site loads.

## 2. Work completed

| Term | Meaning | Example |
| --- | --- | --- |
| LAN | Network in a small area. | A computer lab. |
| MAN | Network across a city. | Two campuses in the same city. |
| WAN | Network over long distances. | Offices in different states. |
| DNS | Looks up records for a name, including its IP addresses. | Looking up `example.com`. |
| Router | Sends packets between networks. | A router sending traffic to the internet provider. |
| Protocol | Rules for sending and receiving data. | HTTP. |
| Packet switching | Sends data in small pieces over shared links. | A file arriving in many packets. |
| Client-server | The client asks for something and the server replies. | A browser asking for a web page. |

`curl` reached `example.com` and got HTTP 200. `dig` found two IPv4 addresses for the site, `104.20.23.154` and `172.66.147.243`, and two IPv6 addresses.

1. I type a URL in the browser. The browser is the client.
2. DNS looks up the site's address if the browser needs it.
3. The browser connects to that address. Routers pass the packets along.
4. HTTPS secures the connection. The client uses the HTTP protocol to ask for the page.
5. The server sends back a response.
6. The browser loads any other files it needs and shows the page.

## 3. Commands / tools used

`curl` checked for a reply from the site. `dig +short example.com A` checked IPv4 records and `dig +short example.com AAAA` checked IPv6 records.

## 4. My understanding

DNS gives the address. The HTTPS test tells me if I can get a reply from the website.

## 5. Difficulties faced

The lookup gave more than one address.

## 6. How I resolved them

I looked up IPv4 and IPv6 separately and recorded what each returned.

## 7. Evidence / files

The HTTP and DNS results are above.

## 8. Commit details

Local. Commit and push pending.
