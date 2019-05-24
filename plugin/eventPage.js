var menuItem = {
    "id": "selectText",
    "title": "SelectText",
    "contexts": ["selection"]
};
// 우클릭시 우리 메뉴가 나타나게 한다.
chrome.contextMenus.create(menuItem);

//드레그 후 우리의 메뉴를 클릭했을 때, 해당 text를 storage에 저장한다.
chrome.contextMenus.onClicked.addListener(function(clickData){   
    if (clickData.menuItemId == "selectText" && clickData.selectionText){            
        var newTotal = "";
        newTotal += clickData.selectionText;
        chrome.storage.sync.set({'total': newTotal}, function(){               
        });
    }
});


// 해당 text가 저장이 된 event가 발생했일때, 우리 메뉴에 text가 들어왔다는 표시를 해준다.
chrome.storage.onChanged.addListener(function(changes, storageName){
    chrome.browserAction.setBadgeText({"text": changes.total.newValue.toString()});
});

$('.starRev span').click(function(){
    $(this).parent().children('span').removeClass('on');
    $(this).addClass('on').prevAll('span').addClass('on');
    return false;
  });