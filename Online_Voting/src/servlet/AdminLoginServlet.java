package servlet;

import bean.Admin;
import bean.User;
import cn.itcast.commons.CommonUtils;
import dao.AdminDao;
import service.AdminException;
import service.AdminService;



import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;


public class AdminLoginServlet extends javax.servlet.http.HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws javax.servlet.ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        request.setCharacterEncoding("UTF-8");


        Admin form = CommonUtils.toBean(request.getParameterMap(),Admin.class);
        AdminService adminService = new AdminService();

        try{
            Admin admin = adminService.login(form);
            request.getSession().setAttribute("sessionAdmin",admin);
            response.sendRedirect(request.getContextPath()+"/JSP/Admin.jsp");

        }catch (AdminException e){
            request.setAttribute("msg",e.getMessage());
            request.getRequestDispatcher("/JSP/AdminLogin.jsp").forward(request,response);
        }

    }
}
