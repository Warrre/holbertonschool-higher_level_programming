## 1. Differences Between HTTP and HTTPS

| Criteria          | HTTP                             | HTTPS                               |
|-------------------|---------------------------------|-----------------------------------|
| Default Port      | 80                              | 443                               |
| Encryption        | None                            | SSL/TLS encryption                |
| Security          | Data sent in plain text          | Data encrypted and secure         |
| Certificate       | Not required                    | Requires SSL certificate          |
| Use Cases         | Public websites, non-sensitive  | Sites handling sensitive data (banking, login) |
| URL Prefix        | `http://`                      | `https://`                       |
| Speed             | Slightly faster                 | Slightly slower due to encryption |

**Summary:**  
HTTPS is HTTP enhanced with encryption and authentication via SSL/TLS. It protects data from interception and tampering.

---

## 2. Structure of an HTTP Request and Response

### HTTP Request Components:

- **Request Line**: Contains the HTTP method, URI, and protocol version  
  Example:  
GET /index.html HTTP/1.1

vbnet
Copier
Modifier

- **Headers**: Key-value pairs providing metadata such as Host, User-Agent, Accept  
Example:  
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html

yaml
Copier
Modifier

- **Blank Line**: Marks the end of headers

- **Body** (optional): Data sent with POST, PUT, PATCH methods

---

### HTTP Response Components:

- **Status Line**: Contains HTTP version, status code, and status message  
Example:  
HTTP/1.1 200 OK

markdown
Copier
Modifier

- **Headers**: Metadata such as Content-Type, Content-Length, Server  
Example:  
Content-Type: text/html
Content-Length: 1024

yaml
Copier
Modifier

- **Blank Line**: Marks the end of headers

- **Body**: Contains the requested content (HTML, JSON, etc.)

---

## 3. Common HTTP Methods

| Method | Description                        | Typical Use Case                  |
|--------|----------------------------------|---------------------------------|
| GET    | Retrieve data                    | Loading a webpage or API data    |
| POST   | Submit data to server             | Sending form data or creating resources |
| PUT    | Replace a resource               | Updating an entire user profile  |
| PATCH  | Modify part of a resource        | Changing one field in a profile  |
| DELETE | Remove a resource                | Deleting an article or user      |
| HEAD   | Retrieve headers only            | Checking resource metadata       |
| OPTIONS| Discover supported methods       | CORS preflight requests          |

---

## 4. Common HTTP Status Codes

### Success (2xx)

- **200 OK**: Request succeeded
- **201 Created**: New resource created
- **204 No Content**: Request succeeded but no content to return

### Redirection (3xx)

- **301 Moved Permanently**: Resource permanently moved
- **302 Found**: Temporary redirect
- **304 Not Modified**: Cached resource is still valid

### Client Errors (4xx)

- **400 Bad Request**: Request syntax invalid
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Access denied
- **404 Not Found**: Resource not found

### Server Errors (5xx)

- **500 Internal Server Error**: Server malfunction
- **502 Bad Gateway**: Invalid response from upstream server
- **503 Service Unavailable**: Server temporarily unavailable

---

## Summary

- HTTP is the base protocol for transferring data on the web.
- HTTPS adds encryption and authentication for secure communication.
- HTTP requests and responses have defined structures.
- Common HTTP methods and status codes allow clients and servers to communicate effectively.

---