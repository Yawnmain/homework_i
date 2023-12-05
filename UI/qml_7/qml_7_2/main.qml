import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    width: 300
    height: 400
    visible: true

        Rectangle {
            id: passwordField1
            color: "white"
            width: parent.width
            height: 50
            Layout.alignment: Qt.AlignCenter

            Row {
                spacing: 6
                anchors.centerIn: parent

                Repeater {
                    model: 6
                    Label {
                        width: 20
                        height: 20
                        font.pixelSize: 36
                        text: "*"
                        Layout.alignment: Qt.AlignCenter
                        color: index < passwordField.text.length ? "black" : "lightgrey"
                    }
                }
            }
        }

        GridLayout {
            id: keypad
            rows: 4
            columns: 3
            width: parent.width
            anchors.top: passwordField1.bottom
            anchors.topMargin: 20

            Button {
                text: "1"
                onClicked: {
                    passwordField.text += "1"
                    updateStarColors()
                }
            }

            Button {
                text: "2"
                onClicked: {
                    passwordField.text += "2"
                    updateStarColors()
                }
            }
            Button {
                text: "3"
                onClicked: {
                    passwordField.text += "3"
                    updateStarColors()
                }
            }
            Button {
                text: "4"
                onClicked: {
                    passwordField.text += "4"
                    updateStarColors()
                }
            }
            Button {
                text: "5"
                onClicked: {
                    passwordField.text += "5"
                    updateStarColors()
                }
            }
            Button {
                text: "6"
                onClicked: {
                    passwordField.text += "6"
                    updateStarColors()
                }
            }
            Button {
                text: "7"
                onClicked: {
                    passwordField.text += "7"
                    updateStarColors()
                }
            }
            Button {
                text: "8"
                onClicked: {
                    passwordField.text += "8"
                    updateStarColors()
                }
            }
            Button {
                text: "9"
                onClicked: {
                    passwordField.text += "9"
                    updateStarColors()
                }
            }
            Button {
                text: "Clear"
                onClicked: {
                    passwordField.text = ""
                    updateStarColors()
                }
            }
            Button {
                text: "Login"
            }
        }

        function updateStarColors() {
            for (var i = 0; i < 6; i++) {
                var star = passwordField1.children[i];
                if (i < passwordField.text.length) {
                    star.color = "black";
                } else {
                    star.color = "lightgrey";
                }
            }
        }

        TextInput {
            id: passwordField
            text: ""
            opacity: 0
        }
    }
