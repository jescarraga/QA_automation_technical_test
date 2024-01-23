# Part 1

For this part of the technical test, fist **Postman** was used to develop the tests.

Begining with the **scenario 3**, making a **POST** request to the endpoint **https://the-internet.herokuapp.com/login** with the following body:

    "username": "tomsmith",
    "password": "SuperSecretPassword!"

And making the following test using javascript for Postman:

```javascript

pm.test('Status code is 200',function(){
    pm.response.to.have.status(200);
})

pm.test('Login Success',function(){
   const content_html = pm.response.text();
   const html = cheerio.load(content_html);
   const text_page = html('[ class="flash success"]').text();
   pm.expect(text_page).includes("You logged into a secure area!")
})
```

Verify that the status code is 200 and that the login was successful, using the **cheerio** library to extract the text from the html response.

The **scenario 4** was the upload of a file to the endpoint **https://the-internet.herokuapp.com/upload** using the **POST** method. The fila is a jpeg called **test_image.jpeg** and is located in this folder.

![alt text](image.png)

The test for this scenario was, verify that the status code is 200 and that the file was uploaded successfully, using the **cheerio** library to extract the text from the html response.

```javascript
pm.test('Status code is 200',function(){
    pm.response.to.have.status(200);
})
pm.variables.get("variable_key");

pm.test('Upload Success',function(){
    const content_html = pm.response.text();
    const html = cheerio.load(content_html);

    const text_page = html('[class="example"]').text();
    pm.expect(text_page).includes("File Uploaded!")
})

```

The Postman collection is located in this folder with the name
[QA_test.postman_collection](QA_test.postman_collection.json)

The second part of the technical test was to develop an automated test list using **Jmeter**.

We can use the same tests that we developed in Postman, but in this case we will use the **Jmeter** assertions.

And we will use the **Jmeter** **HTTP Request** sampler to make the requests, "recording" the requests with the **Jmeter** **HTTP(S) Test Script Recorder**. Using the Proxy Server in the **HTTP(S) Test Script Recorder**.

Also important to note that we will use the **Jmeter** **View Results Tree** to see the responses of the requests and save the cookies for the login test in the **HTTP Cookie Manager**.

The **Jmeter** test plan is located in this folder with the name [HTTP(S) Test Script Recorder](HTTP(S)_Test_Script_Recorder.jmx)