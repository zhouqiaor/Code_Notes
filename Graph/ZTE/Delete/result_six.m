clc
clear
tic
frienddata = csvread('Example_0420.csv');
[clan_a_all,clan_b_all] = size(frienddata);
dirfrienddata = zeros(clan_a_all+clan_b_all,10);
%% 解题思路第一步
for clan_a = 1:1:clan_a_all
    i = 1;
    for clan_b = 1:1:clan_b_all
        if frienddata(clan_a,clan_b) == 1
            dirfrienddata(clan_a,i) = clan_a_all + clan_b;  
            %未区分部落，将b部落人员编号统一跟在a部落后面，即加a部落人数
            i = i + 1;
        end
    end
end
for clan_b = 1:1:clan_b_all
    i = 1;
    for clan_a = 1:1:clan_a_all
        if frienddata(clan_a,clan_b) == 1
            dirfrienddata(clan_a_all+clan_b,i) = clan_a;
            i = i + 1;
        end
    end
end
%% 解题思路第二步
i = 1;
p = zeros(20000,9);
for r = 1:1:(clan_a+clan_b)
    for c = 1:1:10   %首传者赋值
        p(i,1) = r; % p前三位为首传者的坐标 以及编号
        p(i,2) = c;
        p(i,3) = r;
        if c ~= 1 && p(i,4) == 0
            for c_i = 1:1:3
                p(i,c_i) =  p(i-1,c_i);
            end
        end 
        if dirfrienddata(r,c) == 0
            p(i,4) = 0;
            break;
        end        
        if c == 1
        p(i,4) = dirfrienddata(r,c);
        end  
        p(i,4) = dirfrienddata(r,c);
    for c1 = 1:1:10  %二传者赋值
        if c1 ~= 1 && p(i,5) == 0
            for c1_i = 1:1:4
                p(i,c1_i) =  p(i-1,c1_i);
            end
        end
        if dirfrienddata(p(i,4),c1) == 0 
            p(i,5) = 0;
            break;
        end     
        if c1 == 1 
          p(i,5) = dirfrienddata(p(i,4),c1);
        end  
        p(i,5) = dirfrienddata(p(i,4),c1);
 %% 优化思路一
        if   (length(p(i,3:4)) - length(unique(p(i,3:4))))
            p(i,5) = 0;
            break
        end      
     for c2 = 1:1:10  %三传者赋值
        if c2 ~= 1 && p(i,6) == 0
            for c2_i = 1:1:5
                p(i,c2_i) =  p(i-1,c2_i);
            end
        end         
        if dirfrienddata(p(i,5),c2) == 0 
            p(i,6) = 0;
            break;
        end
        if c2 == 1 
          p(i,6) = dirfrienddata(p(i,5),c2);   
        end
        p(i,6) = dirfrienddata(p(i,5),c2);        
        if   (length(p(i,3:5)) - length(unique(p(i,3:5))))
            p(i,6) = 0;
            break
        end 
      for c3 = 1:1:10  %四传者赋值
        if c3 ~= 1 && (p(i,7) == 0)
            for c3_i = 1:1:6
                p(i,c3_i) =  p(i-1,c3_i);
            end
        end  
        if dirfrienddata(p(i,6),c3) == 0 
            p(i,7) = 0;
            break;
        end   
        if c3 == 1 
          p(i,7) = dirfrienddata(p(i,6),c3);   
        end       
        p(i,7) = dirfrienddata(p(i,6),c3);

        if   (length(p(i,3:6)) - length(unique(p(i,3:6))))
            p(i,7) = 0;
            break
        end
      for c4 = 1:1:10  %五传者赋值
        if c4 ~= 1 && (p(i,8) == 0)
            for c4_i = 1:1:7
                p(i,c4_i) =  p(i-1,c4_i);
            end
        end
        if dirfrienddata(p(i,7),c4) == 0 
            p(i,8) = 0;
            break;
        end
        if c4 == 1 
          p(i,8) = dirfrienddata(p(i,7),c4);   
        end       
        p(i,8) = dirfrienddata(p(i,7),c4);

        if   (length(p(i,3:7)) - length(unique(p(i,3:7))))
            p(i,8) = 0;
            break
        end 
      for c5 = 1:1:10  %六传者赋值
        if c5 ~= 1 && (p(i,9) == 0)
            for c5_i = 1:1:8
                p(i,c5_i) =  p(i-1,c5_i);
            end
        end
        if dirfrienddata(p(i,8),c5) == 0 
            p(i,9) = 0;
            break;
        end  
        if c5 == 1 
          p(i,9) = dirfrienddata(p(i,8),c5);   
        end       
        p(i,9) = dirfrienddata(p(i,8),c5);
%% 解题思路第三步
        if   p(i,9) == p(i,3) && ((length(p(i,4:9)) - length(unique(p(i,4:9)))) == 0)      
            i = i+1;
        end    
      end %六传者
      end %五传者
      end %四传者
     end %三传者
    end %二传者
    end %首传者               
end
%% 优化思路二
result = (i-1)/12
toc