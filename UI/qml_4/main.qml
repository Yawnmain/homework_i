import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: "Messenger"

    ListModel {
        id: messageModel
        ListElement { message: "Привет!" }
        ListElement { message: "Как дела?" }
        ListElement { message: "Что нового?" }
    }

    Column {
        anchors.fill: parent

        ListView {
            id: messageListView
            width: parent.width
            height: parent.height - inputRow.height - 10
            model: messageModel
            delegate: Text {
                text: model.message
                wrapMode: Text.Wrap
                font.pixelSize: 16
                padding: 10
            }
        }

        Row {
            id: inputRow
            width: parent.width
            height: 50

            TextField {
                id: messageInput
                width: parent.width - sendButton.width - 10
                placeholderText: "Введите сообщение..."
            }

            Button {
                id: sendButton
                width: 100
                height: parent.height
                text: "Отправить"
                onClicked: {
                    if (messageInput.text !== "") {
                        messageModel.append({ "message": messageInput.text })
                        messageInput.text = ""
                        messageListView.positionViewAtEnd()
                    }
                }
            }
        }
    }
}
