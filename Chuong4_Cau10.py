#Câu 10: Vẽ hình dùng Sleep

import time


hinh1 = """

            *
          * *
        * * *  
* * * * * * *
* * *
* *
*

"""


hinh2 = """

            *
          * *
        *   *  
* * * * * * *
*   *
* *
*

"""


hinh3 = """

      * * * *
      * * *
      * *
      *
    * *
  * * *
* * * *

"""


hinh4 = """
   
      * * * *
      *   *
      * *
      *
    * *
  *   *
* * * *

"""


ds_hinh = [hinh1, hinh2, hinh3, hinh4]


for h in ds_hinh:
    print(h)
    time.sleep(5)