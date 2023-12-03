import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

ApplicationWindow {
    width: 480
    height: 720
    visible: true
    title: "qml_3"

    property int check: 0

    Column {
        anchors.fill: parent
        spacing: 10

        Rectangle {
            width: parent.width
            height: 100
            color: "gray"
            Text {
                anchors.centerIn: parent
                text: ["Header 1", "Header 2", "Header 3"][check]
            }
        }

        Item {
            width: parent.width
            height: parent.height - 100

            Rectangle {
                width: parent.width
                height: parent.height - 50 - 3 * 20
                color: "lightgray"
                Text {
                    anchors.centerIn: parent
                    text: ["Item 1 content", "Item 2 content", "Item 3 content"][check]
                }
            }

            Row {
                width: parent.width
                height: 100
                spacing: 10
                anchors.bottom: parent.bottom

                Repeater {
                    model: 3
                    Rectangle {
                        width: parent.width / 3
                        height: parent.height
                        color: check === index ? "#bbbbbb" : "gray"
                        opacity: check === index ? 1 : 0.5
                        MouseArea {
                            anchors.fill: parent
                            onClicked: check = index
                            Text {
                                anchors.centerIn: parent
                                text: "item " + (index + 1)
                            }
                        }
                    }
                }
            }
        }
    }
}
