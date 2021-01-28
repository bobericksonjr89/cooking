document.addEventListener('DOMContentLoaded', function() {
    // for each button, when clicked, pass it to expand function
    document.querySelectorAll('.read-more').forEach(function(button) {
        button.onclick = function() {
            expand_recipe(button);
        }
    });

    // click detection on delete buttons
    document.querySelectorAll('.delete').forEach(function(button) {
        button.onclick = function() {
                delete_recipe(button);
        }
    });

});


function delete_recipe(button) {
    var result = confirm("Are you sure you want to delete this recipe?");
        if (result) {
            // finds closest parent element with this class
            const box = button.closest(".recipe-box");

            // finds html element with the recipe name, then gets the name
            var name_element = button.parentElement.parentElement.querySelector(".recipe-name")
            if (name_element == null){ // because read-more moves the edit button 
                name_element = button.parentElement.parentElement.parentElement.querySelector(".recipe-name")
            }
            const name = name_element.innerHTML;

            // removes it from the DOM
            box.remove();

            // get csrf token for fetch request
            let csrftoken = getCookie('csrftoken')

            // send cookie and recipe name to delete view
            fetch('/delete', {
                method: 'POST',
                body: JSON.stringify({
                    name: name,
                }),
                headers: { "X-CSRFToken": csrftoken }
                
                })
                .then(response => response.json())
                .then(result => {
                console.log(result);
                });
                
        }
};


function expand_recipe(button) {
    // get the parent element of clicked button (the recipe box)
    recipe = button.parentElement;
    // change directions CSS to display
    directions = recipe.getElementsByClassName("recipe-expand")[0];

    // get recipe creator div
    creator = recipe.getElementsByClassName("recipe-creator")[0];
 
    // display directions
    directions.style.display = 'block';

    // move creator div to end of directions
    directions.appendChild(creator);
    
    // hide show-more button
    button.style.display = 'none';
    
    // find the new read less button
    less = directions.children[1]
    

    // on click, hide directions, and redisplay show more button
    less.addEventListener('click', function() {
        expand = this.parentElement;
        
        // get recipe-details div
        details = expand.parentElement;
        
        // get read-more button & creator div
        button = details.getElementsByClassName("read-more")[0];
        creator = details.getElementsByClassName("recipe-creator")[0];

        // move creator div back into details
        details.appendChild(creator);

        // hide directions and show read-more button
        expand.style.display = 'none';
        button.style.display = 'block';
    });
};

// The following function is copied from 
// https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};