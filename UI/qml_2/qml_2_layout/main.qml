import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    width: 800
    height: 600
    visible: true
    title: "qml_2_layout"

    ColumnLayout {
        anchors.fill: parent
        spacing: 10

        // Header
        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 50
            color: "gray"
            Text {
                anchors.centerIn: parent
                text: "Header"
            }
        }

        // Content
        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: parent.height - 160 // Высота Header + Footer
            color: "white"
            Text {
                anchors.centerIn: parent
                text: "Content"
            }
        }

        // Footer
        RowLayout {
            Layout.fillWidth: true
            Layout.preferredHeight: 100
            spacing: 10

            Repeater {
                model: 3
                Rectangle {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    color: "gray"
                    Text {
                        anchors.centerIn: parent
                        text: (index + 1)
                    }
                }
            }
        }
    }
}
