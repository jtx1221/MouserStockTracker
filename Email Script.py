from dataclasses import replace
import win32com.client

outlook =win32com.client.Dispatch('OUTLOOK.application')
mail = outlook.CreateItem(0)
mail.To = 'Joshua.Hayles@ssc-spc.gc.ca.'
mail.Subject = 'Sample Email'
mail.HTMLBody = '<h3>This is HTML Body</h3>'
mail.Body = "This is the normal body"
mail.Send()

