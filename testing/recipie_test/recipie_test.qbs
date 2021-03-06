import qbs.FileInfo

QtApplication {
    Depends { name: "Qt.widgets" }

    cpp.defines: [
        // You can make your code fail to compile if it uses deprecated APIs.
        // In order to do so, uncomment the following line.
        //"QT_DISABLE_DEPRECATED_BEFORE=0x060000" // disables all the APIs deprecated before Qt 6.0.0
    ]

    files: [
        "helpwindow.ui",
        "loading.ui",
        "loadingbar.ui",
        "main.cpp",
        "mainwindow.cpp",
        "mainwindow.h",
        "mainwindow.ui",
        "recipewindow.ui",
        "recipie_test_en_CA.ts",
    ]

    Group {
        fileTagsFilter: "qm"
        Qt.core.resourcePrefix: "/i18n"
        fileTags: "qt.core.resource_data"
    }

    install: true
    installDir: qbs.targetOS.contains("qnx") ? FileInfo.joinPaths("/tmp", name, "bin") : base
}
