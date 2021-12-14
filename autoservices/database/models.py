from django.db import models
from django.contrib.auth.models import AbstractUser

class tbl_user(AbstractUser):
    uid = models.BigIntegerField(default=0)
    s_password = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=30, default="")
    company_id = models.IntegerField(default=0)
    agents = models.CharField(max_length=1024, default="")
    advisors = models.CharField(max_length=1024, default="")
    reports = models.CharField(max_length=4096, default="[]")
    factor_booked = models.FloatField(default=1)
    factor_transfer = models.FloatField(default=1)

class tbl_user2(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45, default="")
    phone_number = models.CharField(max_length=45, default="")
    email = models.CharField(max_length=45, default="")
    voicemail_number = models.CharField(max_length=45, default="")
    company_id = models.IntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    
class tbl_agent(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=100)
    type = models.IntegerField()
    open_weekly_from = models.CharField(max_length=20)
    open_weekly_to = models.CharField(max_length=20)
    open_sat_from = models.CharField(max_length=20)
    open_sat_to = models.CharField(max_length=20)


class tbl_company(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=50, default="")
    twilio_account_sid = models.CharField(max_length=100)
    twilio_auth_token = models.CharField(max_length=100)
    twilio_phone_number = models.CharField(max_length=100)
    customerInfoAPI = models.URLField(max_length=1000, default="")
    fallbackForwardTo = models.CharField(max_length=100, default="")
    unregisteredForwardTo = models.CharField(max_length=100, default="")
    unregisteredEmailTo = models.EmailField(max_length=200, default="")
    unregisteredSmsTo = models.CharField(max_length=100, default="")
    unregisteredAPICall = models.URLField(max_length=1000, default="")
    licenses_used = models.IntegerField(default=0)
    max_license = models.IntegerField(default=0)
    session_config = models.TextField(default="")
    assistant_config = models.TextField(default="")
    badges_config = models.TextField(default="")


class tbl_advisor(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    company_id = models.IntegerField()
    buddy_list = models.CharField(max_length=300, default="[]")
    caller_response_template = models.CharField(max_length=1000, default="")
    advisor_response_template = models.CharField(max_length=1000, default="")
    caller_text_response_template = models.CharField(max_length=1000, default="")
    manager_response_template = models.CharField(max_length=1000, default="")
    bookingURL = models.URLField(max_length=5000, default="")
    configEscalationOnOff = models.BooleanField(default=False)
    filterMeetingOnOff = models.BooleanField(default=False)
    promptMeetingOptions = models.CharField(max_length=50,default='')
    filterVMOnOff = models.BooleanField(default=False)
    confAskPermissionToText = models.BooleanField(default=False)
    configTimeoutVM = models.IntegerField(default=0)
    configTimeoutNoVMLeft = models.IntegerField(default=0)
    promptGreeting = models.CharField(max_length=1000,default='')
    promptMeetingConclusion = models.CharField(max_length=200,default='')
    promptVMOptions = models.CharField(max_length=200,default='')
    promptVMStart = models.CharField(max_length=200,default='')
    promptVMPermission = models.CharField(max_length=200,default='')
    promptVMConclusion = models.CharField(max_length=200,default='')
    promptFirstName = models.CharField(max_length=100,default='')
    callerMeetingTemplate = models.CharField(max_length=1000,default='')
    advisorMeetingTemplate = models.CharField(max_length=1000,default='')
    includeRecording = models.BooleanField(default=False)
    alert_threshold = models.IntegerField(default=0)
    alert_phone_number = models.CharField(max_length=50,default='')
    alert_email = models.CharField(max_length=50,default='')
    sms_allowed_from = models.CharField(max_length=20,default='')
    sms_allowed_to = models.CharField(max_length=20,default='')
    email_allowed_from = models.CharField(max_length=20,default='')
    email_allowed_to = models.CharField(max_length=20,default='')
    no_text_response_template = models.CharField(max_length=1000,default='')


class tbl_voicemail(models.Model):
    message = models.CharField(max_length=1024)
    caller_phone = models.CharField(max_length=30)
    advisor_phone = models.CharField(max_length=30)
    caller_name = models.CharField(max_length=50)
    ok_text = models.IntegerField(default=0)
    type = models.IntegerField(default=1)
    delay_time = models.IntegerField()
    status = models.IntegerField(default=0)
    alert_to_manager = models.IntegerField(default=0)
    replier_id = models.IntegerField(default=-1)
    flag = models.IntegerField(default=0)
    caller_replied = models.IntegerField(default=0)
    time = models.DateTimeField()


class tbl_voicemail_response(models.Model):
    vm_id = models.IntegerField()
    replier_name = models.CharField(max_length=50)
    message = models.CharField(max_length=1024, default="")
    time = models.DateTimeField()
    
    
class tb_Category_Model(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'category'
