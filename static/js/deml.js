const slider=document.querySelector('.slider');
const leftArrow=document.querySelector('.left');
const rightArrow=document.querySelector('.right');
var sectionIndex=0;
leftArrow.addEventListener('click', function() {
    sectionIndex = (sectionIndex > 0) ? sectionIndex - 1 : 0;
    slider.style.transform = 'translate(' + (sectionIndex) * -25 + '%)';
});
rightArrow.addEventListener('click', function() {
    sectionIndex = (sectionIndex < 3) ? sectionIndex + 1 : 3;
    slider.style.transform = 'translate(' + (sectionIndex) * -25 + '%)';
});



/*function getConfirm(myid)
{
    result=confirm("Are you sure you want to delete(y/n)?")
    if(result)
    {
        myform=document.getElementById(myid)
        myform.submit();

    }
}*/