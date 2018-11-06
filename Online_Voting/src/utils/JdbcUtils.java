package utils;

import java.util.Properties;
import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JdbcUtils {
    private static Properties properties = null;
    //只在该类被加载时执行一次
    static{
        try{
            //1.加载配置文件
            InputStream inputStream=JdbcUtils.class.getClassLoader().getResourceAsStream("dbconfig.properties");
            //2.将配置文件信息装载
            properties=new Properties();
            properties.load(inputStream);
        }catch (IOException e) {
            throw new RuntimeException(e);
        }
        //3.加载驱动类
        try {
            Class.forName(properties.getProperty("driverClassName"));
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
    public static Connection getConnection() throws IOException, ClassNotFoundException, SQLException{

        //4.得到连接
        Connection connection = DriverManager.getConnection(properties.getProperty("url"),
                properties.getProperty("dbUsername"),
                properties.getProperty("dbPassword"));
        return connection;
    }

}
