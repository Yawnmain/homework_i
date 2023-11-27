import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 400
    title: "Прямоугольная фигура"

    Rectangle {
        width: 200
        height: 200
        color: "lightblue"
        anchors.centerIn: parent
    }

    Rectangle {
        width: 50
        height: 50
        color: "red"
        anchors.top: parent.top
        anchors.left: parent.left
    }

    Rectangle {
        width: 50
        height: 50
        color: "green"
        anchors.top: parent.top
        anchors.right: parent.right
    }

    Rectangle {
        width: 50
        height: 50
        color: "yellow"
        anchors.bottom: parent.bottom
        anchors.left: parent.left
    }

    Rectangle {
        width: 50
        height: 50
        color: "purple"
        anchors.bottom: parent.bottom
        anchors.right: parent.right
    }
}
