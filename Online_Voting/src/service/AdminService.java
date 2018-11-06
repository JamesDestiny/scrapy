
package service;


import bean.Admin;
import dao.AdminDao;

import java.sql.SQLException;

//实现逻辑功能层，
public class AdminService {
    //service 依赖dao层
    private AdminDao  adminDao= new AdminDao();
    //实现管理员登录功能
    public Admin login(Admin form)throws AdminException{
        Admin admin = null;
        try {
            admin = adminDao.findByName(form.getAname());
        }catch (SQLException e){
            e.printStackTrace();
        }
        if (admin==null){
            throw new AdminException("管理员不存在");
        }
        if ((!form.getApd().equals(admin.getApd()))){
            throw new AdminException("管理员密码错误！");
        }
        return admin;
    }

}

