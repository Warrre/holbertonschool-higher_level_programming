# Using an API with `curl` in the command line

In this document, we will explore how to use the `curl` tool to interact with REST APIs, step by step, with clear explanations and concrete examples.

---

## 1. What is `curl`?

**curl** (Client URL) is a command line tool for transferring data to or from a server via protocols such as HTTP, HTTPS, FTP, etc.  
It is widely used for testing, debugging, and consuming RESTful APIs.

---

## 2. Installing and verifying `curl`

- **Linux (Debian/Ubuntu):**  
        
        sudo apt install curl


- **macOS:**  

        brew install curl


- **Windows:**  
Use [WSL](https://docs.microsoft.com/fr-fr/windows/wsl/) or download curl for Windows.

**Verification:**

        curl --version


*Displays the version of curl and the supported protocols.*

---

## 3. Performing a simple GET request

To retrieve the content of a web page: 
        curl http://example.com
This returns the raw HTML of the example.com page. This is equivalent to visiting the site with a browser, but without the display.

To query a public API (JSONPlaceholder):
        curl https://jsonplaceholder.typicode.com/posts/1

**Example output:**

        {
        ‘userId’: 1,
        ‘id’: 1,
        ‘title’: ‘sunt aut facere repellat...’,
        ‘body’: ‘quia et suscipit...’
        }

#### ASCII diagram of the flow

        [Terminal] --GET--> [API server] <-- JSON --

---

## 4. Retrieve only the HTTP headers

Use the `-I` option to obtain only the response headers:
        curl -I https://jsonplaceholder.typicode.com/posts


**Example output:**

        HTTP/2 200
        content-type: application/json; charset=utf-8
        date: Wed, 11 Jun 2025 14:00:00 GMT

---

## 5. Perform a POST request

To send data and simulate the creation of a resource:
        curl -X POST -d ‘title=foo&body=bar&userId=1’ https://jsonplaceholder.typicode.com/posts

**Example output:**
        {
        ‘title’: ‘foo’,
        ‘body’: ‘bar’,
        ‘userId’: ‘1’,
        ‘id’: 101
        }

*Note: JSONPlaceholder does not actually create the resource; it simulates creation with a fictitious ID.*

#### ASCII diagram of the POST request

        [Terminal] --POST (data)--> [API server] <-- JSON (new simulated object) --

---

## 6. Explanation of the `curl` options used

| Option         | Role                                                                 |
|----------------|---------------------------------------------------------------------|
| `-I`           | Retrieves only HTTP headers                               |
| `-X <METHOD>`  | Specifies the HTTP method (GET, POST, PUT, DELETE, etc.)             |
| `-d`           | Sends data in the request body (used with POST)   |

---

Translated with DeepL.com (free version)


## 7. Tip: Format JSON output

To improve the readability of JSON responses, use the [jq](https://stedolan.github.io/jq/) tool:
        curl -s https://jsonplaceholder.typicode.com/posts | jq

text

---

## 8. Visual summary of an API request cycle with `curl`

        +----------------+ (HTTP request) +-------------------+
        | Terminal  | ---------------------- -> |  API server |
        | (curl) | <--------------------- | (JSONPlaceholder) |
        +----------------+ (JSON response) +-------------------+

---

## Conclusion

`curl` is a powerful and versatile tool for exploring, testing, and consuming REST APIs directly from the terminal.  
It allows you to:

- Retrieve resources (**GET**)
- Send data (**POST**)
- Inspect HTTP headers
- Automate API testing

Translated with DeepL.com (free version)
