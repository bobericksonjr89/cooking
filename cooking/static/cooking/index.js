document.addEventListener('DOMContentLoaded', function() {
    // for each button, when clicked, pass it to expand function
    document.querySelectorAll('.read-more').forEach(function(button) {
        button.onclick = function() {
            expand_recipe(button);
        }
    });

    document.querySelectorAll('.delete').forEach(function(button) {
        button.onclick = function() {
            confirm("Are you sure you want to delete this recipe?");
            // then do a delete function
            // w/ API fetch call to delete view??
        }
    })

});

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