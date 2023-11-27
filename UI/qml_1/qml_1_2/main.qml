import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

ApplicationWindow {
    visible: true
    width: 720
    height: 1080
    title: "qml_1_2"

    Rectangle {
        id: mainRect
        width: parent.width
        height: parent.height

        Rectangle {
            id: header
            width: parent.width
            height: 100
            color: "grey"
            Text {
                anchors.centerIn: parent
                text: "Header"
                color: "black"
            }
        }

        Rectangle {
            id: content
            width: parent.width
            height: parent.height - header.height - footerRow.height - 20
            color: "white"
            anchors.top: header.bottom
            anchors.margins: 10
            anchors.bottom: footerRow.top
            Text {
                anchors.centerIn: parent
                text: "Content"
                color: "black"
            }
        }

        Row {
            id: footerRow
            width: parent.width
            height: 100
            anchors.bottom: parent.bottom
            spacing: 10

            Repeater {
                model: 3
                Rectangle {
                    width: parent.width / 3
                    height: parent.height
                    color: "grey"
                    Text {
                        anchors.centerIn: parent
                        text: (index + 1)
                        color: "black"
                    }
                }
            }
        }
    }
}
