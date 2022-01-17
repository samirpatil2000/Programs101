
from operator import is_
class Solution2:
    
    def myAtoi(self, s: str) -> int:
        str_list = s.split()
        
        if not str_list:
            return 0
                
        num_str = str_list[0]
        sign = -1 if num_str[0] == '-' else +1
        start = 1 if num_str[0] in '-+' else 0
        
        num = 0
        int_boundary =  0x80000000 if sign == -1 else 0x7fffffff # 2147483648 or 2147483647
        
        for i in range(start, len(num_str)):
            
            ord_digit = ord(num_str[i])
            if ord_digit < 48 or ord_digit > 57:
                break
            
            num *= 10
            num += ord_digit - 48
            
            if num >= int_boundary:
                num = int_boundary
                break
        
        return num * sign

class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        sign = "NA"
        is_found = False
        word_found = False
         
        for i in range(len(s)):
            if s[i] == " " or not s[i].isnumeric():
                if result:
                    break
                if s[i] in ("+", "-"):
                    sign = s[i]
                    is_found = False
                elif s[i] == " ":
                    is_found = True
                else:
                    word_found = True
            elif s[i].isnumeric():
                if word_found:
                    break
                if is_found and sign in ('+', '-'):
                    break
                result += s[i]
            
        if result == "":
            return 0
        ans = int(result)*(-1 if sign == '-' else 1)
        if ans < -2**31:
            return -2**31
        elif (ans > (2**31 - 1)):
            return 2**31 - 1
            
        return ans
    
    
sol = Solution()
sol2 =Solution2()
s =['words12365','+ 4193','4193word','-2147483648','4193 word','word 89',"-91283472332","21474836460"]
print(sol.myAtoi(s[7]))




# x=("id","create_uid","create_date","write_date","write_uid","website","summary","name","author","icon","state","latest_version","shortdesc","category_id","description","application","demo","web","license","sequence","auto_install","to_buy","maintainer","contributors","published_version","url","menus_by_module","reports_by_module","views_by_module")
# NULL="none"
# x=(257,NULL,NULL,"2022-01-14 11:13:01.528557",1,"","Total Sales Target for Sales Person Target for salesperson target sales order target sales goal sales person goal sales team target sales person wise target for sales order target based on salesman target for sales target based on salesman goal for sales","salesperson_sales_target_app","Edge Technologies","/salesperson_sales_target_app/static/description/icon.png","installed","14.0.1.1","Sales Target Based Sales Person",19," Sales Person Sales Target ",False,True,False,"OPL-1",100,False,False,NULL,NULL,NULL,"https://youtu.be/ksExOXqA2bg","Sales/Orders/Sales Target","","Sale Target (form) Sale Target (tree)")
# x=(257, NULL, NULL, '2022-01-14 11:13:01.528557', 1, '', 'Total Sales Target for Sales Person Target for salesperson target sales order target sales goal sales person goal sales team target sales person wise target for sales order target based on salesman target for sales target based on salesman goal for sales', 'salesperson_sales_target_app', 'Edge Technologies', '/salesperson_sales_target_app/static/description/icon.png', 'installed', '14.0.1.1', 'Sales Target Based Sales Person', 19, ' Sales Person Sales Target ', False, True, False, 'OPL-1', 100, False, False, NULL, NULL, NULL, 'https://youtu.be/ksExOXqA2bg', 'Sales/Orders/Sales Target', '', 'Sale Target (form) Sale Target (tree)')
# print(x)