import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

ApplicationWindow {
    width: 800
    height: 600
    visible: true

            Button {
                id: backButton
                text: "<-"
                visible: stackView.depth > 1
                onClicked: stackView.pop()
                z: 1
            }


    StackView {
        id: stackView
        anchors.fill: parent

        Component {
            id: redPage
            Rectangle {
                width: stackView.width
                height: stackView.height
                color: "red"

                property string itemName: "Page Red"

                Text {
                    anchors.centerIn: parent
                    text: itemName
                    color: "white"
                    font.pixelSize: 20
                }

                Row {
                    anchors.bottom: parent.bottom
                    anchors.horizontalCenter: parent.horizontalCenter

                    Button {
                        text: "Green"
                        onClicked: stackView.push(greenPage.createObject())
                    }
                    Button {
                        text: "Yellow"
                        onClicked: stackView.push(yellowPage.createObject())
                    }
                }
            }
        }

        Component {
            id: greenPage
            Rectangle {
                width: stackView.width
                height: stackView.height
                color: "green"

                property string itemName: "Page Green"

                Text {
                    anchors.centerIn: parent
                    text: itemName
                    color: "white"
                    font.pixelSize: 20
                }

                Row {
                    anchors.bottom: parent.bottom
                    anchors.horizontalCenter: parent.horizontalCenter

                    Button {
                        text: "Red"
                        onClicked: stackView.push(redPage.createObject())
                    }
                    Button {
                        text: "Yellow"
                        onClicked: stackView.push(yellowPage.createObject())
                    }
                }
            }
        }

        Component {
            id: yellowPage
            Rectangle {
                width: stackView.width
                height: stackView.height
                color: "yellow"

                property string itemName: "Page Yellow"

                Text {
                    anchors.centerIn: parent
                    text: itemName
                    color: "black"
                    font.pixelSize: 20
                }

                Row {
                    anchors.bottom: parent.bottom
                    anchors.horizontalCenter: parent.horizontalCenter

                    Button {
                        text: "Red"
                        onClicked: stackView.push(redPage.createObject())
                    }
                    Button {
                        text: "Green"
                        onClicked: stackView.push(greenPage.createObject())
                    }
                }
            }
        }

        initialItem: redPage
        onCurrentItemChanged: {
            backButton.visible = stackView.depth > 1;
            header_page_text.text = stackView.currentItem ? stackView.currentItem.itemName : "Home";
        }
    }
}
