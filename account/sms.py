import ghasedak_sms
sms_api = ghasedak_sms.Ghasedak(apikey='495df957a36aaa2f58a051a28dbcc17b96f1b9a6b85ca9f075a7470edd8b29c1seobCY2G5nh6AvzP')




otp = ghasedak_sms.SendOtpInput(
    send_date=None,
    receptors=[
        ghasedak_sms.SendOtpReceptorDto(
            mobile='09113057167',
            client_reference_id='client_ref_id'
        )
    ],
    template_name='Ghasedak',
    inputs=[
        ghasedak_sms.SendOtpInput.OtpInput(param='parm1', value='1111'),
        ghasedak_sms.SendOtpInput.OtpInput(param='Name', value='name')
    ],
    udh=False
)

response = sms_api.send_otp_sms(otp)

print(response)