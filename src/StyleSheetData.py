splitter_style = "QSplitter::handle:vertical { border-color: #2b303b; width: 0px }"

layout_widget_style = "background-color: #2b303b;"

tree_view_style = "QTreeView { "\
                  "    border: none;"\
                  "    color: #eff1f5; "\
                  "    background-color: transparent; "\
                  "    selection-background-color: transparent;"\
                  "    selection-color: transparent;"\
                  "    show-decoration-selected: 1;"\
                  "}"\
                  "QTreeView::item:hover {"\
                  "    background: #65737e;"\
                  "}"\
                  "QTreeView::item:selected {"\
                  "    color: white;"\
                  "    background: #65737e;"\
                  "}"\
                  "QTreeView::branch:has-children:!has-siblings:closed,"\
                  "QTreeView::branch:closed:has-children:has-siblings"\
                  "{"\
                  "    border-image: none;"\
                  "    image: url(../assets/images/branch_closed.png);"\
                  "}"\
                  "QTreeView::branch:open:has-children:!has-siblings,"\
                  "QTreeView::branch:open:has-children:has-siblings"\
                  "{"\
                  "    border-image: none;"\
                  "    image: url(../assets/images/branch_open.png);"\
                  "}"

push_button_style = "QPushButton {"\
                    "   color: rgb(255,255,255)"\
                    "}"

delete_button_style = "QPushButton { "\
                       "    background-color: transparent;"\
                       "    border-image: url(../assets/images/del_course_button.png);"\
                       "    background: none;"\
                       "    border: none;"\
                       "    background-repeat: none;"\
                       "    min-width: 32px;"\
                       "    max-width: 32px;"\
                       "    min-height: 32px;"\
                       "    max-height: 32px;"\
                       "}"\
                       "QPushButton:hover { "\
                       "    border-image: url(../assets/images/del_course_button_highlight.png); "\
                       "}"\
                       "QPushButton:pressed { "\
                       "    border-image: url(../assets/images/del_course_button_pressed.png); "\
                       "}"

add_button_style = "QPushButton { "\
                   "    background-color: transparent;"\
                   "    border-image: url(../assets/images/add_course_button.png);"\
                   "    background: none;"\
                   "    border: none;"\
                   "    background-repeat: none;"\
                   "    min-width: 32px;"\
                   "    max-width: 32px;"\
                   "    min-height: 32px;"\
                   "    max-height: 32px;"\
                   "}"\
                   "QPushButton:hover { "\
                   "    border-image: url(../assets/images/add_course_button_highlight.png); "\
                   "}"\
                   "QPushButton:pressed { "\
                   "    border-image: url(../assets/images/add_course_button_pressed.png); "\
                   "}"

grade_sheet_style = "QTableWidget {"\
                    "   border: none;"\
                    "   background-color: #eff1f5;"\
                    "   selection-background-color: #b48ead;"\
                    "}"\
                    "QTableCornerButton::section {"\
                    "   background-color: red;"\
                    "   border: 2px transparent red;"\
                    "   border-radius: 0px;"\
                    "}"

horiz_header_style = "QHeaderView::section{ border: none; background-color: #c0c5ce}"\
                     "QHeaderView::section:checked { background-color: #bf616a}"

vert_header_style = "QHeaderView::section{ "\
                    "   border: none;"\
                    "   padding: 6px;"\
                    "   background-color: #c0c5ce"\
                    "}"\
                    "QHeaderView::section:checked { background-color: #bf616a}"
