import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    width: 920
    height: 480
    visible: true

    ColumnLayout {
        anchors.fill: parent
        spacing: 10

        Rectangle {
            id: rect1
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
