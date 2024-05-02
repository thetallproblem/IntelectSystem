def only_physics(rus, math, physics, summary, sphere, plan):
    if sphere == 2:
        if plan == 1:
            if summary >= 169:
                if summary >= 174:
                    if rus >= 50 and math >= 39 and physics >= 39:
                        return "Бюджет", ["Современная математика и математическое моделирование",
                                          "Вычислительная математика и компьютерное моделирование"]

                if rus >= 50 and math >= 39 and physics >= 39:
                    return "Бюджет", ["Вычислительная математика и компьютерное моделирование"]

        if plan == 2:
            if summary >= 118:
                if rus >= 40 and math >= 39 and physics >= 39:
                    return "Платное", ["Современная математика и математическое моделирование",
                                       "Вычислительная математика и компьютерное моделирование"]

    if sphere == 3:
        if plan == 1:
            if summary >= 128:
                if summary >= 185:
                    if rus >= 50 and math >= 39 and physics >= 39:
                        return "Бюджет", ["Информационные системы и технологии",
                                          "Программное и аппаратное обеспечение БАС"]

                if rus >= 50 and math >= 39 and physics >= 39:
                    return "Бюджет", ["Программное и аппаратное обеспечение БАС"]

        if plan == 2:
            if summary >= 118:
                if rus >= 40 and math >= 39 and physics >= 39:
                    return "Платное", ["Информационные системы и технологии",
                                       "Программное и аппаратное обеспечение БАС"]

    if sphere == 4:
        if plan == 1:
            if summary >= 171:
                if rus >= 50 and math >= 39 and physics >= 39:
                    return "Бюджет", ["Управление инновациями в наукоемких технологиях"]

        if plan == 2:
            if summary >= 118:
                if rus >= 40 and math >= 39 and physics >= 39:
                    return "Платное", ["Управление инновациями в наукоемких технологиях"]

    return 0, 0
