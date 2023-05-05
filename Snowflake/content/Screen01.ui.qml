

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.2
import QtQuick.Controls 6.2
import Snowflake

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    TextInput {
        id: textInput
        x: 51
        y: 1786
        width: 978
        height: 87
        text: qsTr("Text Input")
        font.pixelSize: 34
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        cursorVisible: false
        selectionColor: "#4d4df4"
        font.family: "Courier"
    }
    states: [
        State {
            name: "clicked"
            when: button.checked
        }
    ]
}
