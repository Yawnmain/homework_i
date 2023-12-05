import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    width: 800
    height: 600
    visible: true

    Rectangle {
        id: trafficLight
        width: 100
        height: 300
        color: "black"
        anchors.centerIn: parent

        states: [
            State {
                name: "stop"
                PropertyChanges { target: redLight; visible: true; color: "red" }
                PropertyChanges { target: yellowLight; visible: false }
                PropertyChanges { target: greenLight; visible: false }
            },
            State {
                name: "caution"
                PropertyChanges { target: redLight; visible: false }
                PropertyChanges { target: yellowLight; visible: true; color: "yellow" }
                PropertyChanges { target: greenLight; visible: false }
            },
            State {
                name: "go"
                PropertyChanges { target: redLight; visible: false }
                PropertyChanges { target: yellowLight; visible: false }
                PropertyChanges { target: greenLight; visible: true; color: "green" }
            }
        ]

        transitions: [
            Transition {
                from: "stop"; to: "caution"
                SequentialAnimation {
                    ColorAnimation { target: redLight; property: "color"; to: "black"; duration: 500 }
                    ColorAnimation { target: yellowLight; property: "color"; to: "yellow"; duration: 500 }
                }
            },
            Transition {
                from: "caution"; to: "go"
                ColorAnimation { target: yellowLight; property: "color"; to: "black"; duration: 500 }
                ColorAnimation { target: greenLight; property: "color"; to: "green"; duration: 500 }
            },
            Transition {
                from: "go"; to: "stop"
                SequentialAnimation {
                    ColorAnimation { target: greenLight; property: "color"; to: "black"; duration: 500 }
                    ColorAnimation { target: redLight; property: "color"; to: "red"; duration: 500 }
                }
            }
        ]

        Rectangle {
            id: redLight
            width: 80
            height: 80
            radius: width / 2
            color: "black"
            anchors.horizontalCenter: trafficLight.horizontalCenter
            anchors.top: trafficLight.top
        }

        Rectangle {
            id: yellowLight
            width: 80
            height: 80
            radius: width / 2
            color: "black"
            anchors.horizontalCenter: trafficLight.horizontalCenter
            anchors.top: redLight.bottom
            anchors.topMargin: 20
        }

        Rectangle {
            id: greenLight
            width: 80
            height: 80
            radius: width / 2
            color: "black"
            anchors.horizontalCenter: trafficLight.horizontalCenter
            anchors.top: yellowLight.bottom
            anchors.topMargin: 20
        }

        MouseArea {
            anchors.fill: parent
            onClicked: {
                if (trafficLight.state === "stop") {
                    trafficLight.state = "caution";
                } else if (trafficLight.state === "caution") {
                    trafficLight.state = "go";
                } else {
                    trafficLight.state = "stop";
                }
            }
        }
    }
}
