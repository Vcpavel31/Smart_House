#ifndef MONEY_H
#define MONEY_H

#include <QMainWindow>
#include <QSqlQuery>
#include <QSqlError>

#include <tablemodel.h>

QT_BEGIN_NAMESPACE
namespace Ui { class Money; }
QT_END_NAMESPACE

class Money : public QMainWindow
{
    Q_OBJECT

    TableModel *model;

public:
    Money(QWidget *parent = nullptr);
    ~Money();

private:
    Ui::Money *ui;

};
#endif // MONEY_H
