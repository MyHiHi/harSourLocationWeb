var list = new Array();
start();
console.log(jsPlumb)

function setDot() {
    try {
        removeAllNodes();
        trans2Matrix();
        num = Number(num = $('#dot_num').val());
        s = "";
        for (var t = 1; t <= num; t++) {
            s += "<div id='" + t + "' class='item'>" + t + "</div>";
        };
        $("#diagramContainer").html(s);
        setJsPlumb(num);
    } catch (err) {
        alert('请输入节点个数！')
        console.log(err)
    }

};

function setJsPlumb(num) {
    for (var t = 1; t <= num; t++) {
        jsPlumb.addEndpoint('' + t, window.common)
        jsPlumb.draggable('' + t)
    }
}


function start() {
    jsPlumb.setContainer('diagramContainer')

    window.common = {
        isSource: true,
        isTarget: true,
        DragOptions: {
            cursor: "pointer",
            zIndex: 15
        },
        connector: 'Straight',
        endpoint: 'Dot',
        connectorStyle: {
            outlineStroke: 'green',
            strokeWidth: 1,

        },
        connectorHoverStyle: {
            strokeWidth: 2
        },
        maxConnections: -1,
        connectorOverlays: [
            ["Arrow", {
                location: 0.5
            }]
        ]

    }
    jsPlumb.bind('click', function (conn) {
        if (confirm('确定删除所点击的链接吗？')) {
            jsPlumb.deleteConnection(conn)
        }
    })
}

function trans2Matrix() {
    connections = jsPlumb.getAllConnections(); //获取所有的链接;
    for (var i in connections) {
        p3 = connections[i].sourceId; // 线的起始html元素的ID
        p4 = connections[i].targetId; // 线的目标html元素的ID
        list[i] = new Array();
        list[i][0] = p3;
        list[i][1] = p4;
    }
    console.log(arrToStr(list));
}

function removeAllNodes() {
    for (var i in jsPlumb.getAllConnections()) {
        p3 = connections[i].sourceId; // 线的起始html元素的ID
        console.log()
    }

}

function arrToStr(objarr) {
    var arrLen = objarr.length;
    var row = "[";
    for (var i = 0; i < arrLen; i++) {
        row += "[";
        for (var j = 0; j < objarr[i].length; j++) {
            row += objarr[i][j];
            if (j < objarr[i].length - 1) {
                row += ",";
            }
        }
        row += "]";
        if (i < arrLen - 1) {
            row += ",";
        }
    }
    row += "]";
    return row;
}