function fillDropdown(withId, ofLength, withContent){
    $(function(){
    console.log("we are now executing scripts from different files")
    console.log(ofLength)
    console.log(withContent)
    var ul = $(withId)
    var tmp = withContent.split(';')
    for (var i = 0 ; i < ofLength; i++){
    //console.log(tmp[i])
    if (tmp[i] == ", u&#39"){
        continue
    }
    if (tmp[i] == "[u&#39"){
        continue
     }else{
        var string = tmp[i].substring(0,tmp[i].length-4)
        $(withId).append('<li><a>' + string + '</a></li>');
    }
    }
});
}