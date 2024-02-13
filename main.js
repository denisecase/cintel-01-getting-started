/* 
Purpose: JavaScript provides the logic or behavior for the web page.

Configure two 'event listeners'.

1. One that listens continuously for the user entering their name. 
1. One that listens continuously for the user entering their favorite language(s). 

Use document.getElementById().addEventListener() to configure the event listeners.

Provide the logic when the event is triggered.
*/

document.getElementById("nameInput").addEventListener("input", () => { 
     /* Logic on updating the html element with id= 'nameInput'.

    - Use 'document.getElementById("nameInput").value' to retrieve the text 
    the user has entered into the input field and store it in a variable named 'user'.

    - Use backticks (which create a template literal) to construct a personalized greeting 
    from an embedded expression and store it in a variable named 'welcome_string'.

    - Find the html element with id='welcome' (a paragraph tag in our HTML) 
    and change its inner text to the personalized greeting. 
    
    The webpage updates in real time, displaying our custom greeting.

    TODO: Keep ${user}, but change the rest of the string to a custom greeting.
    */
    let user = document.getElementById("nameInput").value;
    let welcome_string = `Greetings ${user}!`;
    document.getElementById("welcomeOutput").innerText = welcome_string;
});

document.getElementById("languageInput").addEventListener("input", () => {
     /* Logic on updating the html element with id= 'languageInput'.*/

    let answer = document.getElementById("languageInput").value;
    let count = answer.length;
    let language_string = `You like ${answer}. That takes ${count} characters.`;
    document.getElementById("insightsOutput").innerText = language_string;
});