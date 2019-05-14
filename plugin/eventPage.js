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
                newTotal += budget.total;
                newTotal += clickData.selectionText;
                chrome.storage.sync.set({'total': newTotal}, function(){               
                });
            });
        
    }
});

chrome.storage.onChanged.addListener(function(changes, storageName){
    chrome.browserAction.setBadgeText({"text": changes.total.newValue.toString()});
});
