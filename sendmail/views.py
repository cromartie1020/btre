from django.shortcuts import render

from django.core.mail import send_mail
def sendmail(request):
    subject ='A new test.'
    phone=request.POST[phone]
    message=request.POST['message']
    from_email='cromarties2913@gmail.com'
    recipient_list=['hrc345@gmail.com','hrc245@gmail.com']

    '''
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )

    '''

    test=send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=True
    )
     
    context={
        'test':test
    }
    return render(request,'sendmail/sendmail.html',context)
