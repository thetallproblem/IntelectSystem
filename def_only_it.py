def only_it(rus, math, it, summary, sphere, plan):
    if sphere == 1:
        if plan == 1:
            if summary >= 207:
                if summary >= 221:
                    if summary >= 236:
                        if summary >= 254:
                            if rus >= 56 and math >= 45 and it >= 53:
                                if math >= 50 and it >= 65:
                                    return "Бюджет", ["Программная инженерия",
                                                      "Искусственный интеллект и разработка программных продуктов",
                                                      "DevOps-инженерия в администрировании инфраструктуры "
                                                      "ИТ-разработки",
                                                      "Искусственный интеллект и большие данные"]

                                return "Бюджет", [
                                    "Искусственный интеллект и разработка программных продуктов",
                                    "DevOps-инженерия в администрировании инфраструктуры ИТ-разработки",
                                    "Искусственный интеллект и большие данные"]

                        if rus >= 56 and math >= 45 and it >= 53:
                            return "Бюджет", [
                                "DevOps-инженерия в администрировании инфраструктуры ИТ-разработки",
                                "Искусственный интеллект и большие данные"]

                    if rus >= 56 and math >= 45 and it >= 53:
                        return "Бюджет", ["Искусственный интеллект и разработка программных продуктов",
                                          "DevOps-инженерия в администрировании инфраструктуры ИТ-разработки",
                                          "Искусственный интеллект и большие данные"]

                if rus >= 56 and math >= 45 and it >= 53:
                    return "Бюджет", ["DevOps-инженерия в администрировании инфраструктуры "
                                      "ИТ-разработки"]

        if plan == 2:
            if summary >= 118:
                if summary >= 228:
                    if rus >= 40 and math >= 39 and it >= 44:
                        if rus >= 56 and math >= 50 and it >= 65:
                            return "Платное", ["Программная инженерия",
                                               "Искусственный интеллект и разработка программных "
                                               "продуктов",
                                               "DevOps-инженерия в администрировании инфраструктуры "
                                               "ИТ-разработки",
                                               "Искусственный интеллект и большие данные"]

                        return "Платное", [
                            "Искусственный интеллект и разработка программных продуктов",
                            "DevOps-инженерия в администрировании инфраструктуры ИТ-разработки",
                            "Искусственный интеллект и большие данные"]

                if rus >= 40 and math >= 39 and it >= 44:
                    return "Платное", ["Искусственный интеллект и разработка программных продуктов",
                                       "DevOps-инженерия в администрировании инфраструктуры "
                                       "ИТ-разработки",
                                       "Искусственный интеллект и большие данные"]

    if sphere == 2:
        if plan == 1:
            if summary >= 169:
                if summary >= 171:
                    if summary >= 174:
                        if rus >= 50 and math >= 39 and it >= 44:
                            if rus >= 56 and math >= 45 and it >= 53:
                                return "Бюджет", [
                                    "Современная математика и математическое моделирование",
                                    "Вычислительная математика и компьютерное моделирование",
                                    "Прикладная математика и инженерия цифровых проектов",
                                    "Математическое моделирование и информационные системы"]

                            return "Бюджет", ["Современная математика и математическое моделирование",
                                              "Вычислительная математика и компьютерное моделирование"]

                    if rus >= 56 and math >= 45 and it >= 53:
                        return "Бюджет", [
                            "Вычислительная математика и компьютерное моделирование",
                            "Прикладная математика и инженерия цифровых проектов"]

                if rus >= 50 and math >= 39 and it >= 44:
                    return "Бюджет", ["Вычислительная математика и компьютерное моделирование"]

        if plan == 2:
            if summary >= 118:
                if rus >= 40 and math >= 39 and it >= 44:
                    return "Платное", [
                        "Современная математика и математическое моделирование",
                        "Вычислительная математика и компьютерное моделирование",
                        "Прикладная математика и инженерия цифровых проектов",
                        "Математическое моделирование и информационные системы"]

    if sphere == 3:
        if plan == 1:
            if summary >= 128:
                if summary >= 185:
                    if rus >= 50 and math >= 39 and it >= 44:
                        return "Бюджет", ["Информационные системы и технологии",
                                          "Программное и аппаратное обеспечение БАС"]

                if rus >= 50 and math >= 39 and it >= 44:
                    return "Бюджет", ["Программное и аппаратное обеспечение БАС"]

        if plan == 2:
            if summary >= 118:
                if rus >= 40 and math >= 39 and it >= 44:
                    return "Платное", ["Информационные системы и технологии",
                                       "Программное и аппаратное обеспечение БАС"]

    if sphere == 4:
        if plan == 1:
            if summary >= 171:
                if rus >= 50 and math >= 39 and it >= 44:
                    if rus >= 56 and math >= 45 and it >= 53:
                        return "Бюджет", ["Управление инновациями в наукоемких технологиях",
                                          "Математические методы в цифровой экономике"]

                    return "Бюджет", ["Управление инновациями в наукоемких технологиях"]

        if plan == 2:
            if summary >= 118:
                if rus >= 40 and math >= 39 and it >= 44:
                    return "Платное", ["Управление инновациями в наукоемких технологиях",
                                       "Математические методы в цифровой экономике"]

    return 0, 0
