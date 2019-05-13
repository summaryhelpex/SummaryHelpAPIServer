var menuItem = {
    "id": "selectText",
    "title": "SelectText",
    "contexts": ["selection"]
};

chrome.contextMenus.create(menuItem);

chrome.contextMenus.onClicked.addListener(function(clickData){   
    if (clickData.menuItemId == "selectText" && clickData.selectionText){            
            chrome.storage.sync.get(['total'], function(budget){
                var newTotal = "";
                newTotal += clickData.selectionText;
                chrome.storage.sync.set({'total': newTotal}, function(){               
                });
            });
            // 이 데이터를 서버에 보내고,

            // 데이ㅓ를 서버에서 받고
            

            //알람을 띠워준다.
            //alert("hi");

    }
});

chrome.storage.onChanged.addListener(function(changes, storageName){
    chrome.browserAction.setBadgeText({"text": changes.total.newValue.toString()});
});
