import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    width: 800
    height: 600
    visible: true

    Rectangle {
        width: 200
        height: 150
        anchors.centerIn: parent

        Column {
            spacing: 10
            anchors.centerIn: parent

            TextField {
                id: loginField
                width: 180
                placeholderText: "Enter your login"
            }

            TextField {
                id: passwordField
                width: 180
                placeholderText: "Enter your password"
                echoMode: TextInput.Password
            }

            Row {
                spacing: 10

                Button {
                    text: "Login"
                    onClicked: {
                        console.log("Login button clicked")
                    }
                }

                Button {
                    text: "Clear"
                    onClicked: {
                        loginField.text = ""
                        passwordField.text = ""
                    }
                }
            }
        }
    }
}
