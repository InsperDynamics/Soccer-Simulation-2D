/****************************************************************************
** Meta object code from reading C++ file 'config_dialog.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.12.8)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "config_dialog.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'config_dialog.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.12.8. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_FontButton_t {
    QByteArrayData data[4];
    char stringdata0[35];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_FontButton_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_FontButton_t qt_meta_stringdata_FontButton = {
    {
QT_MOC_LITERAL(0, 0, 10), // "FontButton"
QT_MOC_LITERAL(1, 11, 11), // "fontChanged"
QT_MOC_LITERAL(2, 23, 0), // ""
QT_MOC_LITERAL(3, 24, 10) // "fontDialog"

    },
    "FontButton\0fontChanged\0\0fontDialog"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_FontButton[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   24,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       3,    0,   25,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void,

       0        // eod
};

void FontButton::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<FontButton *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->fontChanged(); break;
        case 1: _t->fontDialog(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (FontButton::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&FontButton::fontChanged)) {
                *result = 0;
                return;
            }
        }
    }
    Q_UNUSED(_a);
}

QT_INIT_METAOBJECT const QMetaObject FontButton::staticMetaObject = { {
    &QPushButton::staticMetaObject,
    qt_meta_stringdata_FontButton.data,
    qt_meta_data_FontButton,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *FontButton::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *FontButton::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_FontButton.stringdata0))
        return static_cast<void*>(this);
    return QPushButton::qt_metacast(_clname);
}

int FontButton::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QPushButton::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void FontButton::fontChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
struct qt_meta_stringdata_ConfigDialog_t {
    QByteArrayData data[87];
    char stringdata0[1436];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_ConfigDialog_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_ConfigDialog_t qt_meta_stringdata_ConfigDialog = {
    {
QT_MOC_LITERAL(0, 0, 12), // "ConfigDialog"
QT_MOC_LITERAL(1, 13, 10), // "configured"
QT_MOC_LITERAL(2, 24, 0), // ""
QT_MOC_LITERAL(3, 25, 13), // "canvasResized"
QT_MOC_LITERAL(4, 39, 4), // "size"
QT_MOC_LITERAL(5, 44, 9), // "updateAll"
QT_MOC_LITERAL(6, 54, 15), // "slideFieldScale"
QT_MOC_LITERAL(7, 70, 5), // "value"
QT_MOC_LITERAL(8, 76, 14), // "editFieldScale"
QT_MOC_LITERAL(9, 91, 27), // "slotTeamGraphicScaleChanged"
QT_MOC_LITERAL(10, 119, 21), // "clickShowPlayerNumber"
QT_MOC_LITERAL(11, 141, 7), // "checked"
QT_MOC_LITERAL(12, 149, 19), // "clickShowPlayerType"
QT_MOC_LITERAL(13, 169, 16), // "clickShowStamina"
QT_MOC_LITERAL(14, 186, 24), // "clickShowStaminaCapacity"
QT_MOC_LITERAL(15, 211, 17), // "clickShowViewArea"
QT_MOC_LITERAL(16, 229, 18), // "clickShowCatchArea"
QT_MOC_LITERAL(17, 248, 19), // "clickShowTackleArea"
QT_MOC_LITERAL(18, 268, 22), // "clickShowKickAccelArea"
QT_MOC_LITERAL(19, 291, 16), // "clickShowPointto"
QT_MOC_LITERAL(20, 308, 13), // "clickShowCard"
QT_MOC_LITERAL(21, 322, 23), // "clickShowIllegalDefense"
QT_MOC_LITERAL(22, 346, 19), // "clickShowScoreBoard"
QT_MOC_LITERAL(23, 366, 21), // "clickShowKeepawayArea"
QT_MOC_LITERAL(24, 388, 20), // "clickShowTeamGraphic"
QT_MOC_LITERAL(25, 409, 17), // "clickShowDrawInfo"
QT_MOC_LITERAL(26, 427, 13), // "clickShowBall"
QT_MOC_LITERAL(27, 441, 15), // "clickShowPlayer"
QT_MOC_LITERAL(28, 457, 13), // "clickShowFlag"
QT_MOC_LITERAL(29, 471, 20), // "clickShowOffsideLine"
QT_MOC_LITERAL(30, 492, 18), // "clickShowGridCoord"
QT_MOC_LITERAL(31, 511, 13), // "slideGridStep"
QT_MOC_LITERAL(32, 525, 12), // "editGridStep"
QT_MOC_LITERAL(33, 538, 4), // "text"
QT_MOC_LITERAL(34, 543, 17), // "clickAntiAliasing"
QT_MOC_LITERAL(35, 561, 14), // "clickFocusBall"
QT_MOC_LITERAL(36, 576, 16), // "clickFocusPlayer"
QT_MOC_LITERAL(37, 593, 18), // "clickSelectAutoAll"
QT_MOC_LITERAL(38, 612, 19), // "clickSelectAutoLeft"
QT_MOC_LITERAL(39, 632, 20), // "clickSelectAutoRight"
QT_MOC_LITERAL(40, 653, 14), // "clickSelectFix"
QT_MOC_LITERAL(41, 668, 12), // "choicePlayer"
QT_MOC_LITERAL(42, 681, 6), // "number"
QT_MOC_LITERAL(43, 688, 18), // "changeBallVelCycle"
QT_MOC_LITERAL(44, 707, 16), // "selectColorEntry"
QT_MOC_LITERAL(45, 724, 16), // "QListWidgetItem*"
QT_MOC_LITERAL(46, 741, 4), // "item"
QT_MOC_LITERAL(47, 746, 15), // "setDefaultColor"
QT_MOC_LITERAL(48, 762, 11), // "cancelColor"
QT_MOC_LITERAL(49, 774, 16), // "updateFieldScale"
QT_MOC_LITERAL(50, 791, 6), // "zoomIn"
QT_MOC_LITERAL(51, 798, 7), // "zoomOut"
QT_MOC_LITERAL(52, 806, 11), // "fitToScreen"
QT_MOC_LITERAL(53, 818, 15), // "applyCanvasSize"
QT_MOC_LITERAL(54, 834, 20), // "toggleShowScoreBoard"
QT_MOC_LITERAL(55, 855, 22), // "toggleShowKeepawayArea"
QT_MOC_LITERAL(56, 878, 21), // "toggleShowTeamGraphic"
QT_MOC_LITERAL(57, 900, 14), // "toggleShowFlag"
QT_MOC_LITERAL(58, 915, 16), // "toggleShowPlayer"
QT_MOC_LITERAL(59, 932, 14), // "toggleShowBall"
QT_MOC_LITERAL(60, 947, 22), // "toggleShowPlayerNumber"
QT_MOC_LITERAL(61, 970, 20), // "toggleShowPlayerType"
QT_MOC_LITERAL(62, 991, 17), // "toggleShowStamina"
QT_MOC_LITERAL(63, 1009, 25), // "toggleShowStaminaCapacity"
QT_MOC_LITERAL(64, 1035, 18), // "toggleShowViewArea"
QT_MOC_LITERAL(65, 1054, 19), // "toggleShowCatchArea"
QT_MOC_LITERAL(66, 1074, 20), // "toggleShowTackleArea"
QT_MOC_LITERAL(67, 1095, 23), // "toggleShowKickAccelArea"
QT_MOC_LITERAL(68, 1119, 17), // "toggleShowPointto"
QT_MOC_LITERAL(69, 1137, 14), // "toggleShowCard"
QT_MOC_LITERAL(70, 1152, 24), // "toggleShowIllegalDefense"
QT_MOC_LITERAL(71, 1177, 21), // "toggleShowOffsideLine"
QT_MOC_LITERAL(72, 1199, 18), // "toggleShowDrawInfo"
QT_MOC_LITERAL(73, 1218, 12), // "editBallSize"
QT_MOC_LITERAL(74, 1231, 14), // "editPlayerSize"
QT_MOC_LITERAL(75, 1246, 15), // "toggleFocusBall"
QT_MOC_LITERAL(76, 1262, 17), // "toggleFocusPlayer"
QT_MOC_LITERAL(77, 1280, 11), // "setFocusFix"
QT_MOC_LITERAL(78, 1292, 13), // "setFocusPoint"
QT_MOC_LITERAL(79, 1306, 5), // "point"
QT_MOC_LITERAL(80, 1312, 19), // "toggleSelectAutoAll"
QT_MOC_LITERAL(81, 1332, 20), // "toggleSelectAutoLeft"
QT_MOC_LITERAL(82, 1353, 21), // "toggleSelectAutoRight"
QT_MOC_LITERAL(83, 1375, 15), // "toggleSelectFix"
QT_MOC_LITERAL(84, 1391, 11), // "setUnselect"
QT_MOC_LITERAL(85, 1403, 19), // "selectPlayerWithKey"
QT_MOC_LITERAL(86, 1423, 12) // "selectPlayer"

    },
    "ConfigDialog\0configured\0\0canvasResized\0"
    "size\0updateAll\0slideFieldScale\0value\0"
    "editFieldScale\0slotTeamGraphicScaleChanged\0"
    "clickShowPlayerNumber\0checked\0"
    "clickShowPlayerType\0clickShowStamina\0"
    "clickShowStaminaCapacity\0clickShowViewArea\0"
    "clickShowCatchArea\0clickShowTackleArea\0"
    "clickShowKickAccelArea\0clickShowPointto\0"
    "clickShowCard\0clickShowIllegalDefense\0"
    "clickShowScoreBoard\0clickShowKeepawayArea\0"
    "clickShowTeamGraphic\0clickShowDrawInfo\0"
    "clickShowBall\0clickShowPlayer\0"
    "clickShowFlag\0clickShowOffsideLine\0"
    "clickShowGridCoord\0slideGridStep\0"
    "editGridStep\0text\0clickAntiAliasing\0"
    "clickFocusBall\0clickFocusPlayer\0"
    "clickSelectAutoAll\0clickSelectAutoLeft\0"
    "clickSelectAutoRight\0clickSelectFix\0"
    "choicePlayer\0number\0changeBallVelCycle\0"
    "selectColorEntry\0QListWidgetItem*\0"
    "item\0setDefaultColor\0cancelColor\0"
    "updateFieldScale\0zoomIn\0zoomOut\0"
    "fitToScreen\0applyCanvasSize\0"
    "toggleShowScoreBoard\0toggleShowKeepawayArea\0"
    "toggleShowTeamGraphic\0toggleShowFlag\0"
    "toggleShowPlayer\0toggleShowBall\0"
    "toggleShowPlayerNumber\0toggleShowPlayerType\0"
    "toggleShowStamina\0toggleShowStaminaCapacity\0"
    "toggleShowViewArea\0toggleShowCatchArea\0"
    "toggleShowTackleArea\0toggleShowKickAccelArea\0"
    "toggleShowPointto\0toggleShowCard\0"
    "toggleShowIllegalDefense\0toggleShowOffsideLine\0"
    "toggleShowDrawInfo\0editBallSize\0"
    "editPlayerSize\0toggleFocusBall\0"
    "toggleFocusPlayer\0setFocusFix\0"
    "setFocusPoint\0point\0toggleSelectAutoAll\0"
    "toggleSelectAutoLeft\0toggleSelectAutoRight\0"
    "toggleSelectFix\0setUnselect\0"
    "selectPlayerWithKey\0selectPlayer"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_ConfigDialog[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      77,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,  399,    2, 0x06 /* Public */,
       3,    1,  400,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       5,    0,  403,    2, 0x08 /* Private */,
       6,    1,  404,    2, 0x08 /* Private */,
       8,    1,  407,    2, 0x08 /* Private */,
       9,    1,  410,    2, 0x08 /* Private */,
      10,    1,  413,    2, 0x08 /* Private */,
      12,    1,  416,    2, 0x08 /* Private */,
      13,    1,  419,    2, 0x08 /* Private */,
      14,    1,  422,    2, 0x08 /* Private */,
      15,    1,  425,    2, 0x08 /* Private */,
      16,    1,  428,    2, 0x08 /* Private */,
      17,    1,  431,    2, 0x08 /* Private */,
      18,    1,  434,    2, 0x08 /* Private */,
      19,    1,  437,    2, 0x08 /* Private */,
      20,    1,  440,    2, 0x08 /* Private */,
      21,    1,  443,    2, 0x08 /* Private */,
      22,    1,  446,    2, 0x08 /* Private */,
      23,    1,  449,    2, 0x08 /* Private */,
      24,    1,  452,    2, 0x08 /* Private */,
      25,    1,  455,    2, 0x08 /* Private */,
      26,    1,  458,    2, 0x08 /* Private */,
      27,    1,  461,    2, 0x08 /* Private */,
      28,    1,  464,    2, 0x08 /* Private */,
      29,    1,  467,    2, 0x08 /* Private */,
      30,    1,  470,    2, 0x08 /* Private */,
      31,    1,  473,    2, 0x08 /* Private */,
      32,    1,  476,    2, 0x08 /* Private */,
      34,    1,  479,    2, 0x08 /* Private */,
      35,    0,  482,    2, 0x08 /* Private */,
      36,    0,  483,    2, 0x08 /* Private */,
      37,    0,  484,    2, 0x08 /* Private */,
      38,    0,  485,    2, 0x08 /* Private */,
      39,    0,  486,    2, 0x08 /* Private */,
      40,    0,  487,    2, 0x08 /* Private */,
      41,    1,  488,    2, 0x08 /* Private */,
      43,    1,  491,    2, 0x08 /* Private */,
      44,    1,  494,    2, 0x08 /* Private */,
      47,    0,  497,    2, 0x08 /* Private */,
      48,    0,  498,    2, 0x08 /* Private */,
      49,    0,  499,    2, 0x0a /* Public */,
      50,    0,  500,    2, 0x0a /* Public */,
      51,    0,  501,    2, 0x0a /* Public */,
      52,    0,  502,    2, 0x0a /* Public */,
      53,    0,  503,    2, 0x0a /* Public */,
      54,    0,  504,    2, 0x0a /* Public */,
      55,    0,  505,    2, 0x0a /* Public */,
      56,    0,  506,    2, 0x0a /* Public */,
      57,    0,  507,    2, 0x0a /* Public */,
      58,    0,  508,    2, 0x0a /* Public */,
      59,    0,  509,    2, 0x0a /* Public */,
      60,    0,  510,    2, 0x0a /* Public */,
      61,    0,  511,    2, 0x0a /* Public */,
      62,    0,  512,    2, 0x0a /* Public */,
      63,    0,  513,    2, 0x0a /* Public */,
      64,    0,  514,    2, 0x0a /* Public */,
      65,    0,  515,    2, 0x0a /* Public */,
      66,    0,  516,    2, 0x0a /* Public */,
      67,    0,  517,    2, 0x0a /* Public */,
      68,    0,  518,    2, 0x0a /* Public */,
      69,    0,  519,    2, 0x0a /* Public */,
      70,    0,  520,    2, 0x0a /* Public */,
      71,    0,  521,    2, 0x0a /* Public */,
      72,    0,  522,    2, 0x0a /* Public */,
      73,    1,  523,    2, 0x0a /* Public */,
      74,    1,  526,    2, 0x0a /* Public */,
      75,    0,  529,    2, 0x0a /* Public */,
      76,    0,  530,    2, 0x0a /* Public */,
      77,    0,  531,    2, 0x0a /* Public */,
      78,    1,  532,    2, 0x0a /* Public */,
      80,    0,  535,    2, 0x0a /* Public */,
      81,    0,  536,    2, 0x0a /* Public */,
      82,    0,  537,    2, 0x0a /* Public */,
      83,    0,  538,    2, 0x0a /* Public */,
      84,    0,  539,    2, 0x0a /* Public */,
      85,    0,  540,    2, 0x0a /* Public */,
      86,    1,  541,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::QSize,    4,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    7,
    QMetaType::Void, QMetaType::QString,    2,
    QMetaType::Void, QMetaType::Double,    7,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Int,    7,
    QMetaType::Void, QMetaType::QString,   33,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,   42,
    QMetaType::Void, QMetaType::Int,    7,
    QMetaType::Void, 0x80000000 | 45,   46,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString,   33,
    QMetaType::Void, QMetaType::QString,   33,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QPoint,   79,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,   42,

       0        // eod
};

void ConfigDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<ConfigDialog *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->configured(); break;
        case 1: _t->canvasResized((*reinterpret_cast< const QSize(*)>(_a[1]))); break;
        case 2: _t->updateAll(); break;
        case 3: _t->slideFieldScale((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->editFieldScale((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->slotTeamGraphicScaleChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 6: _t->clickShowPlayerNumber((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->clickShowPlayerType((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 8: _t->clickShowStamina((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->clickShowStaminaCapacity((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->clickShowViewArea((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 11: _t->clickShowCatchArea((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 12: _t->clickShowTackleArea((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 13: _t->clickShowKickAccelArea((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 14: _t->clickShowPointto((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 15: _t->clickShowCard((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 16: _t->clickShowIllegalDefense((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 17: _t->clickShowScoreBoard((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 18: _t->clickShowKeepawayArea((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 19: _t->clickShowTeamGraphic((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 20: _t->clickShowDrawInfo((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 21: _t->clickShowBall((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 22: _t->clickShowPlayer((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 23: _t->clickShowFlag((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 24: _t->clickShowOffsideLine((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 25: _t->clickShowGridCoord((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 26: _t->slideGridStep((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 27: _t->editGridStep((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 28: _t->clickAntiAliasing((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 29: _t->clickFocusBall(); break;
        case 30: _t->clickFocusPlayer(); break;
        case 31: _t->clickSelectAutoAll(); break;
        case 32: _t->clickSelectAutoLeft(); break;
        case 33: _t->clickSelectAutoRight(); break;
        case 34: _t->clickSelectFix(); break;
        case 35: _t->choicePlayer((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 36: _t->changeBallVelCycle((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 37: _t->selectColorEntry((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 38: _t->setDefaultColor(); break;
        case 39: _t->cancelColor(); break;
        case 40: _t->updateFieldScale(); break;
        case 41: _t->zoomIn(); break;
        case 42: _t->zoomOut(); break;
        case 43: _t->fitToScreen(); break;
        case 44: _t->applyCanvasSize(); break;
        case 45: _t->toggleShowScoreBoard(); break;
        case 46: _t->toggleShowKeepawayArea(); break;
        case 47: _t->toggleShowTeamGraphic(); break;
        case 48: _t->toggleShowFlag(); break;
        case 49: _t->toggleShowPlayer(); break;
        case 50: _t->toggleShowBall(); break;
        case 51: _t->toggleShowPlayerNumber(); break;
        case 52: _t->toggleShowPlayerType(); break;
        case 53: _t->toggleShowStamina(); break;
        case 54: _t->toggleShowStaminaCapacity(); break;
        case 55: _t->toggleShowViewArea(); break;
        case 56: _t->toggleShowCatchArea(); break;
        case 57: _t->toggleShowTackleArea(); break;
        case 58: _t->toggleShowKickAccelArea(); break;
        case 59: _t->toggleShowPointto(); break;
        case 60: _t->toggleShowCard(); break;
        case 61: _t->toggleShowIllegalDefense(); break;
        case 62: _t->toggleShowOffsideLine(); break;
        case 63: _t->toggleShowDrawInfo(); break;
        case 64: _t->editBallSize((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 65: _t->editPlayerSize((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 66: _t->toggleFocusBall(); break;
        case 67: _t->toggleFocusPlayer(); break;
        case 68: _t->setFocusFix(); break;
        case 69: _t->setFocusPoint((*reinterpret_cast< const QPoint(*)>(_a[1]))); break;
        case 70: _t->toggleSelectAutoAll(); break;
        case 71: _t->toggleSelectAutoLeft(); break;
        case 72: _t->toggleSelectAutoRight(); break;
        case 73: _t->toggleSelectFix(); break;
        case 74: _t->setUnselect(); break;
        case 75: _t->selectPlayerWithKey(); break;
        case 76: _t->selectPlayer((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (ConfigDialog::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&ConfigDialog::configured)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (ConfigDialog::*)(const QSize & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&ConfigDialog::canvasResized)) {
                *result = 1;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject ConfigDialog::staticMetaObject = { {
    &QDialog::staticMetaObject,
    qt_meta_stringdata_ConfigDialog.data,
    qt_meta_data_ConfigDialog,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *ConfigDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *ConfigDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_ConfigDialog.stringdata0))
        return static_cast<void*>(this);
    return QDialog::qt_metacast(_clname);
}

int ConfigDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 77)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 77;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 77)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 77;
    }
    return _id;
}

// SIGNAL 0
void ConfigDialog::configured()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void ConfigDialog::canvasResized(const QSize & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
