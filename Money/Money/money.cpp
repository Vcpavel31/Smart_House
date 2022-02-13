#include "money.h"
#include "ui_money.h"
#include <QSqlDatabase>

Money::Money(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Money)
{
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    db.setHostName("10.0.0.16");
    db.setPort(3306);
    db.setDatabaseName("Pavels House_v2");
    db.setUserName("root");
    db.setPassword("Pavel31213");
    bool ok = db.open();
qDebug() << ok;

    QSqlQuery query;

    qDebug() <<  query.exec("SELECT * FROM `Values`");
 qDebug() << query.lastError().text();
    while(query.next())
        {
            qDebug()<<query.value(0).toInt()<<","<<query.value(1).toString();
        }

    ui->setupUi(this);

    model = new TableModel();
    ui->tableView->setModel(model);



    ui->tableView->setSelectionMode(QAbstractItemView::ExtendedSelection);
    ui->tableView->setDragEnabled(true);
    ui->tableView->viewport()->setAcceptDrops(true);
    ui->tableView->setDropIndicatorShown(true);
    ui->tableView->setDragDropMode(QAbstractItemView::DragDrop);
    ui->tableView->setDragDropOverwriteMode(false);
}

Money::~Money()
{
    delete ui;
}
