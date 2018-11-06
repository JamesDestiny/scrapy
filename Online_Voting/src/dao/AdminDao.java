package dao;


import bean.Admin;
import cn.itcast.jdbc.TxQueryRunner;
import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;

import java.sql.SQLException;


//模型层，用于处理登录（查询数据）
/*
数据类，
实现两个方法：1，添加管理员；2，根据管理名查找管理员是否存在;3,删除管理员
 */
public class AdminDao {
    //添加管理员
    public void addAdmin(Admin admin)throws SQLException{
        QueryRunner qRunner = new TxQueryRunner();
        //写出sql语句模板
        String sql = "insert into admin values(null,?,?)";
        //为sql语句添加参数
        Object[] params = {admin.getAname(),admin.getApd()};
        qRunner.update(sql,params);
    }
    //按管理员名查找管理员是否存在
    public Admin findByName(String adminname)throws SQLException{
        QueryRunner qRunner = new TxQueryRunner();
        String sql = "select * from admin where Admin_name=?";
        Object[] params = {adminname};
        Admin admin = qRunner.query(sql,new BeanHandler<Admin>(Admin.class),params);
        return admin;
    }
    //按管理员名删除管理员
    public void deleteAdmin(Admin admin)throws SQLException{
        QueryRunner qRunner = new TxQueryRunner();
        String sql = "delete from admin where Admin_name=？";
        Object[] params = {admin.getAname()};
        qRunner.update(sql,params);
    }

}
