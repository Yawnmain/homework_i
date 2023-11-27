import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    width: 920
    height: 480
    visible: true

    RowLayout {
        anchors.fill: parent

        Rectangle {
            id: rect1
            Layout.fillWidth: true
            Layout.preferredHeight: 120
            border.width: 1
            color: Qt.rgba(Math.random(), Math.random(), Math.random(), 0.7)
            Text {
                text: "My color:" + rect1.color
                anchors.centerIn: rect1
                font.pixelSize: 24
            }
        }

        Item {
            Layout.fillHeight: true
            Layout.preferredHeight: 10
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 120
            border.width: 1
            color: Qt.rgba(Math.random(), Math.random(), Math.random(), 0.7)
            Text {
                text: "My color:" + rect1.color
                anchors.centerIn: parent
                font.pixelSize: 24
            }
        }

        Item {
            Layout.fillHeight: true
            Layout.preferredHeight: 10
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 120
            border.width: 1
            color: Qt.rgba(Math.random(), Math.random(), Math.random(), 0.7)
            Text {
                text: "My color:" + rect1.color
                anchors.centerIn: parent
                font.pixelSize: 24
            }
        }
    }
}
