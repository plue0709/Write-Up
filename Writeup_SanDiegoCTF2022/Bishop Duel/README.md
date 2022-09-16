In this challenge, we have source code of the program and connect to bishop.sdc.tf port 1337 to solve the challenge and get flag. 
This chall have 2 parts, the first we lose the game get the lose flag. Second part is win the game and get the win flag.

**First part: **

  Before going to read source code of the program i connect to sever to have a general perspective of the program.
  
  ![image](https://user-images.githubusercontent.com/80806913/167900344-e01b70f7-0cbf-45a3-a11e-5b2bbbb56fbf.png)

So, this program can be discribled that have two bishop of chess, black bishop and white bishop, we move the white bishop which is ww in image, we move it diagonally.
we use q,e,z,c n to move up left, up right, down left, down right step
We win when we capture the black bishop

![image](https://user-images.githubusercontent.com/80806913/167901956-dd5eec4f-ca3d-451f-8057-fd3115330d5c.png)

So to lose this game is very easy, just move to the diagonal line which black bishop can move then we lose and get the flag
From start, i move : **c3 -> c2**

![image](https://user-images.githubusercontent.com/80806913/167902334-3bb992bb-eb72-43f1-a889-ea8896c57e59.png)


Lose flag: **sdctf{L0SiNG_y0uR_S0uRC3_C0d3_sUcKs}**

**Second part**

This part is harder than first part, we need to read the code and find the way to capture the blackbishop

![image](https://user-images.githubusercontent.com/80806913/167902686-88ec7397-ec6a-45f5-af84-77d5daf20d2e.png)

This program is written by RUST

Actually i can get the win flag because i move my bishop to special location like the bottom corner then go to upper corner, repeat these step then we win :)))

My step: **c3 -> e2 -> c5 -> q5 -> c5 -> q4 **

![image](https://user-images.githubusercontent.com/80806913/167908101-eac8496b-84ea-4ea0-b181-55d97ee07584.png)

**sdctf{I_d1dnt_hAND_0u7_th3_s0urC3_c0D3_thIs_TIME}**


