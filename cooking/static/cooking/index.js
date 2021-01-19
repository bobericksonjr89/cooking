document.addEventListener('DOMContentLoaded', function() {
    // for each button, when clicked, pass it to expand function
    document.querySelectorAll('.read-more').forEach(function(button) {
        button.onclick = function() {
            expand_recipe(button);
        }
    });

});

function expand_recipe(button) {
    // get the parent element of clicked button (the recipe box)
    recipe = button.parentElement;
    // change directions CSS to display
    directions = recipe.getElementsByClassName("recipe-expand")[0];
    directions.style.display = 'block';
    button.style.display = 'none';
    
    console.log(directions);

    // find the new read less button
    less = directions.children[1]
    console.log(less)

    // on click, hide directions, and redisplay show more button
    less.addEventListener('click', function() {
        expand = this.parentElement;
        console.log(expand)
        details = expand.parentElement;
        console.log(details)
        button = details.getElementsByClassName("read-more")[0];
        console.log(button)

        expand.style.display = 'none';
        button.style.display = 'block';
    });




    // TO DO: make read more button disappear (display: none;)
    // have a read less button at bottom instead (hardcoded but hidden?)
    // when read less clicked, directions box display:none and read more diplay: block;

    // SIMPLE!!
}