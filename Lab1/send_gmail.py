from gmail import GMail, Message
import random


sickness_list = ['đau bụng','đau chân','đau tay','đau đầu']
sickness = random.choice(sickness_list)

gmail = GMail('thanhtrungomg1@gmail.com','123456Li@')

teamplate = '''
<p>Ch&agrave;o sếp</p>
<p>H&ocirc;m nay , em ngủ dậy thấy mệt lắm , b&aacute;c sĩ bảo em bị ebola</p>
<p>Sếp cho em nghỉ l&agrave;m nh&eacute; :))</p>
<p>nh&acirc;n vi&ecirc;n của sếp&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></p>
'''

symton = 'anh'
a = teamplate.replace('{{...}}', sickness)
 


message = Message('Xin nghỉ làm',to='trungtrunpro9x@gmail.com',html= a)

gmail.send(message)