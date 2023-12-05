import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    width: 300
    height: 400
    visible: true

    SwipeView {
        id: view
        currentIndex: 0
        anchors.fill: parent
        interactive: SwipeView.ForceElasticity

        Item {
            id: redPage
            Rectangle {
                color: "red"
                anchors.fill: parent
                Text {
                    text: "Red Light"
                    color: "white"
                    anchors.centerIn: parent
                }
            }
        }

        Item {
            id: yellowPage
            Rectangle {
                color: "yellow"
                anchors.fill: parent
                Text {
                    text: "Yellow Light"
                    color: "black"
                    anchors.centerIn: parent
                }
            }
        }

        Item {
            id: greenPage
            Rectangle {
                color: "green"
                anchors.fill: parent
                Text {
                    text: "Green Light"
                    color: "white"
                    anchors.centerIn: parent
                }
            }
        }
    }

    PageIndicator {
        id: indicator
        count: view.count
        currentIndex: view.currentIndex
        anchors.bottom: view.bottom
        anchors.horizontalCenter: parent.horizontalCenter
    }
}
