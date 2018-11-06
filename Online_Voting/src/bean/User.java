package bean;



public class User {
    private int Uid;
    private String Uname;
    private String Upwd;
    private String Uphonenumber;
    private String Uaddress;
    private String Umail;
    private String verifyCode;

    public User(){

    }
    public User(String Uname,String Upwd){
        this.Uname= Uname;
        this.Upwd= Upwd;
    }

    public User(String Uname,String Upwd,String Uphonenumber,String Uaddress,String Umail){
        this.Upwd=Upwd;
        this.Uname=Uname;
        this.Uaddress=Uaddress;
        this.Uphonenumber=Uphonenumber;
        this.Umail=Umail;
    }

    public int getUid() {
        return Uid;
    }

    public String getUaddress() {
        return Uaddress;
    }

    public String getUmail() {
        return Umail;
    }

    public String getUname() {
        return Uname;
    }

    public String getUphonenumber() {
        return Uphonenumber;
    }

    public String getUpwd() {
        return Upwd;
    }

    public String getVerifyCode() {
        return verifyCode;
    }

    public void setUaddress(String uaddress) {
        Uaddress = uaddress;
    }

    public void setUid(int uid) {
        Uid = uid;
    }

    public void setUmail(String umail) {
        Umail = umail;
    }

    public void setUname(String uname) {
        Uname = uname;
    }

    public void setUphonenumber(String uphonenumber) {
        Uphonenumber = uphonenumber;
    }

    public void setUpwd(String upwd) {
        Upwd = upwd;

    }

    public void setVerifyCode(String verifyCode) {
        this.verifyCode = verifyCode;
    }
}
