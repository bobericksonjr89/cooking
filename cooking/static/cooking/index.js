document.addEventListener('DOMContentLoaded', function() {
    // for each button, when clicked, pass it to expand function
    document.querySelectorAll('button').forEach(function(button) {
        button.onclick = function() {
            expand_recipe(button);
        }
    });

});

function expand_recipe(button) {
    // get the parent element of clicked button (the recipe box)
    recipe = button.parentElement;
    // change direction CSS to display it
    directions = recipe.getElementsByClassName("recipe-directions")[0];
    directions.style.display = 'block';
    
    console.log(directions);

    // TO DO: make read more button dissapear (display: none;)
    // have a read less button at bottom instead (hardcoded but hidden?)
    // when read less clicked, directions box display:none and read more diplay: block;

    // SIMPLE!!
}