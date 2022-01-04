#include "money.h"
#include "ui_money.h"
#include <QSqlDatabase>

Money::Money(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Money)
{
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    db.setHostName("10.0.0.16:3306");
    db.setDatabaseName("Pavels House_v2");
    db.setUserName("root");
    db.setPassword("Pavel31213");
    bool ok = db.open();
qDebug() << ok;

    ui->setupUi(this);
    //ui->tableWidget->insertRow(0);
    //ui->tableWidget->setItem( 0, 2, new QTableWidgetItem("Added"));

    model = new TableModel();
    ui->tableView->setModel(model);

    ui->tableView->setSelectionMode(QAbstractItemView::ExtendedSelection);
    ui->tableView->setDragEnabled(true);
    ui->tableView->viewport()->setAcceptDrops(true);
    ui->tableView->setDropIndicatorShown(true);
    ui->tableView->setDragDropMode(QAbstractItemView::DragDrop); // same as far as I can tell
    ui->tableView->setDragDropOverwriteMode(false);
}

Money::~Money()
{
    delete ui;
}
