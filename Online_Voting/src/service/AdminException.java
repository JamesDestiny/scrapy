package service;

public class AdminException extends Exception {
    //定义异常类
    public AdminException(){
        super();
    }
    public AdminException(String message,Throwable cause){
        super(message,cause);
    }
    public AdminException(String message){
        super(message);
    }
    public AdminException(Throwable cause){
        super(cause);
    }
}
