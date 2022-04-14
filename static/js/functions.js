const ogList = document.querySelectorAll(".oglist");
const tab = document.querySelectorAll(".tabShow");

function changeTabs(panelIndex)
{
    tab.forEach(function(node) {
        node.style.display = "none";
});
    tab[panelIndex].style.display = "block";
}
changeTabs(0);

