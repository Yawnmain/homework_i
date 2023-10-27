import java.io.File

fun main(args: Array<String>) {
    val mess = Message("yawnishe.671@yandex.ru", null, "RU", "Arnold")
    val output = File("html.html")
    output.writeText(mess.toHTML())
}
