class Message(val address: String?, val topic: String?, val country: String?, val from: String?) {
    fun toHTML() : String {
        var template = ""
        address.let {
            template += ""
        }
        // ниже используется интерполяция строк (подстановка переменных как в PHP/Python)
        address?.let { template += "<tr><td>address</td><td>$it</td></tr> \n" }
        topic?.let { template += "<tr><td>topic</td><td>$it</td></tr> \n" }
        country?.let { template += "<tr><td>country</td><td>$it</td></tr> \n" }
        from?.let { template += "<tr><td>from</td><td>$it</td></tr> \n" }
        if (template.length == 0) {
            return ""
        }
        val head = "<!DOCTYPE html>\n" +
                "<html lang=\"en\">\n" +
                "<head>\n" +
                "    <meta charset=\"UTF-8\">\n" +
                "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" +
                "    <title>Styled Table</title>\n" +
                "    <style>\n" +
                "        table {\n" +
                "            font-family: \"Arial\", sans-serif;\n" +
                "            border-collapse: collapse;\n" +
                "            width: 40%;\n" +
                "            margin: 20px;\n" +
                "        }\n" +
                "\n" +
                "        th, td {\n" +
                "            border: 1px solid #333;\n" +
                "            padding: 10px;\n" +
                "            text-align: left;\n" +
                "            font-family: \"Helvetica Neue\", sans-serif;\n" +
                "        }\n" +
                "\n" +
                "        th {\n" +
                "            background-color: #0077b6;\n" +
                "            color: #fff;\n" +
                "        }\n" +
                "\n" +
                "        tr:nth-child(even) {\n" +
                "            background-color: #83c5be;\n" +
                "        }\n" +
                "\n" +
                "        tr:nth-child(odd) {\n" +
                "            background-color: #f0a500;\n" +
                "        }\n" +
                "    </style>\n</head>\n<body>\n"

        return  head + "<table>${template}</table>"
    }
}