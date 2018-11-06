<%--
  Created by IntelliJ IDEA.
  User: hasee
  Date: 2018/10/30
  Time: 15:08
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
  String path = request.getContextPath();
  String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<html>
  <head>
    <title>管理员登录</title>
    <link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/css/bootstrap.min.css"/>

    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache">
    <meta http-equiv="expires" content="0">
    <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
    <meta http-equiv="description" content="This is my page">
    <!--
    <link rel="stylesheet" type="text/css" href="styles.css">
    -->

  </head>
  <body>
  <div class="container">
    <br>
    <div class=" col-sm-offset-2"><a href="${pageContext.request.contextPath}/index.jsp">返回首页</a> </div>
    <br>
    <p style="color: red ; font-weight: 600">${msg }</p>
    <form class="form-horizontal" action="${pageContext.request.contextPath}/AdminLoginServlet" method="post">
      <div class="form-group">
        <label for="username" class="col-sm-2 control-label">管理员名</label>
        <div class="col-sm-8">
          <input type="text" class="form-control" name="Aname" id="Aname" placeholder="管理员名">
        </div>
      </div>
      <div class="form-group">
        <label for="password" class="col-sm-2 control-label">密码</label>
        <div class="col-sm-8">
          <input type="password" class="form-control" name="Apd" id="Apd" placeholder="密码">
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
          <button type="submit" class="btn btn btn-info" id="login">登录</button>
        </div>
      </div>
    </form>
  </div>
  <script type="text/javascript">
      window.onload=function(){
          var u=document.getElementById('Aname');
          var psw=document.getElementById('Apd');
          var lo=document.getElementById('login');
          lo.onclick=function(){
              if(u.value==""||psw.value==""){
                  alert("账号或密码不能为空");
                  return false;
              }
          }
      }
  </script>

  </body>
</html>
