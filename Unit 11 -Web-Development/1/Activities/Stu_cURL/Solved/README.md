# Getting Started with cURL

## Instructions

Navigate to the Postman Echo home page at: <https://docs.postman-echo.com/>

Use the documentation and examples to formulate the requests below. Note that all your requests will go to an endpoint at `https://postman-echo.com`, such as: `https://postman-echo.com/put`, etc.

- Send a GET request to the `/get` endpoint. Set the following query parameters:
  - `name`, with value equal to your name
  - `location` with value set to your current city
  - Record the URL you send your request to.
  - Be sure to wrap your URL in quotation marks!
    > **Solution**: `curl --request https://postman-echo.com/get?name=rodric&location=atlanta`

- Find your query parameters in the beginning of the response data to verify they were sent properly.

- Next, resend the request above, but use the option to print out both request/response headers.
    > **Solution**: `curl -v --request https://postman-echo.com/get?name=rodric&location=atlanta`

- The output from cURL has three sections:
  - A section at the top, with lines starting with `*`
  - The request in the middle, with lines starting with `>`
  - The response at the end, with lines starting with `<`

- Look at the section at the top.
  - What do you see in the first line that starts with `*`? What does this line indicate cURL is attempting to do?
    > **Solution**: `Connected to postman-echo.com (54.234.238.118) port 443 (#0)`. This indicates that cURL has opened a TCP connection to `54.234.238.118:443`.
  - Look at the line starting with `CAfile`. What do you think this file is for?
    > **Solution**: The CAfile contains information about the server's digital certificates. These are used to establish the HTTPS connection.
  - Look at the lines below, which start with `TLSv1.2`. Which protocol do these lines relate to? What do they imply for the rest of your communications for the server?
    > **Solution**: These lines provide details of the client/server TLS handshake, which encrypts all ensuing HTTP traffic.

- Skip down to the request.
  - Identify your query parameters in the request line.
  - What is the value of the `User-Agent` header?
    > **Solution**: `curl/7.61.1`.
  - What kind of data does the client expect?
    > **Solution**: Data of any type. Note the `Accept: */*` header.

- Skip down to the response.
  - What is the status code of the response?
    > **Solution**: `200 OK`
  - According to the headers, which kind of data does the response contain?
    > **Solution**: The headers report `Content-Type: application/json`, so this response contains JSON data.
  - What kind of server is providing the response?
    > **Solution**: The headers report `Server: nginx`, so the server is running an Apache Nginx server of unspecified version.
  - Identify your query parameters in the response.
    > **Solution**: The query parameters are visible in the request line.

- Next, send a POST request to the `/post` endpoint. Send the same data you sent as query parameters, but use cURL's `--data` option instead. 
  - Be sure to use the verbose flag to print out requests/responses.
    > **Solution**: `curl -v --request POST --url https://postman-echo.com/post --data 'name=rodric&location=davis'`

- Look at the request.
  - Which headers are present in this request that you did not see in the GET request? Why were they added?
    > **Solution**: The new headers are `Content-Length: 28` and `Content-Type: application/x-www-form-urlencoded`. These were added because the request data is now sent through the request body, _not_ in query parameters, so the request needs to tell the server how much data to expect.
  - Identify where the data you sent appears in the request.
    > **Solution**: The server echoes the submitted data in the end of the its JSON response.

- Look at the end of the response data to verify that the server received your data, even if it isn't explicitly visible in the request.

## Questions

- Use the Postman Echo documentation to define the use cases for each of the below HTTP verbs.
  - `GET`: Used to retrieve data from a server.
  - `POST`: Used to transfer data to the server, typically to create a new file, and elicit a response.
  - `PUT`: Used to transfer data to the server, often to continue an interrupted upload, and elicit a response.
  - `PATCH`: Used to update an existing resource on the server.
  - `DELETE`: Used to delete a resource on the server.
